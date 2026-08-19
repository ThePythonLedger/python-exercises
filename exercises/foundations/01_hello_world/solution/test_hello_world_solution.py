def test_prints_hello_world(run_script, expect_output):
    stdout, _ = run_script("hello_world_solution.py")
    expect_output(stdout, "Hello, World!")
