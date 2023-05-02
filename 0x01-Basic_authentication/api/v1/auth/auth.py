#!/usr/bin/env python3

"""
Defines the class `Auth` that is the template for all authentication
systems.
"""

from flask import request
from typing import List, TypeVar


class Auth():
    """
    Template for all authentication systems
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Checks whether authentication is needed"""
        return False

    def authorization_header(self, request=None):
        """Generates authorization header for a request"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Returns the user object associated with the request ??NOT SURE.
        """
        return None
