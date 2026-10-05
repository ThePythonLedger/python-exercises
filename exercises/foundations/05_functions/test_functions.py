import pytest

from functions import (
    calculate_fuel,
    calculate_trip_cost,
    create_dispatch_summary,
    display_manifest,
    greet_pilot,
)


def test_task1():
    assert greet_pilot("Alex") == "Welcome aboard, Commander Alex. Flight systems ready."
    assert greet_pilot("Sarah") == "Welcome aboard, Commander Sarah. Flight systems ready."


@pytest.mark.skip(reason="Finish task 1 first")
def test_task2():
    assert calculate_fuel(10, 2.5) == 25.0
    assert calculate_fuel(40, 1.5) == 60.0


@pytest.mark.skip(reason="Finish task 2 first")
def test_task3():
    assert calculate_trip_cost(10) == 25.0
    assert calculate_trip_cost(10, 3.0) == 30.0


@pytest.mark.skip(reason="Finish task 3 first")
def test_task4(capsys):
    result = display_manifest("Titanium", 50, "HIGH")
    captured = capsys.readouterr()
    assert captured.out == "[CARGO] 50x Titanium\n[STATUS] Priority: HIGH\n"
    assert result is None

    result_default = display_manifest("Minerals", 10)
    captured_default = capsys.readouterr()
    assert captured_default.out == "[CARGO] 10x Minerals\n[STATUS] Priority: STANDARD\n"
    assert result_default is None


@pytest.mark.skip(reason="Finish task 4 first")
def test_task5():
    assert (
        create_dispatch_summary("Alex", 100, 2.0, 3.0)
        == "Dispatch Plan for Alex: 200.0 fuel units required. Total cost: 600.0 credits."
    )
    assert (
        create_dispatch_summary("Elena", 100)
        == "Dispatch Plan for Elena: 150.0 fuel units required. Total cost: 375.0 credits."
    )
