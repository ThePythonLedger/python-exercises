import pytest

import type_hints_solution as m


def _format_type(t):
    if t is None or t is type(None):
        return "None"
    return getattr(t, "__name__", str(t))


def _check_annotation(target, key, expected):
    ann = getattr(target, "__annotations__", {})
    target_name = getattr(target, "__name__", "Module")
    is_return = key == "return"
    label = (
        f"Return type of {target_name}()"
        if is_return
        else f"Parameter '{key}' in {target_name}()"
    )

    exp_str = _format_type(expected)
    assert key in ann, (
        f"Missing type hint: {label} is not annotated. Expected '{exp_str}'."
    )
    actual = ann[key]
    act_str = _format_type(actual)
    assert actual == expected or (expected is None and actual is type(None)), (
        f"Incorrect type hint: {label} is annotated as '{act_str}', but expected '{exp_str}'."
    )


def _check_module_var_annotation(module, var_name, expected):
    ann = getattr(module, "__annotations__", {})
    exp_str = _format_type(expected)
    assert var_name in ann, (
        f"Missing type hint: module variable '{var_name}' is not annotated. Expected '{exp_str}'."
    )
    actual = ann[var_name]
    act_str = _format_type(actual)
    assert actual == expected or (expected is None and actual is type(None)), (
        f"Incorrect type hint: module variable '{var_name}' is annotated as '{act_str}', but expected '{exp_str}'."
    )


def test_level1():
    _check_annotation(m.format_signal, "channel", int)
    _check_annotation(m.format_signal, "frequency", float)
    _check_annotation(m.format_signal, "active", bool)
    _check_annotation(m.format_signal, "return", str)

    assert (
        m.format_signal(1, 142.5)
        == "Channel 1 (142.5 MHz) is ONLINE."
    )
    assert (
        m.format_signal(2, 108.0, False)
        == "Channel 2 (108.0 MHz) is OFFLINE."
    )


def test_level2(capsys):
    _check_annotation(m.log_transmission, "message", str)
    _check_annotation(m.log_transmission, "priority", int)
    _check_annotation(m.log_transmission, "return", None)

    result = m.log_transmission("Docking clamp engaged.", 2)
    captured = capsys.readouterr()
    assert captured.out == "[PRIORITY 2] TRANSMISSION: Docking clamp engaged.\n"
    assert result is None


def test_level3():
    _check_annotation(m.filter_heavy_cargo, "manifest", dict[str, float])
    _check_annotation(m.filter_heavy_cargo, "threshold", float)
    _check_annotation(m.filter_heavy_cargo, "return", list[str])

    cargo = {"Titanium": 12.5, "Rations": 2.1, "Fuel": 45.0}
    assert m.filter_heavy_cargo(cargo, 10.0) == ["Titanium", "Fuel"]
    assert m.filter_heavy_cargo({"Oxygen": 1.0}, 5.0) == []


def test_level4():
    _check_annotation(m.calculate_vector_distance, "point_a", tuple[float, float])
    _check_annotation(m.calculate_vector_distance, "point_b", tuple[float, float])
    _check_annotation(m.calculate_vector_distance, "return", float)

    _check_annotation(m.bundle_waypoint_names, "waypoints", list[str])
    _check_annotation(m.bundle_waypoint_names, "return", tuple[str, ...])

    dist = m.calculate_vector_distance((0.0, 0.0), (3.0, 4.0))
    assert pytest.approx(dist) == 5.0

    bundled = m.bundle_waypoint_names(["Nav-1", "Nav-2", "Nav-3"])
    assert bundled == ("Nav-1", "Nav-2", "Nav-3")


def test_level5():
    _check_annotation(m.lookup_beacon, "beacons", dict[str, float])
    _check_annotation(m.lookup_beacon, "beacon_id", str)
    _check_annotation(m.lookup_beacon, "return", float | None)

    _check_annotation(m.normalize_reading, "reading", int | float)
    _check_annotation(m.normalize_reading, "return", float)

    beacons = {"BCN-1": 142.5, "BCN-2": 156.8}
    assert m.lookup_beacon(beacons, "BCN-1") == 142.5
    assert m.lookup_beacon(beacons, "UNKNOWN") is None

    assert m.normalize_reading(42) == 42.0
    assert m.normalize_reading(3.14) == 3.14


def test_level6():
    _check_module_var_annotation(m, "active_relays", list[str])
    _check_module_var_annotation(m, "calibration_cache", dict[str, float])
    _check_module_var_annotation(m, "current_target", str | None)

    assert m.active_relays == []
    assert m.calibration_cache == {}
    assert m.current_target is None


def test_level7():
    assert hasattr(m, "Coordinate2D"), (
        "Coordinate2D type alias should be defined in the module."
    )
    assert m.Coordinate2D == tuple[float, float], (
        "Coordinate2D should be an alias for tuple[float, float]."
    )
    assert hasattr(m, "SensorMap"), (
        "SensorMap type alias should be defined in the module."
    )
    assert m.SensorMap == dict[str, float], (
        "SensorMap should be an alias for dict[str, float]."
    )

    _check_annotation(m.validate_docking_clearance, "origin", tuple[float, float])
    _check_annotation(m.validate_docking_clearance, "target", tuple[float, float])
    _check_annotation(m.validate_docking_clearance, "clearances", dict[str, float])
    _check_annotation(m.validate_docking_clearance, "return", bool)

    origin = (0.0, 0.0)
    target = (30.0, 40.0)  # distance 50.0 <= 100
    assert (
        m.validate_docking_clearance(
            origin, target, {"port": 0.8, "starboard": 0.6}
        )
        is True
    )
    assert (
        m.validate_docking_clearance(
            origin, target, {"port": 0.2, "starboard": 0.9}
        )
        is False
    )


def test_level8():
    assert hasattr(m, "FlightRecord"), (
        "FlightRecord type alias should be defined in the module."
    )
    assert m.FlightRecord == dict[str, str | float | None], (
        "FlightRecord should be an alias for dict[str, str | float | None]."
    )

    _check_annotation(
        m.compile_dispatch_report, "records", list[dict[str, str | float | None]]
    )
    _check_annotation(m.compile_dispatch_report, "max_distance", float)
    _check_annotation(m.compile_dispatch_report, "return", tuple[int, list[str]])

    fleet = [
        {"callsign": "Vanguard-1", "distance": 120.0, "cargo": "Titanium"},
        {"callsign": "Hermes-4", "distance": 620.0, "cargo": None},
        {"callsign": "Nebula-9", "distance": 450.0, "cargo": "Water"},
    ]
    count, ships = m.compile_dispatch_report(fleet, 500.0)
    assert count == 2
    assert ships == ["Vanguard-1", "Nebula-9"]
