# Python Exercises

These exercises are intended to complement [The Python Ledger](https://github.com/) curriculum. They should be done alongside the matching lessons, not treated as a standalone tutorial.

> **Note:** Please don't open a PR with your completed solutions. If merged, the exercises would stop being blank for the next learner, and it just creates extra work reverting it. Feel free to commit and push to your own fork though — practicing git is part of the point.

## How To Use These Exercises

1. **Fork and clone** this repository.
2. **Install dependencies.** From the repo root:
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # .venv\Scripts\activate on Windows
   pip install -r requirements-dev.txt
   ```
3. **Each exercise directory contains:**
   - `README.md` — the task description
   - `<exercise_name>.py` — a mostly-empty file where you write your code
   - `test_<exercise_name>.py` — the tests that check your code
   - `solution/` — a reference solution, plus the same tests fully unlocked
4. **Run tests for one exercise** by `cd`-ing into its folder and running:
   ```bash
   pytest test_<exercise_name>.py -v
   ```
   The first run will fail. That's expected — open the exercise file and write the code needed to make it pass.
5. **Some tests start marked `@pytest.mark.skip`.** This is intentional, same idea as unlocking levels. Once the active test passes, open the spec file, remove the `@pytest.mark.skip(...)` line above the next test, and run again. Keep going until every test in the file passes with no skips left.
6. **Once you're done**, compare against `solution/` — but not before. There's more than one valid way to pass the tests; the solution is just one example.

The first exercise, `01_hello_world`, walks through this whole process in detail.

## Two exercise styles

Early exercises don't assume you know about functions yet, so they're written as **plain scripts** — top-level code you'd type straight into the terminal, no `def` or `import`. Their tests use a shared `run_script` fixture (see `conftest.py`) that runs the file exactly like `python <file>.py` and checks what it printed.

Once functions show up in the curriculum, exercises switch to the **function style** you may be more used to seeing: a stub function you fill in, imported directly into the test file. Each exercise's README says which style it is, but you can also tell from the stub file itself — a bare script vs. a `def`.

## Running everything at once

From the repo root, `pytest` (no arguments) will discover and run every non-skipped test in the repo — handy as a sanity check, but exercises are meant to be done one at a time.

## Debugging

Run with `pytest test_<exercise_name>.py -v --pdb` to drop into the debugger on the first failure, or set a breakpoint directly in your code with `breakpoint()`.

## Contributing

Suggestions for new exercises or fixes to existing ones are welcome — see `CONTRIBUTING.md`.
