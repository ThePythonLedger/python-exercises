"""Shared fixtures for script-style exercises — the ones that don't use
functions yet. Available automatically in every test file in this repo.
"""

import runpy
from pathlib import Path

import pytest


@pytest.fixture
def run_script(request, capsys):
    """Run a .py file exactly as `python <file>` would, and capture its output.

    Returns (stdout, namespace):
      - stdout: everything the script printed, as one string
      - namespace: the script's top-level variables after it finished running,
        for exercises that check a variable's value instead of (or alongside)
        printed output

    Usage in a test:

        def test_prints_hello_world(run_script):
            stdout, _ = run_script("hello_world.py")
            assert stdout.strip() == "Hello, World!"

    The filename is resolved relative to the test file itself, so this works
    whether pytest is run from inside the exercise folder or from the repo
    root.
    """

    def _run(filename):
        script_path = Path(request.fspath).parent / filename
        namespace = runpy.run_path(str(script_path), run_name="__main__")
        captured = capsys.readouterr()
        return captured.out, namespace

    return _run


@pytest.fixture
def expect_output():
    """Assert a script's entire printed output matches exactly, with a
    plain-language failure message instead of pytest's default diff.

    Usage:
        def test_prints_hello_world(run_script, expect_output):
            stdout, _ = run_script("hello_world.py")
            expect_output(stdout, "Hello, World!")
    """

    def _expect(stdout, expected):
        actual = stdout.strip()
        if actual != expected:
            printed = actual if actual else "(nothing at all)"
            pytest.fail(
                "Expected your script to print exactly:\n"
                f"  {expected!r}\n"
                "but it actually printed:\n"
                f"  {printed!r}",
                pytrace=False,
            )

    return _expect


@pytest.fixture
def expect_line():
    """Assert that a specific (1-indexed) line of a script's output matches
    exactly, with a plain-language message — including when the script
    hasn't printed that many lines yet, instead of a raw IndexError.

    Usage:
        def test_prints_the_difference(run_script, expect_line):
            stdout, _ = run_script("add_numbers.py")
            expect_line(stdout, 2, "5")
    """

    def _expect(stdout, line_number, expected):
        lines = stdout.strip().splitlines() if stdout.strip() else []
        if len(lines) < line_number:
            pytest.fail(
                f"Expected your script to print at least {line_number} line(s) "
                f"of output, but it only printed {len(lines)}.\n"
                "Have you added a print() statement for this part yet?",
                pytrace=False,
            )
        actual = lines[line_number - 1]
        if actual != expected:
            pytest.fail(
                f"Line {line_number} of your output should be {expected!r}, "
                f"but it was {actual!r}.",
                pytrace=False,
            )

    return _expect
