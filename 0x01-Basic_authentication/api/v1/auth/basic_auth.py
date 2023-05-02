#!/usr/bin/env python3

"""
Implementation of basic authentication
"""

from api.v1.auth.auth import Auth
from models.user import User
from base64 import b64decode
from typing import TypeVar


class BasicAuth(Auth):
    """Basic Auth implementation class"""

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """Extracts the correct auth header for basic auth"""

        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if 'Basic ' not in authorization_header:
            return None
        return authorization_header.split(' ')[1]

    def decode_base64_authorization_header(self,
                                           base_authentication_header: str):
        """Decodes a base64 header"""
        if base_authentication_header is None:
            return None
        if not isinstance(base_authentication_header, str):
            return None
        try:
            decoded_h = b64decode(base_authentication_header)
            return decoded_h.decode('utf-8')
        except Exception as e:
            return None

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header: str):
        """Extracts user credentials from decoded base64 string"""
        if decoded_base64_authorization_header is None:
            return (None, None)
        if not isinstance(decoded_base64_authorization_header, str):
            return (None, None)
        if ':' not in decoded_base64_authorization_header:
            return (None, None)
        uname, password = decoded_base64_authorization_header.split(':')
        return (uname, password)

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """ returns the User instance based on his email and password """
        if (
           not user_email or
           not isinstance(user_email, str) or
           not user_pwd or
           not isinstance(user_pwd, str)
           ):
            return None
        objs = User().search({"email": user_email})
        if not objs:
            return None
        if objs[0].is_valid_password(user_pwd):
            return objs[0]
        else:
            return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Retrieves the user associated with the request"""
        if not request:
            return None
        auth_header = Auth().authorization_header(request)
        auth_header = self.extract_base64_authorization_header(auth_header)
        dec_header = self.decode_base64_authorization_header(auth_header)
        uname, password = self.extract_user_credentials(dec_header)
        return self.user_object_from_credentials(uname, password)
