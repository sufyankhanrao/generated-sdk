
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
from apimatic_core.utilities.file_helper import (
    FileHelper,
)

from tester.api_helper import APIHelper
from tester.models.boolean_as_optional import (
    BooleanAsOptional,
)
from tester.models.date_as_optional import DateAsOptional
from tester.models.delete_body import DeleteBody
from tester.models.dynamic_as_optional import (
    DynamicAsOptional,
)
from tester.models.long_as_optional import LongAsOptional
from tester.models.model_with_optional_rfc_1123_date_time import (
    ModelWithOptionalRfc1123DateTime,
)
from tester.models.model_with_optional_rfc_3339_date_time import (
    ModelWithOptionalRfc3339DateTime,
)
from tester.models.number_as_optional import (
    NumberAsOptional,
)
from tester.models.person import Employee
from tester.models.precision_as_optional import (
    PrecisionAsOptional,
)
from tester.models.send_rfc_339_date_time import (
    SendRfc339DateTime,
)
from tester.models.send_rfc_1123_date_time import (
    SendRfc1123DateTime,
)
from tester.models.send_unix_date_time import (
    SendUnixDateTime,
)
from tester.models.string_as_optional import (
    AllOptionals,
    StringAsOptional,
)
from tester.models.test_nstring_encoding import (
    TestNstringEncoding,
)
from tester.models.test_r_nstring_encoding import (
    TestRNstringEncoding,
)
from tester.models.test_rstring_encoding import (
    TestRstringEncoding,
)
from tester.models.unix_date_time import UnixDateTime
from tester.models.uuid_as_optional import UuidAsOptional
from tests.controllers.controller_test_base import (
    ControllerTestBase,
)


