"""Orbital Station Alpha - Telemetry Relay (Type Hints)

Add the appropriate modern type hints to each function and variable below.
Do not change the function names or their internal logic.
"""

# LEVEL 1 - Comm Link Beacon
def format_signal(channel, frequency, active=True):
    status = "ONLINE" if active else "OFFLINE"
    return f"Channel {channel} ({frequency:.1f} MHz) is {status}."


# LEVEL 2 - Terminal Broadcast
def log_transmission(message, priority=1):
    print(f"[PRIORITY {priority}] TRANSMISSION: {message}")


# LEVEL 3 - Cargo Manifest Filter
def filter_heavy_cargo(manifest, threshold):
    return [item for item, weight in manifest.items() if weight > threshold]


# LEVEL 4 - Navigation Vectors
def calculate_vector_distance(point_a, point_b):
    dx = point_b[0] - point_a[0]
    dy = point_b[1] - point_a[1]
    return (dx**2 + dy**2) ** 0.5


def bundle_waypoint_names(waypoints):
    return tuple(waypoints)


# LEVEL 5 - Beacon Lookup & Sensor Normalization
def lookup_beacon(beacons, beacon_id):
    return beacons.get(beacon_id)


def normalize_reading(reading):
    return float(reading)


# LEVEL 6 - Station Telemetry Buffers
# Annotate these module variables with their expected types:
active_relays = []
calibration_cache = {}
current_target = None


# LEVEL 7 - Telemetry Protocol
# Define the type aliases here:
# Coordinate2D: a tuple of exactly two floats
# SensorMap: a dictionary mapping strings to floats


def validate_docking_clearance(origin, target, clearances):
    dx = target[0] - origin[0]
    dy = target[1] - origin[1]
    dist = (dx**2 + dy**2) ** 0.5
    all_clear = all(reading >= 0.5 for reading in clearances.values())
    return dist <= 100.0 and all_clear


# LEVEL 8 - BOSS: Flight Dispatch Pipeline
# Define the type alias here:
# FlightRecord: a dictionary mapping string keys to str | float | None


def compile_dispatch_report(records, max_distance=500.0):
    eligible = []
    for ship in records:
        dist = ship.get("distance")
        callsign = ship.get("callsign")
        if isinstance(dist, (int, float)) and isinstance(callsign, str):
            if dist <= max_distance:
                eligible.append(callsign)
    return (len(eligible), eligible)
