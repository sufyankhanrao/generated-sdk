"""testcodesamples.

This file was automatically generated for Stamplay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

import dateutil.parser

from testcodesamples.api_helper import APIHelper


class Person(object):
    """Implementation of the 'Person' model.

    Attributes:
        address (str): The model property of type str.
        age (int): The model property of type int.
        birthday (date): The model property of type date.
        birthtime (datetime): The model property of type datetime.
        name (str): The model property of type str.
        uid (str): The model property of type str.
        person_type (str): The model property of type str.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "address": "address",
        "age": "age",
        "name": "name",
        "uid": "uid",
        "birthday": "birthday",
        "birthtime": "birthtime",
        "person_type": "personType",
    }

    _optionals = [
        "birthday",
        "birthtime",
        "person_type",
    ]

    def __init__(self,
                 address=None,
                 age=None,
                 name=None,
                 uid=None,
                 birthday=APIHelper.SKIP,
                 birthtime=APIHelper.SKIP,
                 person_type="Per",
                 additional_properties=None):
        """Initialize a Person instance."""
        # Initialize members of the class
        self.address = address
        self.age = age
        if birthday is not APIHelper.SKIP:
            self.birthday = birthday
        if birthtime is not APIHelper.SKIP:
            self.birthtime =\
                 APIHelper.apply_datetime_converter(
                birthtime, APIHelper.RFC3339DateTime) if birthtime else None
        self.name = name
        self.uid = uid
        self.person_type = person_type

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

        discriminators = {
            "Empl": EmployeeRequired.from_dictionary,
            "Empl": EmployeeOptional.from_dictionary,
            "Boss": Boss.from_dictionary,
        }
        unboxer = discriminators.get(dictionary.get("personType"))

        # Delegate unboxing to another function if a discriminator
        # value for a child class is present.
        if unboxer:
            return unboxer(dictionary)

        # Extract variables from the dictionary
        address = dictionary.get("address") if dictionary.get("address") else None
        age = dictionary.get("age") if dictionary.get("age") else None
        name = dictionary.get("name") if dictionary.get("name") else None
        uid = dictionary.get("uid") if dictionary.get("uid") else None
        birthday = dateutil.parser.parse(dictionary.get("birthday")).date()\
            if dictionary.get("birthday") else APIHelper.SKIP
        birthtime = APIHelper.RFC3339DateTime.from_value(
            dictionary.get("birthtime")).datetime\
            if dictionary.get("birthtime") else APIHelper.SKIP
        person_type =\
            dictionary.get("personType")\
            if dictionary.get("personType") else "Per"
        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(address,
                   age,
                   name,
                   uid,
                   birthday,
                   birthtime,
                   person_type,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        return (f"{self.__class__.__name__}("
                f"address={self.address!r}, "
                f"age={self.age!r}, "
                f"birthday={(self.birthday
                     if hasattr(self, 'birthday') else None)!r}, "
                f"birthtime={(self.birthtime
                     if hasattr(self, 'birthtime') else None)!r}, "
                f"name={self.name!r}, "
                f"uid={self.uid!r}, "
                f"person_type={(self.person_type
                     if hasattr(self, 'person_type') else None)!r}, "
                f"additional_properties={self.additional_properties!r})")

    def __str__(self):
        """Return a human-readable string representation."""
        return (f"{self.__class__.__name__}("
                f"address={self.address!s}, "
                f"age={self.age!s}, "
                f"birthday={(self.birthday
                     if hasattr(self, 'birthday') else None)!s}, "
                f"birthtime={(self.birthtime
                     if hasattr(self, 'birthtime') else None)!s}, "
                f"name={self.name!s}, "
                f"uid={self.uid!s}, "
                f"person_type={(self.person_type
                     if hasattr(self, 'person_type') else None)!s}, "
                f"additional_properties={self.additional_properties!s})")

