"""
Task 01 · Core · Build a Stack

A stack is LIFO: last in, first out. Implement it on top of a Python list,
using the END of the list as the top (append/pop at the end are O(1)).

Required behaviour:
    s.push(val)     O(1)  put val on top
    s.pop()         O(1)  remove + return the top value; IndexError if empty
    s.peek()        O(1)  return the top value without removing; IndexError if empty
    s.is_empty()    O(1)
    len(s)          O(1)
    s.to_list()     values bottom -> top, as a NEW list (mutating it must not
                    affect the stack)

Example:
    s = Stack()
    s.push(1); s.push(2); s.push(3)
    s.pop()   -> 3
    s.peek()  -> 2
    len(s)    -> 2
"""

from typing import Any


class Stack:
    def __init__(self):
        raise NotImplementedError

    def push(self, val: Any) -> None:
        raise NotImplementedError

    def pop(self) -> Any:
        raise NotImplementedError

    def peek(self) -> Any:
        raise NotImplementedError

    def is_empty(self) -> bool:
        raise NotImplementedError

    def __len__(self) -> int:
        raise NotImplementedError

    def to_list(self) -> list:
        raise NotImplementedError
