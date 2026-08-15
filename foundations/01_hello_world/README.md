# Exercise 01 - Hello World

The main purpose of this exercise is to walk you through running the tests and confirm your setup works correctly.

In this directory you'll find 2 other files:

1. `hello_world.py`
2. `test_hello_world.py`

Unlike exercises later in the curriculum, this one doesn't use a function — you don't know about those yet. You'll just write plain code that runs top-to-bottom, exactly like typing lines directly into the terminal.

Let's look at the test file first:

```python
def test_prints_hello_world(run_script):
    stdout, _ = run_script("hello_world.py")
    assert stdout.strip() == "Hello, World!"
```

`run_script` is a helper set up once for the whole repo. It runs `hello_world.py` exactly the way Python would if you typed `python hello_world.py`, and hands back everything it printed. The test then checks that what got printed matches `'Hello, World!'` exactly — capitalization and punctuation included.

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

For these early exercises you won't need `import`, `def`, or `return` — just write the code the same way you'd type it directly.
