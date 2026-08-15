def test_prints_the_sum(run_script):
    stdout, _ = run_script("add_numbers_solution.py")
    lines = stdout.strip().splitlines()
    assert lines[0] == "11"


def test_prints_the_difference(run_script):
    stdout, _ = run_script("add_numbers_solution.py")
    lines = stdout.strip().splitlines()
    assert lines[1] == "5"


def test_prints_the_product(run_script):
    stdout, _ = run_script("add_numbers_solution.py")
    lines = stdout.strip().splitlines()
    assert lines[2] == "24"
