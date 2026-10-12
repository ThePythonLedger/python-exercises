# Exercise 06 - Scope Station: Reactor Rescue (Scope and Namespaces)

## Description
Orbital Station Alpha is failing! Engineers rushed the code and left variables in the wrong places: some are trapped inside functions, some are missing the right keyword, and some are hiding Python's own tools.

This is a **debugging game**. `scopes.py` is already written, but it is *almost* working. Your job in each level is to figure out **where each variable must live** (and which keyword, if any, it needs) so the system runs.

Remember the question from the lesson: *"Where does this name live, and who needs to see it?"*

> Do not rename the functions. The tests call them by name. You decide where the variables go.

---

## Levels

### Level 1 - Power Grid (Local vs. Global)
`show_banner()` crashes with a `NameError`. The station name is created inside `boot_system()`, but two functions need it.
* **Your job**: make both `boot_system()` and `show_banner()` work.
* **Expected**: `show_banner()` returns `"=== Orbital Station Alpha ==="`.

> **Next step:** Run `python check.py 06`. Once Level 1 passes, remove the `@pytest.mark.skip` line above `test_level2` in `test_scopes.py`.

### Level 2 - Life Support (Enclosing Scope)
`build_oxygen_monitor()` returns an inner function `read_level()`, but it can't find the oxygen value.
* **Your job**: put `oxygen` where `read_level()` can find it by looking outward, and don't use a global.
* **Expected**: the monitor returns `"Oxygen at 100%"`.

> **Next step:** Unlock `test_level3`.

### Level 3 - Comms Array (Built-in Scope)
`summarize_signals()` fails with `TypeError: ... object is not callable`. Something is hiding Python's built-in tools.
* **Your job**: find what is shadowing the built-ins and fix it.
* **Expected**: `"3 signals, strength 49"`.

> **Next step:** Unlock `test_level4`.

### Level 4 - Reactor Core (`UnboundLocalError`)
`add_bonus_power()` crashes with `UnboundLocalError`.
* **Your job**: fix it by sending the value **in** with a parameter and sending the result **out** with `return`. The global `power` must stay `50`, and `global` is not allowed in this level.
* **Expected**: `add_bonus_power(50)` returns `60`.

> **Next step:** Unlock `test_level5`.

### Level 5 - Cargo Bay (Mutable Objects)
`load_crate()` adds items to a list that vanishes when the function ends, and `get_manifest()` can't find it.
* **Your job**: make both functions share the same list. You don't need `global`, because you only change the list's contents.
* **Expected**: loading `"Titanium"` then `"Ice"` gives a manifest ending in `["Titanium", "Ice"]`.

> **Next step:** Unlock `test_level6`.

### Level 6 - Alarm System (`global`)
`trigger_alarm()` should count alarms in the global `alarm_count`, but crashes.
* **Your job**: let the function rebind the global variable.
* **Expected**: three calls return `1`, `2`, `3` (from a fresh start) and `alarm_count` ends up updated.

> **Next step:** Unlock `test_level7`.

### Level 7 - Drone Memory (`nonlocal`)
Each drone made by `make_drone_counter()` should remember how many scans it did, but `scan()` crashes.
* **Your job**: let the inner function update the enclosing variable.
* **Expected**: one drone counts `1, 2, 3`, and a second drone starts again at `1`.

> **Next step:** Unlock `test_level8`.

### Level 8 - Diagnostics (`globals()` and `locals()`)
Complete the three helper functions in the `LEVEL 8` section:
* `list_local_names(a, b)`: return a **sorted list** of the names in the function's local namespace.
* `is_global(name)`: return `True` if `name` exists in the global namespace.
* `probe_hidden()`: try to read `secret_code` (it only exists inside `_make_secret()`). Return `True` if Python raises `NameError`.

> **Next step:** Unlock `test_level9`.

### Level 9 - BOSS: Reactor Boot Sequence
`run_station()` has **three** different scope bugs at once. Use everything you have learned.
* **Expected**: `"Checks: 3 | Passed: 2 | Peak: 91"`.

> **Next step:** If Level 9 passes, congratulations! You saved the station.

---

## How to Run the Tests
Run the following command from the repository root:
```bash
python check.py 06
```

Or run directly with pytest:
```bash
pytest exercises/foundations/06_scopes/test_scopes.py -v
```

---

## Resources & Notes
Review the concepts covered in this exercise in:
* [The Python Ledger Curriculum: Scope and Namespaces](https://thepythonledger.github.io/Docusaurus-engine/lessons/code-organization/scope-and-namespaces)
