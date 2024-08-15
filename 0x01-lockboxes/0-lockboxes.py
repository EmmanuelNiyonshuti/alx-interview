#!/usr/bin/python3
"""
lockboxes algorithm.
"""


def canUnlockAll(boxes):
    """
    determines if all the boxes can be opened.
    Args:
        boxes (list)- a list of list which contain keys.
    Return:
        True if all boxes can be opened False otherwise.
    """
    n = len(boxes)
    keys = set(boxes[0])
    unlocked = set([0])
    while keys:
        new_key = keys.pop()
        if new_key < n and new_key not in unlocked:
            unlocked.add(new_key)
            keys.update(boxes[new_key])
    return len(unlocked) == n
