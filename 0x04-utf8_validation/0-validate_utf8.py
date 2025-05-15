#!/usr/bin/python3
"""
This module provides a function to validate UTF-8 encoding.
"""

def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    Args:
        data: List of integers representing bytes (only the 8 LSB are relevant)

    Returns:
        True if data is a valid UTF-8 encoding, else False.
    """
    num_bytes = 0

    for byte in data:
        # Mask to consider only the last 8 bits
        byte = byte & 0xFF

        if num_bytes == 0:
            # Determine number of bytes in the UTF-8 character
            if (byte >> 5) == 0b110:
                num_bytes = 1
            elif (byte >> 4) == 0b1110:
                num_bytes = 2
            elif (byte >> 3) == 0b11110:
                num_bytes = 3
            elif (byte >> 7) != 0:
                return False  # Not a valid 1-byte character
        else:
            # All continuation bytes must start with 10xxxxxx
            if (byte >> 6) != 0b10:
                return False
            num_bytes -= 1

    return num_bytes == 0
