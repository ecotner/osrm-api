# conversions from other unit to meters
DIST_CONVERSIONS = {
    "m": 1.0,
    "meter": 1.0,
    "km": 1000.0,
    "kilometer": 1000.0,
    "mi": 1609.34,
    "mile": 1609.34,
    "foot": 0.3048,
    "ft": 0.3048,
}

# conversions from other unit to seconds
TIME_CONVERSIONS = {
    "s": 1.0,
    "sec": 1.0,
    "second": 1.0,
    "m": 60.0,
    "min": 60.0,
    "minute": 60.0,
    "hour": 3600.0,
    "hr": 3600.0,
    "h": 3600.0,
    "day": 24 * 3600.0,
    "d": 24 * 3600.0,
}

# this is the "mean polar radius"
EARTH_RADIUS_KM = 6371.0


def convert_dist_units(qty, like="meter", to="km"):
    qty = (qty * DIST_CONVERSIONS[like]) / DIST_CONVERSIONS[to]
    return qty


def convert_time_units(qty, like="sec", to="min"):
    qty = (qty * TIME_CONVERSIONS[like]) / TIME_CONVERSIONS[to]
    return qty