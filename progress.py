"""
Progress dashboard: runs every test and shows which tasks you've cracked.

    python progress.py              # all modules
    python progress.py m02          # just one module (prefix match)
    python progress.py --solutions  # sanity-check the reference solutions
"""
import contextlib
import io
import sys
from collections import defaultdict
from pathlib import Path

import pytest

ROOT = Path(__file__).parent


class _Collector:
    def __init__(self):
        # test file path -> [passed, total]
        self.results = defaultdict(lambda: [0, 0])

    def pytest_runtest_logreport(self, report):
        # Count each test once: at "call", or at "setup" if setup itself failed.
        if report.when == "call" or (report.when == "setup" and not report.passed):
            file = report.nodeid.split("::")[0]
            self.results[file][1] += 1
            if report.passed:
                self.results[file][0] += 1


def main(argv):
    solutions = "--solutions" in argv
    filters = [a for a in argv if not a.startswith("--")]
    module_dirs = sorted(p for p in ROOT.glob("m[0-9][0-9]_*") if p.is_dir())
    if filters:
        module_dirs = [p for p in module_dirs if any(p.name.startswith(f) for f in filters)]
    if not module_dirs:
        print("No matching modules.")
        return 1

    collector = _Collector()
    args = [str(p) for p in module_dirs] + ["-p", "no:cacheprovider"]
    if solutions:
        args.append("--solutions")
    output = io.StringIO()
    with contextlib.redirect_stdout(output):  # hide pytest's own report
        exit_code = pytest.main(args, plugins=[collector])
    if exit_code not in (pytest.ExitCode.OK, pytest.ExitCode.TESTS_FAILED):
        print(output.getvalue())  # collection/usage error: show what went wrong
        return 1

    grand_done = grand_total = 0
    for module in module_dirs:
        rows = []
        for test_file in sorted((module / "tests").glob("test_t*.py")):
            key = str(test_file.relative_to(ROOT))
            passed, total = collector.results.get(key, (0, 0))
            rows.append((test_file.stem.removeprefix("test_"), passed, total))
        done = sum(1 for _, p, t in rows if t and p == t)
        grand_done += done
        grand_total += len(rows)
        print(f"\n{module.name}  ({done}/{len(rows)} tasks complete)")
        for name, passed, total in rows:
            if total and passed == total:
                mark = "DONE"
            elif passed:
                mark = "...."
            else:
                mark = "    "
            bar = "#" * round(20 * passed / total) if total else ""
            print(f"  [{mark}] {name:<42} {passed:>3}/{total:<3} {bar}")

    print(f"\nOverall: {grand_done}/{grand_total} tasks complete\n")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
