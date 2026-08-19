#!/usr/bin/env python3
"""Scaffold a new exercise: README, stub, test file, and a matching solution/.

Usage:
    python scripts/new_exercise.py <category_path> "<Exercise Title>" [--style script|function]

--style script    (default) plain top-level code, no def/import needed.
                  Use this for anything before functions are taught in
                  the curriculum. Tests use the shared `run_script`
                  fixture from the root conftest.py.
--style function  the exercise defines and exports a function, tested by
                  importing it directly. Use this once functions have
                  been introduced.

Examples:
    python scripts/new_exercise.py foundations "Say Hi"
    python scripts/new_exercise.py foundations "Number Checker" --style function
"""

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

FUNCTION_README_TEMPLATE = """# Exercise {number:02d} - {title}

## Description

TODO: describe the task here. What should `{func_name}` do? What are its
inputs and expected output?

## Notes

TODO: mention any edge cases, hints, or background concepts a learner
needs before attempting this.
"""

FUNCTION_STUB_TEMPLATE = '''def {func_name}():
    """TODO: implement me."""
    pass
'''

FUNCTION_TEST_TEMPLATE = '''import pytest

from {module_name} import {func_name}


def test_{func_name}_placeholder():
    """TODO: replace with a real assertion, then add more tests below
    using @pytest.mark.skip(reason="...") on all but the first."""
    assert {func_name}() is None
'''

FUNCTION_SOLUTION_TEMPLATE = '''def {func_name}():
    """TODO: write the reference solution."""
    raise NotImplementedError
'''

SCRIPT_README_TEMPLATE = """# Exercise {number:02d} - {title}

## Description

TODO: describe the task here. This is a script-style exercise — plain
top-level code, no functions needed. Say what the script should print
(or which variables it should end up with).

### Run the tests
To run the tests, run the following command in the directory root (`python-excercises`):
```bash
python check.py {number:02d}
```

## Notes

TODO: mention any edge cases, hints, or background concepts a learner
needs before attempting this.
"""

SCRIPT_STUB_TEMPLATE = """# TODO: write your code here
"""

SCRIPT_TEST_TEMPLATE = '''def test_{func_name}_placeholder(run_script):
    """TODO: replace with a real assertion, then add more tests below
    using @pytest.mark.skip(reason="...") on all but the first.
    `run_script` returns (stdout, namespace) — check printed output via
    stdout, or a variable's value via namespace["some_var"]."""
    stdout, _ = run_script("{module_name}.py")
    assert stdout.strip() == ""
'''

SCRIPT_SOLUTION_TEMPLATE = """# TODO: write the reference solution here (plain top-level code)
"""


def to_snake_case(name: str) -> str:
    """Turn a human title like 'Number Checker' into 'number_checker'."""
    name = re.sub(r"[\s\-]+", "_", name.strip())
    name = re.sub(r"(?<!^)(?=[A-Z])", "_", name)
    name = re.sub(r"_+", "_", name)
    return name.lower()


def next_number(category_dir: Path) -> int:
    """Find the next free numeric prefix within a category directory."""
    if not category_dir.exists():
        return 1
    existing = [
        p for p in category_dir.iterdir() if p.is_dir() and re.match(r"^\d+_", p.name)
    ]
    numbers = [int(p.name.split("_", 1)[0]) for p in existing]
    return max(numbers, default=0) + 1


def create_exercise(category_path: str, title: str, style: str) -> None:
    category_dir = ROOT / category_path
    category_dir.mkdir(parents=True, exist_ok=True)

    func_name = to_snake_case(title)
    number = next_number(category_dir)
    dir_name = f"{number:02d}_{func_name}"
    exercise_dir = category_dir / dir_name
    solution_dir = exercise_dir / "solution"

    if exercise_dir.exists():
        print(f"Refusing to overwrite existing directory: {exercise_dir}")
        sys.exit(1)

    solution_dir.mkdir(parents=True)

    module_name = func_name
    solution_module_name = f"{func_name}_solution"

    if style == "function":
        (exercise_dir / "README.md").write_text(
            FUNCTION_README_TEMPLATE.format(
                number=number, title=title, func_name=func_name
            )
        )
        (exercise_dir / f"{module_name}.py").write_text(
            FUNCTION_STUB_TEMPLATE.format(func_name=func_name)
        )
        (exercise_dir / f"test_{module_name}.py").write_text(
            FUNCTION_TEST_TEMPLATE.format(module_name=module_name, func_name=func_name)
        )
        (solution_dir / f"{solution_module_name}.py").write_text(
            FUNCTION_SOLUTION_TEMPLATE.format(func_name=func_name)
        )
        (solution_dir / f"test_{solution_module_name}.py").write_text(
            FUNCTION_TEST_TEMPLATE.format(
                module_name=solution_module_name, func_name=func_name
            )
        )
    else:
        (exercise_dir / "README.md").write_text(
            SCRIPT_README_TEMPLATE.format(number=number, title=title)
        )
        (exercise_dir / f"{module_name}.py").write_text(SCRIPT_STUB_TEMPLATE)
        (exercise_dir / f"test_{module_name}.py").write_text(
            SCRIPT_TEST_TEMPLATE.format(func_name=func_name, module_name=module_name)
        )
        (solution_dir / f"{solution_module_name}.py").write_text(
            SCRIPT_SOLUTION_TEMPLATE
        )
        (solution_dir / f"test_{solution_module_name}.py").write_text(
            SCRIPT_TEST_TEMPLATE.format(
                func_name=func_name, module_name=solution_module_name
            )
        )

    print(f"Created {exercise_dir.relative_to(ROOT)} (style: {style})")
    print("Next steps:")
    print(f"  1. Write the real task description in {exercise_dir / 'README.md'}")
    print(f"  2. Write real tests in {exercise_dir / f'test_{module_name}.py'}")
    print("     (first test unskipped, rest behind @pytest.mark.skip)")
    print(f"  3. Write the reference solution in {solution_dir}")
    print(f"     then verify with: cd {solution_dir} && pytest -v")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("category_path", help="e.g. foundations")
    parser.add_argument("title", help="e.g. 'Number Checker'")
    parser.add_argument(
        "--style",
        choices=["script", "function"],
        default="script",
        help="script (default, no functions) or function (import + call a function)",
    )
    args = parser.parse_args()
    create_exercise(args.category_path, args.title, args.style)


if __name__ == "__main__":
    main()
