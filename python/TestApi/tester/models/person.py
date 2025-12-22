"""tester.

This file was automatically generated for Stamplay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

import dateutil.parser

from tester.api_helper import APIHelper


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
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "address": "address",
        "age": "age",
        "birthday": "birthday",
        "birthtime": "birthtime",
        "name": "name",
        "uid": "uid",
        "person_type": "personType",
    }

    _optionals = [
        "person_type",
    ]

    def __init__(
        self,
        address=None,
        age=None,
        birthday=None,
        birthtime=None,
        name=None,
        uid=None,
        person_type="Per",
        additional_properties=None):
        """Initialize a Person instance."""
        # Initialize members of the class
        self.address = address
        self.age = age
        self.birthday = birthday
        self.birthtime =\
             APIHelper.apply_datetime_converter(
            birthtime, APIHelper.RFC3339DateTime)\
             if birthtime else None
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
            "Empl": Employee.from_dictionary,
            "Boss": Boss.from_dictionary,
        }
        unboxer = discriminators.get(dictionary.get("personType"))

        # Delegate unboxing to another function if a discriminator
        # value for a child class is present.
        if unboxer:
            return unboxer(dictionary)

        # Extract variables from the dictionary
        address =\
            dictionary.get("address")\
            if dictionary.get("address")\
                else None
        age =\
            dictionary.get("age")\
            if dictionary.get("age")\
                else None
        birthday = dateutil.parser.parse(
            dictionary.get("birthday")).date()\
            if dictionary.get("birthday") else None
        birthtime = APIHelper.RFC3339DateTime.from_value(
            dictionary.get("birthtime")).datetime\
            if dictionary.get("birthtime") else None
        name =\
            dictionary.get("name")\
            if dictionary.get("name")\
                else None
        uid =\
            dictionary.get("uid")\
            if dictionary.get("uid")\
                else None
        person_type =\
            dictionary.get("personType")\
            if dictionary.get("personType")\
                else "Per"

        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(address,
                   age,
                   birthday,
                   birthtime,
                   name,
                   uid,
                   person_type,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _address=self.address
        _age=self.age
        _birthday=self.birthday
        _birthtime=self.birthtime
        _name=self.name
        _uid=self.uid
        _person_type=(
            self.person_type
            if hasattr(self, "person_type")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"address={_address!r}"
            f"age={_age!r}"
            f"birthday={_birthday!r}"
            f"birthtime={_birthtime!r}"
            f"name={_name!r}"
            f"uid={_uid!r}"
            f"person_type={_person_type!r}"
            f"additional_properties={_additional_properties!r}"
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _address=self.address
        _age=self.age
        _birthday=self.birthday
        _birthtime=self.birthtime
        _name=self.name
        _uid=self.uid
        _person_type=(
            self.person_type
            if hasattr(self, "person_type")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"address={_address!s}"
            f"age={_age!s}"
            f"birthday={_birthday!s}"
            f"birthtime={_birthtime!s}"
            f"name={_name!s}"
            f"uid={_uid!s}"
            f"person_type={_person_type!s}"
            f"additional_properties={_additional_properties!s}"
            f")"
        )

class Employee(Person):
    """Implementation of the 'Employee' model.
    NOTE: This class inherits from 'Person'.

    Attributes:
        department (str): The model property of type str.
        dependents (List[Person]): The model property of type List[Person].
        hired_at (datetime): The model property of type datetime.
        joining_day (Days1Enum): The model property of type Days1Enum.
        salary (int): The model property of type int.
        working_days (List[DaysEnum]): The model property of type List[DaysEnum].
        boss (Person): The model property of type Person.
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "address": "address",
        "age": "age",
        "birthday": "birthday",
        "birthtime": "birthtime",
        "boss": "boss",
        "department": "department",
        "dependents": "dependents",
        "hired_at": "hiredAt",
        "joining_day": "joiningDay",
        "name": "name",
        "salary": "salary",
        "uid": "uid",
        "working_days": "workingDays",
        "person_type": "personType",
    }

    _nullables = [
        "boss",
    ]

    def __init__(
        self,
        address=None,
        age=None,
        birthday=None,
        birthtime=None,
        boss=None,
        department=None,
        dependents=None,
        hired_at=None,
        joining_day="Monday",
        name=None,
        salary=None,
        uid=None,
        working_days=None,
        person_type="Empl",
        additional_properties=None):
        """Initialize a Employee instance."""
        # Initialize members of the class
        self.department = department
        self.dependents = dependents
        self.hired_at =\
             APIHelper.apply_datetime_converter(
            hired_at, APIHelper.HttpDateTime)\
             if hired_at else None
        self.joining_day = joining_day
        self.salary = salary
        self.working_days = working_days
        self.boss = boss

        # Call the constructor for the base class
        super(Employee, self).__init__(
            address,
            age,
            birthday,
            birthtime,
            name,
            uid,
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
        address =\
            dictionary.get("address")\
            if dictionary.get("address")\
                else None
        age =\
            dictionary.get("age")\
            if dictionary.get("age")\
                else None
        birthday = dateutil.parser.parse(
            dictionary.get("birthday")).date()\
            if dictionary.get("birthday") else None
        birthtime = APIHelper.RFC3339DateTime.from_value(
            dictionary.get("birthtime")).datetime\
            if dictionary.get("birthtime") else None
        boss =\
            Person.from_dictionary(
            dictionary.get("boss"))\
                if dictionary.get("boss") else None
        department =\
            dictionary.get("department")\
            if dictionary.get("department")\
                else None
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
            if dictionary.get("joiningDay")\
                else "Monday"
        name =\
            dictionary.get("name")\
            if dictionary.get("name")\
                else None
        salary =\
            dictionary.get("salary")\
            if dictionary.get("salary")\
                else None
        uid =\
            dictionary.get("uid")\
            if dictionary.get("uid")\
                else None
        working_days =\
            dictionary.get("workingDays")\
            if dictionary.get("workingDays")\
                else None
        person_type =\
            dictionary.get("personType")\
            if dictionary.get("personType")\
                else "Empl"

        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(address,
                   age,
                   birthday,
                   birthtime,
                   boss,
                   department,
                   dependents,
                   hired_at,
                   joining_day,
                   name,
                   salary,
                   uid,
                   working_days,
                   person_type,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _department=self.department
        _dependents=self.dependents
        _hired_at=self.hired_at
        _joining_day=self.joining_day
        _salary=self.salary
        _working_days=self.working_days
        _boss=self.boss
        _base_repr = super().__repr__()
        _base_repr = _base_repr[_base_repr.find("(") + 1:-1]
        return (
            f"{self.__class__.__name__}("
            f"base_repr={_base_repr!r}"
            f"department={_department!r}"
            f"dependents={_dependents!r}"
            f"hired_at={_hired_at!r}"
            f"joining_day={_joining_day!r}"
            f"salary={_salary!r}"
            f"working_days={_working_days!r}"
            f"boss={_boss!r}"
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _department=self.department
        _dependents=self.dependents
        _hired_at=self.hired_at
        _joining_day=self.joining_day
        _salary=self.salary
        _working_days=self.working_days
        _boss=self.boss
        _base_str = super().__str__()
        _base_str = _base_str[_base_str.find("(") + 1:-1]
        return (
            f"{self.__class__.__name__}("
            f"base_str={_base_str!s}"
            f"department={_department!s}"
            f"dependents={_dependents!s}"
            f"hired_at={_hired_at!s}"
            f"joining_day={_joining_day!s}"
            f"salary={_salary!s}"
            f"working_days={_working_days!s}"
            f"boss={_boss!s}"
            f")"
        )

class Boss(Employee):
    """Implementation of the 'Boss' model.

    Testing circular reference.
    NOTE: This class inherits from 'Employee'.

    Attributes:
        promoted_at (datetime): The model property of type datetime.
        assistant (Employee): The model property of type Employee.
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "address": "address",
        "age": "age",
        "assistant": "assistant",
        "birthday": "birthday",
        "birthtime": "birthtime",
        "boss": "boss",
        "department": "department",
        "dependents": "dependents",
        "hired_at": "hiredAt",
        "joining_day": "joiningDay",
        "name": "name",
        "promoted_at": "promotedAt",
        "salary": "salary",
        "uid": "uid",
        "working_days": "workingDays",
        "person_type": "personType",
    }

    _nullables = [
        "assistant",
    ]
    _nullables.extend(Employee._nullables)

    def __init__(
        self,
        address=None,
        age=None,
        assistant=None,
        birthday=None,
        birthtime=None,
        boss=None,
        department=None,
        dependents=None,
        hired_at=None,
        joining_day="Monday",
        name=None,
        promoted_at=None,
        salary=None,
        uid=None,
        working_days=None,
        person_type="Boss",
        additional_properties=None):
        """Initialize a Boss instance."""
        # Initialize members of the class
        self.promoted_at =\
             APIHelper.apply_datetime_converter(
            promoted_at, APIHelper.UnixDateTime)\
             if promoted_at else None
        self.assistant = assistant

        # Call the constructor for the base class
        super(Boss, self).__init__(
            address,
            age,
            birthday,
            birthtime,
            boss,
            department,
            dependents,
            hired_at,
            joining_day,
            name,
            salary,
            uid,
            working_days,
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
        address =\
            dictionary.get("address")\
            if dictionary.get("address")\
                else None
        age =\
            dictionary.get("age")\
            if dictionary.get("age")\
                else None
        assistant =\
            Employee.from_dictionary(
            dictionary.get("assistant"))\
                if dictionary.get("assistant") else None
        birthday = dateutil.parser.parse(
            dictionary.get("birthday")).date()\
            if dictionary.get("birthday") else None
        birthtime = APIHelper.RFC3339DateTime.from_value(
            dictionary.get("birthtime")).datetime\
            if dictionary.get("birthtime") else None
        boss =\
            Person.from_dictionary(
            dictionary.get("boss"))\
                if dictionary.get("boss") else None
        department =\
            dictionary.get("department")\
            if dictionary.get("department")\
                else None
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
            if dictionary.get("joiningDay")\
                else "Monday"
        name =\
            dictionary.get("name")\
            if dictionary.get("name")\
                else None
        promoted_at = APIHelper.UnixDateTime.from_value(
            dictionary.get("promotedAt")).datetime\
            if dictionary.get("promotedAt") else None
        salary =\
            dictionary.get("salary")\
            if dictionary.get("salary")\
                else None
        uid =\
            dictionary.get("uid")\
            if dictionary.get("uid")\
                else None
        working_days =\
            dictionary.get("workingDays")\
            if dictionary.get("workingDays")\
                else None
        person_type =\
            dictionary.get("personType")\
            if dictionary.get("personType")\
                else "Boss"

        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(address,
                   age,
                   assistant,
                   birthday,
                   birthtime,
                   boss,
                   department,
                   dependents,
                   hired_at,
                   joining_day,
                   name,
                   promoted_at,
                   salary,
                   uid,
                   working_days,
                   person_type,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _promoted_at=self.promoted_at
        _assistant=self.assistant
        _base_repr = super().__repr__()
        _base_repr = _base_repr[_base_repr.find("(") + 1:-1]
        return (
            f"{self.__class__.__name__}("
            f"base_repr={_base_repr!r}"
            f"promoted_at={_promoted_at!r}"
            f"assistant={_assistant!r}"
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _promoted_at=self.promoted_at
        _assistant=self.assistant
        _base_str = super().__str__()
        _base_str = _base_str[_base_str.find("(") + 1:-1]
        return (
            f"{self.__class__.__name__}("
            f"base_str={_base_str!s}"
            f"promoted_at={_promoted_at!s}"
            f"assistant={_assistant!s}"
            f")"
        )
