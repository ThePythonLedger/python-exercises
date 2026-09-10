# Contributing

Found an issue with an exercise, or have an idea for a new one? Open an issue first before writing any code — it saves everyone rework if the idea doesn't fit the curriculum sequence.

## How tests look like for beginner exercises 
```python
def test_prints_hello_world(run_script):
    stdout, _ = run_script("hello_world.py")
    assert stdout.strip() == "Hello, World!"
```

## No AI generated exercises
This course is to teach students how to code and do things properly. If we use AI what example are we setting?

### Fixtures
Raw pytest failures (`IndexError`, `assert '' == 'Hello, World!'`) are confusing before you know what a list or an assertion diff even is. Script-style tests instead use four shared helpers from `conftest.py`.

We have implemented a few custom functions (*fixtures*) built to make errors less scary for students. Please use these until later exercises where students cover specific erorrs and how to handle them.

* `run_script` - Run a .py file exactly as `python <file>` would, and capture its output.
* `expect_output` - Assert a script's entire printed output matches exactly, with a
    plain-language failure message instead of pytest's default diff.
* `expect_line` - Assert that a specific (1-indexed) line of a script's output matches
    exactly, with a plain-language message — including when the script
    hasn't printed that many lines yet, instead of a raw `IndexError`.
* `expect_variables` - Assert that several variables in a script's namespace all match
    expected values at once, with a single friendly summary of everything
    that's missing or wrong — instead of stopping at the first problem
    like `expect_variable` does.
* `expect_variable_type` - Assert that a variable exists and is of a given type, without caring
    about its exact value — e.g. "is this a string" rather than "is this
    exactly 'hello'".

You can find more about these functions in their docstrings in [conftest.py file](https://github.com/ThePythonLedger/python-exercises/blob/main/conftest.py)

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
