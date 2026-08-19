def test_string_definition(run_script, expect_variable_type):
    _, namespace = run_script("datatypes_solution.py")
    expect_variable_type(namespace, "mystring", str)


def test_integer_definition(run_script, expect_variable_type):
    _, namespace = run_script("datatypes_solution.py")
    expect_variable_type(namespace, "myinteger", int)


def test_float_definition(run_script, expect_variable_type):
    _, namespace = run_script("datatypes_solution.py")
    expect_variable_type(namespace, "myfloat", float)


def test_boolean_definition(run_script, expect_variable_type):
    _, namespace = run_script("datatypes_solution.py")
    expect_variable_type(namespace, "myboolean", bool)


def test_none_definition(run_script, expect_variable_type):
    _, namespace = run_script("datatypes_solution.py")
    expect_variable_type(namespace, "mynonevalue", type(None))
