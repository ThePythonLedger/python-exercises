def test_prints_hello_world(run_script, expect_output):
    stdout, _ = run_script("hello_world.py")
    expect_output(stdout, "Hello, World!")
