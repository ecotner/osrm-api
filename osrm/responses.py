from functools import cached_property

from requests import Response
import polyline
import numpy as np

from osrm.utils import convert_dist_units, convert_time_units


class OSRMResponse:
    def __init__(self, response: Response):
        assert response.ok, f"Bad response {response.status_code}"
        self.response = response

    @cached_property
    def json(self):
        return self.response.json()


class RouteResponse(OSRMResponse):
    def distance(self, unit="km"):
        dist = self.json["routes"][0]["distance"]
        return convert_dist_units(dist, to=unit)

    def duration(self, unit="min"):
        dur = self.json["routes"][0]["duration"]
        return convert_time_units(dur, to=unit)

    def polyline_coords(self):
        line = self.json["routes"][0]["geometry"]
        return polyline.decode(line, precision=5)


class TableResponse(OSRMResponse):
    def distances(self, unit="km"):
        D = np.array(self.json["distances"])
        return convert_dist_units(D, to=unit)