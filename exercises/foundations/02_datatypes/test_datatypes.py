import pytest


def test_task1(run_script, expect_variable_type):
    _, namespace = run_script("datatypes.py")
    expect_variable_type(namespace, "station_name", str)
    expect_variable_type(namespace, "module_count", int)
    expect_variable_type(namespace, "signal_frequency", float)
    expect_variable_type(namespace, "life_support_active", bool)
    expect_variable_type(namespace, "backup_generator", type(None))


def test_task2(run_script, expect_variables):
    _, namespace = run_script("datatypes.py")
    expect_variables(
        namespace,
        {
            "raw_energy_reading": "100",
            "energy_level": 100,
            "raw_distance_reading": 45,
            "exact_distance": 45.0,
            "raw_status_code": 1,
            "is_operational": True,
        },
    )


@pytest.mark.skip(reason="Finish earlier task first")
def test_task3(run_script, expect_variable_type, expect_output):
    stdout, namespace = run_script("datatypes.py")
    expect_variable_type(namespace, "station_status", str)
    test_st_mod_count = namespace["module_count"]
    test_st_name = namespace["station_name"]
    expect_output(stdout, f"{test_st_mod_count} - {test_st_name}")
