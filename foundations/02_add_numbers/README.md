# Exercise 02 - Add, Subtract, Multiply

## Description

Two numbers are already defined for you at the top of `add_numbers.py`:

```python
num1 = 8
num2 = 3
```

Using `print()`, output the following, one value per line, in this order:

1. Their sum
2. Their difference (`num1 - num2`)
3. Their product

This exercise also introduces **skipped tests** — same idea as leveling up. Open `test_add_numbers.py`: one test is active, the other two are marked `@pytest.mark.skip(...)`. Get the sum printing and that first test passing, then delete the `@pytest.mark.skip(...)` line above the next test, add the next `print()` line to your script, and run again. Repeat until nothing is skipped.

## Notes

- Print only the numbers themselves — no labels, no extra text, one per line.
- Don't change the values of `num1` or `num2`.
