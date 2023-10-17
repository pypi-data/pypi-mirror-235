"""Component to move the simulation objects."""
import itertools
import logging
import warnings
from typing import Callable, List, Optional

import numpy as np
import pyproj
import shapely
import shapely.geometry

from .container import HasContainer, HasMultiContainer
from .locatable import Locatable
from .log import Log, LogState, PerformsActivity

# can be removed if we switch to python>=3.10
try:
    from itertools import pairwise
except ImportError:
    # redefine if needed
    def pairwise(iterable):  # type: ignore
        # pairwise('ABCDEFG') --> AB BC CD DE EF FG
        a, b = itertools.tee(iterable)
        next(b, None)
        return zip(a, b)


logger = logging.getLogger(__name__)

# we only have one earth, defined here.
WGS84 = pyproj.Geod(ellps="WGS84")


class Movable(Locatable, PerformsActivity, Log):
    """
    Movable class.

    Used for object that can move with a fixed speed
    geometry: point used to track its current location

    Parameters
    ----------
    v: speed, speed over ground of the object in m/s
    engine_order: factor that determines how much of the speed is used.
    """

    def __init__(self, v: float = 1, engine_order: float = 1, *args, **kwargs):
        super().__init__(*args, **kwargs)
        """Construct a movable object."""
        self._v = v
        self.engine_order = 1.0

    def move(
        self,
        destination: Optional[Locatable] = None,
        duration: Optional[float] = None,
        engine_order: Optional[float] = None,
    ):
        """Determine distance between origin and destination.

        Yield the time it takes to travel based on speed properties and load factor of
        the speed.

        The moving step can be part of an activity. Set the `activity_id` to the
        movable object to have it recorded in the log and in the timeout value.

        """
        if destination is None:
            raise ValueError("Movable in OpenCLSim does not support empty destination")

        # we got an egnine setting, store it.
        if engine_order is not None:
            self.engine_order = engine_order

        # Log the start event
        self.log_entry_v1(
            self.env.now,
            self.activity_id,
            LogState.START,
        )

        # Determine the sailing_duration
        if duration is None:
            duration = self.compute_duration(self.geometry, destination.geometry)

        # Check out the time based on duration of sailing event
        yield self.env.timeout(duration, value=self.activity_id)

        # Set mover geometry to destination geometry
        self.geometry = shapely.geometry.shape(destination.geometry)

        # Log the stop event
        self.log_entry_v1(
            self.env.now,
            self.activity_id,
            LogState.STOP,
        )

    @property
    def v(self):
        """return the velocity * engine_order"""
        return self._v * self.engine_order

    @property
    def current_speed(self):
        warnings.warn(
            "The property `.current_speed` is deprected. Use `.v` instead.",
            DeprecationWarning,
        )
        return self.v

    @staticmethod
    def compute_distance(origin: shapely.Geometry, destination: shapely.Geometry):
        """Determine the sailing distance based on great circle path from origin to destination."""
        orig = shapely.geometry.shape(origin)
        dest = shapely.geometry.shape(destination)
        _, _, distance = WGS84.inv(orig.x, orig.y, dest.x, dest.y)
        return distance

    def compute_duration(
        self, origin: shapely.Geometry, destination: shapely.Geometry, engine_order=1.0
    ):
        """Determine the duration based on great circle path from origin to destination."""
        distance = self.compute_distance(origin, destination)
        return distance / (self.v * engine_order)


class ContainerDependentMovable(Movable, HasContainer):
    """
    ContainerDependentMovable class.

    Used for objects that move with a speed dependent on the container level

    Parameters
    ----------
    compute_v
        a function that returns the current speed, given the fraction of the
        the container that is filled (in [0,1]), e.g.:
            lambda x: x * (v_full - v_empty) + v_empty
        It can also be constant, e.g.:
            lambda x: 10
    """

    def __init__(self, compute_v, *args, **kwargs):
        """Init of the containerdependent moveable."""
        super().__init__(*args, **kwargs)
        self.compute_v = compute_v

    @property
    def v(self):
        return self.compute_v(
            self.container.get_level() / self.container.get_capacity()
        )


