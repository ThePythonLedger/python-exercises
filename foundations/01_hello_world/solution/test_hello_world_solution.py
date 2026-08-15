def test_prints_hello_world(run_script):
    stdout, _ = run_script("hello_world_solution.py")
    assert stdout.strip() == "Hello, World!"
