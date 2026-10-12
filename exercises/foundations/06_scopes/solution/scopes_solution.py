# ORBITAL STATION ALPHA - Reactor Rescue (reference solution)

# LEVEL 1 - Power Grid: shared by two functions -> module level
STATION_NAME = "Orbital Station Alpha"


def boot_system():
    return f"Booting {STATION_NAME}..."


def show_banner():
    return f"=== {STATION_NAME} ==="


# LEVEL 2 - Life Support: lives in the enclosing function
def calibrate_sensors():
    return "Sensors calibrated"


def build_oxygen_monitor():
    oxygen = 100

    def read_level():
        return f"Oxygen at {oxygen}%"

    return read_level


# LEVEL 3 - Comms Array: don't shadow built-ins
signals = [12, 7, 30]


def summarize_signals():
    return f"{len(signals)} signals, strength {sum(signals)}"


# LEVEL 4 - Reactor Core: parameter + return instead of global
power = 50


def add_bonus_power(current_power):
    print("Current power:", current_power)
    return current_power + 10


# LEVEL 5 - Cargo Bay: shared mutable list, no `global` needed
cargo = []


def load_crate(item):
    cargo.append(item)


def get_manifest():
    return cargo


# LEVEL 6 - Alarm System: rebinding a global needs `global`
alarm_count = 0


def trigger_alarm():
    global alarm_count
    alarm_count = alarm_count + 1
    return alarm_count


# LEVEL 7 - Drone Memory: rebinding an enclosing variable needs `nonlocal`
def make_drone_counter():
    scans = 0

    def scan():
        nonlocal scans
        scans = scans + 1
        return scans

    return scan


# LEVEL 8 - Diagnostics
def _make_secret():
    secret_code = 42
    return "secret stored"


def list_local_names(a, b):
    c = a + b
    return sorted(locals().keys())


def is_global(name):
    return name in globals()


def probe_hidden():
    _make_secret()
    try:
        secret_code
    except NameError:
        return True
    return False


# LEVEL 9 - BOSS: Reactor Boot Sequence
REACTOR_TARGET = 80
readings = [72, 91, 85]


def configure_reactor():
    return "Reactor configured"


def run_station():
    checks = 0

    def run_check(reading):
        nonlocal checks
        checks = checks + 1
        return reading >= REACTOR_TARGET

    results = [run_check(r) for r in readings]
    highest = max(readings)
    return f"Checks: {checks} | Passed: {results.count(True)} | Peak: {highest}"
