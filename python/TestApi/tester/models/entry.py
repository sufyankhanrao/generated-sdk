# -*- coding: utf-8 -*-

"""
tester

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
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "author": 'author',
        "categories": 'categories',
        "content": 'content',
        "content_snippet": 'contentSnippet',
        "link": 'link',
        "published_date": 'publishedDate',
        "title": 'title'
    }

    def __init__(self,
                 author=None,
                 categories=None,
                 content=None,
                 content_snippet=None,
                 link=None,
                 published_date=None,
                 title=None,
                 additional_properties=None):
        """Constructor for the Entry class"""

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
        author = dictionary.get("author") if dictionary.get("author") else None
        categories = dictionary.get("categories") if dictionary.get("categories") else None
        content = dictionary.get("content") if dictionary.get("content") else None
        content_snippet = dictionary.get("contentSnippet") if dictionary.get("contentSnippet") else None
        link = dictionary.get("link") if dictionary.get("link") else None
        published_date = dictionary.get("publishedDate") if dictionary.get("publishedDate") else None
        title = dictionary.get("title") if dictionary.get("title") else None
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
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
        return (f'{self.__class__.__name__}('
                f'title={self.title!r}, '
                f'link={self.link!r}, '
                f'author={self.author!r}, '
                f'published_date={self.published_date!r}, '
                f'content_snippet={self.content_snippet!r}, '
                f'content={self.content!r}, '
                f'categories={self.categories!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'title={self.title!s}, '
                f'link={self.link!s}, '
                f'author={self.author!s}, '
                f'published_date={self.published_date!s}, '
                f'content_snippet={self.content_snippet!s}, '
                f'content={self.content!s}, '
                f'categories={self.categories!s}, '
                f'additional_properties={self.additional_properties!s})')
