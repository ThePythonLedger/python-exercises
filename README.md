# Python Exercises

These exercises are intended to complement [The Python Ledger](https://thepythonledger.github.io/Docusaurus-engine/) curriculum. They should be done alongside the matching lessons, not treated as a standalone tutorial.

> **Note:** Please don't open a PR with your completed solutions. If merged, the exercises would stop being blank for the next learner, and it just creates extra work reverting it. Feel free to commit and push to your own fork though — practicing git is part of the point.

## How To Use These Exercises

1. **Fork and clone** this repository.
    **Forking** is making copies of somebody elses code under your own profile. This is standard practice in open source. Follow [Guide on Forking Repository](https://docs.github.com/en/pull-requests/how-tos/work-with-forks/fork-a-repo#forking-a-repository) to learn more on how it works.

    **Cloning** is downloading repository to your own local machine so you can modify and run it. Follow [Guide on Cloning Repository](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository-from-github/cloning-a-repository) to learn more about how this works.
2. **Install dependencies.** From the repo root:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements-dev.txt
   ```
3. **Each exercise directory contains:**
   - `README.md` — the task description
   - `<exercise_name>.py` — a mostly-empty file where you write your code
   - `test_<exercise_name>.py` — the tests that check your code
   - `solution/` — a reference solution, plus the same tests fully unlocked
4. **Run tests for first exercise** by running:
   ```bash
   python check.py 01
   ```
   The first run will fail. That's expected — open the exercise file and write the code needed to make it pass.

   All excercises are marked numericly, so you can use the number, or use the full path to test (TAB completions work too)
   ```bash
   python check.py foundations/01_hello_world
   ```
5. **Some tests start marked `@pytest.mark.skip`.** This is intentional, same idea as unlocking levels. Once the active test passes, open the spec file, remove the `@pytest.mark.skip(...)` line above the next test, and run again. Keep going until every test in the file passes with no skips left.
6. **Once you're done**, compare against `solution/` — but not before. There's more than one valid way to pass the tests; the solution is just one example.

The first exercise, `01_hello_world`, walks through this whole process in detail.

## Contributing

Suggestions for new exercises or fixes to existing ones are welcome — see `CONTRIBUTING.md`.
