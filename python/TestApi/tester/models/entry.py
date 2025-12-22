"""tester.

This file was automatically generated for Stamplay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

class Entry(object):
    """Implementation of the 'Entry' model.

    Attributes:
        title (str): The model property of type str.
        link (str): The model property of type str.
        author (str): The model property of type str.
        published_date (str): The model property of type str.
        content_snippet (str): The model property of type str.
        content (str): The model property of type str.
        categories (List[str]): The model property of type List[str].
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "author": "author",
        "categories": "categories",
        "content": "content",
        "content_snippet": "contentSnippet",
        "link": "link",
        "published_date": "publishedDate",
        "title": "title",
    }

    def __init__(
        self,
        author=None,
        categories=None,
        content=None,
        content_snippet=None,
        link=None,
        published_date=None,
        title=None,
        additional_properties=None):
        """Initialize a Entry instance."""
        # Initialize members of the class
        self.title = title
        self.link = link
        self.author = author
        self.published_date = published_date
        self.content_snippet = content_snippet
        self.content = content
        self.categories = categories

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
        author =\
            dictionary.get("author")\
            if dictionary.get("author")\
                else None
        categories =\
            dictionary.get("categories")\
            if dictionary.get("categories")\
                else None
        content =\
            dictionary.get("content")\
            if dictionary.get("content")\
                else None
        content_snippet =\
            dictionary.get("contentSnippet")\
            if dictionary.get("contentSnippet")\
                else None
        link =\
            dictionary.get("link")\
            if dictionary.get("link")\
                else None
        published_date =\
            dictionary.get("publishedDate")\
            if dictionary.get("publishedDate")\
                else None
        title =\
            dictionary.get("title")\
            if dictionary.get("title")\
                else None

        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(author,
                   categories,
                   content,
                   content_snippet,
                   link,
                   published_date,
                   title,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _title=self.title
        _link=self.link
        _author=self.author
        _published_date=self.published_date
        _content_snippet=self.content_snippet
        _content=self.content
        _categories=self.categories
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"title={_title!r}"
            f"link={_link!r}"
            f"author={_author!r}"
            f"published_date={_published_date!r}"
            f"content_snippet={_content_snippet!r}"
            f"content={_content!r}"
            f"categories={_categories!r}"
            f"additional_properties={_additional_properties!r}"
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _title=self.title
        _link=self.link
        _author=self.author
        _published_date=self.published_date
        _content_snippet=self.content_snippet
        _content=self.content
        _categories=self.categories
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"title={_title!s}"
            f"link={_link!s}"
            f"author={_author!s}"
            f"published_date={_published_date!s}"
            f"content_snippet={_content_snippet!s}"
            f"content={_content!s}"
            f"categories={_categories!s}"
            f"additional_properties={_additional_properties!s}"
            f")"
        )