class EmployeeRequired(Person):
    """Implementation of the 'EmployeeRequired' model.
    NOTE: This class inherits from 'Person'.

    Attributes:
        department (str): The model property of type str.
        boolean_var (bool): The model property of type bool.
        object_var (Any): The model property of type Any.
        dynamic_var (Any): The model property of type Any.
        date_time_unix_var (datetime): The model property of type datetime.
        r_fc_1123_var (datetime): The model property of type datetime.
        r_fc_3339_var (datetime): The model property of type datetime.
        date_var (date): The model property of type date.
        dependents (List[Person]): The model property of type List[Person].
        hired_at (datetime): The model property of type datetime.
        joining_day (Days): The model property of type Days.
        salary (int): The model property of type int.
        boss (Person): The model property of type Person.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "department": "department",
        "boolean_var": "booleanVar",
        "object_var": "objectVar",
        "dynamic_var": "dynamicVar",
        "date_time_unix_var": "dateTimeUnixVar",
        "r_fc_1123_var": "rFC1123Var",
        "r_fc_3339_var": "rFC3339Var",
        "date_var": "dateVar",
        "dependents": "dependents",
        "hired_at": "hiredAt",
        "joining_day": "joiningDay",
        "salary": "salary",
        "boss": "boss",
        "address": "address",
        "age": "age",
        "name": "name",
        "uid": "uid",
        "birthday": "birthday",
        "birthtime": "birthtime",
        "person_type": "personType",
    }

    _nullables = [
        "boss",
    ]

    def __init__(self,
                 department=None,
                 boolean_var=None,
                 object_var=None,
                 dynamic_var=None,
                 date_time_unix_var=None,
                 r_fc_1123_var=None,
                 r_fc_3339_var=None,
                 date_var=None,
                 dependents=None,
                 hired_at=None,
                 joining_day="Monday",
                 salary=None,
                 boss=None,
                 address=None,
                 age=None,
                 name=None,
                 uid=None,
                 birthday=APIHelper.SKIP,
                 birthtime=APIHelper.SKIP,
                 person_type="Empl",
                 additional_properties=None):
        """Initialize a EmployeeRequired instance."""
        # Initialize members of the class
        self.department = department
        self.boolean_var = boolean_var
        self.object_var = object_var
        self.dynamic_var = dynamic_var
        self.date_time_unix_var =\
             APIHelper.apply_datetime_converter(
            date_time_unix_var, APIHelper.UnixDateTime) if date_time_unix_var else None
        self.r_fc_1123_var =\
             APIHelper.apply_datetime_converter(
            r_fc_1123_var, APIHelper.HttpDateTime) if r_fc_1123_var else None
        self.r_fc_3339_var =\
             APIHelper.apply_datetime_converter(
            r_fc_3339_var, APIHelper.RFC3339DateTime) if r_fc_3339_var else None
        self.date_var = date_var
        self.dependents = dependents
        self.hired_at =\
             APIHelper.apply_datetime_converter(
            hired_at, APIHelper.HttpDateTime) if hired_at else None
        self.joining_day = joining_day
        self.salary = salary
        self.boss = boss

        # Call the constructor for the base class
        super(EmployeeRequired, self).__init__(address,
                                               age,
                                               name,
                                               uid,
                                               birthday,
                                               birthtime,
                                               person_type,
                                               additional_properties)

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

        discriminators = {
            "Boss": Boss.from_dictionary,
        }
        unboxer = discriminators.get(dictionary.get("personType"))

        # Delegate unboxing to another function if a discriminator
        # value for a child class is present.
        if unboxer:
            return unboxer(dictionary)

        # Extract variables from the dictionary
        department =\
            dictionary.get("department")\
            if dictionary.get("department") else None
        boolean_var =\
            dictionary.get("booleanVar")\
            if "booleanVar" in dictionary.keys() else None
        object_var =\
            dictionary.get("objectVar")\
            if dictionary.get("objectVar") else None
        dynamic_var =\
            dictionary.get("dynamicVar")\
            if dictionary.get("dynamicVar") else None
        date_time_unix_var = APIHelper.UnixDateTime.from_value(
            dictionary.get("dateTimeUnixVar")).datetime\
            if dictionary.get("dateTimeUnixVar") else None
        r_fc_1123_var = APIHelper.HttpDateTime.from_value(
            dictionary.get("rFC1123Var")).datetime\
            if dictionary.get("rFC1123Var") else None
        r_fc_3339_var = APIHelper.RFC3339DateTime.from_value(
            dictionary.get("rFC3339Var")).datetime\
            if dictionary.get("rFC3339Var") else None
        date_var = dateutil.parser.parse(dictionary.get("dateVar")).date()\
            if dictionary.get("dateVar") else None
        dependents = None
        if dictionary.get("dependents") is not None:
            dependents = [
                Person.from_dictionary(x)
                    for x in dictionary.get("dependents")
            ]
        hired_at = APIHelper.HttpDateTime.from_value(
            dictionary.get("hiredAt")).datetime\
            if dictionary.get("hiredAt") else None
        joining_day =\
            dictionary.get("joiningDay")\
            if dictionary.get("joiningDay") else "Monday"
        salary = dictionary.get("salary") if dictionary.get("salary") else None
        boss = Person.from_dictionary(
            dictionary.get("boss"))\
            if dictionary.get("boss") else None
        address = dictionary.get("address") if dictionary.get("address") else None
        age = dictionary.get("age") if dictionary.get("age") else None
        name = dictionary.get("name") if dictionary.get("name") else None
        uid = dictionary.get("uid") if dictionary.get("uid") else None
        birthday = dateutil.parser.parse(dictionary.get("birthday")).date()\
            if dictionary.get("birthday") else APIHelper.SKIP
        birthtime = APIHelper.RFC3339DateTime.from_value(
            dictionary.get("birthtime")).datetime\
            if dictionary.get("birthtime") else APIHelper.SKIP
        person_type =\
            dictionary.get("personType")\
            if dictionary.get("personType") else "Empl"
        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(department,
                   boolean_var,
                   object_var,
                   dynamic_var,
                   date_time_unix_var,
                   r_fc_1123_var,
                   r_fc_3339_var,
                   date_var,
                   dependents,
                   hired_at,
                   joining_day,
                   salary,
                   boss,
                   address,
                   age,
                   name,
                   uid,
                   birthday,
                   birthtime,
                   person_type,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        base_repr = super().__repr__()
        return (f"{self.__class__.__name__}("
                f"{base_repr[base_repr.find('(') + 1:-1]}, "
                f"department={self.department!r}, "
                f"boolean_var={self.boolean_var!r}, "
                f"object_var={self.object_var!r}, "
                f"dynamic_var={self.dynamic_var!r}, "
                f"date_time_unix_var={self.date_time_unix_var!r}, "
                f"r_fc_1123_var={self.r_fc_1123_var!r}, "
                f"r_fc_3339_var={self.r_fc_3339_var!r}, "
                f"date_var={self.date_var!r}, "
                f"dependents={self.dependents!r}, "
                f"hired_at={self.hired_at!r}, "
                f"joining_day={self.joining_day!r}, "
                f"salary={self.salary!r}, "
                f"boss={self.boss!r})")

    def __str__(self):
        """Return a human-readable string representation."""
        base_str = super().__str__()
        return (f"{self.__class__.__name__}("
                f"{base_str[base_str.find('(') + 1:-1]}, "
                f"department={self.department!s}, "
                f"boolean_var={self.boolean_var!s}, "
                f"object_var={self.object_var!s}, "
                f"dynamic_var={self.dynamic_var!s}, "
                f"date_time_unix_var={self.date_time_unix_var!s}, "
                f"r_fc_1123_var={self.r_fc_1123_var!s}, "
                f"r_fc_3339_var={self.r_fc_3339_var!s}, "
                f"date_var={self.date_var!s}, "
                f"dependents={self.dependents!s}, "
                f"hired_at={self.hired_at!s}, "
                f"joining_day={self.joining_day!s}, "
                f"salary={self.salary!s}, "
                f"boss={self.boss!s})")

class EmployeeOptional(Person):
    """Implementation of the 'EmployeeOptional' model.
    NOTE: This class inherits from 'Person'.

    Attributes:
        department (str): The model property of type str.
        boolean_var (bool): The model property of type bool.
        object_var (Any): The model property of type Any.
        dynamic_var (Any): The model property of type Any.
        date_time_unix_var (datetime): The model property of type datetime.
        r_fc_1123_var (datetime): The model property of type datetime.
        r_fc_3339_var (datetime): The model property of type datetime.
        date_var (date): The model property of type date.
        dependents (List[Person]): The model property of type List[Person].
        hired_at (datetime): The model property of type datetime.
        joining_day (Days): The model property of type Days.
        salary (int): The model property of type int.
        boss (Person): The model property of type Person.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "address": "address",
        "age": "age",
        "name": "name",
        "uid": "uid",
        "department": "department",
        "boolean_var": "booleanVar",
        "object_var": "objectVar",
        "dynamic_var": "dynamicVar",
        "date_time_unix_var": "dateTimeUnixVar",
        "r_fc_1123_var": "rFC1123Var",
        "r_fc_3339_var": "rFC3339Var",
        "date_var": "dateVar",
        "dependents": "dependents",
        "hired_at": "hiredAt",
        "joining_day": "joiningDay",
        "salary": "salary",
        "boss": "boss",
        "birthday": "birthday",
        "birthtime": "birthtime",
        "person_type": "personType",
    }

    _optionals = [
        "department",
        "boolean_var",
        "object_var",
        "dynamic_var",
        "date_time_unix_var",
        "r_fc_1123_var",
        "r_fc_3339_var",
        "date_var",
        "dependents",
        "hired_at",
        "joining_day",
        "salary",
        "boss",
    ]
    _optionals.extend(Person._optionals)

    _nullables = [
        "boss",
    ]

    def __init__(self,
                 address=None,
                 age=None,
                 name=None,
                 uid=None,
                 department=APIHelper.SKIP,
                 boolean_var=APIHelper.SKIP,
                 object_var=APIHelper.SKIP,
                 dynamic_var=APIHelper.SKIP,
                 date_time_unix_var=APIHelper.SKIP,
                 r_fc_1123_var=APIHelper.SKIP,
                 r_fc_3339_var=APIHelper.SKIP,
                 date_var=APIHelper.SKIP,
                 dependents=APIHelper.SKIP,
                 hired_at=APIHelper.SKIP,
                 joining_day="Monday",
                 salary=APIHelper.SKIP,
                 boss=APIHelper.SKIP,
                 birthday=APIHelper.SKIP,
                 birthtime=APIHelper.SKIP,
                 person_type="Empl",
                 additional_properties=None):
        """Initialize a EmployeeOptional instance."""
        # Initialize members of the class
        if department is not APIHelper.SKIP:
            self.department = department
        if boolean_var is not APIHelper.SKIP:
            self.boolean_var = boolean_var
        if object_var is not APIHelper.SKIP:
            self.object_var = object_var
        if dynamic_var is not APIHelper.SKIP:
            self.dynamic_var = dynamic_var
        if date_time_unix_var is not APIHelper.SKIP:
            self.date_time_unix_var =\
                 APIHelper.apply_datetime_converter(
                date_time_unix_var, APIHelper.UnixDateTime) if date_time_unix_var else None
        if r_fc_1123_var is not APIHelper.SKIP:
            self.r_fc_1123_var =\
                 APIHelper.apply_datetime_converter(
                r_fc_1123_var, APIHelper.HttpDateTime) if r_fc_1123_var else None
        if r_fc_3339_var is not APIHelper.SKIP:
            self.r_fc_3339_var =\
                 APIHelper.apply_datetime_converter(
                r_fc_3339_var, APIHelper.RFC3339DateTime) if r_fc_3339_var else None
        if date_var is not APIHelper.SKIP:
            self.date_var = date_var
        if dependents is not APIHelper.SKIP:
            self.dependents = dependents
        if hired_at is not APIHelper.SKIP:
            self.hired_at =\
                 APIHelper.apply_datetime_converter(
                hired_at, APIHelper.HttpDateTime) if hired_at else None
        self.joining_day = joining_day
        if salary is not APIHelper.SKIP:
            self.salary = salary
        if boss is not APIHelper.SKIP:
            self.boss = boss

        # Call the constructor for the base class
        super(EmployeeOptional, self).__init__(address,
                                               age,
                                               name,
                                               uid,
                                               birthday,
                                               birthtime,
                                               person_type,
                                               additional_properties)

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
        address = dictionary.get("address") if dictionary.get("address") else None
        age = dictionary.get("age") if dictionary.get("age") else None
        name = dictionary.get("name") if dictionary.get("name") else None
        uid = dictionary.get("uid") if dictionary.get("uid") else None
        department =\
            dictionary.get("department")\
            if dictionary.get("department") else APIHelper.SKIP
        boolean_var =\
            dictionary.get("booleanVar")\
            if "booleanVar" in dictionary.keys() else APIHelper.SKIP
        object_var =\
            dictionary.get("objectVar")\
            if dictionary.get("objectVar") else APIHelper.SKIP
        dynamic_var =\
            dictionary.get("dynamicVar")\
            if dictionary.get("dynamicVar") else APIHelper.SKIP
        date_time_unix_var = APIHelper.UnixDateTime.from_value(
            dictionary.get("dateTimeUnixVar")).datetime\
            if dictionary.get("dateTimeUnixVar") else APIHelper.SKIP
        r_fc_1123_var = APIHelper.HttpDateTime.from_value(
            dictionary.get("rFC1123Var")).datetime\
            if dictionary.get("rFC1123Var") else APIHelper.SKIP
        r_fc_3339_var = APIHelper.RFC3339DateTime.from_value(
            dictionary.get("rFC3339Var")).datetime\
            if dictionary.get("rFC3339Var") else APIHelper.SKIP
        date_var = dateutil.parser.parse(dictionary.get("dateVar")).date()\
            if dictionary.get("dateVar") else APIHelper.SKIP
        dependents = None
        if dictionary.get("dependents") is not None:
            dependents = [
                Person.from_dictionary(x)
                    for x in dictionary.get("dependents")
            ]
        else:
            dependents = APIHelper.SKIP
        hired_at = APIHelper.HttpDateTime.from_value(
            dictionary.get("hiredAt")).datetime\
            if dictionary.get("hiredAt") else APIHelper.SKIP
        joining_day =\
            dictionary.get("joiningDay")\
            if dictionary.get("joiningDay") else "Monday"
        salary =\
            dictionary.get("salary")\
            if dictionary.get("salary") else APIHelper.SKIP
        if "boss" in dictionary.keys():
            boss = Person.from_dictionary(dictionary.get("boss")) if dictionary.get("boss") else None
        else:
            boss = APIHelper.SKIP
        birthday = dateutil.parser.parse(dictionary.get("birthday")).date()\
            if dictionary.get("birthday") else APIHelper.SKIP
        birthtime = APIHelper.RFC3339DateTime.from_value(
            dictionary.get("birthtime")).datetime\
            if dictionary.get("birthtime") else APIHelper.SKIP
        person_type =\
            dictionary.get("personType")\
            if dictionary.get("personType") else "Empl"
        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(address,
                   age,
                   name,
                   uid,
                   department,
                   boolean_var,
                   object_var,
                   dynamic_var,
                   date_time_unix_var,
                   r_fc_1123_var,
                   r_fc_3339_var,
                   date_var,
                   dependents,
                   hired_at,
                   joining_day,
                   salary,
                   boss,
                   birthday,
                   birthtime,
                   person_type,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        base_repr = super().__repr__()
        return (f"{self.__class__.__name__}("
                f"{base_repr[base_repr.find('(') + 1:-1]}, "
                f"department={(self.department
                     if hasattr(self, 'department') else None)!r}, "
                f"boolean_var={(self.boolean_var
                     if hasattr(self, 'boolean_var') else None)!r}, "
                f"object_var={(self.object_var
                     if hasattr(self, 'object_var') else None)!r}, "
                f"dynamic_var={(self.dynamic_var
                     if hasattr(self, 'dynamic_var') else None)!r}, "
                f"date_time_unix_var={(self.date_time_unix_var
                     if hasattr(self, 'date_time_unix_var') else None)!r}, "
                f"r_fc_1123_var={(self.r_fc_1123_var
                     if hasattr(self, 'r_fc_1123_var') else None)!r}, "
                f"r_fc_3339_var={(self.r_fc_3339_var
                     if hasattr(self, 'r_fc_3339_var') else None)!r}, "
                f"date_var={(self.date_var
                     if hasattr(self, 'date_var') else None)!r}, "
                f"dependents={(self.dependents
                     if hasattr(self, 'dependents') else None)!r}, "
                f"hired_at={(self.hired_at
                     if hasattr(self, 'hired_at') else None)!r}, "
                f"joining_day={(self.joining_day
                     if hasattr(self, 'joining_day') else None)!r}, "
                f"salary={(self.salary if hasattr(self, 'salary') else None)!r}, "
                f"boss={(self.boss if hasattr(self, 'boss') else None)!r})")

    def __str__(self):
        """Return a human-readable string representation."""
        base_str = super().__str__()
        return (f"{self.__class__.__name__}("
                f"{base_str[base_str.find('(') + 1:-1]}, "
                f"department={(self.department
                     if hasattr(self, 'department') else None)!s}, "
                f"boolean_var={(self.boolean_var
                     if hasattr(self, 'boolean_var') else None)!s}, "
                f"object_var={(self.object_var
                     if hasattr(self, 'object_var') else None)!s}, "
                f"dynamic_var={(self.dynamic_var
                     if hasattr(self, 'dynamic_var') else None)!s}, "
                f"date_time_unix_var={(self.date_time_unix_var
                     if hasattr(self, 'date_time_unix_var') else None)!s}, "
                f"r_fc_1123_var={(self.r_fc_1123_var
                     if hasattr(self, 'r_fc_1123_var') else None)!s}, "
                f"r_fc_3339_var={(self.r_fc_3339_var
                     if hasattr(self, 'r_fc_3339_var') else None)!s}, "
                f"date_var={(self.date_var
                     if hasattr(self, 'date_var') else None)!s}, "
                f"dependents={(self.dependents
                     if hasattr(self, 'dependents') else None)!s}, "
                f"hired_at={(self.hired_at
                     if hasattr(self, 'hired_at') else None)!s}, "
                f"joining_day={(self.joining_day
                     if hasattr(self, 'joining_day') else None)!s}, "
                f"salary={(self.salary if hasattr(self, 'salary') else None)!s}, "
                f"boss={(self.boss if hasattr(self, 'boss') else None)!s})")

