import pytest


def test_prints_the_sum(run_script, expect_line):
    stdout, _ = run_script("add_numbers.py")
    expect_line(stdout, 1, "11")


@pytest.mark.skip(reason="unlock once the test above passes")
def test_prints_the_difference(run_script, expect_line):
    stdout, _ = run_script("add_numbers.py")
    expect_line(stdout, 2, "5")


@pytest.mark.skip(reason="unlock once the test above passes")
def test_prints_the_product(run_script, expect_line):
    stdout, _ = run_script("add_numbers.py")
    expect_line(stdout, 3, "24")
