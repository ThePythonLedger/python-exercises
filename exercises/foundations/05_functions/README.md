# Exercise 05 - Orbital Cargo Dispatch (Functions)

## Description
Welcome aboard the Orbital Freight Dispatch Center! Freight shuttles constantly arrive and depart between orbital stations and asteroid mining hubs. Up until now, flight coordinators have been manually copying and pasting repetitive calculation blocks for each flight manifest.

In this exercise, you will bundle these operations into reusable, modular **functions** using the `def` keyword, parameters, default argument values, and `return` statements, adhering to the **DRY (Don't Repeat Yourself)** principle.

---

## Tasks

### Task 1: Pilot Identification (`def`, parameter, string return)
Write a function named `greet_pilot(name)` that takes a pilot's name as a parameter and returns a formal flight greeting.
* **Parameters**: `name` (a string)
* **Returns**: A formatted string: `"Welcome aboard, Commander {name}. Flight systems ready."`
* **Example**:
  ```python
  greet_pilot("Alfred")
  # Returns: "Welcome aboard, Commander Alfred. Flight systems ready."
  ```

> **Next step:** Run `python check.py 05`. Once Task 1 passes, open `test_functions.py` and remove the `@pytest.mark.skip` line above `test_task2`.

---

### Task 2: Fuel Consumption Calculator (Multiple parameters, arithmetic, return)
Write a function named `calculate_fuel(distance, burn_rate)` that calculates the total fuel needed for a transit jump.
* **Parameters**:
  * `distance` (int or float) — distance in light-sectors
  * `burn_rate` (int or float) — fuel units consumed per sector
* **Returns**: The total fuel units required as a `float` (`distance * burn_rate`).
* **Example**:
  ```python
  calculate_fuel(10, 2.5)
  # Returns: 25.0
  ```

> **Next step:** Run tests. If Task 2 passes, open `test_functions.py` and remove the `@pytest.mark.skip` line above `test_task3`.

---

### Task 3: Trip Cost with Standard Fuel Rate (Default parameter values)
Write a function named `calculate_trip_cost(fuel_needed, price_per_unit=2.5)` that computes the credit cost for fueling a shuttle.
* **Parameters**:
  * `fuel_needed` (int or float) — amount of fuel required
  * `price_per_unit` (int or float, default `2.5`) — cost in credits per fuel unit
* **Returns**: Total credit cost as a `float` (`fuel_needed * price_per_unit`).
* **Example**:
  ```python
  # Using default fuel price (2.5)
  calculate_trip_cost(10)
  # Returns: 25.0

  # Specifying custom fuel price (3.0)
  calculate_trip_cost(10, 3.0)
  # Returns: 30.0
  ```

> **Next step:** Run tests. If Task 3 passes, open `test_functions.py` and remove the `@pytest.mark.skip` line above `test_task4`.

---

### Task 4: Manifest Broadcast (`print()` vs. `return`)
Write a function named `display_manifest(cargo_item, quantity, priority="STANDARD")` that outputs cargo telemetry to the terminal screen.
* **Parameters**:
  * `cargo_item` (string) — the name of the cargo item (e.g. `"Minerals"`)
  * `quantity` (int) — number of cargo crates
  * `priority` (string, default `"STANDARD"`) — shipment priority level
* **Output**: Must print exactly two lines to the console:
  ```text
  [CARGO] {quantity}x {cargo_item}
  [STATUS] Priority: {priority}
  ```
* **Return value**: This function must **not** return anything (it should implicitly return `None`). Remember: `print()` displays text on the screen for humans to read, while `return` hands data back to the program.
* **Example**:
  ```python
  result = display_manifest("Titanium", 50, "HIGH")
  # Console output:
  # [CARGO] 50x Titanium
  # [STATUS] Priority: HIGH
  # result is None
  ```

> **Next step:** Run tests. If Task 4 passes, open `test_functions.py` and remove the `@pytest.mark.skip` line above `test_task5`.

---

### Task 5: Dispatch Summary Pipeline (Function Composition & DRY)
Bring your modular functions together to generate a complete flight dispatch summary without duplicating math calculations.
Write a function named `create_dispatch_summary(pilot_name, distance, burn_rate=1.5, price_per_unit=2.5)`.
* **Parameters**:
  * `pilot_name` (string)
  * `distance` (int or float)
  * `burn_rate` (int or float, default `1.5`)
  * `price_per_unit` (int or float, default `2.5`)
* **Logic**:
  1. Call `calculate_fuel(distance, burn_rate)` to compute fuel needed.
  2. Call `calculate_trip_cost(fuel_needed, price_per_unit)` to compute total cost.
  3. Return a formatted string:
     `"Dispatch Plan for {pilot_name}: {fuel_needed} fuel units required. Total cost: {total_cost} credits."`
* **Example**:
  ```python
  create_dispatch_summary("Alex", 100, 2.0, 3.0)
  # Returns: "Dispatch Plan for Alex: 200.0 fuel units required. Total cost: 600.0 credits."

  # Using default rates:
  create_dispatch_summary("Alex", 100)
  # Returns: "Dispatch Plan for Alex: 150.0 fuel units required. Total cost: 375.0 credits."
  ```

> **Next step:** Run tests. If Task 5 passes, congratulations! You have completed Exercise 05.

---

## How to Run the Tests
Run the following command from the repository root:
```bash
python check.py 05
```

Or run directly with pytest:
```bash
pytest exercises/foundations/05_functions/test_functions.py -v
```

---

## Resources & Notes
Review the concepts covered in this exercise in:
* [The Python Ledger Curriculum: Functions](https://thepythonledger.github.io/Docusaurus-engine/lessons/code-organization/functions)
