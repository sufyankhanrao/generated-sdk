# -*- coding: utf-8 -*-

"""
testerfilesandmultipart

This file was automatically generated for Stamplay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
import dateutil.parser

from testerfilesandmultipart.api_helper import APIHelper


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
        "address": 'address',
        "age": 'age',
        "birthday": 'birthday',
        "birthtime": 'birthtime',
        "name": 'name',
        "uid": 'uid',
        "person_type": 'personType'
    }

    _optionals = [
        'person_type',
    ]

    def __init__(self,
                 address=None,
                 age=None,
                 birthday=None,
                 birthtime=None,
                 name=None,
                 uid=None,
                 person_type='Per',
                 additional_properties=None):
        """Constructor for the Person class"""

        # Initialize members of the class
        self.address = address 
        self.age = age 
        self.birthday = birthday 
        self.birthtime = APIHelper.apply_datetime_converter(birthtime, APIHelper.RFC3339DateTime) if birthtime else None 
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

        discriminators = {
            'Empl': Employee.from_dictionary,
            'Boss': Boss.from_dictionary
        }
        unboxer = discriminators.get(dictionary.get('personType'))

        # Delegate unboxing to another function if a discriminator
        # value for a child class is present.
        if unboxer:
            return unboxer(dictionary)

        # Extract variables from the dictionary
        address = dictionary.get("address") if dictionary.get("address") else None
        age = dictionary.get("age") if dictionary.get("age") else None
        birthday = dateutil.parser.parse(dictionary.get('birthday')).date() if dictionary.get('birthday') else None
        birthtime = APIHelper.RFC3339DateTime.from_value(dictionary.get("birthtime")).datetime if dictionary.get("birthtime") else None
        name = dictionary.get("name") if dictionary.get("name") else None
        uid = dictionary.get("uid") if dictionary.get("uid") else None
        person_type = dictionary.get("personType") if dictionary.get("personType") else 'Per'
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
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
        return (f'{self.__class__.__name__}('
                f'address={self.address!r}, '
                f'age={self.age!r}, '
                f'birthday={self.birthday!r}, '
                f'birthtime={self.birthtime!r}, '
                f'name={self.name!r}, '
                f'uid={self.uid!r}, '
                f'person_type={(self.person_type if hasattr(self, "person_type") else None)!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'address={self.address!s}, '
                f'age={self.age!s}, '
                f'birthday={self.birthday!s}, '
                f'birthtime={self.birthtime!s}, '
                f'name={self.name!s}, '
                f'uid={self.uid!s}, '
                f'person_type={(self.person_type if hasattr(self, "person_type") else None)!s}, '
                f'additional_properties={self.additional_properties!s})')

class Employee(Person):

    """Implementation of the 'Employee' model.
    NOTE: This class inherits from 'Person'.

    Attributes:
        department (str): The model property of type str.
        dependents (List[Person]): The model property of type List[Person].
        hired_at (datetime): The model property of type datetime.
        joining_day (Days): The model property of type Days.
        salary (int): The model property of type int.
        working_days (List[Days]): The model property of type List[Days].
        boss (Person): The model property of type Person.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "address": 'address',
        "age": 'age',
        "birthday": 'birthday',
        "birthtime": 'birthtime',
        "boss": 'boss',
        "department": 'department',
        "dependents": 'dependents',
        "hired_at": 'hiredAt',
        "joining_day": 'joiningDay',
        "name": 'name',
        "salary": 'salary',
        "uid": 'uid',
        "working_days": 'workingDays',
        "person_type": 'personType'
    }

    _nullables = [
        'boss',
    ]

    def __init__(self,
                 address=None,
                 age=None,
                 birthday=None,
                 birthtime=None,
                 boss=None,
                 department=None,
                 dependents=None,
                 hired_at=None,
                 joining_day='Monday',
                 name=None,
                 salary=None,
                 uid=None,
                 working_days=None,
                 person_type='Empl',
                 additional_properties=None):
        """Constructor for the Employee class"""

        # Initialize members of the class
        self.department = department 
        self.dependents = dependents 
        self.hired_at = APIHelper.apply_datetime_converter(hired_at, APIHelper.HttpDateTime) if hired_at else None 
        self.joining_day = joining_day 
        self.salary = salary 
        self.working_days = working_days 
        self.boss = boss 

        # Call the constructor for the base class
        super(Employee, self).__init__(address,
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

        discriminators = {
            'Boss': Boss.from_dictionary
        }
        unboxer = discriminators.get(dictionary.get('personType'))

        # Delegate unboxing to another function if a discriminator
        # value for a child class is present.
        if unboxer:
            return unboxer(dictionary)

        # Extract variables from the dictionary
        address = dictionary.get("address") if dictionary.get("address") else None
        age = dictionary.get("age") if dictionary.get("age") else None
        birthday = dateutil.parser.parse(dictionary.get('birthday')).date() if dictionary.get('birthday') else None
        birthtime = APIHelper.RFC3339DateTime.from_value(dictionary.get("birthtime")).datetime if dictionary.get("birthtime") else None
        boss = Person.from_dictionary(dictionary.get('boss')) if dictionary.get('boss') else None
        department = dictionary.get("department") if dictionary.get("department") else None
        dependents = None
        if dictionary.get('dependents') is not None:
            dependents = [Person.from_dictionary(x) for x in dictionary.get('dependents')]
        hired_at = APIHelper.HttpDateTime.from_value(dictionary.get("hiredAt")).datetime if dictionary.get("hiredAt") else None
        joining_day = dictionary.get("joiningDay") if dictionary.get("joiningDay") else 'Monday'
        name = dictionary.get("name") if dictionary.get("name") else None
        salary = dictionary.get("salary") if dictionary.get("salary") else None
        uid = dictionary.get("uid") if dictionary.get("uid") else None
        working_days = dictionary.get("workingDays") if dictionary.get("workingDays") else None
        person_type = dictionary.get("personType") if dictionary.get("personType") else 'Empl'
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
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
        base_repr = super().__repr__()
        return (f'{self.__class__.__name__}('
                f'{base_repr[base_repr.find("(") + 1:-1]}, '
                f'department={self.department!r}, '
                f'dependents={self.dependents!r}, '
                f'hired_at={self.hired_at!r}, '
                f'joining_day={self.joining_day!r}, '
                f'salary={self.salary!r}, '
                f'working_days={self.working_days!r}, '
                f'boss={self.boss!r})')

    def __str__(self):
        base_str = super().__str__()
        return (f'{self.__class__.__name__}('
                f'{base_str[base_str.find("(") + 1:-1]}, '
                f'department={self.department!s}, '
                f'dependents={self.dependents!s}, '
                f'hired_at={self.hired_at!s}, '
                f'joining_day={self.joining_day!s}, '
                f'salary={self.salary!s}, '
                f'working_days={self.working_days!s}, '
                f'boss={self.boss!s})')

class Boss(Employee):

    """Implementation of the 'Boss' model.

    Testing circular reference.
    NOTE: This class inherits from 'Employee'.

    Attributes:
        promoted_at (datetime): The model property of type datetime.
        assistant (Employee): The model property of type Employee.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "address": 'address',
        "age": 'age',
        "assistant": 'assistant',
        "birthday": 'birthday',
        "birthtime": 'birthtime',
        "boss": 'boss',
        "department": 'department',
        "dependents": 'dependents',
        "hired_at": 'hiredAt',
        "joining_day": 'joiningDay',
        "name": 'name',
        "promoted_at": 'promotedAt',
        "salary": 'salary',
        "uid": 'uid',
        "working_days": 'workingDays',
        "person_type": 'personType'
    }

    _nullables = [
        'assistant',
    ]
    _nullables.extend(Employee._nullables)

    def __init__(self,
                 address=None,
                 age=None,
                 assistant=None,
                 birthday=None,
                 birthtime=None,
                 boss=None,
                 department=None,
                 dependents=None,
                 hired_at=None,
                 joining_day='Monday',
                 name=None,
                 promoted_at=None,
                 salary=None,
                 uid=None,
                 working_days=None,
                 person_type='Boss',
                 additional_properties=None):
        """Constructor for the Boss class"""

        # Initialize members of the class
        self.promoted_at = APIHelper.apply_datetime_converter(promoted_at, APIHelper.UnixDateTime) if promoted_at else None 
        self.assistant = assistant 

        # Call the constructor for the base class
        super(Boss, self).__init__(address,
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
        address = dictionary.get("address") if dictionary.get("address") else None
        age = dictionary.get("age") if dictionary.get("age") else None
        assistant = Employee.from_dictionary(dictionary.get('assistant')) if dictionary.get('assistant') else None
        birthday = dateutil.parser.parse(dictionary.get('birthday')).date() if dictionary.get('birthday') else None
        birthtime = APIHelper.RFC3339DateTime.from_value(dictionary.get("birthtime")).datetime if dictionary.get("birthtime") else None
        boss = Person.from_dictionary(dictionary.get('boss')) if dictionary.get('boss') else None
        department = dictionary.get("department") if dictionary.get("department") else None
        dependents = None
        if dictionary.get('dependents') is not None:
            dependents = [Person.from_dictionary(x) for x in dictionary.get('dependents')]
        hired_at = APIHelper.HttpDateTime.from_value(dictionary.get("hiredAt")).datetime if dictionary.get("hiredAt") else None
        joining_day = dictionary.get("joiningDay") if dictionary.get("joiningDay") else 'Monday'
        name = dictionary.get("name") if dictionary.get("name") else None
        promoted_at = APIHelper.UnixDateTime.from_value(dictionary.get("promotedAt")).datetime if dictionary.get("promotedAt") else None
        salary = dictionary.get("salary") if dictionary.get("salary") else None
        uid = dictionary.get("uid") if dictionary.get("uid") else None
        working_days = dictionary.get("workingDays") if dictionary.get("workingDays") else None
        person_type = dictionary.get("personType") if dictionary.get("personType") else 'Boss'
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
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
        base_repr = super().__repr__()
        return (f'{self.__class__.__name__}('
                f'{base_repr[base_repr.find("(") + 1:-1]}, '
                f'promoted_at={self.promoted_at!r}, '
                f'assistant={self.assistant!r})')

    def __str__(self):
        base_str = super().__str__()
        return (f'{self.__class__.__name__}('
                f'{base_str[base_str.find("(") + 1:-1]}, '
                f'promoted_at={self.promoted_at!s}, '
                f'assistant={self.assistant!s})')
