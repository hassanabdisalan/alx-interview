#!/usr/bin/python3
"""
0-lockboxes.py - Determines if all boxes can be unlocked.
"""


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.

    Parameters:
    boxes (list of list of int): A list where each index represents a box and
                                 contains a list of keys found in that box.

    Returns:
    bool: True if all boxes can be opened, False otherwise.
    """
    if not boxes or not isinstance(boxes, list):
        return False

    n = len(boxes)
    unlocked = set([0])
    keys = set(boxes[0])

    while keys:
        key = keys.pop()
        if isinstance(key, int) and 0 <= key < n and key not in unlocked:
            unlocked.add(key)
            keys.update(boxes[key])

    return len(unlocked) == n
