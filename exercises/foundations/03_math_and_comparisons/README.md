# Exercise 03 - Math, String Operations, and Comparisons

## Description
In this exercise, you will build basic RPG combat mechanics to practice working with numbers, string manipulation, and comparison operators.

## Tasks

### Task 1: Character Setup
Define the following variables with their exact values:
* `player_class` — string set to `"Wizard"`
* `player_attack` — integer set to `35`
* `player_defense` — integer set to `13`
* `enemy_attack` — integer set to `28`
* `enemy_defense` — integer set to `16`

> **Next step:** Run tests. If `test_task_1` passes, open your test file and remove the `@pytest.mark.skip` decorator above `test_task_2`.

### Task 2: Calculate Power Ratings
* Define `player_attack_power` by multiplying `player_attack` by `player_defense`.
* Define `enemy_attack_power` by multiplying `enemy_attack` by `enemy_defense`.

> **Next step:** Run tests. If `test_task_2` passes, open your test file and remove the `@pytest.mark.skip` decorator above `test_task_3`.

### Task 3: Resolve Damage
* Define `damage_dealt` by subtracting `enemy_attack_power` from `player_attack_power`.

> **Next step:** Run tests. If `test_task_3` passes, open your test file and remove the `@pytest.mark.skip` decorator above `test_task_4`.

### Task 4: Output the Combat Log
* Define a variable named `combat_log` using an **f-string**.
* The string must format `player_class` in **ALL CAPS** and insert `damage_dealt`:
  `"WIZARD has suffered 7 damage."`

> **Next step:** Run tests. If `test_task_4` passes, open your test file and remove the `@pytest.mark.skip` decorator above `test_task_5`.

### Task 5: Battle Comparisons
* Define a boolean `is_player_stronger` that checks if `player_attack_power` is greater than `enemy_attack_power`.
* Define a boolean `is_balanced` that checks if `player_defense` is equal to `enemy_defense`.

> **Next step:** Run tests. If `test_task_5` passes, open your test file and remove the `@pytest.mark.skip` decorator above `test_task_6`.

### Task 6: Class Code Extraction
* Define a variable `class_initial` that extracts the **first letter** of `player_class`.
* Define a variable `class_code` that extracts the **first 3 letters** of `player_class` in lowercase (e.g., `"wiz"`).

> **Next step:** Run tests. If `test_task_6` passes, congratulation, you have successfully passed this exercise.

---

## Notes
Review the concepts covered in this exercise in [The Python Ledger lesson](https://thepythonledger.github.io/Docusaurus-engine/lessons/python-foundations/math-strops-and-comparisons).
