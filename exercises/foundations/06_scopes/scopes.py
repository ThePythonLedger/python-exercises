# ORBITAL STATION ALPHA - Reactor Rescue
# Every system below is almost working. Find WHERE each variable should live.
# Do not rename the functions - the tests call them by name.


# LEVEL 1 - Power Grid
def boot_system():
    STATION_NAME = "Orbital Station Alpha"
    return f"Booting {STATION_NAME}..."


def show_banner():
    return f"=== {STATION_NAME} ==="


# LEVEL 2 - Life Support
def calibrate_sensors():
    oxygen = 100
    return "Sensors calibrated"


def build_oxygen_monitor():
    def read_level():
        return f"Oxygen at {oxygen}%"

    return read_level


# LEVEL 3 - Comms Array
list = [12, 7, 30]  # incoming signal strengths
sum = 0  # total strength


def summarize_signals():
    return f"{len(list)} signals, strength {sum(list)}"


# LEVEL 4 - Reactor Core
power = 50


def add_bonus_power():
    print("Current power:", power)
    power = power + 10
    return power


# LEVEL 5 - Cargo Bay
def load_crate(item):
    cargo = []
    cargo.append(item)


def get_manifest():
    return cargo


# LEVEL 6 - Alarm System
alarm_count = 0


def trigger_alarm():
    alarm_count = alarm_count + 1
    return alarm_count


# LEVEL 7 - Drone Memory
def make_drone_counter():
    scans = 0

    def scan():
        scans = scans + 1
        return scans

    return scan


# LEVEL 8 - Diagnostics
def _make_secret():
    secret_code = 42
    return "secret stored"


def list_local_names(a, b):
    c = a + b
    # Return a sorted list of the names in THIS function's local namespace.
    pass


def is_global(name):
    # Return True if `name` exists in the global namespace.
    pass


def probe_hidden():
    _make_secret()
    # Try to read `secret_code` here. Return True if Python raises NameError
    # (it is hidden inside _make_secret), otherwise return False.
    pass


# LEVEL 9 - BOSS: Reactor Boot Sequence
def configure_reactor():
    REACTOR_TARGET = 80
    return "Reactor configured"


readings = [72, 91, 85]
max = 0  # highest reading seen so far


def run_station():
    checks = 0

    def run_check(reading):
        checks = checks + 1
        return reading >= REACTOR_TARGET

    results = [run_check(r) for r in readings]
    highest = max(readings)
    return f"Checks: {checks} | Passed: {results.count(True)} | Peak: {highest}"