class FormParamsControllerTests(ControllerTestBase):
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
        cls.controller = cls.client.form_params
        cls.response_catcher = cls.controller.http_call_back

    def test_delete_form_test(self):
        """
        Api call test for `test_delete_form_test`.
        """
        # Parameters for the API call
        body = APIHelper.json_deserialize(
            "{\"name\":\"farhan\",\"field\":\"QA\"}",
            DeleteBody.from_dictionary,
        )

        # Perform the API call through the SDK function
        result = self.controller.send_delete_form(
            body,
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

    def test_delete_form_test_with_multiliner_name(self):
        """
        Api call test for `test_delete_form_test_with_multiliner_name`.
        """
        # Parameters for the API call
        body = APIHelper.json_deserialize(
            "{\"name\":\"farhan\\nnouman\",\"field\":\"QA\"}",
            DeleteBody.from_dictionary,
        )

        # Perform the API call through the SDK function
        result = self.controller.send_delete_form(
            body,
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

    def test_delete_form_test_with_special_characters_field(self):
        """
        Api call test for `test_delete_form_test_with_special_characters_field`.
        """
        # Parameters for the API call
        body = APIHelper.json_deserialize(
            "{\"name\":\"farhan\",\"field\":\"&&&\"}",
            DeleteBody.from_dictionary,
        )

        # Perform the API call through the SDK function
        result = self.controller.send_delete_form(
            body,
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

    def test_delete_form_test_with_blank_field(self):
        """
        Api call test for `test_delete_form_test_with_blank_field`.
        """
        # Parameters for the API call
        body = APIHelper.json_deserialize(
            "{\"name\":\"farhan\",\"field\":\" \"}",
            DeleteBody.from_dictionary,
        )

        # Perform the API call through the SDK function
        result = self.controller.send_delete_form(
            body,
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

    def test_delete_form_test_with_blank_name_field(self):
        """
        Api call test for `test_delete_form_test_with_blank_name_field`.
        """
        # Parameters for the API call
        body = APIHelper.json_deserialize(
            "{\"name\":\" \",\"field\":\" \"}",
            DeleteBody.from_dictionary,
        )

        # Perform the API call through the SDK function
        result = self.controller.send_delete_form(
            body,
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

    def test_delete_form_test_with_blank_name(self):
        """
        Api call test for `test_delete_form_test_with_blank_name`.
        """
        # Parameters for the API call
        body = APIHelper.json_deserialize(
            "{\"name\":\" \",\"field\":\"QA\"}",
            DeleteBody.from_dictionary,
        )

        # Perform the API call through the SDK function
        result = self.controller.send_delete_form(
            body,
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

    def test_send_date_array(self):
        """
        Api call test for `test_send_date_array`.
        """
        # Parameters for the API call
        dates = [
            dateutil.parser.parse(element).date()
            for element in "[\"1994-02-13\",\"1994-02-13\"]"
        ]

        # Perform the API call through the SDK function
        result = self.controller.send_date_array(
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

    def test_send_date(self):
        """
        Api call test for `test_send_date`.
        """
        # Parameters for the API call
        date = dateutil.parser.parse(
            "1994-02-13",
        ).date()

        # Perform the API call through the SDK function
        result = self.controller.send_date(
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

    def test_send_unix_date_time(self):
        """
        Api call test for `test_send_unix_date_time`.
        """
        # Parameters for the API call
        datetime = APIHelper.UnixDateTime.from_value(
            1484719381,
        ).datetime

        # Perform the API call through the SDK function
        result = self.controller.send_unix_date_time(
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

    def test_send_rfc_1123_date_time(self):
        """
        Api call test for `test_send_rfc_1123_date_time`.
        """
        # Parameters for the API call
        datetime = APIHelper.HttpDateTime.from_value(
            "Sun, 06 Nov 1994 08:49:37 GMT",
        ).datetime

        # Perform the API call through the SDK function
        result = self.controller.send_rfc_1123_date_time(
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

    def test_send_rfc_3339_date_time(self):
        """
        Api call test for `test_send_rfc_3339_date_time`.
        """
        # Parameters for the API call
        datetime = APIHelper.RFC3339DateTime.from_value(
            "1994-02-13T14:01:54.9571247Z",
        ).datetime

        # Perform the API call through the SDK function
        result = self.controller.send_rfc_3339_date_time(
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

    def test_send_unix_date_time_array(self):
        """
        Api call test for `test_send_unix_date_time_array`.
        """
        # Parameters for the API call
        datetimes = [
            element.datetime for element in APIHelper.json_deserialize(
                "[1484719381,1484719381]",
                APIHelper.UnixDateTime.from_value,
            )
        ]

        # Perform the API call through the SDK function
        result = self.controller.send_unix_date_time_array(
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

    def test_send_rfc_1123_date_time_array(self):
        """
        Api call test for `test_send_rfc_1123_date_time_array`.
        """
        # Parameters for the API call
        datetimes = [
            element.datetime for element in APIHelper.json_deserialize(
                "[\"Sun, 06 Nov 1994 08:49:37 GMT\",\"Sun, 06 Nov 1994 08:49:37 GMT"
            "\"]",
                APIHelper.HttpDateTime.from_value,
            )
        ]

        # Perform the API call through the SDK function
        result = self.controller.send_rfc_1123_date_time_array(
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

    def test_send_long(self):
        """
        Api call test for `test_send_long`.
        """
        # Parameters for the API call
        value = 5147483647

        # Perform the API call through the SDK function
        result = self.controller.send_long(
            value,
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

    def test_send_integer_array(self):
        """
        Api call test for `test_send_integer_array`.
        """
        # Parameters for the API call
        integers = APIHelper.json_deserialize(
            "[1,2,3,4,5]",
        )

        # Perform the API call through the SDK function
        result = self.controller.send_integer_array(
            integers,
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

    def test_send_string_array(self):
        """
        Api call test for `test_send_string_array`.
        """
        # Parameters for the API call
        strings = APIHelper.json_deserialize(
            "[\"abc\",\"def\"]",
        )

        # Perform the API call through the SDK function
        result = self.controller.send_string_array(
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

    def test_allow_dynamic_form_fields(self):
        """
        Api call test for `test_allow_dynamic_form_fields`.
        """
        # Parameters for the API call
        name = "farhan"

        # dictionary for optional form parameters
        optional_form_parameters = {}
        optional_form_parameters["field"] =  "QA"

        # Perform the API call through the SDK function
        result = self.controller.allow_dynamic_form_fields(
            name,
            optional_form_parameters,
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

    def test_send_model(self):
        """
        Api call test for `test_send_model`.
        """
        # Parameters for the API call
        model = APIHelper.json_deserialize(
            "{\"name\":\"Shahid Khaliq\",\"age\":5147483645,\"address\":\"H # 5"
            "31, S # 20\",\"uid\":\"123321\",\"birthday\":\"1994-02-13\",\"birt"
            "htime\":\"1994-02-13T14:01:54.9571247Z\",\"salary\":20000,\"depart"
            "ment\":\"Software Development\",\"joiningDay\":\"Saturday\",\"work"
            "ingDays\":[\"Monday\",\"Tuesday\",\"Friday\"],\"boss\":{\"personTy"
            "pe\":\"Boss\",\"name\":\"Zeeshan Ejaz\",\"age\":5147483645,\"addre"
            "ss\":\"H # 531, S # 20\",\"uid\":\"123321\",\"birthday\":\"1994-02"
            "-13\",\"birthtime\":\"1994-02-13T14:01:54.9571247Z\",\"salary\":20"
            "000,\"department\":\"Software Development\",\"joiningDay\":\"Satur"
            "day\",\"workingDays\":[\"Monday\",\"Tuesday\",\"Friday\"],\"depend"
            "ents\":[{\"name\":\"Future Wife\",\"age\":5147483649,\"address\":"
            "\"H # 531, S # 20\",\"uid\":\"123412\",\"birthday\":\"1994-02-13\""
            ",\"birthtime\":\"1994-02-13T14:01:54.9571247Z\"},{\"name\":\"Futur"
            "e Kid\",\"age\":5147483648,\"address\":\"H # 531, S # 20\",\"uid\""
            ":\"312341\",\"birthday\":\"1994-02-13\",\"birthtime\":\"1994-02-13"
            "T14:01:54.9571247Z\"}],\"hiredAt\":\"Sun, 06 Nov 1994 08:49:37 GMT"
            "\",\"promotedAt\":1484719381},\"dependents\":[{\"name\":\"Future W"
            "ife\",\"age\":5147483649,\"address\":\"H # 531, S # 20\",\"uid\":"
            "\"123412\",\"birthday\":\"1994-02-13\",\"birthtime\":\"1994-02-13T"
            "14:01:54.9571247Z\"},{\"name\":\"Future Kid\",\"age\":5147483648,"
            "\"address\":\"H # 531, S # 20\",\"uid\":\"312341\",\"birthday\":\""
            "1994-02-13\",\"birthtime\":\"1994-02-13T14:01:54.9571247Z\"}],\"hi"
            "redAt\":\"Sun, 06 Nov 1994 08:49:37 GMT\"}",
            Employee.from_dictionary,
        )

        # Perform the API call through the SDK function
        result = self.controller.send_model(
            model,
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

    def test_send_model_array(self):
        """
        Api call test for `test_send_model_array`.
        """
        # Parameters for the API call
        models = APIHelper.json_deserialize(
            "[{\"name\":\"Shahid Khaliq\",\"age\":5147483645,\"address\":\"H # "
            "531, S # 20\",\"uid\":\"123321\",\"birthday\":\"1994-02-13\",\"bir"
            "thtime\":\"1994-02-13T14:01:54.9571247Z\",\"salary\":20000,\"depar"
            "tment\":\"Software Development\",\"joiningDay\":\"Saturday\",\"wor"
            "kingDays\":[\"Monday\",\"Tuesday\",\"Friday\"],\"boss\":{\"personT"
            "ype\":\"Boss\",\"name\":\"Zeeshan Ejaz\",\"age\":5147483645,\"addr"
            "ess\":\"H # 531, S # 20\",\"uid\":\"123321\",\"birthday\":\"1994-0"
            "2-13\",\"birthtime\":\"1994-02-13T14:01:54.9571247Z\",\"salary\":2"
            "0000,\"department\":\"Software Development\",\"joiningDay\":\"Satu"
            "rday\",\"workingDays\":[\"Monday\",\"Tuesday\",\"Friday\"],\"depen"
            "dents\":[{\"name\":\"Future Wife\",\"age\":5147483649,\"address\":"
            "\"H # 531, S # 20\",\"uid\":\"123412\",\"birthday\":\"1994-02-13\""
            ",\"birthtime\":\"1994-02-13T14:01:54.9571247Z\"},{\"name\":\"Futur"
            "e Kid\",\"age\":5147483648,\"address\":\"H # 531, S # 20\",\"uid\""
            ":\"312341\",\"birthday\":\"1994-02-13\",\"birthtime\":\"1994-02-13"
            "T14:01:54.9571247Z\"}],\"hiredAt\":\"Sun, 06 Nov 1994 08:49:37 GMT"
            "\",\"promotedAt\":1484719381},\"dependents\":[{\"name\":\"Future W"
            "ife\",\"age\":5147483649,\"address\":\"H # 531, S # 20\",\"uid\":"
            "\"123412\",\"birthday\":\"1994-02-13\",\"birthtime\":\"1994-02-13T"
            "14:01:54.9571247Z\"},{\"name\":\"Future Kid\",\"age\":5147483648,"
            "\"address\":\"H # 531, S # 20\",\"uid\":\"312341\",\"birthday\":\""
            "1994-02-13\",\"birthtime\":\"1994-02-13T14:01:54.9571247Z\"}],\"hi"
            "redAt\":\"Sun, 06 Nov 1994 08:49:37 GMT\"},{\"name\":\"Shahid Khal"
            "iq\",\"age\":5147483645,\"address\":\"H # 531, S # 20\",\"uid\":\""
            "123321\",\"birthday\":\"1994-02-13\",\"birthtime\":\"1994-02-13T14"
            ":01:54.9571247Z\",\"salary\":20000,\"department\":\"Software Devel"
            "opment\",\"joiningDay\":\"Saturday\",\"workingDays\":[\"Monday\","
            "\"Tuesday\",\"Friday\"],\"boss\":{\"personType\":\"Boss\",\"name\""
            ":\"Zeeshan Ejaz\",\"age\":5147483645,\"address\":\"H # 531, S # 20"
            "\",\"uid\":\"123321\",\"birthday\":\"1994-02-13\",\"birthtime\":\""
            "1994-02-13T14:01:54.9571247Z\",\"salary\":20000,\"department\":\"S"
            "oftware Development\",\"joiningDay\":\"Saturday\",\"workingDays\":"
            "[\"Monday\",\"Tuesday\",\"Friday\"],\"dependents\":[{\"name\":\"Fu"
            "ture Wife\",\"age\":5147483649,\"address\":\"H # 531, S # 20\",\"u"
            "id\":\"123412\",\"birthday\":\"1994-02-13\",\"birthtime\":\"1994-0"
            "2-13T14:01:54.9571247Z\"},{\"name\":\"Future Kid\",\"age\":5147483"
            "648,\"address\":\"H # 531, S # 20\",\"uid\":\"312341\",\"birthday"
            "\":\"1994-02-13\",\"birthtime\":\"1994-02-13T14:01:54.9571247Z\"}]"
            ",\"hiredAt\":\"Sun, 06 Nov 1994 08:49:37 GMT\",\"promotedAt\":1484"
            "719381},\"dependents\":[{\"name\":\"Future Wife\",\"age\":51474836"
            "49,\"address\":\"H # 531, S # 20\",\"uid\":\"123412\",\"birthday\""
            ":\"1994-02-13\",\"birthtime\":\"1994-02-13T14:01:54.9571247Z\"},{"
            "\"name\":\"Future Kid\",\"age\":5147483648,\"address\":\"H # 531, "
            "S # 20\",\"uid\":\"312341\",\"birthday\":\"1994-02-13\",\"birthtim"
            "e\":\"1994-02-13T14:01:54.9571247Z\"}],\"hiredAt\":\"Sun, 06 Nov 1"
            "994 08:49:37 GMT\"}]",
            Employee.from_dictionary,
        )

        # Perform the API call through the SDK function
        result = self.controller.send_model_array(
            models,
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

    def test_send_file(self):
        """
        Api call test for `test_send_file`.
        """
        # Parameters for the API call
        file = FileHelper.get_file("http://localhost:3000/response/image")

        # Perform the API call through the SDK function
        result = self.controller.send_file(
            file,
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

    def test_send_multiple_files(self):
        """
        Api call test for `test_send_multiple_files`.
        """
        # Parameters for the API call
        file = FileHelper.get_file("http://localhost:3000/response/image")
        file_1 = FileHelper.get_file("http://localhost:3000/response/image")

        # Perform the API call through the SDK function
        self.controller.send_multiple_files(
            file,
            file_1,
        )
        # Test response code
        assert self.response_catcher.response.status_code == 200

    def test_send_string(self):
        """
        Api call test for `test_send_string`.
        """
        # Parameters for the API call
        value = "TestString"

        # Perform the API call through the SDK function
        result = self.controller.send_string(
            value,
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

    def test_send_multiliner_string(self):
        """
        Api call test for `test_send_multiliner_string`.
        """
        # Parameters for the API call
        value = "TestString\nnouman"

        # Perform the API call through the SDK function
        result = self.controller.send_string(
            value,
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

    def test_send_string_with_special_characters(self):
        """
        Api call test for `test_send_string_with_special_characters`.
        """
        # Parameters for the API call
        value = "$%^!@#$%^&*"

        # Perform the API call through the SDK function
        result = self.controller.send_string(
            value,
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

    def test_send_string_with_only_space(self):
        """
        Api call test for `test_send_string_with_only_space`.
        """
        # Parameters for the API call
        value = " "

        # Perform the API call through the SDK function
        result = self.controller.send_string(
            value,
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

    def test_send_empty_string(self):
        """
        Api call test for `test_send_empty_string`.
        """
        # Parameters for the API call
        value = ""

        # Perform the API call through the SDK function
        result = self.controller.send_string(
            value,
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

    def test_send_rfc_3339_date_time_array(self):
        """
        Api call test for `test_send_rfc_3339_date_time_array`.
        """
        # Parameters for the API call
        datetimes = [
            element.datetime for element in APIHelper.json_deserialize(
                "[\"1994-02-13T14:01:54.9571247Z\",\"1994-02-13T14:01:54.9571247Z\""
            "]",
                APIHelper.RFC3339DateTime.from_value,
            )
        ]

        # Perform the API call through the SDK function
        result = self.controller.send_rfc_3339_date_time_array(
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

    def test_send_mixed_array(self):
        """
        Api call test for `test_send_mixed_array`.
        """
        # Parameters for the API call
        options = {}
        options["file"] = FileHelper.get_file("http://localhost:3000/response/image")
        options["integers"] = APIHelper.json_deserialize(
            "[1,2,3,4,5]",
        )
        options["models"] = APIHelper.json_deserialize(
            "[{\"name\":\"Shahid Khaliq\",\"age\":5147483645,\"address\":\"H # "
            "531, S # 20\",\"uid\":\"123321\",\"birthday\":\"1994-02-13\",\"bir"
            "thtime\":\"1994-02-13T14:01:54.9571247Z\",\"salary\":20000,\"depar"
            "tment\":\"Software Development\",\"joiningDay\":\"Saturday\",\"wor"
            "kingDays\":[\"Monday\",\"Tuesday\",\"Friday\"],\"boss\":{\"personT"
            "ype\":\"Boss\",\"name\":\"Zeeshan Ejaz\",\"age\":5147483645,\"addr"
            "ess\":\"H # 531, S # 20\",\"uid\":\"123321\",\"birthday\":\"1994-0"
            "2-13\",\"birthtime\":\"1994-02-13T14:01:54.9571247Z\",\"salary\":2"
            "0000,\"department\":\"Software Development\",\"joiningDay\":\"Satu"
            "rday\",\"workingDays\":[\"Monday\",\"Tuesday\",\"Friday\"],\"depen"
            "dents\":[{\"name\":\"Future Wife\",\"age\":5147483649,\"address\":"
            "\"H # 531, S # 20\",\"uid\":\"123412\",\"birthday\":\"1994-02-13\""
            ",\"birthtime\":\"1994-02-13T14:01:54.9571247Z\"},{\"name\":\"Futur"
            "e Kid\",\"age\":5147483648,\"address\":\"H # 531, S # 20\",\"uid\""
            ":\"312341\",\"birthday\":\"1994-02-13\",\"birthtime\":\"1994-02-13"
            "T14:01:54.9571247Z\"}],\"hiredAt\":\"Sun, 06 Nov 1994 08:49:37 GMT"
            "\",\"promotedAt\":1484719381},\"dependents\":[{\"name\":\"Future W"
            "ife\",\"age\":5147483649,\"address\":\"H # 531, S # 20\",\"uid\":"
            "\"123412\",\"birthday\":\"1994-02-13\",\"birthtime\":\"1994-02-13T"
            "14:01:54.9571247Z\"},{\"name\":\"Future Kid\",\"age\":5147483648,"
            "\"address\":\"H # 531, S # 20\",\"uid\":\"312341\",\"birthday\":\""
            "1994-02-13\",\"birthtime\":\"1994-02-13T14:01:54.9571247Z\"}],\"hi"
            "redAt\":\"Sun, 06 Nov 1994 08:49:37 GMT\"},{\"name\":\"Shahid Khal"
            "iq\",\"age\":5147483645,\"address\":\"H # 531, S # 20\",\"uid\":\""
            "123321\",\"birthday\":\"1994-02-13\",\"birthtime\":\"1994-02-13T14"
            ":01:54.9571247Z\",\"salary\":20000,\"department\":\"Software Devel"
            "opment\",\"joiningDay\":\"Saturday\",\"workingDays\":[\"Monday\","
            "\"Tuesday\",\"Friday\"],\"boss\":{\"personType\":\"Boss\",\"name\""
            ":\"Zeeshan Ejaz\",\"age\":5147483645,\"address\":\"H # 531, S # 20"
            "\",\"uid\":\"123321\",\"birthday\":\"1994-02-13\",\"birthtime\":\""
            "1994-02-13T14:01:54.9571247Z\",\"salary\":20000,\"department\":\"S"
            "oftware Development\",\"joiningDay\":\"Saturday\",\"workingDays\":"
            "[\"Monday\",\"Tuesday\",\"Friday\"],\"dependents\":[{\"name\":\"Fu"
            "ture Wife\",\"age\":5147483649,\"address\":\"H # 531, S # 20\",\"u"
            "id\":\"123412\",\"birthday\":\"1994-02-13\",\"birthtime\":\"1994-0"
            "2-13T14:01:54.9571247Z\"},{\"name\":\"Future Kid\",\"age\":5147483"
            "648,\"address\":\"H # 531, S # 20\",\"uid\":\"312341\",\"birthday"
            "\":\"1994-02-13\",\"birthtime\":\"1994-02-13T14:01:54.9571247Z\"}]"
            ",\"hiredAt\":\"Sun, 06 Nov 1994 08:49:37 GMT\",\"promotedAt\":1484"
            "719381},\"dependents\":[{\"name\":\"Future Wife\",\"age\":51474836"
            "49,\"address\":\"H # 531, S # 20\",\"uid\":\"123412\",\"birthday\""
            ":\"1994-02-13\",\"birthtime\":\"1994-02-13T14:01:54.9571247Z\"},{"
            "\"name\":\"Future Kid\",\"age\":5147483648,\"address\":\"H # 531, "
            "S # 20\",\"uid\":\"312341\",\"birthday\":\"1994-02-13\",\"birthtim"
            "e\":\"1994-02-13T14:01:54.9571247Z\"}],\"hiredAt\":\"Sun, 06 Nov 1"
            "994 08:49:37 GMT\"}]",
            Employee.from_dictionary,
        )
        options["strings"] = APIHelper.json_deserialize(
            "[\"abc\",\"def\"]",
        )

        # Perform the API call through the SDK function
        result = self.controller.send_mixed_array(
            options,
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

    def test_update_model_with_form(self):
        """
        Api call test for `test_update_model_with_form`.
        """
        # Parameters for the API call
        model = APIHelper.json_deserialize(
            "{\"name\":\"Shahid Khaliq\",\"age\":5147483645,\"address\":\"H # 5"
            "31, S # 20\",\"uid\":\"123321\",\"birthday\":\"1994-02-13\",\"birt"
            "htime\":\"1994-02-13T14:01:54.9571247Z\",\"salary\":20000,\"depart"
            "ment\":\"Software Development\",\"joiningDay\":\"Saturday\",\"work"
            "ingDays\":[\"Monday\",\"Tuesday\",\"Friday\"],\"boss\":{\"personTy"
            "pe\":\"Boss\",\"name\":\"Zeeshan Ejaz\",\"age\":5147483645,\"addre"
            "ss\":\"H # 531, S # 20\",\"uid\":\"123321\",\"birthday\":\"1994-02"
            "-13\",\"birthtime\":\"1994-02-13T14:01:54.9571247Z\",\"salary\":20"
            "000,\"department\":\"Software Development\",\"joiningDay\":\"Satur"
            "day\",\"workingDays\":[\"Monday\",\"Tuesday\",\"Friday\"],\"depend"
            "ents\":[{\"name\":\"Future Wife\",\"age\":5147483649,\"address\":"
            "\"H # 531, S # 20\",\"uid\":\"123412\",\"birthday\":\"1994-02-13\""
            ",\"birthtime\":\"1994-02-13T14:01:54.9571247Z\"},{\"name\":\"Futur"
            "e Kid\",\"age\":5147483648,\"address\":\"H # 531, S # 20\",\"uid\""
            ":\"312341\",\"birthday\":\"1994-02-13\",\"birthtime\":\"1994-02-13"
            "T14:01:54.9571247Z\"}],\"hiredAt\":\"Sun, 06 Nov 1994 08:49:37 GMT"
            "\",\"promotedAt\":1484719381},\"dependents\":[{\"name\":\"Future W"
            "ife\",\"age\":5147483649,\"address\":\"H # 531, S # 20\",\"uid\":"
            "\"123412\",\"birthday\":\"1994-02-13\",\"birthtime\":\"1994-02-13T"
            "14:01:54.9571247Z\"},{\"name\":\"Future Kid\",\"age\":5147483648,"
            "\"address\":\"H # 531, S # 20\",\"uid\":\"312341\",\"birthday\":\""
            "1994-02-13\",\"birthtime\":\"1994-02-13T14:01:54.9571247Z\"}],\"hi"
            "redAt\":\"Sun, 06 Nov 1994 08:49:37 GMT\"}",
            Employee.from_dictionary,
        )

        # Perform the API call through the SDK function
        result = self.controller.update_model_with_form(
            model,
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

    def test_delete_form_test_with_model(self):
        """
        Api call test for `test_delete_form_test_with_model`.
        """
        # Parameters for the API call
        model = APIHelper.json_deserialize(
            "{\"name\":\"Shahid Khaliq\",\"age\":5147483645,\"address\":\"H # 5"
            "31, S # 20\",\"uid\":\"123321\",\"birthday\":\"1994-02-13\",\"birt"
            "htime\":\"1994-02-13T14:01:54.9571247Z\",\"salary\":20000,\"depart"
            "ment\":\"Software Development\",\"joiningDay\":\"Saturday\",\"work"
            "ingDays\":[\"Monday\",\"Tuesday\",\"Friday\"],\"boss\":{\"personTy"
            "pe\":\"Boss\",\"name\":\"Zeeshan Ejaz\",\"age\":5147483645,\"addre"
            "ss\":\"H # 531, S # 20\",\"uid\":\"123321\",\"birthday\":\"1994-02"
            "-13\",\"birthtime\":\"1994-02-13T14:01:54.9571247Z\",\"salary\":20"
            "000,\"department\":\"Software Development\",\"joiningDay\":\"Satur"
            "day\",\"workingDays\":[\"Monday\",\"Tuesday\",\"Friday\"],\"depend"
            "ents\":[{\"name\":\"Future Wife\",\"age\":5147483649,\"address\":"
            "\"H # 531, S # 20\",\"uid\":\"123412\",\"birthday\":\"1994-02-13\""
            ",\"birthtime\":\"1994-02-13T14:01:54.9571247Z\"},{\"name\":\"Futur"
            "e Kid\",\"age\":5147483648,\"address\":\"H # 531, S # 20\",\"uid\""
            ":\"312341\",\"birthday\":\"1994-02-13\",\"birthtime\":\"1994-02-13"
            "T14:01:54.9571247Z\"}],\"hiredAt\":\"Sun, 06 Nov 1994 08:49:37 GMT"
            "\",\"promotedAt\":1484719381},\"dependents\":[{\"name\":\"Future W"
            "ife\",\"age\":5147483649,\"address\":\"H # 531, S # 20\",\"uid\":"
            "\"123412\",\"birthday\":\"1994-02-13\",\"birthtime\":\"1994-02-13T"
            "14:01:54.9571247Z\"},{\"name\":\"Future Kid\",\"age\":5147483648,"
            "\"address\":\"H # 531, S # 20\",\"uid\":\"312341\",\"birthday\":\""
            "1994-02-13\",\"birthtime\":\"1994-02-13T14:01:54.9571247Z\"}],\"hi"
            "redAt\":\"Sun, 06 Nov 1994 08:49:37 GMT\"}",
            Employee.from_dictionary,
        )

        # Perform the API call through the SDK function
        result = self.controller.send_delete_form_1(
            model,
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

    def test_send_delete_form_with_model_array(self):
        """
        Api call test for `test_send_delete_form_with_model_array`.
        """
        # Parameters for the API call
        models = APIHelper.json_deserialize(
            "[{\"name\":\"Shahid Khaliq\",\"age\":5147483645,\"address\":\"H # "
            "531, S # 20\",\"uid\":\"123321\",\"birthday\":\"1994-02-13\",\"bir"
            "thtime\":\"1994-02-13T14:01:54.9571247Z\",\"salary\":20000,\"depar"
            "tment\":\"Software Development\",\"joiningDay\":\"Saturday\",\"wor"
            "kingDays\":[\"Monday\",\"Tuesday\",\"Friday\"],\"boss\":{\"personT"
            "ype\":\"Boss\",\"name\":\"Zeeshan Ejaz\",\"age\":5147483645,\"addr"
            "ess\":\"H # 531, S # 20\",\"uid\":\"123321\",\"birthday\":\"1994-0"
            "2-13\",\"birthtime\":\"1994-02-13T14:01:54.9571247Z\",\"salary\":2"
            "0000,\"department\":\"Software Development\",\"joiningDay\":\"Satu"
            "rday\",\"workingDays\":[\"Monday\",\"Tuesday\",\"Friday\"],\"depen"
            "dents\":[{\"name\":\"Future Wife\",\"age\":5147483649,\"address\":"
            "\"H # 531, S # 20\",\"uid\":\"123412\",\"birthday\":\"1994-02-13\""
            ",\"birthtime\":\"1994-02-13T14:01:54.9571247Z\"},{\"name\":\"Futur"
            "e Kid\",\"age\":5147483648,\"address\":\"H # 531, S # 20\",\"uid\""
            ":\"312341\",\"birthday\":\"1994-02-13\",\"birthtime\":\"1994-02-13"
            "T14:01:54.9571247Z\"}],\"hiredAt\":\"Sun, 06 Nov 1994 08:49:37 GMT"
            "\",\"promotedAt\":1484719381},\"dependents\":[{\"name\":\"Future W"
            "ife\",\"age\":5147483649,\"address\":\"H # 531, S # 20\",\"uid\":"
            "\"123412\",\"birthday\":\"1994-02-13\",\"birthtime\":\"1994-02-13T"
            "14:01:54.9571247Z\"},{\"name\":\"Future Kid\",\"age\":5147483648,"
            "\"address\":\"H # 531, S # 20\",\"uid\":\"312341\",\"birthday\":\""
            "1994-02-13\",\"birthtime\":\"1994-02-13T14:01:54.9571247Z\"}],\"hi"
            "redAt\":\"Sun, 06 Nov 1994 08:49:37 GMT\"},{\"name\":\"Shahid Khal"
            "iq\",\"age\":5147483645,\"address\":\"H # 531, S # 20\",\"uid\":\""
            "123321\",\"birthday\":\"1994-02-13\",\"birthtime\":\"1994-02-13T14"
            ":01:54.9571247Z\",\"salary\":20000,\"department\":\"Software Devel"
            "opment\",\"joiningDay\":\"Saturday\",\"workingDays\":[\"Monday\","
            "\"Tuesday\",\"Friday\"],\"boss\":{\"personType\":\"Boss\",\"name\""
            ":\"Zeeshan Ejaz\",\"age\":5147483645,\"address\":\"H # 531, S # 20"
            "\",\"uid\":\"123321\",\"birthday\":\"1994-02-13\",\"birthtime\":\""
            "1994-02-13T14:01:54.9571247Z\",\"salary\":20000,\"department\":\"S"
            "oftware Development\",\"joiningDay\":\"Saturday\",\"workingDays\":"
            "[\"Monday\",\"Tuesday\",\"Friday\"],\"dependents\":[{\"name\":\"Fu"
            "ture Wife\",\"age\":5147483649,\"address\":\"H # 531, S # 20\",\"u"
            "id\":\"123412\",\"birthday\":\"1994-02-13\",\"birthtime\":\"1994-0"
            "2-13T14:01:54.9571247Z\"},{\"name\":\"Future Kid\",\"age\":5147483"
            "648,\"address\":\"H # 531, S # 20\",\"uid\":\"312341\",\"birthday"
            "\":\"1994-02-13\",\"birthtime\":\"1994-02-13T14:01:54.9571247Z\"}]"
            ",\"hiredAt\":\"Sun, 06 Nov 1994 08:49:37 GMT\",\"promotedAt\":1484"
            "719381},\"dependents\":[{\"name\":\"Future Wife\",\"age\":51474836"
            "49,\"address\":\"H # 531, S # 20\",\"uid\":\"123412\",\"birthday\""
            ":\"1994-02-13\",\"birthtime\":\"1994-02-13T14:01:54.9571247Z\"},{"
            "\"name\":\"Future Kid\",\"age\":5147483648,\"address\":\"H # 531, "
            "S # 20\",\"uid\":\"312341\",\"birthday\":\"1994-02-13\",\"birthtim"
            "e\":\"1994-02-13T14:01:54.9571247Z\"}],\"hiredAt\":\"Sun, 06 Nov 1"
            "994 08:49:37 GMT\"}]",
            Employee.from_dictionary,
        )

        # Perform the API call through the SDK function
        result = self.controller.send_delete_form_with_model_array(
            models,
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

    def test_update_model_array_with_form(self):
        """
        Api call test for `test_update_model_array_with_form`.
        """
        # Parameters for the API call
        models = APIHelper.json_deserialize(
            "[{\"name\":\"Shahid Khaliq\",\"age\":5147483645,\"address\":\"H # "
            "531, S # 20\",\"uid\":\"123321\",\"birthday\":\"1994-02-13\",\"bir"
            "thtime\":\"1994-02-13T14:01:54.9571247Z\",\"salary\":20000,\"depar"
            "tment\":\"Software Development\",\"joiningDay\":\"Saturday\",\"wor"
            "kingDays\":[\"Monday\",\"Tuesday\",\"Friday\"],\"boss\":{\"personT"
            "ype\":\"Boss\",\"name\":\"Zeeshan Ejaz\",\"age\":5147483645,\"addr"
            "ess\":\"H # 531, S # 20\",\"uid\":\"123321\",\"birthday\":\"1994-0"
            "2-13\",\"birthtime\":\"1994-02-13T14:01:54.9571247Z\",\"salary\":2"
            "0000,\"department\":\"Software Development\",\"joiningDay\":\"Satu"
            "rday\",\"workingDays\":[\"Monday\",\"Tuesday\",\"Friday\"],\"depen"
            "dents\":[{\"name\":\"Future Wife\",\"age\":5147483649,\"address\":"
            "\"H # 531, S # 20\",\"uid\":\"123412\",\"birthday\":\"1994-02-13\""
            ",\"birthtime\":\"1994-02-13T14:01:54.9571247Z\"},{\"name\":\"Futur"
            "e Kid\",\"age\":5147483648,\"address\":\"H # 531, S # 20\",\"uid\""
            ":\"312341\",\"birthday\":\"1994-02-13\",\"birthtime\":\"1994-02-13"
            "T14:01:54.9571247Z\"}],\"hiredAt\":\"Sun, 06 Nov 1994 08:49:37 GMT"
            "\",\"promotedAt\":1484719381},\"dependents\":[{\"name\":\"Future W"
            "ife\",\"age\":5147483649,\"address\":\"H # 531, S # 20\",\"uid\":"
            "\"123412\",\"birthday\":\"1994-02-13\",\"birthtime\":\"1994-02-13T"
            "14:01:54.9571247Z\"},{\"name\":\"Future Kid\",\"age\":5147483648,"
            "\"address\":\"H # 531, S # 20\",\"uid\":\"312341\",\"birthday\":\""
            "1994-02-13\",\"birthtime\":\"1994-02-13T14:01:54.9571247Z\"}],\"hi"
            "redAt\":\"Sun, 06 Nov 1994 08:49:37 GMT\"},{\"name\":\"Shahid Khal"
            "iq\",\"age\":5147483645,\"address\":\"H # 531, S # 20\",\"uid\":\""
            "123321\",\"birthday\":\"1994-02-13\",\"birthtime\":\"1994-02-13T14"
            ":01:54.9571247Z\",\"salary\":20000,\"department\":\"Software Devel"
            "opment\",\"joiningDay\":\"Saturday\",\"workingDays\":[\"Monday\","
            "\"Tuesday\",\"Friday\"],\"boss\":{\"personType\":\"Boss\",\"name\""
            ":\"Zeeshan Ejaz\",\"age\":5147483645,\"address\":\"H # 531, S # 20"
            "\",\"uid\":\"123321\",\"birthday\":\"1994-02-13\",\"birthtime\":\""
            "1994-02-13T14:01:54.9571247Z\",\"salary\":20000,\"department\":\"S"
            "oftware Development\",\"joiningDay\":\"Saturday\",\"workingDays\":"
            "[\"Monday\",\"Tuesday\",\"Friday\"],\"dependents\":[{\"name\":\"Fu"
            "ture Wife\",\"age\":5147483649,\"address\":\"H # 531, S # 20\",\"u"
            "id\":\"123412\",\"birthday\":\"1994-02-13\",\"birthtime\":\"1994-0"
            "2-13T14:01:54.9571247Z\"},{\"name\":\"Future Kid\",\"age\":5147483"
            "648,\"address\":\"H # 531, S # 20\",\"uid\":\"312341\",\"birthday"
            "\":\"1994-02-13\",\"birthtime\":\"1994-02-13T14:01:54.9571247Z\"}]"
            ",\"hiredAt\":\"Sun, 06 Nov 1994 08:49:37 GMT\",\"promotedAt\":1484"
            "719381},\"dependents\":[{\"name\":\"Future Wife\",\"age\":51474836"
            "49,\"address\":\"H # 531, S # 20\",\"uid\":\"123412\",\"birthday\""
            ":\"1994-02-13\",\"birthtime\":\"1994-02-13T14:01:54.9571247Z\"},{"
            "\"name\":\"Future Kid\",\"age\":5147483648,\"address\":\"H # 531, "
            "S # 20\",\"uid\":\"312341\",\"birthday\":\"1994-02-13\",\"birthtim"
            "e\":\"1994-02-13T14:01:54.9571247Z\"}],\"hiredAt\":\"Sun, 06 Nov 1"
            "994 08:49:37 GMT\"}]",
            Employee.from_dictionary,
        )

        # Perform the API call through the SDK function
        result = self.controller.update_model_array_with_form(
            models,
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

    def test_update_string_with_form(self):
        """
        Api call test for `test_update_string_with_form`.
        """
        # Parameters for the API call
        value = "TestString"

        # Perform the API call through the SDK function
        result = self.controller.update_string_with_form(
            value,
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

    def test_update_special_string_with_form(self):
        """
        Api call test for `test_update_special_string_with_form`.
        """
        # Parameters for the API call
        value = "$%^!@#$%^&*"

        # Perform the API call through the SDK function
        result = self.controller.update_string_with_form(
            value,
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

    def test_update_multiliner_string_with_form(self):
        """
        Api call test for `test_update_multiliner_string_with_form`.
        """
        # Parameters for the API call
        value = "TestString\nnouman"

        # Perform the API call through the SDK function
        result = self.controller.update_string_with_form(
            value,
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

    def test_update_string_with_form_corner_case(self):
        """
        Api call test for `test_update_string_with_form_corner_case`.
        """
        # Parameters for the API call
        value = " "

        # Perform the API call through the SDK function
        result = self.controller.update_string_with_form(
            value,
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

    def test_update_empty_string_with_form(self):
        """
        Api call test for `test_update_empty_string_with_form`.
        """
        # Parameters for the API call
        value = ""

        # Perform the API call through the SDK function
        result = self.controller.update_string_with_form(
            value,
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

    def test_update_string_array_with_form(self):
        """
        Api call test for `test_update_string_array_with_form`.
        """
        # Parameters for the API call
        strings = APIHelper.json_deserialize(
            "[\"abc\",\"def\"]",
        )

        # Perform the API call through the SDK function
        result = self.controller.update_string_array_with_form(
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

    def test_send_integer_enum_array(self):
        """
        Api call test for `test_send_integer_enum_array`.
        """
        # Parameters for the API call
        suites = APIHelper.json_deserialize(
            "[1,3,4,2,3]",
        )

        # Perform the API call through the SDK function
        result = self.controller.send_integer_enum_array(
            suites,
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

    def test_send_string_enum_array(self):
        """
        Api call test for `test_send_string_enum_array`.
        """
        # Parameters for the API call
        days = APIHelper.json_deserialize(
            "[\"Tuesday\",\"Saturday\",\"Wednesday\",\"Monday\",\"Sunday\"]",
        )

        # Perform the API call through the SDK function
        result = self.controller.send_string_enum_array(
            days,
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

    def test_send_string_in_form_with_new_line_1(self):
        """
        Api call test for `test_send_string_in_form_with_new_line_1`.
        """
        # Parameters for the API call
        body = APIHelper.json_deserialize(
            "{\"name\":\"farhan\",\"field\":\"QA\"}",
            TestNstringEncoding.from_dictionary,
        )

        # Perform the API call through the SDK function
        result = self.controller.send_string_in_form_with_new_line(
            body,
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

    def test_send_string_in_form_with_new_line_2(self):
        """
        Api call test for `test_send_string_in_form_with_new_line_2`.
        """
        # Parameters for the API call
        body = APIHelper.json_deserialize(
            "{\"name\":\"farhan\",\"field\":\"QA&Dev\"}",
            TestNstringEncoding.from_dictionary,
        )

        # Perform the API call through the SDK function
        result = self.controller.send_string_in_form_with_new_line(
            body,
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

    def test_send_string_in_form_with_new_line_3(self):
        """
        Api call test for `test_send_string_in_form_with_new_line_3`.
        """
        # Parameters for the API call
        body = APIHelper.json_deserialize(
            "{\"name\":\"farhan&nouman\",\"field\":\"QA\"}",
            TestNstringEncoding.from_dictionary,
        )

        # Perform the API call through the SDK function
        result = self.controller.send_string_in_form_with_new_line(
            body,
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

    def test_send_string_in_form_with_r_1(self):
        """
        Api call test for `test_send_string_in_form_with_r_1`.
        """
        # Parameters for the API call
        body = APIHelper.json_deserialize(
            "{\"name\":\"farhan\",\"field\":\"QA\"}",
            TestRstringEncoding.from_dictionary,
        )

        # Perform the API call through the SDK function
        result = self.controller.send_string_in_form_with_r(
            body,
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

    def test_send_string_in_form_with_r_2(self):
        """
        Api call test for `test_send_string_in_form_with_r_2`.
        """
        # Parameters for the API call
        body = APIHelper.json_deserialize(
            "{\"name\":\"farhan\",\"field\":\"QA&Dev\"}",
            TestRstringEncoding.from_dictionary,
        )

        # Perform the API call through the SDK function
        result = self.controller.send_string_in_form_with_r(
            body,
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

    def test_send_string_in_form_with_r_3(self):
        """
        Api call test for `test_send_string_in_form_with_r_3`.
        """
        # Parameters for the API call
        body = APIHelper.json_deserialize(
            "{\"name\":\"farhan&nouman\",\"field\":\"QA\"}",
            TestRstringEncoding.from_dictionary,
        )

        # Perform the API call through the SDK function
        result = self.controller.send_string_in_form_with_r(
            body,
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

    def test_send_string_in_form_with_r_n_1(self):
        """
        Api call test for `test_send_string_in_form_with_r_n_1`.
        """
        # Parameters for the API call
        body = APIHelper.json_deserialize(
            "{\"name\":\"farhan\",\"field\":\"QA\"}",
            TestRNstringEncoding.from_dictionary,
        )

        # Perform the API call through the SDK function
        result = self.controller.send_string_in_form_with_r_n(
            body,
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

    def test_send_string_in_form_with_r_n_2(self):
        """
        Api call test for `test_send_string_in_form_with_r_n_2`.
        """
        # Parameters for the API call
        body = APIHelper.json_deserialize(
            "{\"name\":\"farhan\",\"field\":\"QA&Dev\"}",
            TestRNstringEncoding.from_dictionary,
        )

        # Perform the API call through the SDK function
        result = self.controller.send_string_in_form_with_r_n(
            body,
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

    def test_send_string_in_form_with_r_n_3(self):
        """
        Api call test for `test_send_string_in_form_with_r_n_3`.
        """
        # Parameters for the API call
        body = APIHelper.json_deserialize(
            "{\"name\":\"farhan&nouman\",\"field\":\"QA\"}",
            TestRNstringEncoding.from_dictionary,
        )

        # Perform the API call through the SDK function
        result = self.controller.send_string_in_form_with_r_n(
            body,
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

    def test_empty_optionals(self):
        """
        Api call test for `test_empty_optionals`.
        """
        # Parameters for the API call
        model = APIHelper.json_deserialize(
            "{}",
            AllOptionals.from_dictionary,
        )
        option = None

        # Perform the API call through the SDK function
        result = self.controller.all_optionals(
            model,
            option,
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

    def test_set_optionals_with_empty_body(self):
        """
        Api call test for `test_set_optionals_with_empty_body`.
        """
        # Parameters for the API call
        model = APIHelper.json_deserialize(
            "{\"optionalNumbers\":[{},{}],\"optionalLong\":{},\"optionalPrecisi"
            "on\":{},\"string\":\"parent optional string\"}",
            AllOptionals.from_dictionary,
        )
        option = "withEmptyFields"

        # Perform the API call through the SDK function
        result = self.controller.all_optionals(
            model,
            option,
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

    def test_set_optionals_with_set_body(self):
        """
        Api call test for `test_set_optionals_with_set_body`.
        """
        # Parameters for the API call
        model = APIHelper.json_deserialize(
            "{\"id\":14,\"optionalNumbers\":[{\"number\":23},{\"number\":45}],"
            "\"optionalLong\":{\"long\":67899658},\"optionalPrecision\":{\"prec"
            "ision\":45.45},\"string\":\"parent optional string\"}",
            AllOptionals.from_dictionary,
        )
        option = "withFields"

        # Perform the API call through the SDK function
        result = self.controller.all_optionals(
            model,
            option,
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

    def test_send_optional_unix_time_stamp_in_body(self):
        """
        Api call test for `test_send_optional_unix_time_stamp_in_body`.
        """
        # Parameters for the API call
        date_time = APIHelper.UnixDateTime.from_value(
            1484719381,
        ).datetime

        # Perform the API call through the SDK function
        result = self.controller.send_optional_unix_date_time_in_body(
            date_time,
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

    def test_send_optional_rfc_1123_in_body(self):
        """
        Api call test for `test_send_optional_rfc_1123_in_body`.
        """
        # Parameters for the API call
        body = APIHelper.HttpDateTime.from_value(
            "Sun, 06 Nov 1994 08:49:37 GMT",
        ).datetime

        # Perform the API call through the SDK function
        result = self.controller.send_optional_rfc_1123_in_body(
            body,
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

    def test_sending_datetime_as_optional_in_plain_text_body(self):
        """
        Api call test for `test_sending_datetime_as_optional_in_plain_text_body`.
        """
        # Parameters for the API call
        body = APIHelper.RFC3339DateTime.from_value(
            "1994-02-13T14:01:54.9571247Z",
        ).datetime

        # Perform the API call through the SDK function
        result = self.controller.send_datetime_optional_in_endpoint(
            body,
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

    def test_send_optional_unix_time_stamp_in_model_body(self):
        """
        Api call test for `test_send_optional_unix_time_stamp_in_model_body`.
        """
        # Parameters for the API call
        date_time = APIHelper.json_deserialize(
            "{\"dateTime\":1484719381}",
            UnixDateTime.from_dictionary,
        )

        # Perform the API call through the SDK function
        result = self.controller.send_optional_unix_time_stamp_in_model_body(
            date_time,
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

    def test_send_optional_unix_time_stamp_in_nested_model_body(self):
        """
        Api call test for `test_send_optional_unix_time_stamp_in_nested_model_body`.
        """
        # Parameters for the API call
        date_time = APIHelper.json_deserialize(
            "{\"dateTime\":{\"dateTime\":1484719381}}",
            SendUnixDateTime.from_dictionary,
        )

        # Perform the API call through the SDK function
        result = self.controller.send_optional_unix_time_stamp_in_nested_model_body(
            date_time,
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

    def test_sending_rfc_1123_date_time_in_nested_mode(self):
        """
        Api call test for `test_sending_rfc_1123_date_time_in_nested_mode`.
        """
        # Parameters for the API call
        body = APIHelper.json_deserialize(
            "{\"dateTime\":{\"dateTime\":\"Sun, 06 Nov 1994 08:49:37 GMT\"}}",
            SendRfc1123DateTime.from_dictionary,
        )

        # Perform the API call through the SDK function
        result = self.controller.send_rfc_1123_date_time_in_nested_model(
            body,
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

    def test_send_optional_rfc_1123_date_time_in_model_body(self):
        """
        Api call test for `test_send_optional_rfc_1123_date_time_in_model_body`.
        """
        # Parameters for the API call
        date_time = APIHelper.json_deserialize(
            "{\"dateTime\":\"Sun, 06 Nov 1994 08:49:37 GMT\"}",
            ModelWithOptionalRfc1123DateTime.from_dictionary,
        )

        # Perform the API call through the SDK function
        result = self.controller.send_rfc_1123_date_time_in_model(
            date_time,
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

    def test_send_optional_datetime_in_model_as_body(self):
        """
        Api call test for `test_send_optional_datetime_in_model_as_body`.
        """
        # Parameters for the API call
        body = APIHelper.json_deserialize(
            "{\"dateTime\":\"1994-02-13T14:01:54.9571247Z\"}",
            ModelWithOptionalRfc3339DateTime.from_dictionary,
        )

        # Perform the API call through the SDK function
        result = self.controller.send_optional_datetime_in_model(
            body,
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

    def test_send_rfc_3339_date_time_in_nested_model(self):
        """
        Api call test for `test_send_rfc_3339_date_time_in_nested_model`.
        """
        # Parameters for the API call
        body = APIHelper.json_deserialize(
            "{\"dateTime\":{\"dateTime\":\"1994-02-13T14:01:54.9571247Z\"}}",
            SendRfc339DateTime.from_dictionary,
        )

        # Perform the API call through the SDK function
        result = self.controller.send_rfc_339_date_time_in_nested_models(
            body,
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

    def test_uuid_as_optional(self):
        """
        Api call test for `test_uuid_as_optional`.
        """
        # Parameters for the API call
        body = APIHelper.json_deserialize(
            "{\"uuid\":\"123e4567-e89b-12d3-a456-426655440000\"}",
            UuidAsOptional.from_dictionary,
        )

        # Perform the API call through the SDK function
        result = self.controller.uuid_as_optional(
            body,
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

    def test_boolean_as_optional(self):
        """
        Api call test for `test_boolean_as_optional`.
        """
        # Parameters for the API call
        body = APIHelper.json_deserialize(
            "{\"boolean\":true}",
            BooleanAsOptional.from_dictionary,
        )

        # Perform the API call through the SDK function
        result = self.controller.boolean_as_optional(
            body,
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

    def test_date_as_optional(self):
        """
        Api call test for `test_date_as_optional`.
        """
        # Parameters for the API call
        body = APIHelper.json_deserialize(
            "{\"date\":\"1994-02-13\"}",
            DateAsOptional.from_dictionary,
        )

        # Perform the API call through the SDK function
        result = self.controller.date_as_optional(
            body,
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

    def test_dynamic_as_optional(self):
        """
        Api call test for `test_dynamic_as_optional`.
        """
        # Parameters for the API call
        body = APIHelper.json_deserialize(
            "{\"dynamic\":{\"dynamic\":\"test\"}}",
            DynamicAsOptional.from_dictionary,
        )

        # Perform the API call through the SDK function
        result = self.controller.dynamic_as_optional(
            body,
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

    def test_string_as_optional(self):
        """
        Api call test for `test_string_as_optional`.
        """
        # Parameters for the API call
        body = APIHelper.json_deserialize(
            "{\"string\":\"test\"}",
            StringAsOptional.from_dictionary,
        )

        # Perform the API call through the SDK function
        result = self.controller.string_as_optional(
            body,
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

    def test_precision_as_optional(self):
        """
        Api call test for `test_precision_as_optional`.
        """
        # Parameters for the API call
        body = APIHelper.json_deserialize(
            "{\"precision\":1.23}",
            PrecisionAsOptional.from_dictionary,
        )

        # Perform the API call through the SDK function
        result = self.controller.precision_as_optional(
            body,
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

    def test_long_as_optional(self):
        """
        Api call test for `test_long_as_optional`.
        """
        # Parameters for the API call
        body = APIHelper.json_deserialize(
            "{\"long\":123123}",
            LongAsOptional.from_dictionary,
        )

        # Perform the API call through the SDK function
        result = self.controller.long_as_optional(
            body,
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

    def test_number_as_optional(self):
        """
        Api call test for `test_number_as_optional`.
        """
        # Parameters for the API call
        body = APIHelper.json_deserialize(
            "{\"number\":1}",
            NumberAsOptional.from_dictionary,
        )

        # Perform the API call through the SDK function
        result = self.controller.send_number_as_optional(
            body,
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

