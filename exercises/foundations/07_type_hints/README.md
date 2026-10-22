# Exercise 07 - Station Telemetry Relay (Type Hints)

## Description

Following the reactor stabilization on Orbital Station Alpha, the station's deep-space communications array has re-established links with incoming automated supply freighters, long-range probes, and orbital sensor buoys.

However, during the crisis, technicians hastily wrote telemetry translation scripts without any data type documentation. Incoming navigation computers and automated dock controllers are failing to handshake because the data contracts are ambiguous:
* Is `channel` an integer or a string?
* Does `lookup_beacon()` return a float or `None` when a buoy is out of range?
* What exact structure does a navigation coordinate tuple require?

Your mission as Telemetry Systems Lead is to inspect `type_hints.py` and supply explicit, modern **type hints** level-by-level to establish clear communication contracts between Station Alpha and incoming spacecraft.

> **Important**: Do not change the function names or modify their internal logic. Your task is to add the correct type annotations to the signatures, type aliases, and module variables.

---

## Levels

### Level 1 - Comm Link Beacon (Primitives & Default Values)
The main transmitter `format_signal` formats outgoing frequency announcements for approaching shuttles.
* **Function**: `format_signal(channel, frequency, active=True)`
* **Your job**:
  * Annotate `channel` as an `int`.
  * Annotate `frequency` as a `float`.
  * Annotate `active` as a `bool` with its default value `True`. (Remember: put the type hint first, followed by the default: `active: bool = True`).
  * Annotate the return type as `str`.
* **Expected return**: e.g., `"Channel 1 (142.5 MHz) is ONLINE."`

> **Next step:** Run `python check.py 07`. Once Level 1 passes, open `test_type_hints.py` and remove the `@pytest.mark.skip` line above `test_level2`.

---

### Level 2 - Terminal Broadcast (`-> None`)
The station terminal logs outgoing alerts to the dispatch console. Functions that perform side effects (such as printing) and return no value must be annotated with `-> None`.
* **Function**: `log_transmission(message, priority=1)`
* **Your job**:
  * Annotate `message` as a `str`.
  * Annotate `priority` as an `int` with default value `1`.
  * Annotate the return type as `None` (`-> None`).

> **Next step:** Unlock `test_level3`.

---

### Level 3 - Cargo Manifest Filter (Collection Generics: `dict` and `list`)
The automated docking crane reads an incoming cargo manifest dictionary mapping item names to weights in metric tons, producing a list of container names exceeding a safety threshold.
* **Function**: `filter_heavy_cargo(manifest, threshold)`
* **Your job**:
  * Annotate `manifest` as a dictionary with `str` keys and `float` values (`dict[str, float]`).
  * Annotate `threshold` as a `float`.
  * Annotate the return type as a list of strings (`list[str]`).

> **Next step:** Unlock `test_level4`.

---

### Level 4 - Navigation Vectors (Fixed-Length vs. Variable-Length Tuples)
Docking computers calculate distance between coordinate pairs of exactly two floats, while telemetry recorders bundle an arbitrary number of waypoint tags into an immutable sequence.
* **Function A**: `calculate_vector_distance(point_a, point_b)`
  * `point_a` and `point_b`: tuples containing **exactly two floats** (`tuple[float, float]`).
  * Return type: `float`.
* **Function B**: `bundle_waypoint_names(waypoints)`
  * `waypoints`: a list of strings (`list[str]`).
  * Return type: a tuple of **any length** containing strings (`tuple[str, ...]`).

> **Next step:** Unlock `test_level5`.

---

### Level 5 - Beacon Lookup & Sensor Normalization (Missing Values & Unions)
Sensors might query an offline buoy (returning `None`), or receive raw telemetry in mixed numeric formats (`int` or `float`). In modern Python, use the pipe operator (`|`).
* **Function A**: `lookup_beacon(beacons, beacon_id)`
  * `beacons`: dictionary with `str` keys and `float` values (`dict[str, float]`).
  * `beacon_id`: `str`.
  * Return type: a `float` or `None` (`float | None`).
* **Function B**: `normalize_reading(reading)`
  * `reading`: accepts either an `int` or a `float` (`int | float`).
  * Return type: `float`.

> **Next step:** Unlock `test_level6`.

---

### Level 6 - Station Telemetry Buffers (Variable Annotations)
When initializing empty collections or nullable state variables at the module level, type annotations clarify what data will be stored before values arrive.
* **Your job**: Annotate the three module-level buffer variables in `type_hints.py`:
  * `active_relays`: a list of strings, initialized to `[]` (`list[str] = []`).
  * `calibration_cache`: a dictionary mapping strings to floats, initialized to `{}` (`dict[str, float] = {}`).
  * `current_target`: an optional string, initialized to `None` (`str | None = None`).

> **Next step:** Unlock `test_level7`.

---

### Level 7 - Telemetry Protocol (Type Aliases)
When type annotations become long or repetitive, define **Type Aliases** to keep your signatures readable and clean.
* **Your job**:
  1. Define two type aliases at the module level:
     * `Coordinate2D = tuple[float, float]`
     * `SensorMap = dict[str, float]`
  2. Annotate `validate_docking_clearance(origin, target, clearances)`:
     * `origin`: `Coordinate2D`
     * `target`: `Coordinate2D`
     * `clearances`: `SensorMap`
     * Return type: `bool`

> **Next step:** Unlock `test_level8`.

---

### Level 8 - BOSS: Flight Dispatch Pipeline (Integration)
Bring your complete type hinting toolkit together! The Master Flight Computer compiles a batch of incoming shuttle records into an eligible launch roster.
* **Your job**:
  1. Define a type alias named `FlightRecord`:
     * `FlightRecord = dict[str, str | float | None]`
  2. Annotate `compile_dispatch_report(records, max_distance=500.0)`:
     * `records`: a list of flight records (`list[FlightRecord]`).
     * `max_distance`: a `float` with default value `500.0` (`max_distance: float = 500.0`).
     * Return type: a tuple containing an `int` (count of ships) and a `list[str]` (ship callsigns): `tuple[int, list[str]]`.

> **Next step:** If Level 8 passes, congratulations! You have restored the telemetry protocol on Station Alpha!

---

## How to Run the Tests

Run the test suite using `check.py` from the repository root:
```bash
python check.py 07
```

Or run directly with `pytest`:
```bash
pytest exercises/foundations/07_type_hints/test_type_hints.py -v
```

---

## Resources & Notes
Review the concepts covered in this exercise in:
* [The Python Ledger Curriculum: Clearer Code with Type Hints](https://thepythonledger.github.io/Docusaurus-engine/lessons/code-organization/type-hints)
