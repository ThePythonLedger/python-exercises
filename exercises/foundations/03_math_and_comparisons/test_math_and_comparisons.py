import pytest


def test_task1(run_script, expect_variables):
    _, namespace = run_script("math_and_comparisons.py")
    expect_variables(
        namespace,
        {
            "player_class": "Wizard",
            "player_attack": 35,
            "player_defense": 13,
            "enemy_attack": 28,
            "enemy_defense": 16,
        },
    )


def test_task2(run_script, expect_variables):
    _, namespace = run_script("math_and_comparisons.py")
    expect_variables(namespace, {"player_attack_power": 455, "enemy_attack_power": 448})


def test_task3(run_script, expect_variables):
    _, namespace = run_script("math_and_comparisons.py")
    expect_variables(namespace, {"damage_dealt": 7})


def test_task4(run_script, expect_variables):
    _, namespace = run_script("math_and_comparisons.py")
    expect_variables(
        namespace,
        {"combat_log": "WIZARD has suffered 7 damage."},
    )


def test_task5(run_script, expect_variables):
    _, namespace = run_script("math_and_comparisons.py")
    expect_variables(
        namespace,
        {"is_player_stronger": True, "is_balanced": False},
    )


def test_task6(run_script, expect_variables):
    _, namespace = run_script("math_and_comparisons.py")
    expect_variables(
        namespace,
        {"class_initial": "W", "class_code": "wiz"},
    )
