import pytest


def test_task1(run_script, expect_variables):
    _, namespace = run_script("loops.py")
    expect_variables(namespace, {"security_level": 0, "countdown_log": "5 4 3 2 1 "})


@pytest.mark.skip(reason="Finish task 1 first")
def test_task2(run_script, expect_variables):
    _, namespace = run_script("loops.py")
    expect_variables(namespace, {"total_energy": 30})


@pytest.mark.skip(reason="Finish task 2 first")
def test_task3(run_script, expect_variables):
    _, namespace = run_script("loops.py")
    expect_variables(namespace, {"bypass_code": 7, "attempts_made": 7})


@pytest.mark.skip(reason="Finish task 3 first")
def test_task4(run_script, expect_variables):
    _, namespace = run_script("loops.py")
    expect_variables(
        namespace,
        {"grid_output": "[1,1],[1,2],[1,3]\n[2,1],[2,2],[2,3]\n[3,1],[3,2],[3,3]"},
    )


@pytest.mark.skip(reason="Finish task 4 first")
def test_task5(run_script, expect_variables):
    _, namespace = run_script("loops.py")
    expect_variables(
        namespace, {"secret_pin": 42, "current_attempt": 42, "valid_checks": 6}
    )
