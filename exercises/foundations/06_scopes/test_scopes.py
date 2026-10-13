import ast
import inspect
import textwrap

import pytest

import scopes as m


def _run(func, *args, hint=""):
  
    try:
        return func(*args)
    except (NameError, TypeError) as err:
        pytest.fail(
            f"{func.__name__}() crashed with {type(err).__name__}: {err}\n"
            f"Hint: {hint}",
            pytrace=False,
        )


def _has_statement(func, node_type):
    tree = ast.parse(textwrap.dedent(inspect.getsource(func)))
    return any(isinstance(node, node_type) for node in ast.walk(tree))


def test_level1():
    assert "STATION_NAME" in vars(m), (
        "STATION_NAME should be defined at module level so every function can see it."
    )
    assert _run(m.boot_system, hint="Who needs the station name?") == (
        "Booting Orbital Station Alpha..."
    )
    assert _run(m.show_banner, hint="Where does STATION_NAME have to live?") == (
        "=== Orbital Station Alpha ==="
    )


@pytest.mark.skip(reason="Finish level 1 first")
def test_level2():
    monitor = _run(m.build_oxygen_monitor, hint="Which function does read_level() sit in?")
    assert _run(monitor, hint="read_level() looks outward: Local, then...?") == (
        "Oxygen at 100%"
    )
    assert "oxygen" not in vars(m), "Don't solve this with a module-level variable."


@pytest.mark.skip(reason="Finish level 2 first")
def test_level3():
    assert "list" not in vars(m), "You have shadowed the built-in `list`."
    assert "sum" not in vars(m), "You have shadowed the built-in `sum`."
    assert _run(m.summarize_signals, hint="Built-in names must stay available.") == (
        "3 signals, strength 49"
    )


@pytest.mark.skip(reason="Finish level 3 first")
def test_level4():
    assert _run(m.add_bonus_power, 50, hint="Pass the value in instead.") == 60
    assert m.power == 50, "The global `power` must not be changed."
    assert not _has_statement(m.add_bonus_power, ast.Global), (
        "Fix this one with a parameter and `return`, not `global`."
    )


@pytest.mark.skip(reason="Finish level 4 first")
def test_level5():
    before = len(_run(m.get_manifest, hint="Where must the cargo list live?"))
    _run(m.load_crate, "Titanium", hint="Both functions share one list.")
    _run(m.load_crate, "Ice", hint="Both functions share one list.")
    assert m.get_manifest()[before:] == ["Titanium", "Ice"]
    assert not _has_statement(m.load_crate, ast.Global), (
        "Mutating a list in place doesn't need `global`."
    )


@pytest.mark.skip(reason="Finish level 5 first")
def test_level6():
    start = m.alarm_count
    for expected in (start + 1, start + 2, start + 3):
        assert _run(m.trigger_alarm, hint="Rebinding a global needs a keyword.") == expected
    assert m.alarm_count == start + 3, "The global alarm_count should be updated."


@pytest.mark.skip(reason="Finish level 6 first")
def test_level7():
    drone_a = m.make_drone_counter()
    drone_b = m.make_drone_counter()
    assert [_run(drone_a, hint="Rebinding an enclosing variable needs a keyword.")
            for _ in range(3)] == [1, 2, 3]
    assert drone_b() == 1, "Each drone should keep its own count."


@pytest.mark.skip(reason="Finish level 7 first")
def test_level8():
    assert m.list_local_names(1, 2) == ["a", "b", "c"]
    assert m.is_global("show_banner") is True
    assert m.is_global("no_such_name_xyz") is False
    assert m.probe_hidden() is True


@pytest.mark.skip(reason="Finish level 8 first")
def test_level9():
    assert "max" not in vars(m), "You have shadowed the built-in `max`."
    assert _run(m.run_station, hint="Three scope bugs are hiding here.") == (
        "Checks: 3 | Passed: 2 | Peak: 91"
    )
