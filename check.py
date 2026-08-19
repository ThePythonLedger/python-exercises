import subprocess
import sys
from pathlib import Path

INSTALL_PYTEST_INSTRUCTIONS = """
python -m venv .venv
source .venv/bin/activate
pip install pytest
"""


def check_for_pytest():
    try:
        import pytest  # pyright: ignore[reportMissingImports] # noqa: F401
    except ImportError:
        print(
            "❌ No `pytest` installed.\nPlease install `pytest` first.\nRun the following commands, one by one:"
        )


def resolve_exercise_path(query: str) -> Path:
    target = Path(query)
    if target.exists():
        return target

    # Exclude non-exercise folders
    IGNORED_DIRS = {"__pycache__"}

    matches = []
    root = Path("./exercises")

    for sub_dir in root.iterdir():
        if (
            sub_dir.is_dir()
            and sub_dir.name not in IGNORED_DIRS
            and not sub_dir.name.startswith(".")
        ):
            matches.extend(sub_dir.glob(f"*{query}*"))

    dirs_only = [m for m in matches if m.is_dir()]

    if len(dirs_only) == 1:
        return dirs_only[0]
    elif len(dirs_only) > 1:
        print(f"⚠️ Ambiguous query '{query}'. Did you mean one of these?")
        for match in dirs_only:
            print(f"  - {match}")
        sys.exit(1)

    print(f"❌ No exercise folder found for: '{query}'")
    sys.exit(1)


def filter_for_excercises_only(exercise_path: Path):
    for path in exercise_path.iterdir():
        if (
            not path.is_dir()
            and not path.name.endswith("solution.py")
            and path.name.endswith(".py")
            and path.name.startswith("test_")
        ):
            print(f"Found: {path}")
            return path


def main():
    if len(sys.argv) < 2:
        print("Usage: python check.py <exercise-folder-or-number>")
        sys.exit(1)

    exercise_path = resolve_exercise_path(sys.argv[1])
    excercise_only_tests = filter_for_excercises_only(exercise_path)

    # pytest test_<exercise_name>.py -v
    cmd = ["pytest", str(excercise_only_tests)]
    result = subprocess.run(cmd)

    if result.returncode == 0:
        print("\n✨ All tests passed! Great job!")


if __name__ == "__main__":
    main()
