#!/usr/bin/env python3
"""
Password Encryption and Validation Module
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """
        Generates a salted and hashed password.

        Args:
                password (str): A string containing the plain text
                password to be hashed.

        Returns:
                bytes: A byte string representing the salted, hashed password.
        """
    encoded = password.encode()
    hashed = bcrypt.hashpw(encoded, bcrypt.gensalt())

    return hashed


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
        Validates whether the provided password matches the hashed password.

        Args:
                hashed_password (bytes): A byte string representing
                the salted, hashed password.
                password (str): A string containing the plain text
                password to be validated.

        Returns:
                bool: True if the provided password matches the hashed
                password, False otherwise.
        """
    valid = False
    encoded = password.encode()
    if bcrypt.checkpw(encoded, hashed_password):
        valid = True
    return valid
