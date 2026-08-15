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
