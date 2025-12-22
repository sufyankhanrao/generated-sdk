
"""
testerfilesandmultipart

This file was automatically generated for Stamplay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

import unittest

from testerfilesandmultipart.configuration import (
    Configuration,
    Environment,
)
from testerfilesandmultipart.testerfilesandmultipart_client import (
    TesterfilesandmultipartClient,
)
from tests.http_response_catcher import HttpResponseCatcher


class ControllerTestBase(unittest.TestCase):
    """
    All test classes inherit from this base class. It abstracts out
    common functionality and configuration variables set up.
    """

    client = None
    config = None

    @classmethod
    def setUpClass(cls):
        """Class method called once before running tests in a test class."""
        cls.request_timeout = 60
        cls.assert_precision = 0.1
        cls.config = ControllerTestBase.create_configuration()
        cls.client = TesterfilesandmultipartClient(config=cls.config)

    @staticmethod
    def create_configuration():
        """
        Build and return the configuration used for controller tests.

        Centralizes common setup such as authentication and callback handling
        to ensure consistent client initialization across the test suite.
        """
        return Configuration.from_environment(
            port="3000", environment=Environment.TESTING,
            http_call_back=HttpResponseCatcher())
