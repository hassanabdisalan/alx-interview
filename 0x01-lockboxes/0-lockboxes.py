#!/usr/bin/python3

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
    visited = set()
    stack = [0]  # Start with box 0

    while stack:
        box = stack.pop()
        if box not in visited:
            visited.add(box)
            for key in boxes[box]:
                if isinstance(key, int) and 0 <= key < n and key not in visited:
                    stack.append(key)

    return len(visited) == n
