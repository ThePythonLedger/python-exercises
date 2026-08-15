# Python Exercises

These exercises are intended to complement [The Python Ledger](https://thepythonledger.github.io/Docusaurus-engine/) curriculum. They should be done alongside the matching lessons, not treated as a standalone tutorial.

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

## Debugging

Run with `pytest test_<exercise_name>.py -v --pdb` to drop into the debugger on the first failure, or set a breakpoint directly in your code with `breakpoint()`.

## Contributing

Suggestions for new exercises or fixes to existing ones are welcome — see `CONTRIBUTING.md`.
