# Exercise 04 — Neural Net Breach (Loops & Control Flow)

## Description
You have gained access to a secure mainframe terminal. To breach the inner vaults, you need to automate your exploit scripts using **`while` loops**, **`for` loops**, and loop controls (**`break`** and **`continue`**).

---

## Tasks

### Task 1: Firewall Override (`while` loop)
Crack the security door lock by counting down security layers.
* You are given a variable `security_level = 5`.
* Initialize a string variable `countdown_log = ""`.
* Write a `while` loop that runs as long as `security_level` is **greater than `0`**.
* Inside the loop:
  * Convert `security_level` to a string and concatenate it (plus a space) onto `countdown_log`.
  * Decrement `security_level` by `1`.
* Result of `countdown_log` should be `"5 4 3 2 1 "`.

> **Next step:** Run pytest. If `test_task_1` passes, open `test_loops.py` and remove the `@pytest.mark.skip` line above `test_task_2`.

---

### Task 2: Power Accumulator (`for` loop with `continue`)
Harvest power units across numbers `1` through `10`, but skip unstable energy frequencies (odd numbers).
* Initialize an integer variable `total_energy = 0`.
* Write a `for` loop using `range(1, 11)`:
  * If the number is **odd** (`number % 2 != 0`), use `continue` to skip it.
  * Otherwise, add the even number to `total_energy`.
* Result of `total_energy` should be `30` (2 + 4 + 6 + 8 + 10).

> **Next step:** Run pytest to verify your energy total.

---

### Task 3: Vault Decryptor (`for` loop with `break`)
Search through code attempts from `1` to `100` until you hit the bypass trigger.
* You are given a target variable `bypass_code = 7`.
* Initialize an integer variable `attempts_made = 0`.
* Write a `for` loop using `range(1, 101)`:
  * Increment `attempts_made` by `1` at the start of each iteration.
  * If the current loop number equals `bypass_code`, trigger a `break` immediately to stop scanning.
* Result of `attempts_made` should be `7`.

### Task 4: Signal Pulse Generator (Nested Loops with `range`)
Generate a matrix of beacon pulses for the tracking grid using nested `range()` calls.
* Initialize an empty string variable named `grid_output = ""`.
* Write an outer `for` loop using `range(1, 4)` representing **sector rows** (`1` to `3`).
* Inside it, write an inner `for` loop using `range(1, 4)` representing **beacon columns** (`1` to `3`).
* On each inner iteration, concatenate `f"[{row},{col}]"` onto `grid_output`.
* At the end of each outer loop iteration (after the inner loop completes), concatenate `"\n"` (a newline) onto `grid_output`.

> **Expected result:** `grid_output` will form a 3x3 text grid of sector-beacon coordinates.

### Task 5: Security Lock Pattern Matching (`while` + `continue` + `break`)
Simulate a keypass brute-force attempt where you skip corrupted attempt indices and stop when you match the key.
* You are given `secret_pin = 42` and `current_attempt = 35`.
* Initialize an integer `valid_checks = 0`.
* Write a `while` loop that runs indefinitely (`while True`):
  * Increment `current_attempt` by `1`.
  * If `current_attempt` is divisible by `5` (e.g., `current_attempt % 5 == 0`), skip it using `continue` (simulating network throttling on multiples of 5).
  * Increment `valid_checks` by `1`.
  * If `current_attempt == secret_pin`, trigger a `break` immediately.

> **Expected result:** `valid_checks` counts only non-throttled attempts made before hitting pin `42`.

---

## How to Run the Tests
Run the following command from the root folder:
```bash
python check.py 04
```

## Resources
Review the concepts covered in this exercise in [The Python Ledger lesson on Loops](https://thepythonledger.github.io/Docusaurus-engine/lessons/python-foundations/loops).