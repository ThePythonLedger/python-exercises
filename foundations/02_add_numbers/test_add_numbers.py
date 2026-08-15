import pytest


def test_prints_the_sum(run_script):
    stdout, _ = run_script("add_numbers.py")
    lines = stdout.strip().splitlines()
    assert lines[0] == "11"


@pytest.mark.skip(reason="unlock once the test above passes")
def test_prints_the_difference(run_script):
    stdout, _ = run_script("add_numbers.py")
    lines = stdout.strip().splitlines()
    assert lines[1] == "5"


@pytest.mark.skip(reason="unlock once the test above passes")
def test_prints_the_product(run_script):
    stdout, _ = run_script("add_numbers.py")
    lines = stdout.strip().splitlines()
    assert lines[2] == "24"
