def test_basic_math(run_script, expect_variables):
    _, namespace = run_script("math_and_comparisons_solution.py")
    expect_variables(
        namespace,
        {"addition": 15, "substraction": -5, "multiplication": 50, "division": 0.5},
    )


def test_string_concat(run_script, expect_variables):
    _, namespace = run_script("math_and_comparisons_solution.py")
    expect_variables(namespace, {"concat_name": "JaneDoe"})


def test_string_indexing(run_script, expect_variables):
    _, namespace = run_script("math_and_comparisons_solution.py")
    expect_variables(namespace, {"first_letter": "M", "second_last_letter": "o"})


def test_convert_case(run_script, expect_variables):
    TEST_STRING = "HeLLo AND WelcomE"
    _, namespace = run_script("math_and_comparisons_solution.py")
    expect_variables(
        namespace,
        {
            "lowercased": TEST_STRING.lower(),
            "uppercased": TEST_STRING.upper(),
            "titlecased": TEST_STRING.title(),
        },
    )
