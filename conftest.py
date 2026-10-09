"""Repo-wide pytest setup: the --solutions flag and a per-test timeout."""
import os
import signal

import pytest

TIMEOUT_SECONDS = 5


def pytest_addoption(parser):
    parser.addoption(
        "--solutions",
        action="store_true",
        help="Run the tests against solutions/ instead of your tasks/.",
    )


def pytest_configure(config):
    # load_task() reads this env var at import time of each test file.
    if config.getoption("--solutions"):
        os.environ["DSA_SOLUTIONS"] = "1"


class TaskTimeout(Exception):
    pass


@pytest.fixture(autouse=True)
def _timeout():
    """Fail a test that runs longer than TIMEOUT_SECONDS instead of hanging forever."""
    if not hasattr(signal, "SIGALRM"):  # Windows: no SIGALRM, just run without a limit
        yield
        return

    def handler(signum, frame):
        raise TaskTimeout(
            f"Test took longer than {TIMEOUT_SECONDS}s. Likely an infinite loop "
            "(e.g. a linked list pointer that now forms a cycle, or a loop whose "
            "bounds never shrink), or your solution is too slow for the target complexity."
        )

    previous = signal.signal(signal.SIGALRM, handler)
    signal.alarm(TIMEOUT_SECONDS)
    try:
        yield
    finally:
        signal.alarm(0)
        signal.signal(signal.SIGALRM, previous)
