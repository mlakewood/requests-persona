import unittest

import requests
from requests_persona import RequestsPersonaAuth

"""
mockmyid.com
123done.com

"""



class TestRequestsPersona(unittest.TestCase):
    """
    Unit tests for requests Persona
    """

    def test_persona(self):
        """
        Test stuff
        """
        # session = requests.session()
        res = requests.get("http://www.123done.com",
                           auth=RequestsPersonaAuth("underplank@mockmyid.com", "foo"))

        print res


if __name__ == '__main__':
    unittest.main()
