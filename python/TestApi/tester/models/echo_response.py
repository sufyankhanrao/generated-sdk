"""tester.

This file was automatically generated for Stamplay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from tester.api_helper import APIHelper
from tester.models.query_parameter import QueryParameter


class EchoResponse(object):
    """Implementation of the 'EchoResponse' model.

    Raw http Request info

    Attributes:
        body (Dict[str, Any]): The model property of type Dict[str, Any].
        headers (Dict[str, str]): The model property of type Dict[str, str].
        method (str): The model property of type str.
        path (str): relativePath
        query (Dict[str, QueryParameter]): The model property of type
            Dict[str, QueryParameter].
        upload_count (int): The model property of type int.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "body": "body",
        "headers": "headers",
        "method": "method",
        "path": "path",
        "query": "query",
        "upload_count": "uploadCount",
    }

    _optionals = [
        "body",
        "headers",
        "method",
        "path",
        "query",
        "upload_count",
    ]

    def __init__(self,
                 body=APIHelper.SKIP,
                 headers=APIHelper.SKIP,
                 method=APIHelper.SKIP,
                 path=APIHelper.SKIP,
                 query=APIHelper.SKIP,
                 upload_count=APIHelper.SKIP,
                 additional_properties=None):
        """Initialize a EchoResponse instance."""
        # Initialize members of the class
        if body is not APIHelper.SKIP:
            self.body = body
        if headers is not APIHelper.SKIP:
            self.headers = headers
        if method is not APIHelper.SKIP:
            self.method = method
        if path is not APIHelper.SKIP:
            self.path = path
        if query is not APIHelper.SKIP:
            self.query = query
        if upload_count is not APIHelper.SKIP:
            self.upload_count = upload_count

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
        body =\
            dictionary.get("body")\
            if dictionary.get("body") else APIHelper.SKIP
        headers =\
            dictionary.get("headers")\
            if dictionary.get("headers") else APIHelper.SKIP
        method =\
            dictionary.get("method")\
            if dictionary.get("method") else APIHelper.SKIP
        path =\
            dictionary.get("path")\
            if dictionary.get("path") else APIHelper.SKIP
        query = QueryParameter.from_dictionary(
            dictionary.get("query"))\
            if "query" in dictionary.keys() else APIHelper.SKIP
        upload_count =\
            dictionary.get("uploadCount")\
            if dictionary.get("uploadCount") else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(body,
                   headers,
                   method,
                   path,
                   query,
                   upload_count,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        return (f"{self.__class__.__name__}("
                f"body={(self.body if hasattr(self, 'body') else None)!r}, "
                f"headers={(self.headers
                     if hasattr(self, 'headers') else None)!r}, "
                f"method={(self.method if hasattr(self, 'method') else None)!r}, "
                f"path={(self.path if hasattr(self, 'path') else None)!r}, "
                f"query={(self.query if hasattr(self, 'query') else None)!r}, "
                f"upload_count={(self.upload_count
                     if hasattr(self, 'upload_count') else None)!r}, "
                f"additional_properties={self.additional_properties!r})")

    def __str__(self):
        """Return a human-readable string representation."""
        return (f"{self.__class__.__name__}("
                f"body={(self.body if hasattr(self, 'body') else None)!s}, "
                f"headers={(self.headers
                     if hasattr(self, 'headers') else None)!s}, "
                f"method={(self.method if hasattr(self, 'method') else None)!s}, "
                f"path={(self.path if hasattr(self, 'path') else None)!s}, "
                f"query={(self.query if hasattr(self, 'query') else None)!s}, "
                f"upload_count={(self.upload_count
                     if hasattr(self, 'upload_count') else None)!s}, "
                f"additional_properties={self.additional_properties!s})")
