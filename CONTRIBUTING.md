# Contributing

Found an issue with an exercise, or have an idea for a new one? Open an issue first before writing any code — it saves everyone rework if the idea doesn't fit the curriculum sequence.

## How tests look like for beginner exercises 
Let's look at the test file first:

```python
def test_prints_hello_world(run_script):
    stdout, _ = run_script("hello_world.py")
    assert stdout.strip() == "Hello, World!"
```

`run_script` is a helper set up once for the whole repo. It runs `hello_world.py` exactly the way Python would if you typed `python hello_world.py`, and hands back everything it printed. The test then checks that what got printed matches `'Hello, World!'` exactly — capitalization and punctuation included.


## Two exercise styles

Early exercises don't assume you know about functions yet, so they're written as **plain scripts** — top-level code you'd type straight into the terminal, no `def` or `import`. Their tests use a shared `run_script` fixture (see `conftest.py`) that runs the file exactly like `python <file>.py` and checks what it printed.

Once functions show up in the curriculum, exercises switch to the **function style** you may be more used to seeing: a stub function you fill in, imported directly into the test file. Each exercise's README says which style it is, but you can also tell from the stub file itself — a bare script vs. a `def`.

## Running everything at once

From the repo root, `pytest` (no arguments) will discover and run every non-skipped test in the repo — handy as a sanity check, but exercises are meant to be done one at a time.


## Adding a new exercise

Don't build the folder by hand. Use the generator:

```bash
python scripts/new_exercise.py <category_path> "<Exercise Title>" [--style script|function]
```

`--style script` (the default) scaffolds a plain-script exercise with no functions — use this for anything that comes before functions are introduced in the curriculum. Its tests use the shared `run_script` fixture in the root `conftest.py`.

`--style function` scaffolds the def-and-import style — use this once functions have been taught.

Examples:

```bash
python scripts/new_exercise.py foundations "Say Hi"
python scripts/new_exercise.py foundations "Number Checker" --style function
```

This creates a numbered directory (auto-incremented within that category) with a README stub, an empty exercise file, a placeholder test file, and a matching `solution/` folder. Fill in:

1. The `README.md` — a clear task description, plus any notes on edge cases.
2. The exercise stub — keep it minimal, just a function signature and a docstring or `pass`.
3. The test file — write the *real* tests here. The first test should be un-skipped; every subsequent test should start with `@pytest.mark.skip(reason="...")` so learners unlock them one at a time.
4. `solution/` — a working reference implementation, and the same test file with every `@pytest.mark.skip` removed.

Before opening a PR, run `pytest` from the `solution/` directory to confirm your reference solution actually passes its own fully-unlocked tests.