class MultiContainerDependentMovable(Movable, HasMultiContainer):
    """
    MultiContainerDependentMovable class.

    Used for objects that move with a speed dependent on the container level.
    This movable is provided with a MultiContainer, thus can handle a container
    containing different objects.
    compute_v
        a function that returns the current speed, given the fraction of the
        the container that is filled (in [0,1]), e.g.:
            lambda x: x * (v_full - v_empty) + v_empty
        It can also be constant, e.g.:
            lambda x: 10
    """

    def __init__(self, compute_v, *args, **kwargs):
        super().__init__(*args, **kwargs)
        """Initialization"""
        self.compute_v = compute_v
        self.conainter_ids = self.container.container_list

    @property
    def v(self):
        sum_level = 0
        sum_capacity = 0
        for id_ in self.container.container_list:
            sum_level = self.container.get_level(id_)
            sum_capacity = self.container.get_capacity(id_)
        fill_degree = sum_level / sum_capacity
        return self.compute_v(fill_degree)


class Routable(Movable, Locatable):
    """Mixin class: Something with a route (networkx node list format)
    route: a list of node ids (available on env.graph) or geometries (shapely.Geometry)
    """

    # one instance on the class

    def __init__(self, route: list, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # call functions when passing edges
        self.route = route
        self.on_pass_edge_functions: List[Callable] = []

        assert hasattr(self.env, "FG"), "expected graph FG to be available on env"

    def move_to_geometry(self, geometry: shapely.geometry.Point):
        """move to geometry"""
        linestring = shapely.geometry.LineString([self.geometry, geometry])
        distance = WGS84.geometry_length(linestring)
        duration = self.v * distance
        yield self.env.timeout(duration)
        self.geometry = geometry

    def pass_linestring(self, geometry: shapely.geometry.LineString):
        """Pass a linestring."""
        a = shapely.geometry.Point(geometry.coords[0])
        b = shapely.geometry.Point(geometry.coords[-1])
        assert isinstance(geometry, shapely.geometry.LineString)
        distance = WGS84.geometry_length(geometry)
        duration = distance / (self.v * self.engine_order)
        self.geometry = a
        yield self.env.timeout(duration)
        self.geometry = b

    @staticmethod
    def order_geometry(
        geometry: shapely.geometry.LineString, a: shapely.geometry.Point
    ):
        """Make sure the linestring starts at a. If the end of the linestring is
        closer to a than the start, the linestring is inverted."""
        start = shapely.geometry.Point(*geometry.coords[0])
        end = shapely.geometry.Point(*geometry.coords[-1])
        _, _, distance_from_start = WGS84.inv(start.x, start.y, a.x, a.y)
        _, _, distance_from_end = WGS84.inv(end.x, end.y, a.x, a.y)
        if distance_from_start > distance_from_end:
            coords = np.flipud(np.array(geometry.coords))
        else:
            coords = geometry.coords
        new_geometry = shapely.geometry.LineString(coords)
        return new_geometry

    def move_over_route(self, route: List[str]):
        """sail over the route, a list of nodes"""
        a = route[0]
        a_geometry = self.graph.nodes[a]["geometry"]
        yield from self.move_to_geometry(a_geometry)
        # move self to node + geometry
        self.node = a
        self.geometry = a_geometry

        for i, (a, b) in enumerate(pairwise(route)):
            a_geometry = self.graph[a]["geometry"]
            b_geometry = self.graph[b]["geometry"]
            edge_geometry = self.graph[(a, b)]["geometry"]
            # make sure we are in the right order
            edge_geometry = self.order_geometry(edge_geometry, a_geometry)
            # go to a (we should already be here)
            self.geometry = a_geometry
            self.node = a
            # pass over the edge
            yield from self.pass_linestring(edge_geometry)
            # call any other functions we have registered
            for pass_edge_function in self.pass_edge_function:
                yield pass_edge_function(
                    movable=self, a=a, b=b, route=route, geometry=edge_geometry
                )
            # we have arrived, go there....
            self.geometry = b_geometry
            self.node = b
