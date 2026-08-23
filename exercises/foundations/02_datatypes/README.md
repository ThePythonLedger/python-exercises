# Exercise 02 — Space Station Diagnostic System

## Description
Welcome aboard the ORION-9 deep-space research station! The central terminal suffered a reboot after a cosmic flare. Before life support and navigation systems can come back online, you must manually declare and initialize the core system variables.

This exercise will guide you through Python's core data types: **String**, **Integer**, **Float**, **Boolean**, and **None**, along with basic type casting and printing.

---

## Tasks

### Task 1: Initialize System Identity
Declare the station's core identification variables:
* `station_name` — a **string** representing the station name (e.g., `"Orion 9"`)
* `module_count` — an **integer** representing active station modules (e.g., `12`)
* `signal_frequency` — a **float** representing the sub-space signal frequency (e.g., `1420.405`)
* `life_support_active` — a **boolean** set to `True`
* `backup_generator` — set to `None` (representing an offline component)

> **Next step:** Run the test suite. If `test_task_1` passes, open `test_core_datatypes.py` and remove the `@pytest.mark.skip` line above `test_task_2`.

### Task 2: Type Casting & Calibration
The telemetry unit sent data in the wrong format! Fix the formats using type casting:
* `raw_energy_reading` is provided as `"100"` (a string). Create a new variable `energy_level` by casting `raw_energy_reading` to an **integer**.
* `raw_distance_reading` is provided as `45` (an integer). Create a new variable `exact_distance` by casting `raw_distance_reading` to a **float**.
* `raw_status_code` is provided as `1` (an integer). Create a new variable `is_operational` by casting `raw_status_code` to a **boolean**.

> **Next step:** Run the test suite. If `test_task_2` passes, open `test_core_datatypes.py` and remove the `@pytest.mark.skip` line above `test_task_3`.

### Task 3: Terminal Broadcast
* Create a variable `station_status` by converting `module_count` to a string and concatenating it with `station_name` (e.g., `"12 - Orion 9"`).
* Print `station_status` to the terminal console using the `print()` function.

> **Next step:** Run the test suite. If `test_task_3` passes, congrats! You have completed then exercise.

---

## How to Run the Tests
Run the following command from the root directory:
```bash
python check.py 02
```

## Resources
Review the core concepts in [The Python Ledger lesson on Core Datatypes](https://thepythonledger.github.io/Docusaurus-engine/lessons/python-foundations/core-datatypes).