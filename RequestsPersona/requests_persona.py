import json

from requests.auth import AuthBase
import requests
"""
Get the cookie
Generate the Keys
send the pub and cookie to PERSONA_ CERT to sign the Keys



"""

CERT = {"underplank@gmail.com":
                        {"created":"2012-08-21T01:48:34.979Z",
                         "type":"secondary",
                         "updated":"2012-08-21T01:48:35.913Z",
                         "pub": {"algorithm":"DS",
                                 "y":"5f5dddbbe9e8bacb9929602dde267d462587c6990cb248f54a2de7ad665cb18eebf94489b94ba29a6e63915a12c909203a85bb9f049755ae4705b173f5f012302b6e4bad4e358a8ee7d19b3eb22a1a7eecd8d3df36cf26c7adee3ef5f5b34084bcaaec50055d363359348865aef48d29f3c1b4bd715c299b1c1bf64a9c5b8ea7",
                                 "p":"ff600483db6abfc5b45eab78594b3533d550d9f1bf2a992a7a8daa6dc34f8045ad4e6e0c429d334eeeaaefd7e23d4810be00e4cc1492cba325ba81ff2d5a5b305a8d17eb3bf4a06a349d392e00d329744a5179380344e82a18c47933438f891e22aeef812d69c8f75e326cb70ea000c3f776dfdbd604638c2ef717fc26d02e17",
                                 "q":"e21e04f911d1ed7991008ecaab3bf775984309c3",
                                 "g":"c52a4a0ff3b7e61fdf1867ce84138369a6154f4afa92966e3c827e25cfa6cf508b90e5de419e1337e07a2e9e2a3cd5dea704d175f8ebf6af397d69e110b96afb17c7a03259329e4829b0d03bbc7896b15b4ade53e130858cc34d96269aa89041f409136c7242a38895c9d5bccad4f389af1d7a4bd1398bd072dffa896233397a"},
                          "priv":{"algorithm":"DS",
                                  "x":"850a23a7e6e6b487f8d1360b413eb739e3203bc2",
                                  "p":"ff600483db6abfc5b45eab78594b3533d550d9f1bf2a992a7a8daa6dc34f8045ad4e6e0c429d334eeeaaefd7e23d4810be00e4cc1492cba325ba81ff2d5a5b305a8d17eb3bf4a06a349d392e00d329744a5179380344e82a18c47933438f891e22aeef812d69c8f75e326cb70ea000c3f776dfdbd604638c2ef717fc26d02e17",
                                  "q":"e21e04f911d1ed7991008ecaab3bf775984309c3",
                                  "g":"c52a4a0ff3b7e61fdf1867ce84138369a6154f4afa92966e3c827e25cfa6cf508b90e5de419e1337e07a2e9e2a3cd5dea704d175f8ebf6af397d69e110b96afb17c7a03259329e4829b0d03bbc7896b15b4ade53e130858cc34d96269aa89041f409136c7242a38895c9d5bccad4f389af1d7a4bd1398bd072dffa896233397a"},
                           "cert":"eyJhbGciOiJSUzI1NiJ9.eyJwdWJsaWMta2V5Ijp7ImFsZ29yaXRobSI6IkRTIiwieSI6IjVmNWRkZGJiZTllOGJhY2I5OTI5NjAyZGRlMjY3ZDQ2MjU4N2M2OTkwY2IyNDhmNTRhMmRlN2FkNjY1Y2IxOGVlYmY5NDQ4OWI5NGJhMjlhNmU2MzkxNWExMmM5MDkyMDNhODViYjlmMDQ5NzU1YWU0NzA1YjE3M2Y1ZjAxMjMwMmI2ZTRiYWQ0ZTM1OGE4ZWU3ZDE5YjNlYjIyYTFhN2VlY2Q4ZDNkZjM2Y2YyNmM3YWRlZTNlZjVmNWIzNDA4NGJjYWFlYzUwMDU1ZDM2MzM1OTM0ODg2NWFlZjQ4ZDI5ZjNjMWI0YmQ3MTVjMjk5YjFjMWJmNjRhOWM1YjhlYTciLCJwIjoiZmY2MDA0ODNkYjZhYmZjNWI0NWVhYjc4NTk0YjM1MzNkNTUwZDlmMWJmMmE5OTJhN2E4ZGFhNmRjMzRmODA0NWFkNGU2ZTBjNDI5ZDMzNGVlZWFhZWZkN2UyM2Q0ODEwYmUwMGU0Y2MxNDkyY2JhMzI1YmE4MWZmMmQ1YTViMzA1YThkMTdlYjNiZjRhMDZhMzQ5ZDM5MmUwMGQzMjk3NDRhNTE3OTM4MDM0NGU4MmExOGM0NzkzMzQzOGY4OTFlMjJhZWVmODEyZDY5YzhmNzVlMzI2Y2I3MGVhMDAwYzNmNzc2ZGZkYmQ2MDQ2MzhjMmVmNzE3ZmMyNmQwMmUxNyIsInEiOiJlMjFlMDRmOTExZDFlZDc5OTEwMDhlY2FhYjNiZjc3NTk4NDMwOWMzIiwiZyI6ImM1MmE0YTBmZjNiN2U2MWZkZjE4NjdjZTg0MTM4MzY5YTYxNTRmNGFmYTkyOTY2ZTNjODI3ZTI1Y2ZhNmNmNTA4YjkwZTVkZTQxOWUxMzM3ZTA3YTJlOWUyYTNjZDVkZWE3MDRkMTc1ZjhlYmY2YWYzOTdkNjllMTEwYjk2YWZiMTdjN2EwMzI1OTMyOWU0ODI5YjBkMDNiYmM3ODk2YjE1YjRhZGU1M2UxMzA4NThjYzM0ZDk2MjY5YWE4OTA0MWY0MDkxMzZjNzI0MmEzODg5NWM5ZDViY2NhZDRmMzg5YWYxZDdhNGJkMTM5OGJkMDcyZGZmYTg5NjIzMzM5N2EifSwicHJpbmNpcGFsIjp7ImVtYWlsIjoidW5kZXJwbGFua0BnbWFpbC5jb20ifSwiaWF0IjoxMzQ1NTEzNzEyMTAzLCJleHAiOjEzNDU1MTczMTIxMDMsImlzcyI6ImxvZ2luLnBlcnNvbmEub3JnIn0.Wk3QKLEtrl8-4cr5cZTpufTzQittLwNJlhJz9e1oTVSVOwPgyP6aeJqDQNg4qUm-mzJdLsw6Q3_rfe8GbpPlXOpZLFfZzX15LG6h9omgyuCwfjE5vKFARBNl8GfkqEnYz2fuXgEzokFpOJ7KI8GpJAd-iFcoBP9vXFKYXwXP78Y0lT2RybPqhj2ohofUicvypct-HcDUKvLUHr6VU2oQ-uYRCmen2oZVAIe8NqR6PJYytAAbHy0APb6qfxkTete2iXDnGyeE1y4UkGNlrF_bQswaxdq0dC26eK0IGFWiApsBCKqE0L9-zIVzxT-EmrbsW01V6q2h6gA9rPdQMYpHdA"}
                           }
