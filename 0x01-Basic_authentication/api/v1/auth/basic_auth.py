#!/usr/bin/env python3

"""
Implementation of basic authentication
"""

from api.v1.auth.auth import Auth
from base64 import b64decode


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
