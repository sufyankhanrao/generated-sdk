# -*- coding: utf-8 -*-

"""
retriestester

This file was automatically generated for Stamplay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

import os
import unittest
from tests.http_response_catcher import HttpResponseCatcher
from retriestester.configuration import Configuration, Environment
from retriestester.retriestester_client import RetriestesterClient


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
        cls.client = RetriestesterClient(config=cls.config)

    @staticmethod
    def create_configuration():
        return Configuration.from_environment(
            environment=Environment.TESTING,
            http_call_back=HttpResponseCatcher())
