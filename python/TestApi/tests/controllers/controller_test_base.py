# -*- coding: utf-8 -*-

"""
tester

This file was automatically generated for Stamplay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

import os
import unittest
from tests.http_response_catcher import HttpResponseCatcher
from tester.configuration import Configuration, Environment
from tester.tester_client import TesterClient


class ControllerTestBase(unittest.TestCase):

    """All test classes inherit from this base class. It abstracts out
    common functionality and configuration variables set up."""

    client = None
    config = None

    @classmethod
    def setUpClass(cls):
        """Class method called once before running tests in a test class."""
        cls.request_timeout = 60
        cls.assert_precision = 0.1
        cls.config = ControllerTestBase.create_configuration()
        cls.client = TesterClient(config=cls.config)

    @staticmethod
    def create_configuration():
        return Configuration.from_environment(
            port='3000', suites=4, environment=Environment.TESTING,
            http_call_back=HttpResponseCatcher())
