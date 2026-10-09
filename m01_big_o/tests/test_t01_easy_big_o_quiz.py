import hashlib
import re

import pytest

from common.loader import load_task

task = load_task(__file__)

# Answers are stored hashed so this file doesn't give them away.
EXPECTED = {
    "q01": ["e54f9541b134e85b"],
    "q02": ["b64ee42813fed58e"],
    "q03": ["1baa1cf36f20f53f"],
    "q04": ["ae3218fb08a9effe"],
    "q05": ["6ea204e87b994847"],
    "q06": ["e3f6b4431b5d6dd8", "1f13a002a059d2ec"],
    "q07": ["ff6230dc8998eea4", "a673447915f14fb4"],
    "q08": ["382e436007fd9561"],
    "q09": ["f83f79da05cacd8c"],
    "q10": ["57b49af692d73141"],
    "q11": ["d4f7613bf526eb2a"],
    "q12": ["6fd4e4fa62640ed5"],
    "q13": ["e6811e6284ca777e"],
    "q14": ["a8d5eb4618339600"],
    "q15": ["b9851876a8a7178c"],
    "q16": ["ef79e2853a209f35"],
    "q17": ["5cb139b62d99b5c7"],
}


def normalize(answer: str) -> str:
    s = answer.strip().lower()
    s = re.sub(r"\s+", "", s)
    s = s.replace("θ", "o").replace("big-o", "").replace("bigo", "")
    s = s.replace("**", "^").replace("²", "^2").replace("³", "^3")
    s = re.sub(r"[*·×]", "", s)
    s = re.sub(r"(?:log|lg)(?:_?2)?\((\w)\)", r"log\1", s)
    s = re.sub(r"(?:log|lg)(?:_?2)?(?=[a-z])", "log", s)
    if not s.startswith("o("):
        s = f"o({s})"
    return s


def digest(qid: str, answer: str) -> str:
    return hashlib.sha256(f"dsa-quiz:{qid}:{normalize(answer)}".encode()).hexdigest()[:16]


def test_all_questions_present():
    assert set(task.ANSWERS) == set(EXPECTED), "Don't add/remove keys from ANSWERS"


@pytest.mark.parametrize("qid", sorted(EXPECTED))
def test_answer(qid):
    answer = task.ANSWERS.get(qid, "")
    assert answer.strip(), f"{qid} not answered yet"
    assert digest(qid, answer) in EXPECTED[qid], (
        f"{qid}: {answer!r} is not right. Re-read the snippet; count how many times "
        "the innermost line runs as n grows."
    )
