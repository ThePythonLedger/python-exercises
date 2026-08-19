# Exercise 01 - Hello World

The main purpose of this exercise is to walk you through running the tests and confirm your setup works correctly.

In this directory you'll find 2 other files:

1. `hello_world.py`
2. `test_hello_world.py`

Run the test from inside this directory:

```bash
pytest test_hello_world.py -v
```

Watch it fail. Right now `hello_world.py` is empty, so nothing gets printed.

Open `hello_world.py` and add one line:

```python
print("Hello, World!")
```

Run the test again — it should pass.

Congratulations, your first exercise is passing. Let's get more done.
