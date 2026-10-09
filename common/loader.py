"""Import the code a test file is testing: your task stub, or the reference solution."""
import importlib
import os
from pathlib import Path
from types import ModuleType


def use_solutions() -> bool:
    return os.environ.get("DSA_SOLUTIONS") == "1"


def load_task(test_file: str) -> ModuleType:
    """
    Given a test file path like .../m02_linked_lists/tests/test_t02_easy_reverse_list.py,
    import m02_linked_lists.tasks.t02_easy_reverse_list (or .solutions. with --solutions).
    """
    path = Path(test_file)
    module_dir = path.parent.parent.name
    task_name = path.stem.removeprefix("test_")
    folder = "solutions" if use_solutions() else "tasks"
    return importlib.import_module(f"{module_dir}.{folder}.{task_name}")