class Boss(EmployeeRequired):
    """Implementation of the 'Boss' model.

    Testing circular reference.
    NOTE: This class inherits from 'EmployeeRequired'.

    Attributes:
        promoted_at (datetime): The model property of type datetime.
        assistant (EmployeeRequired): The model property of type
            EmployeeRequired.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "promoted_at": "promotedAt",
        "assistant": "assistant",
        "department": "department",
        "boolean_var": "booleanVar",
        "object_var": "objectVar",
        "dynamic_var": "dynamicVar",
        "date_time_unix_var": "dateTimeUnixVar",
        "r_fc_1123_var": "rFC1123Var",
        "r_fc_3339_var": "rFC3339Var",
        "date_var": "dateVar",
        "dependents": "dependents",
        "hired_at": "hiredAt",
        "joining_day": "joiningDay",
        "salary": "salary",
        "boss": "boss",
        "address": "address",
        "age": "age",
        "name": "name",
        "uid": "uid",
        "birthday": "birthday",
        "birthtime": "birthtime",
        "person_type": "personType",
    }

    _nullables = [
        "assistant",
    ]
    _nullables.extend(EmployeeRequired._nullables)

    def __init__(self,
                 promoted_at=None,
                 assistant=None,
                 department=None,
                 boolean_var=None,
                 object_var=None,
                 dynamic_var=None,
                 date_time_unix_var=None,
                 r_fc_1123_var=None,
                 r_fc_3339_var=None,
                 date_var=None,
                 dependents=None,
                 hired_at=None,
                 joining_day="Monday",
                 salary=None,
                 boss=None,
                 address=None,
                 age=None,
                 name=None,
                 uid=None,
                 birthday=APIHelper.SKIP,
                 birthtime=APIHelper.SKIP,
                 person_type="Boss",
                 additional_properties=None):
        """Initialize a Boss instance."""
        # Initialize members of the class
        self.promoted_at =\
             APIHelper.apply_datetime_converter(
            promoted_at, APIHelper.UnixDateTime) if promoted_at else None
        self.assistant = assistant

        # Call the constructor for the base class
        super(Boss, self).__init__(department,
                                   boolean_var,
                                   object_var,
                                   dynamic_var,
                                   date_time_unix_var,
                                   r_fc_1123_var,
                                   r_fc_3339_var,
                                   date_var,
                                   dependents,
                                   hired_at,
                                   joining_day,
                                   salary,
                                   boss,
                                   address,
                                   age,
                                   name,
                                   uid,
                                   birthday,
                                   birthtime,
                                   person_type,
                                   additional_properties)

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
        promoted_at = APIHelper.UnixDateTime.from_value(
            dictionary.get("promotedAt")).datetime\
            if dictionary.get("promotedAt") else None
        assistant = EmployeeRequired.from_dictionary(
            dictionary.get("assistant"))\
            if dictionary.get("assistant") else None
        department =\
            dictionary.get("department")\
            if dictionary.get("department") else None
        boolean_var =\
            dictionary.get("booleanVar")\
            if "booleanVar" in dictionary.keys() else None
        object_var =\
            dictionary.get("objectVar")\
            if dictionary.get("objectVar") else None
        dynamic_var =\
            dictionary.get("dynamicVar")\
            if dictionary.get("dynamicVar") else None
        date_time_unix_var = APIHelper.UnixDateTime.from_value(
            dictionary.get("dateTimeUnixVar")).datetime\
            if dictionary.get("dateTimeUnixVar") else None
        r_fc_1123_var = APIHelper.HttpDateTime.from_value(
            dictionary.get("rFC1123Var")).datetime\
            if dictionary.get("rFC1123Var") else None
        r_fc_3339_var = APIHelper.RFC3339DateTime.from_value(
            dictionary.get("rFC3339Var")).datetime\
            if dictionary.get("rFC3339Var") else None
        date_var = dateutil.parser.parse(dictionary.get("dateVar")).date()\
            if dictionary.get("dateVar") else None
        dependents = None
        if dictionary.get("dependents") is not None:
            dependents = [
                Person.from_dictionary(x)
                    for x in dictionary.get("dependents")
            ]
        hired_at = APIHelper.HttpDateTime.from_value(
            dictionary.get("hiredAt")).datetime\
            if dictionary.get("hiredAt") else None
        joining_day =\
            dictionary.get("joiningDay")\
            if dictionary.get("joiningDay") else "Monday"
        salary = dictionary.get("salary") if dictionary.get("salary") else None
        boss = Person.from_dictionary(
            dictionary.get("boss"))\
            if dictionary.get("boss") else None
        address = dictionary.get("address") if dictionary.get("address") else None
        age = dictionary.get("age") if dictionary.get("age") else None
        name = dictionary.get("name") if dictionary.get("name") else None
        uid = dictionary.get("uid") if dictionary.get("uid") else None
        birthday = dateutil.parser.parse(dictionary.get("birthday")).date()\
            if dictionary.get("birthday") else APIHelper.SKIP
        birthtime = APIHelper.RFC3339DateTime.from_value(
            dictionary.get("birthtime")).datetime\
            if dictionary.get("birthtime") else APIHelper.SKIP
        person_type =\
            dictionary.get("personType")\
            if dictionary.get("personType") else "Boss"
        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(promoted_at,
                   assistant,
                   department,
                   boolean_var,
                   object_var,
                   dynamic_var,
                   date_time_unix_var,
                   r_fc_1123_var,
                   r_fc_3339_var,
                   date_var,
                   dependents,
                   hired_at,
                   joining_day,
                   salary,
                   boss,
                   address,
                   age,
                   name,
                   uid,
                   birthday,
                   birthtime,
                   person_type,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        base_repr = super().__repr__()
        return (f"{self.__class__.__name__}("
                f"{base_repr[base_repr.find('(') + 1:-1]}, "
                f"promoted_at={self.promoted_at!r}, "
                f"assistant={self.assistant!r})")

    def __str__(self):
        """Return a human-readable string representation."""
        base_str = super().__str__()
        return (f"{self.__class__.__name__}("
                f"{base_str[base_str.find('(') + 1:-1]}, "
                f"promoted_at={self.promoted_at!s}, "
                f"assistant={self.assistant!s})")
