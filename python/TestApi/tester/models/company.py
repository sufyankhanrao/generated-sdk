"""tester.

This file was automatically generated for Stamplay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

class Company(object):
    """Implementation of the 'Company' model.

    Attributes:
        company_name (str): The model property of type str.
        address (str): The model property of type str.
        cell_number (str): The model property of type str.
        company (str): The model property of type str.
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "address": "address",
        "cell_number": "cell number",
        "company_name": "company name",
        "company": "company",
    }

    _optionals = [
        "company",
    ]

    def __init__(
        self,
        address=None,
        cell_number=None,
        company_name=None,
        company="comp",
        additional_properties=None):
        """Initialize a Company instance."""
        # Initialize members of the class
        self.company_name = company_name
        self.address = address
        self.cell_number = cell_number
        self.company = company

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
            "boss_comp": BossCompany.from_dictionary,
            "empl_comp": EmployeeComp.from_dictionary,
            "Software_Tester": SoftwareTester.from_dictionary,
            "developer": Developer.from_dictionary,
        }
        unboxer = discriminators.get(dictionary.get("company"))

        # Delegate unboxing to another function if a discriminator
        # value for a child class is present.
        if unboxer:
            return unboxer(dictionary)

        # Extract variables from the dictionary
        address =\
            dictionary.get("address")\
            if dictionary.get("address")\
                else None
        cell_number =\
            dictionary.get("cell number")\
            if dictionary.get("cell number")\
                else None
        company_name =\
            dictionary.get("company name")\
            if dictionary.get("company name")\
                else None
        company =\
            dictionary.get("company")\
            if dictionary.get("company")\
                else "comp"

        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(address,
                   cell_number,
                   company_name,
                   company,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _company_name=self.company_name
        _address=self.address
        _cell_number=self.cell_number
        _company=(
            self.company
            if hasattr(self, "company")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"company_name={_company_name!r}"
            f"address={_address!r}"
            f"cell_number={_cell_number!r}"
            f"company={_company!r}"
            f"additional_properties={_additional_properties!r}"
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _company_name=self.company_name
        _address=self.address
        _cell_number=self.cell_number
        _company=(
            self.company
            if hasattr(self, "company")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"company_name={_company_name!s}"
            f"address={_address!s}"
            f"cell_number={_cell_number!s}"
            f"company={_company!s}"
            f"additional_properties={_additional_properties!s}"
            f")"
        )

class BossCompany(Company):
    """Implementation of the 'Boss_company' model.
    NOTE: This class inherits from 'Company'.

    Attributes:
        first_name (str): The model property of type str.
        last_name (str): The model property of type str.
        address_boss (str): The model property of type str.
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "address": "address",
        "address_boss": "address_boss",
        "cell_number": "cell number",
        "company_name": "company name",
        "first_name": "first name",
        "last_name": "last name",
        "company": "company",
    }

    def __init__(
        self,
        address=None,
        address_boss=None,
        cell_number=None,
        company_name=None,
        first_name=None,
        last_name=None,
        company="boss_comp",
        additional_properties=None):
        """Initialize a BossCompany instance."""
        # Initialize members of the class
        self.first_name = first_name
        self.last_name = last_name
        self.address_boss = address_boss

        # Call the constructor for the base class
        super(BossCompany, self).__init__(
            address,
            cell_number,
            company_name,
            company,
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
        address_boss =\
            dictionary.get("address_boss")\
            if dictionary.get("address_boss")\
                else None
        cell_number =\
            dictionary.get("cell number")\
            if dictionary.get("cell number")\
                else None
        company_name =\
            dictionary.get("company name")\
            if dictionary.get("company name")\
                else None
        first_name =\
            dictionary.get("first name")\
            if dictionary.get("first name")\
                else None
        last_name =\
            dictionary.get("last name")\
            if dictionary.get("last name")\
                else None
        company =\
            dictionary.get("company")\
            if dictionary.get("company")\
                else "boss_comp"

        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(address,
                   address_boss,
                   cell_number,
                   company_name,
                   first_name,
                   last_name,
                   company,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _first_name=self.first_name
        _last_name=self.last_name
        _address_boss=self.address_boss
        _base_repr = super().__repr__()
        _base_repr = _base_repr[_base_repr.find("(") + 1:-1]
        return (
            f"{self.__class__.__name__}("
            f"base_repr={_base_repr!r}"
            f"first_name={_first_name!r}"
            f"last_name={_last_name!r}"
            f"address_boss={_address_boss!r}"
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _first_name=self.first_name
        _last_name=self.last_name
        _address_boss=self.address_boss
        _base_str = super().__str__()
        _base_str = _base_str[_base_str.find("(") + 1:-1]
        return (
            f"{self.__class__.__name__}("
            f"base_str={_base_str!s}"
            f"first_name={_first_name!s}"
            f"last_name={_last_name!s}"
            f"address_boss={_address_boss!s}"
            f")"
        )

class EmployeeComp(Company):
    """Implementation of the 'employee_comp' model.
    NOTE: This class inherits from 'Company'.

    Attributes:
        first_name (str): The model property of type str.
        last_name (str): The model property of type str.
        id (str): The model property of type str.
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "address": "address",
        "cell_number": "cell number",
        "company_name": "company name",
        "first_name": "first name",
        "id": "id",
        "last_name": "last name",
        "company": "company",
    }

    def __init__(
        self,
        address=None,
        cell_number=None,
        company_name=None,
        first_name=None,
        id=None,
        last_name=None,
        company="empl_comp",
        additional_properties=None):
        """Initialize a EmployeeComp instance."""
        # Initialize members of the class
        self.first_name = first_name
        self.last_name = last_name
        self.id = id

        # Call the constructor for the base class
        super(EmployeeComp, self).__init__(
            address,
            cell_number,
            company_name,
            company,
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
            "Software_Tester": SoftwareTester.from_dictionary,
            "developer": Developer.from_dictionary,
        }
        unboxer = discriminators.get(dictionary.get("company"))

        # Delegate unboxing to another function if a discriminator
        # value for a child class is present.
        if unboxer:
            return unboxer(dictionary)

        # Extract variables from the dictionary
        address =\
            dictionary.get("address")\
            if dictionary.get("address")\
                else None
        cell_number =\
            dictionary.get("cell number")\
            if dictionary.get("cell number")\
                else None
        company_name =\
            dictionary.get("company name")\
            if dictionary.get("company name")\
                else None
        first_name =\
            dictionary.get("first name")\
            if dictionary.get("first name")\
                else None
        id =\
            dictionary.get("id")\
            if dictionary.get("id")\
                else None
        last_name =\
            dictionary.get("last name")\
            if dictionary.get("last name")\
                else None
        company =\
            dictionary.get("company")\
            if dictionary.get("company")\
                else "empl_comp"

        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(address,
                   cell_number,
                   company_name,
                   first_name,
                   id,
                   last_name,
                   company,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _first_name=self.first_name
        _last_name=self.last_name
        _id=self.id
        _base_repr = super().__repr__()
        _base_repr = _base_repr[_base_repr.find("(") + 1:-1]
        return (
            f"{self.__class__.__name__}("
            f"base_repr={_base_repr!r}"
            f"first_name={_first_name!r}"
            f"last_name={_last_name!r}"
            f"id={_id!r}"
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _first_name=self.first_name
        _last_name=self.last_name
        _id=self.id
        _base_str = super().__str__()
        _base_str = _base_str[_base_str.find("(") + 1:-1]
        return (
            f"{self.__class__.__name__}("
            f"base_str={_base_str!s}"
            f"first_name={_first_name!s}"
            f"last_name={_last_name!s}"
            f"id={_id!s}"
            f")"
        )

class SoftwareTester(EmployeeComp):
    """Implementation of the 'Software Tester' model.
    NOTE: This class inherits from 'EmployeeComp'.

    Attributes:
        team (str): The model property of type str.
        designation (str): The model property of type str.
        role (str): The model property of type str.
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "address": "address",
        "cell_number": "cell number",
        "company_name": "company name",
        "designation": "designation",
        "first_name": "first name",
        "id": "id",
        "last_name": "last name",
        "role": "role",
        "team": "team",
        "company": "company",
    }

    def __init__(
        self,
        address=None,
        cell_number=None,
        company_name=None,
        designation=None,
        first_name=None,
        id=None,
        last_name=None,
        role=None,
        team=None,
        company="Software_Tester",
        additional_properties=None):
        """Initialize a SoftwareTester instance."""
        # Initialize members of the class
        self.team = team
        self.designation = designation
        self.role = role

        # Call the constructor for the base class
        super(SoftwareTester, self).__init__(
            address,
            cell_number,
            company_name,
            first_name,
            id,
            last_name,
            company,
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
        cell_number =\
            dictionary.get("cell number")\
            if dictionary.get("cell number")\
                else None
        company_name =\
            dictionary.get("company name")\
            if dictionary.get("company name")\
                else None
        designation =\
            dictionary.get("designation")\
            if dictionary.get("designation")\
                else None
        first_name =\
            dictionary.get("first name")\
            if dictionary.get("first name")\
                else None
        id =\
            dictionary.get("id")\
            if dictionary.get("id")\
                else None
        last_name =\
            dictionary.get("last name")\
            if dictionary.get("last name")\
                else None
        role =\
            dictionary.get("role")\
            if dictionary.get("role")\
                else None
        team =\
            dictionary.get("team")\
            if dictionary.get("team")\
                else None
        company =\
            dictionary.get("company")\
            if dictionary.get("company")\
                else "Software_Tester"

        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(address,
                   cell_number,
                   company_name,
                   designation,
                   first_name,
                   id,
                   last_name,
                   role,
                   team,
                   company,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _team=self.team
        _designation=self.designation
        _role=self.role
        _base_repr = super().__repr__()
        _base_repr = _base_repr[_base_repr.find("(") + 1:-1]
        return (
            f"{self.__class__.__name__}("
            f"base_repr={_base_repr!r}"
            f"team={_team!r}"
            f"designation={_designation!r}"
            f"role={_role!r}"
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _team=self.team
        _designation=self.designation
        _role=self.role
        _base_str = super().__str__()
        _base_str = _base_str[_base_str.find("(") + 1:-1]
        return (
            f"{self.__class__.__name__}("
            f"base_str={_base_str!s}"
            f"team={_team!s}"
            f"designation={_designation!s}"
            f"role={_role!s}"
            f")"
        )

class Developer(EmployeeComp):
    """Implementation of the 'developer' model.
    NOTE: This class inherits from 'EmployeeComp'.

    Attributes:
        team (str): The model property of type str.
        designation (str): The model property of type str.
        role (str): The model property of type str.
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "address": "address",
        "cell_number": "cell number",
        "company_name": "company name",
        "designation": "designation",
        "first_name": "first name",
        "id": "id",
        "last_name": "last name",
        "role": "role",
        "team": "team",
        "company": "company",
    }

    def __init__(
        self,
        address=None,
        cell_number=None,
        company_name=None,
        designation=None,
        first_name=None,
        id=None,
        last_name=None,
        role=None,
        team=None,
        company="developer",
        additional_properties=None):
        """Initialize a Developer instance."""
        # Initialize members of the class
        self.team = team
        self.designation = designation
        self.role = role

        # Call the constructor for the base class
        super(Developer, self).__init__(
            address,
            cell_number,
            company_name,
            first_name,
            id,
            last_name,
            company,
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
        cell_number =\
            dictionary.get("cell number")\
            if dictionary.get("cell number")\
                else None
        company_name =\
            dictionary.get("company name")\
            if dictionary.get("company name")\
                else None
        designation =\
            dictionary.get("designation")\
            if dictionary.get("designation")\
                else None
        first_name =\
            dictionary.get("first name")\
            if dictionary.get("first name")\
                else None
        id =\
            dictionary.get("id")\
            if dictionary.get("id")\
                else None
        last_name =\
            dictionary.get("last name")\
            if dictionary.get("last name")\
                else None
        role =\
            dictionary.get("role")\
            if dictionary.get("role")\
                else None
        team =\
            dictionary.get("team")\
            if dictionary.get("team")\
                else None
        company =\
            dictionary.get("company")\
            if dictionary.get("company")\
                else "developer"

        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(address,
                   cell_number,
                   company_name,
                   designation,
                   first_name,
                   id,
                   last_name,
                   role,
                   team,
                   company,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _team=self.team
        _designation=self.designation
        _role=self.role
        _base_repr = super().__repr__()
        _base_repr = _base_repr[_base_repr.find("(") + 1:-1]
        return (
            f"{self.__class__.__name__}("
            f"base_repr={_base_repr!r}"
            f"team={_team!r}"
            f"designation={_designation!r}"
            f"role={_role!r}"
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _team=self.team
        _designation=self.designation
        _role=self.role
        _base_str = super().__str__()
        _base_str = _base_str[_base_str.find("(") + 1:-1]
        return (
            f"{self.__class__.__name__}("
            f"base_str={_base_str!s}"
            f"team={_team!s}"
            f"designation={_designation!s}"
            f"role={_role!s}"
            f")"
        )
