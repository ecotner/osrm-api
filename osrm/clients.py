from typing import Iterable, Dict, Any

import requests
from requests.models import Response


def format_coords(coords) -> str:
    coords = ";".join([f"{lon},{lat}" for lat, lon in coords])
    return coords


def format_options(options: Dict[str, Any]) -> str:
    options = "&".join([f"{op}={val}" for op, val in options.items()])
    if options:
        return "?" + options
    return options


def format_request(
    host: str,
    service: str,
    coords: Iterable[Iterable[float]],
    options: Dict[str, Any] = None,
    profile: str = "driving",
    version: str = "v1",
) -> str:
    coords = format_coords(coords)
    options = "" if options is None else format_options(options)
    req = f"http://{host}/{service}/{version}/{profile}/{coords}{options}"
    return req


class Client:
    def __init__(self, host):
        self.host = host

    def request(
        self,
        service: str,
        coords: Iterable[Iterable[float]],
        options: Dict[str, Any] = None,
        profile: str = "driving",
        version: str = "v1",
    ):
        req = format_request(self.host, service, coords, options, profile, version)
        response = requests.get(req)
        return response