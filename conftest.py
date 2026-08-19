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


@pytest.fixture
def expect_variables():
    """Assert that several variables in a script's namespace all match
    expected values at once, with a single friendly summary of everything
    that's missing or wrong — instead of stopping at the first problem
    like expect_variable does.

    Usage:
        def test_conversions_are_correct(run_script, expect_variables):
            _, namespace = run_script("fahrenheit.py")
            expect_variables(namespace, {"fahrenheit": 68.0, "kelvin": 293.15})
    """

    def _expect(namespace, expected):
        missing = [name for name in expected if name not in namespace]
        wrong = {
            name: (namespace[name], expected_value)
            for name, expected_value in expected.items()
            if name in namespace and namespace[name] != expected_value
        }

        if not missing and not wrong:
            return

        lines = []
        if missing:
            names = ", ".join(f"'{name}'" for name in missing)
            lines.append(f"Missing variable(s): {names}. Have you created them yet?")
        for name, (actual, expected_value) in wrong.items():
            lines.append(
                f"'{name}' should be {expected_value!r}, but it was {actual!r}."
            )

        pytest.fail("\n".join(lines), pytrace=False)

    return _expect


@pytest.fixture
def expect_variable_type():
    """Assert that a variable exists and is of a given type, without caring
    about its exact value — e.g. "is this a string" rather than "is this
    exactly 'hello'".

    Usage:
        def test_name_is_a_string(run_script, expect_variable_type):
            _, namespace = run_script("about_you.py")
            expect_variable_type(namespace, "name", str)
    """

    friendly_names = {
        str: "text (str)",
        int: "a whole number (int)",
        float: "a decimal number (float)",
        bool: "True or False (bool)",
        list: "a list",
        dict: "a dictionary",
        tuple: "a tuple",
    }

    def _friendly(t):
        return friendly_names.get(t, t.__name__)

    def _expect(namespace, name, expected_type):
        if name not in namespace:
            pytest.fail(
                f"Expected a variable named '{name}', but it doesn't exist.\n"
                f"Have you created a variable called '{name}' yet?",
                pytrace=False,
            )
        actual = namespace[name]
        if not isinstance(actual, expected_type):
            pytest.fail(
                f"Expected '{name}' to be {_friendly(expected_type)}, "
                f"but it was {_friendly(type(actual))} ({actual!r}).",
                pytrace=False,
            )

    return _expect