CSRF_URL = "https://login.persona.org/wsapi/session_context"
CSRF_METHOD = "GET"


PERSONA_LOGIN_URL = "https://login.persona.org/wsapi/authenticate_user"
PERSONA_LOGIN_METHOD = "POST"


PERSONA_CERT_URL = "https://login.persona.org/wsapi/cert_key"
PERSONA_CERT_METHOD = "POST"

class RequestsPersonaAuth(AuthBase):
    """Attaches HTTP Pizza Authentication to the given Request object."""
    def __init__(self, email, password, ephermeral=True):
        # setup any auth-related data here
        self.email = email
        self.password = password
        self.ephemeral = ephermeral

    def __call__(self, r):
        # modify and return the request
        print PERSONA_LOGIN_URL
        print PERSONA_CERT_URL
        self._get_cookie()
        self._generate_keys()
        self._sign_keys()
        return r

    def _get_cookie(self):
        """
        Fetch the cookie from PERSONA_LOGIN_URL using passed in authentication 
        credentials passed into the init
        """

        res = requests.request(CSRF_METHOD, CSRF_URL)
        csrf_data = json.loads(res.content)

        data = data={"email": self.email,
                      "pass":  self.password,
                      "ephemeral": True,
                      "csrf": csrf_data['csrf_token']}

        res = requests.request(PERSONA_LOGIN_METHOD, PERSONA_LOGIN_URL, data=json.dumps(data), cookies=res.cookies)
        print "getting cookie"

    def _generate_keys(self):
        """
        Use the cookie to generate public private keys
        """
        print "generate_keys"

    def _sign_keys(self):
        """
        Send the keys to PERSONA_CERT_URL to be signed
        """
        print "sign keys"