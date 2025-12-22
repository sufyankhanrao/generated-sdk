
"""
tester

This file was automatically generated for Stamplay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: PLR0915, W291
import dateutil.parser
from apimatic_core.utilities.comparison_helper import (
    ComparisonHelper,
)

from tester.api_helper import APIHelper
from tester.models.complex_type import ComplexType
from tests.controllers.controller_test_base import (
    ControllerTestBase,
)


class QueryParamControllerTests(ControllerTestBase):
    """
    Endpoint tests for validating the API behavior.

    Ensures controller methods execute correctly and produce the expected
    responses using the shared test client and response catcher.
    """

    controller = None

    @classmethod
    def setUpClass(cls):
        """
        Initialize the shared test client and controller for all test methods.
        """
        super().setUpClass()
        cls.controller = cls.client.query_param
        cls.response_catcher = cls.controller.http_call_back

    def test_date_array(self):
        """
        Api call test for `test_date_array`.
        """
        # Parameters for the API call
        dates = [
            dateutil.parser.parse(element).date()
            for element in APIHelper.json_deserialize(
            "[\"1994-02-13\",\"1994-02-13\"]",
        )
        ]

        # Perform the API call through the SDK function
        result = self.controller.date_array(
            dates,
        )
        # Test response code
        assert self.response_catcher.response.status_code == 200
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize(
            "{\"passed\":true}",
        )
        received_body = APIHelper.json_deserialize(
            self.response_catcher.response.text,
        )
        assert ComparisonHelper.match_body(
            expected_body,
            received_body,
            check_values = True,
        )

    def test_optional_dynamic_query_param(self):
        """
        Api call test for `test_optional_dynamic_query_param`.
        """
        # Parameters for the API call
        name = "farhan"

        # dictionary for optional query parameters
        optional_query_parameters = {}
        optional_query_parameters["field"] =  "QA"

        # Perform the API call through the SDK function
        result = self.controller.optional_dynamic_query_param(
            name,
            optional_query_parameters,
        )
        # Test response code
        assert self.response_catcher.response.status_code == 200
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize(
            "{\"passed\":true}",
        )
        received_body = APIHelper.json_deserialize(
            self.response_catcher.response.text,
        )
        assert ComparisonHelper.match_body(
            expected_body,
            received_body,
            check_values = True,
        )

    def test_date(self):
        """
        Api call test for `test_date`.
        """
        # Parameters for the API call
        date = dateutil.parser.parse(
            "1994-02-13",
        ).date()

        # Perform the API call through the SDK function
        result = self.controller.date(
            date,
        )
        # Test response code
        assert self.response_catcher.response.status_code == 200
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize(
            "{\"passed\":true}",
        )
        received_body = APIHelper.json_deserialize(
            self.response_catcher.response.text,
        )
        assert ComparisonHelper.match_body(
            expected_body,
            received_body,
            check_values = True,
        )

    def test_unix_date_time_array(self):
        """
        Api call test for `test_unix_date_time_array`.
        """
        # Parameters for the API call
        datetimes = [
            element.datetime for element in APIHelper.json_deserialize(
                "[1484719381,1484719381]",
                APIHelper.UnixDateTime.from_value,
            )
        ]

        # Perform the API call through the SDK function
        result = self.controller.unix_date_time_array(
            datetimes,
        )
        # Test response code
        assert self.response_catcher.response.status_code == 200
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize(
            "{\"passed\":true}",
        )
        received_body = APIHelper.json_deserialize(
            self.response_catcher.response.text,
        )
        assert ComparisonHelper.match_body(
            expected_body,
            received_body,
            check_values = True,
        )

    def test_unix_date_time(self):
        """
        Api call test for `test_unix_date_time`.
        """
        # Parameters for the API call
        datetime = APIHelper.UnixDateTime.from_value(
            1484719381,
        ).datetime

        # Perform the API call through the SDK function
        result = self.controller.unix_date_time(
            datetime,
        )
        # Test response code
        assert self.response_catcher.response.status_code == 200
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize(
            "{\"passed\":true}",
        )
        received_body = APIHelper.json_deserialize(
            self.response_catcher.response.text,
        )
        assert ComparisonHelper.match_body(
            expected_body,
            received_body,
            check_values = True,
        )

    def test_rfc_1123_date_time(self):
        """
        Api call test for `test_rfc_1123_date_time`.
        """
        # Parameters for the API call
        datetime = APIHelper.HttpDateTime.from_value(
            "Sun, 06 Nov 1994 08:49:37 GMT",
        ).datetime

        # Perform the API call through the SDK function
        result = self.controller.rfc_1123_date_time(
            datetime,
        )
        # Test response code
        assert self.response_catcher.response.status_code == 200
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize(
            "{\"passed\":true}",
        )
        received_body = APIHelper.json_deserialize(
            self.response_catcher.response.text,
        )
        assert ComparisonHelper.match_body(
            expected_body,
            received_body,
            check_values = True,
        )

    def test_rfc_1123_date_time_array(self):
        """
        Api call test for `test_rfc_1123_date_time_array`.
        """
        # Parameters for the API call
        datetimes = [
            element.datetime for element in APIHelper.json_deserialize(
                "[\"Sun, 06 Nov 1994 08:49:37 GMT\",\"Sun, 06 Nov 1994 08:49:37 GMT\"]",
                APIHelper.HttpDateTime.from_value,
            )
        ]

        # Perform the API call through the SDK function
        result = self.controller.rfc_1123_date_time_array(
            datetimes,
        )
        # Test response code
        assert self.response_catcher.response.status_code == 200
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize(
            "{\"passed\":true}",
        )
        received_body = APIHelper.json_deserialize(
            self.response_catcher.response.text,
        )
        assert ComparisonHelper.match_body(
            expected_body,
            received_body,
            check_values = True,
        )

    def test_rfc_3339_date_time_array(self):
        """
        Api call test for `test_rfc_3339_date_time_array`.
        """
        # Parameters for the API call
        datetimes = [
            element.datetime for element in APIHelper.json_deserialize(
                "[\"1994-02-13T14:01:54.9571247Z\",\"1994-02-13T14:01:54.9571247Z\"]",
                APIHelper.RFC3339DateTime.from_value,
            )
        ]

        # Perform the API call through the SDK function
        result = self.controller.rfc_3339_date_time_array(
            datetimes,
        )
        # Test response code
        assert self.response_catcher.response.status_code == 200
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize(
            "{\"passed\":true}",
        )
        received_body = APIHelper.json_deserialize(
            self.response_catcher.response.text,
        )
        assert ComparisonHelper.match_body(
            expected_body,
            received_body,
            check_values = True,
        )

    def test_rfc_3339_date_time(self):
        """
        Api call test for `test_rfc_3339_date_time`.
        """
        # Parameters for the API call
        datetime = APIHelper.RFC3339DateTime.from_value(
            "1994-02-13T14:01:54.9571247Z",
        ).datetime

        # Perform the API call through the SDK function
        result = self.controller.rfc_3339_date_time(
            datetime,
        )
        # Test response code
        assert self.response_catcher.response.status_code == 200
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize(
            "{\"passed\":true}",
        )
        received_body = APIHelper.json_deserialize(
            self.response_catcher.response.text,
        )
        assert ComparisonHelper.match_body(
            expected_body,
            received_body,
            check_values = True,
        )

    def test_no_params(self):
        """
        Api call test for `test_no_params`.
        """
        # Perform the API call through the SDK function
        result = self.controller.no_params()
        # Test response code
        assert self.response_catcher.response.status_code == 200
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize(
            "{\"passed\":true}",
        )
        received_body = APIHelper.json_deserialize(
            self.response_catcher.response.text,
        )
        assert ComparisonHelper.match_body(
            expected_body,
            received_body,
            check_values = True,
        )

    def test_string_param(self):
        """
        Api call test for `test_string_param`.
        """
        # Parameters for the API call
        string = "l;asd;asdwe[2304&&;'.d??\\a\\\\\\;sd//"

        # Perform the API call through the SDK function
        result = self.controller.string_param(
            string,
        )
        # Test response code
        assert self.response_catcher.response.status_code == 200
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize(
            "{\"passed\":true}",
        )
        received_body = APIHelper.json_deserialize(
            self.response_catcher.response.text,
        )
        assert ComparisonHelper.match_body(
            expected_body,
            received_body,
            check_values = True,
        )

    def test_url_param(self):
        """
        Api call test for `test_url_param`.
        """
        # Parameters for the API call
        url = "https://www.shahidisawesome.com/and/also/a/narcissist?thisis=aparameter&another=one"

        # Perform the API call through the SDK function
        result = self.controller.url_param(
            url,
        )
        # Test response code
        assert self.response_catcher.response.status_code == 200
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize(
            "{\"passed\":true}",
        )
        received_body = APIHelper.json_deserialize(
            self.response_catcher.response.text,
        )
        assert ComparisonHelper.match_body(
            expected_body,
            received_body,
            check_values = True,
        )

    def test_number_array(self):
        """
        Api call test for `test_number_array`.
        """
        # Parameters for the API call
        integers = APIHelper.json_deserialize(
            "[1,2,3,4,5]",
        )

        # Perform the API call through the SDK function
        result = self.controller.number_array(
            integers,
        )
        # Test response code
        assert self.response_catcher.response.status_code in list(range(200, 209))
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize(
            "{\"passed\":true}",
        )
        received_body = APIHelper.json_deserialize(
            self.response_catcher.response.text,
        )
        assert ComparisonHelper.match_body(
            expected_body,
            received_body,
            check_values = True,
        )

    def test_string_array(self):
        """
        Api call test for `test_string_array`.
        """
        # Parameters for the API call
        strings = APIHelper.json_deserialize(
            "[\"abc\",\"def\"]",
        )

        # Perform the API call through the SDK function
        result = self.controller.string_array(
            strings,
        )
        # Test response code
        assert self.response_catcher.response.status_code == 200
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize(
            "{\"passed\":true}",
        )
        received_body = APIHelper.json_deserialize(
            self.response_catcher.response.text,
        )
        assert ComparisonHelper.match_body(
            expected_body,
            received_body,
            check_values = True,
        )

    def test_simple_query(self):
        """
        Api call test for `test_simple_query`.
        """
        # Parameters for the API call
        boolean = True
        number = 4
        string = "TestString"

        # dictionary for optional query parameters
        optional_query_parameters = {}

        # Perform the API call through the SDK function
        result = self.controller.simple_query(
            boolean,
            number,
            string,
            optional_query_parameters,
        )
        # Test response code
        assert self.response_catcher.response.status_code == 200
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize(
            "{\"passed\":true}",
        )
        received_body = APIHelper.json_deserialize(
            self.response_catcher.response.text,
        )
        assert ComparisonHelper.match_body(
            expected_body,
            received_body,
            check_values = True,
        )

    def test_string_enum_array(self):
        """
        Api call test for `test_string_enum_array`.
        """
        # Parameters for the API call
        days = APIHelper.json_deserialize(
            "[\"Tuesday\",\"Saturday\",\"Wednesday\",\"Monday\",\"Sunday\"]",
        )

        # Perform the API call through the SDK function
        result = self.controller.string_enum_array(
            days,
        )
        # Test response code
        assert self.response_catcher.response.status_code == 200
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize(
            "{\"passed\":true}",
        )
        received_body = APIHelper.json_deserialize(
            self.response_catcher.response.text,
        )
        assert ComparisonHelper.match_body(
            expected_body,
            received_body,
            check_values = True,
        )

    def test_multiple_params(self):
        """
        Api call test for `test_multiple_params`.
        """
        # Parameters for the API call
        number = 123412312
        precision = 1112.34
        string = "\"\"test./;\";12&&3asl\"\";\"qw1&34\"///..//."
        url = "http://www.abc.com/test?a=b&c=\"http://lolol.com?param=no&another=lol\""

        # Perform the API call through the SDK function
        result = self.controller.multiple_params(
            number,
            precision,
            string,
            url,
        )
        # Test response code
        assert self.response_catcher.response.status_code == 200
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize(
            "{\"passed\":true}",
        )
        received_body = APIHelper.json_deserialize(
            self.response_catcher.response.text,
        )
        assert ComparisonHelper.match_body(
            expected_body,
            received_body,
            check_values = True,
        )

    def test_integer_enum_array(self):
        """
        Api call test for `test_integer_enum_array`.
        """
        # Parameters for the API call
        suites = APIHelper.json_deserialize(
            "[1,3,4,2,3]",
        )

        # Perform the API call through the SDK function
        result = self.controller.integer_enum_array(
            suites,
        )
        # Test response code
        assert self.response_catcher.response.status_code == 200
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize(
            "{\"passed\":true}",
        )
        received_body = APIHelper.json_deserialize(
            self.response_catcher.response.text,
        )
        assert ComparisonHelper.match_body(
            expected_body,
            received_body,
            check_values = True,
        )

    def test_send_unindexed_complex_type_in_query(self):
        """
        Api call test for `test_send_unindexed_complex_type_in_query`.
        """
        # Parameters for the API call
        complex_type = APIHelper.json_deserialize(
            "{\"numberListType\":[555,666,777],\"numberMapType\":{\"num1\":1,\"num3\""
            ":2,\"num2\":3},\"innerComplexType\":{\"stringType\":\"MyString1\",\"bool"
            "eanType\":true,\"dateTimeType\":\"1994-11-06T08:49:37Z\",\"dateType\":\""
            "1994-02-13\",\"uuidType\":\"a5e48529-745b-4dfb-aac0-a7d844debd8b\",\"lon"
            "gType\":500000000,\"precisionType\":5.43,\"objectType\":{\"long2\":10000"
            "00000,\"long1\":500000000},\"stringListType\":[\"Item1\",\"Item2\"]},\"i"
            "nnerComplexListType\":[{\"stringType\":\"MyString1\",\"booleanType\":tru"
            "e,\"dateTimeType\":\"1994-11-06T08:49:37Z\",\"dateType\":\"1994-02-13\","
            "\"uuidType\":\"a5e48529-745b-4dfb-aac0-a7d844debd8b\",\"longType\":50000"
            "0000,\"precisionType\":5.43,\"objectType\":{\"long2\":1000000000,\"long1"
            "\":500000000},\"stringListType\":[\"Item1\",\"Item2\"]},{\"stringType\":"
            "\"MyString2\",\"booleanType\":false,\"dateTimeType\":\"1994-11-07T08:49:"
            "37Z\",\"dateType\":\"1994-02-12\",\"uuidType\":\"b46ba2d3-b4ac-4b40-ae62"
            "-6326e88c89a6\",\"longType\":1000000000,\"precisionType\":5.43,\"objectT"
            "ype\":{\"bool1\":true,\"bool2\":false},\"stringListType\":[\"Item1\",\"I"
            "tem2\"]}]}",
            ComplexType.from_dictionary,
        )

        # Perform the API call through the SDK function
        result = self.controller.send_indexed_complex_type_in_query(
            complex_type,
        )
        # Test response code
        assert self.response_catcher.response.status_code == 200
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize(
            "{\"passed\":true}",
        )
        received_body = APIHelper.json_deserialize(
            self.response_catcher.response.text,
        )
        assert ComparisonHelper.match_body(
            expected_body,
            received_body,
            check_values = True,
        )

    def test_send_indexed_list_of_complex_type_in_query(self):
        """
        Api call test for `test_send_indexed_list_of_complex_type_in_query`.
        """
        # Parameters for the API call
        complex_type = APIHelper.json_deserialize(
            "[{\"numberListType\":[555,666,777],\"numberMapType\":{\"num1\":1,\"num3"
            "\":2,\"num2\":3},\"innerComplexType\":{\"stringType\":\"MyString1\",\"bo"
            "oleanType\":true,\"dateTimeType\":\"1994-11-06T08:49:37Z\",\"dateType\":"
            "\"1994-02-13\",\"uuidType\":\"a5e48529-745b-4dfb-aac0-a7d844debd8b\",\"l"
            "ongType\":500000000,\"precisionType\":5.43,\"objectType\":{\"long2\":100"
            "0000000,\"long1\":500000000},\"stringListType\":[\"Item1\",\"Item2\"]},"
            "\"innerComplexListType\":[{\"stringType\":\"MyString1\",\"booleanType\":"
            "true,\"dateTimeType\":\"1994-11-06T08:49:37Z\",\"dateType\":\"1994-02-13"
            "\",\"uuidType\":\"a5e48529-745b-4dfb-aac0-a7d844debd8b\",\"longType\":50"
            "0000000,\"precisionType\":5.43,\"objectType\":{\"long2\":1000000000,\"lo"
            "ng1\":500000000},\"stringListType\":[\"Item1\",\"Item2\"]},{\"stringType"
            "\":\"MyString2\",\"booleanType\":false,\"dateTimeType\":\"1994-11-07T08:"
            "49:37Z\",\"dateType\":\"1994-02-12\",\"uuidType\":\"b46ba2d3-b4ac-4b40-a"
            "e62-6326e88c89a6\",\"longType\":1000000000,\"precisionType\":5.43,\"obje"
            "ctType\":{\"bool1\":true,\"bool2\":false},\"stringListType\":[\"Item1\","
            "\"Item2\"]}]},{\"numberListType\":[555,666,777],\"numberMapType\":{\"num"
            "1\":1,\"num3\":2,\"num2\":3},\"innerComplexType\":{\"stringType\":\"MySt"
            "ring1\",\"booleanType\":true,\"dateTimeType\":\"1994-11-06T08:49:37Z\","
            "\"dateType\":\"1994-02-13\",\"uuidType\":\"a5e48529-745b-4dfb-aac0-a7d84"
            "4debd8b\",\"longType\":500000000,\"precisionType\":5.43,\"objectType\":{"
            "\"long2\":1000000000,\"long1\":500000000},\"stringListType\":[\"Item1\","
            "\"Item2\"]},\"innerComplexListType\":[{\"stringType\":\"MyString1\",\"bo"
            "oleanType\":true,\"dateTimeType\":\"1994-11-06T08:49:37Z\",\"dateType\":"
            "\"1994-02-13\",\"uuidType\":\"a5e48529-745b-4dfb-aac0-a7d844debd8b\",\"l"
            "ongType\":500000000,\"precisionType\":5.43,\"objectType\":{\"long2\":100"
            "0000000,\"long1\":500000000},\"stringListType\":[\"Item1\",\"Item2\"]},{"
            "\"stringType\":\"MyString2\",\"booleanType\":false,\"dateTimeType\":\"19"
            "94-11-07T08:49:37Z\",\"dateType\":\"1994-02-12\",\"uuidType\":\"b46ba2d3"
            "-b4ac-4b40-ae62-6326e88c89a6\",\"longType\":1000000000,\"precisionType\""
            ":5.43,\"objectType\":{\"bool1\":true,\"bool2\":false},\"stringListType\""
            ":[\"Item1\",\"Item2\"]}]}]",
            ComplexType.from_dictionary,
        )

        # Perform the API call through the SDK function
        result = self.controller.send_indexed_list_of_complex_type_in_query(
            complex_type,
        )
        # Test response code
        assert self.response_catcher.response.status_code == 200
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize(
            "{\"passed\":true}",
        )
        received_body = APIHelper.json_deserialize(
            self.response_catcher.response.text,
        )
        assert ComparisonHelper.match_body(
            expected_body,
            received_body,
            check_values = True,
        )

    def test_send_indexed_map_of_complex_type_in_query(self):
        """
        Api call test for `test_send_indexed_map_of_complex_type_in_query`.
        """
        # Parameters for the API call
        complex_type = APIHelper.json_deserialize(
            "{\"key1\":{\"numberListType\":[555,666,777],\"numberMapType\":{\"num1\":"
            "1,\"num3\":2,\"num2\":3},\"innerComplexType\":{\"stringType\":\"MyString"
            "1\",\"booleanType\":true,\"dateTimeType\":\"1994-11-06T08:49:37Z\",\"dat"
            "eType\":\"1994-02-13\",\"uuidType\":\"a5e48529-745b-4dfb-aac0-a7d844debd"
            "8b\",\"longType\":500000000,\"precisionType\":5.43,\"objectType\":{\"lon"
            "g2\":1000000000,\"long1\":500000000},\"stringListType\":[\"Item1\",\"Ite"
            "m2\"]},\"innerComplexListType\":[{\"stringType\":\"MyString1\",\"boolean"
            "Type\":true,\"dateTimeType\":\"1994-11-06T08:49:37Z\",\"dateType\":\"199"
            "4-02-13\",\"uuidType\":\"a5e48529-745b-4dfb-aac0-a7d844debd8b\",\"longTy"
            "pe\":500000000,\"precisionType\":5.43,\"objectType\":{\"long2\":10000000"
            "00,\"long1\":500000000},\"stringListType\":[\"Item1\",\"Item2\"]},{\"str"
            "ingType\":\"MyString2\",\"booleanType\":false,\"dateTimeType\":\"1994-11"
            "-07T08:49:37Z\",\"dateType\":\"1994-02-12\",\"uuidType\":\"b46ba2d3-b4ac"
            "-4b40-ae62-6326e88c89a6\",\"longType\":1000000000,\"precisionType\":5.43"
            ",\"objectType\":{\"bool1\":true,\"bool2\":false},\"stringListType\":[\"I"
            "tem1\",\"Item2\"]}]},\"key2\":{\"numberListType\":[555,666,777],\"number"
            "MapType\":{\"num1\":1,\"num3\":2,\"num2\":3},\"innerComplexType\":{\"str"
            "ingType\":\"MyString1\",\"booleanType\":true,\"dateTimeType\":\"1994-11-"
            "06T08:49:37Z\",\"dateType\":\"1994-02-13\",\"uuidType\":\"a5e48529-745b-"
            "4dfb-aac0-a7d844debd8b\",\"longType\":500000000,\"precisionType\":5.43,"
            "\"objectType\":{\"long2\":1000000000,\"long1\":500000000},\"stringListTy"
            "pe\":[\"Item1\",\"Item2\"]},\"innerComplexListType\":[{\"stringType\":\""
            "MyString1\",\"booleanType\":true,\"dateTimeType\":\"1994-11-06T08:49:37Z"
            "\",\"dateType\":\"1994-02-13\",\"uuidType\":\"a5e48529-745b-4dfb-aac0-a7"
            "d844debd8b\",\"longType\":500000000,\"precisionType\":5.43,\"objectType"
            "\":{\"long2\":1000000000,\"long1\":500000000},\"stringListType\":[\"Item"
            "1\",\"Item2\"]},{\"stringType\":\"MyString2\",\"booleanType\":false,\"da"
            "teTimeType\":\"1994-11-07T08:49:37Z\",\"dateType\":\"1994-02-12\",\"uuid"
            "Type\":\"b46ba2d3-b4ac-4b40-ae62-6326e88c89a6\",\"longType\":1000000000,"
            "\"precisionType\":5.43,\"objectType\":{\"bool1\":true,\"bool2\":false},"
            "\"stringListType\":[\"Item1\",\"Item2\"]}]}}",
            ComplexType.from_dictionary,
            as_dict=True,
        )

        # Perform the API call through the SDK function
        result = self.controller.send_indexed_map_of_complex_type_in_query(
            complex_type,
        )
        # Test response code
        assert self.response_catcher.response.status_code == 200
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize(
            "{\"passed\":true}",
        )
        received_body = APIHelper.json_deserialize(
            self.response_catcher.response.text,
        )
        assert ComparisonHelper.match_body(
            expected_body,
            received_body,
            check_values = True,
        )

