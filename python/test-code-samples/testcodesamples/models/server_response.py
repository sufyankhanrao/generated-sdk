"""testcodesamples.

This file was automatically generated for Stamplay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from testcodesamples.api_helper import APIHelper


class ServerResponse(object):
    """Implementation of the 'ServerResponse' model.

    Attributes:
        passed (bool): The model property of type bool.
        message (str): The model property of type str.
        input (Dict[str, Any]): The model property of type Dict[str, Any].
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "passed": "passed",
        "message": "Message",
        "input": "input",
    }

    _optionals = [
        "message",
        "input",
    ]

    def __init__(self,
                 passed=None,
                 message=APIHelper.SKIP,
                 input=APIHelper.SKIP,
                 additional_properties=None):
        """Initialize a ServerResponse instance."""
        # Initialize members of the class
        self.passed = passed
        if message is not APIHelper.SKIP:
            self.message = message
        if input is not APIHelper.SKIP:
            self.input = input

        # Add additional model properties to the instance
        if additional_properties is None:
            additional_properties = {}
        self.additional_properties = additional_properties

    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Create an instance of this model from a dictionary

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
        passed =\
            dictionary.get("passed")\
            if "passed" in dictionary.keys() else None
        message =\
            dictionary.get("Message")\
            if dictionary.get("Message") else APIHelper.SKIP
        input =\
            dictionary.get("input")\
            if dictionary.get("input") else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(passed,
                   message,
                   input,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        return (f"{self.__class__.__name__}("
                f"passed={self.passed!r}, "
                f"message={(self.message
                     if hasattr(self, 'message') else None)!r}, "
                f"input={(self.input if hasattr(self, 'input') else None)!r}, "
                f"additional_properties={self.additional_properties!r})")

    def __str__(self):
        """Return a human-readable string representation."""
        return (f"{self.__class__.__name__}("
                f"passed={self.passed!s}, "
                f"message={(self.message
                     if hasattr(self, 'message') else None)!s}, "
                f"input={(self.input if hasattr(self, 'input') else None)!s}, "
                f"additional_properties={self.additional_properties!s})")
