"""tester.

This file was automatically generated for Stamplay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from tester.models.entry import Entry


class Feed(object):
    """Implementation of the 'Feed' model.

    Attributes:
        feed_url (str): The model property of type str.
        title (str): The model property of type str.
        link (str): The model property of type str.
        author (str): The model property of type str.
        description (str): The model property of type str.
        mtype (str): The model property of type str.
        entries (List[Entry]): The model property of type List[Entry].
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "author": "author",
        "description": "description",
        "entries": "entries",
        "feed_url": "feedUrl",
        "link": "link",
        "title": "title",
        "mtype": "type",
    }

    def __init__(
        self,
        author=None,
        description=None,
        entries=None,
        feed_url=None,
        link=None,
        title=None,
        mtype=None,
        additional_properties=None):
        """Initialize a Feed instance."""
        # Initialize members of the class
        self.feed_url = feed_url
        self.title = title
        self.link = link
        self.author = author
        self.description = description
        self.mtype = mtype
        self.entries = entries

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
        description =\
            dictionary.get("description")\
            if dictionary.get("description")\
                else None
        entries = None
        if dictionary.get("entries") is not None:
            entries = [
                Entry.from_dictionary(x)
                    for x in dictionary.get("entries")
            ]
        feed_url =\
            dictionary.get("feedUrl")\
            if dictionary.get("feedUrl")\
                else None
        link =\
            dictionary.get("link")\
            if dictionary.get("link")\
                else None
        title =\
            dictionary.get("title")\
            if dictionary.get("title")\
                else None
        mtype =\
            dictionary.get("type")\
            if dictionary.get("type")\
                else None

        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(author,
                   description,
                   entries,
                   feed_url,
                   link,
                   title,
                   mtype,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _feed_url=self.feed_url
        _title=self.title
        _link=self.link
        _author=self.author
        _description=self.description
        _mtype=self.mtype
        _entries=self.entries
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"feed_url={_feed_url!r}"
            f"title={_title!r}"
            f"link={_link!r}"
            f"author={_author!r}"
            f"description={_description!r}"
            f"mtype={_mtype!r}"
            f"entries={_entries!r}"
            f"additional_properties={_additional_properties!r}"
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _feed_url=self.feed_url
        _title=self.title
        _link=self.link
        _author=self.author
        _description=self.description
        _mtype=self.mtype
        _entries=self.entries
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"feed_url={_feed_url!s}"
            f"title={_title!s}"
            f"link={_link!s}"
            f"author={_author!s}"
            f"description={_description!s}"
            f"mtype={_mtype!s}"
            f"entries={_entries!s}"
            f"additional_properties={_additional_properties!s}"
            f")"
        )
