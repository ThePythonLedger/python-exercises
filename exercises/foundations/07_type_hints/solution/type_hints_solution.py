"""Orbital Station Alpha - Telemetry Relay (Reference Solution)"""

# LEVEL 1 - Comm Link Beacon
def format_signal(channel: int, frequency: float, active: bool = True) -> str:
    status = "ONLINE" if active else "OFFLINE"
    return f"Channel {channel} ({frequency:.1f} MHz) is {status}."


# LEVEL 2 - Terminal Broadcast
def log_transmission(message: str, priority: int = 1) -> None:
    print(f"[PRIORITY {priority}] TRANSMISSION: {message}")


# LEVEL 3 - Cargo Manifest Filter
def filter_heavy_cargo(manifest: dict[str, float], threshold: float) -> list[str]:
    return [item for item, weight in manifest.items() if weight > threshold]


# LEVEL 4 - Navigation Vectors
def calculate_vector_distance(
    point_a: tuple[float, float], point_b: tuple[float, float]
) -> float:
    dx = point_b[0] - point_a[0]
    dy = point_b[1] - point_a[1]
    return (dx**2 + dy**2) ** 0.5


def bundle_waypoint_names(waypoints: list[str]) -> tuple[str, ...]:
    return tuple(waypoints)


# LEVEL 5 - Beacon Lookup & Sensor Normalization
def lookup_beacon(beacons: dict[str, float], beacon_id: str) -> float | None:
    return beacons.get(beacon_id)


def normalize_reading(reading: int | float) -> float:
    return float(reading)


# LEVEL 6 - Station Telemetry Buffers
active_relays: list[str] = []
calibration_cache: dict[str, float] = {}
current_target: str | None = None


# LEVEL 7 - Telemetry Protocol
Coordinate2D = tuple[float, float]
SensorMap = dict[str, float]


def validate_docking_clearance(
    origin: Coordinate2D, target: Coordinate2D, clearances: SensorMap
) -> bool:
    dx = target[0] - origin[0]
    dy = target[1] - origin[1]
    dist = (dx**2 + dy**2) ** 0.5
    all_clear = all(reading >= 0.5 for reading in clearances.values())
    return dist <= 100.0 and all_clear


# LEVEL 8 - BOSS: Flight Dispatch Pipeline
FlightRecord = dict[str, str | float | None]


def compile_dispatch_report(
    records: list[FlightRecord], max_distance: float = 500.0
) -> tuple[int, list[str]]:
    eligible = []
    for ship in records:
        dist = ship.get("distance")
        callsign = ship.get("callsign")
        if isinstance(dist, (int, float)) and isinstance(callsign, str):
            if dist <= max_distance:
                eligible.append(callsign)
    return (len(eligible), eligible)
