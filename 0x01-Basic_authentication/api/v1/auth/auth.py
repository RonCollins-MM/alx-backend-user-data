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
        """Checks whether authentication is needed

        parameters
        ----------
        path : str
            Path to be checked
        excluded_paths: List[str]
            List of paths to be exlcuded

        Returns
        -------
        Boolean
            Whether the path should be authenticated or not
        """

        if path is None:
            return True
        if excluded_paths is None or excluded_paths == '':
            return True
        if path[-1] != '/':
            path += '/'
        if path in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None):
        """Generates authorization header for a request"""
        if request is None:
            return None
        if 'Authorization' not in request.headers:
            return None
        return request.headers['Authorization']

    def current_user(self, request=None) -> TypeVar('User'):
        """Returns the user object associated with the request ??NOT SURE.
        """
        return None
