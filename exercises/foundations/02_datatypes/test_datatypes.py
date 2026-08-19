import pytest


def test_string_definition(run_script, expect_variable_type):
    _, namespace = run_script("datatypes.py")
    expect_variable_type(namespace, "mystring", str)


@pytest.mark.skip(reason="Finish earlier task first")
def test_integer_definition(run_script, expect_variable_type):
    _, namespace = run_script("datatypes.py")
    expect_variable_type(namespace, "myinteger", int)


@pytest.mark.skip(reason="Finish earlier task first")
def test_float_definition(run_script, expect_variable_type):
    _, namespace = run_script("datatypes.py")
    expect_variable_type(namespace, "myfloat", float)


@pytest.mark.skip(reason="Finish earlier task first")
def test_boolean_definition(run_script, expect_variable_type):
    _, namespace = run_script("datatypes.py")
    expect_variable_type(namespace, "myboolean", bool)


@pytest.mark.skip(reason="Finish earlier task first")
def test_none_definition(run_script, expect_variable_type):
    _, namespace = run_script("datatypes.py")
    expect_variable_type(namespace, "mynonevalue", None)
