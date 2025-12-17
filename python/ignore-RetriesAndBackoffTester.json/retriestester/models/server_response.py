# -*- coding: utf-8 -*-

"""
retriestester

This file was automatically generated for Stamplay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from retriestester.api_helper import APIHelper


class ServerResponse(object):

    """Implementation of the 'ServerResponse' model.

    Attributes:
        passed (bool): The model property of type bool.
        retry_count (int): The model property of type int.
        idle_time_between_api_calls (List[int]): The model property of type
            List[int].
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "passed": 'passed',
        "retry_count": 'retryCount',
        "idle_time_between_api_calls": 'idleTimeBetweenApiCalls'
    }

    _optionals = [
        'idle_time_between_api_calls',
    ]

    def __init__(self,
                 passed=None,
                 retry_count=None,
                 idle_time_between_api_calls=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the ServerResponse class"""

        # Initialize members of the class
        self.passed = passed 
        self.retry_count = retry_count 
        if idle_time_between_api_calls is not APIHelper.SKIP:
            self.idle_time_between_api_calls = idle_time_between_api_calls 

        # Add additional model properties to the instance
        if additional_properties is None:
            additional_properties = {}
        self.additional_properties = additional_properties

    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """

        if not isinstance(dictionary, dict) or dictionary is None:
            return None

        # Extract variables from the dictionary
        passed = dictionary.get("passed") if "passed" in dictionary.keys() else None
        retry_count = dictionary.get("retryCount") if dictionary.get("retryCount") else None
        idle_time_between_api_calls = dictionary.get("idleTimeBetweenApiCalls") if dictionary.get("idleTimeBetweenApiCalls") else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(passed,
                   retry_count,
                   idle_time_between_api_calls,
                   additional_properties)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'passed={self.passed!r}, '
                f'retry_count={self.retry_count!r}, '
                f'idle_time_between_api_calls={(self.idle_time_between_api_calls if hasattr(self, "idle_time_between_api_calls") else None)!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'passed={self.passed!s}, '
                f'retry_count={self.retry_count!s}, '
                f'idle_time_between_api_calls={(self.idle_time_between_api_calls if hasattr(self, "idle_time_between_api_calls") else None)!s}, '
                f'additional_properties={self.additional_properties!s})')
