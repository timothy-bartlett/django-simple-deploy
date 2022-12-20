---
title: "Running Unit Tests"
hide:
    - footer
---

# Running Unit Tests

This page focuses solely on running unit tests. If you want to understand the overall unit testing process, or write unit tests for a newly-supported platform, see the rest of the documentation in this section.

You can run unit tests for a single platform, or for all platforms. Currently, it doesn't take much longer to test for all the platforms, because most of the testing time is spent creating the initial test project. Testing a single platform takes about 12 seconds, and running the entire test suite takes about 16 seconds. (This is based on my intel-based macOS system.)

## Setting up a development environment

If you haven't already set up a development environment for `django-simple-deploy`, see these [brief instructions](../contributing/development_environment/#make-a-local-working-copy-of-the-project).

## Running the entire test suite

To run the entire test suite, `cd` into the `unit_tests/` directory, and then run `pytest`. Make sure you're working in an active virtual environment.

!!! warning

    Make sure you are in the `unit_tests/` directory! If you run `pytest` from the root directory, you'll start running integration tests as well. Since integration tests almost always try to make resources on an external platform, the two kinds of tests should always be kept separate.

```
(dsd_env) $ cd unit_tests/
(dsd_env)unit_tests $ pytest
```

You should see output similar to the following:

```
==================== test session starts ====================
platform darwin -- Python 3.10.0, pytest-7.1.2, pluggy-1.0.0
rootdir: django-simple-deploy
collected 22 items

platform_agnostic_tests/test_invalid_cli_commands.py ..
platforms/fly_io/test_flyio_config.py .......
platforms/heroku/test_heroku_config.py .......
platforms/platform_sh/test_platformsh_config.py ......
==================== 22 passed in 18.07s ====================
```

## Running tests for a single platform

Let's say you're focused on supporting Fly.io, and you just want to run tests for that platform. Here's how to do that:

```
(dsd_env)unit_tests $ pytest platforms/fly_io/
```

## Running all platform-agnostic tests

Similarly, you can run just the platform-agnostic tests:

```
(dsd_env)unit_tests $ pytest platform_agnostic_tests/
```

## Helpful pytest notes

If you're new to using pytest, here are some useful notes. (If you have any suggestions for what else to include here, please feel free to share them.)

- `pytest -x`
    - This is identical to `pytest --exitfirst`, which stops after the first failing test. This is especially helpful when diagnosing unit test failures.
    - A number of ways to run `pytest` are described in [How to invoke pytest](https://docs.pytest.org/en/latest/how-to/usage.html).
- `pytest -k`
    - Run a single test, or a test matching a pattern.
    - For example, if you want to run the test for the `pyproject.toml` file on Fly.io, you can use the following command: `$ pytest -k platforms/fly_io test_pyproject_toml`. This will actually run any test in the module that has that phrase in its name, but practically this is an effective way to isolate tests.
    - Pytest docs: [Using -k expr to select tests based on their name](https://docs.pytest.org/en/latest/example/markers.html#using-k-expr-to-select-tests-based-on-their-name)