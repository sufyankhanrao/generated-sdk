
"""
testerfilesandmultipart

This file was automatically generated for Stamplay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: PLR0915, W291
from apimatic_core.utilities.comparison_helper import (
    ComparisonHelper,
)
from apimatic_core.utilities.file_helper import (
    FileHelper,
)

from testerfilesandmultipart.api_helper import (
    APIHelper,
)
from testerfilesandmultipart.models.person import (
    Employee,
)
from tests.controllers.controller_test_base import (
    ControllerTestBase,
)


class MultipartParamsControllerTests(ControllerTestBase):
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
        cls.controller = cls.client.multipart_params
        cls.response_catcher = cls.controller.http_call_back

    def test_send_mixed_array(self):
        """
        Api call test for `test_send_mixed_array`.
        """
        # Parameters for the API call
        options = {}
        options["file"] = FileHelper.get_file("http://localhost:3000/response/image")
        options["integers"] = 1
        options["models"] = APIHelper.json_deserialize(
            "[{\"name\":\"Shahid Khaliq\",\"age\":5147483645,\"address\":\"H # 531, S"
            " # 20\",\"uid\":\"123321\",\"birthday\":\"1994-02-13\",\"birthtime\":\"1"
            "994-02-13T14:01:54.9571247Z\",\"salary\":20000,\"department\":\"Software"
            " Development\",\"joiningDay\":\"Saturday\",\"workingDays\":[\"Monday\","
            "\"Tuesday\",\"Friday\"],\"boss\":{\"personType\":\"Boss\",\"name\":\"Zee"
            "shan Ejaz\",\"age\":5147483645,\"address\":\"H # 531, S # 20\",\"uid\":"
            "\"123321\",\"birthday\":\"1994-02-13\",\"birthtime\":\"1994-02-13T14:01:"
            "54.9571247Z\",\"salary\":20000,\"department\":\"Software Development\","
            "\"joiningDay\":\"Saturday\",\"workingDays\":[\"Monday\",\"Tuesday\",\"Fr"
            "iday\"],\"dependents\":[{\"name\":\"Future Wife\",\"age\":5147483649,\"a"
            "ddress\":\"H # 531, S # 20\",\"uid\":\"123412\",\"birthday\":\"1994-02-1"
            "3\",\"birthtime\":\"1994-02-13T14:01:54.9571247Z\"},{\"name\":\"Future K"
            "id\",\"age\":5147483648,\"address\":\"H # 531, S # 20\",\"uid\":\"312341"
            "\",\"birthday\":\"1994-02-13\",\"birthtime\":\"1994-02-13T14:01:54.95712"
            "47Z\"}],\"hiredAt\":\"Sun, 06 Nov 1994 08:49:37 GMT\",\"promotedAt\":148"
            "4719381},\"dependents\":[{\"name\":\"Future Wife\",\"age\":5147483649,\""
            "address\":\"H # 531, S # 20\",\"uid\":\"123412\",\"birthday\":\"1994-02-"
            "13\",\"birthtime\":\"1994-02-13T14:01:54.9571247Z\"},{\"name\":\"Future "
            "Kid\",\"age\":5147483648,\"address\":\"H # 531, S # 20\",\"uid\":\"31234"
            "1\",\"birthday\":\"1994-02-13\",\"birthtime\":\"1994-02-13T14:01:54.9571"
            "247Z\"}],\"hiredAt\":\"Sun, 06 Nov 1994 08:49:37 GMT\"},{\"name\":\"Shah"
            "id Khaliq\",\"age\":5147483645,\"address\":\"H # 531, S # 20\",\"uid\":"
            "\"123321\",\"birthday\":\"1994-02-13\",\"birthtime\":\"1994-02-13T14:01:"
            "54.9571247Z\",\"salary\":20000,\"department\":\"Software Development\","
            "\"joiningDay\":\"Saturday\",\"workingDays\":[\"Monday\",\"Tuesday\",\"Fr"
            "iday\"],\"boss\":{\"personType\":\"Boss\",\"name\":\"Zeeshan Ejaz\",\"ag"
            "e\":5147483645,\"address\":\"H # 531, S # 20\",\"uid\":\"123321\",\"birt"
            "hday\":\"1994-02-13\",\"birthtime\":\"1994-02-13T14:01:54.9571247Z\",\"s"
            "alary\":20000,\"department\":\"Software Development\",\"joiningDay\":\"S"
            "aturday\",\"workingDays\":[\"Monday\",\"Tuesday\",\"Friday\"],\"dependen"
            "ts\":[{\"name\":\"Future Wife\",\"age\":5147483649,\"address\":\"H # 531"
            ", S # 20\",\"uid\":\"123412\",\"birthday\":\"1994-02-13\",\"birthtime\":"
            "\"1994-02-13T14:01:54.9571247Z\"},{\"name\":\"Future Kid\",\"age\":51474"
            "83648,\"address\":\"H # 531, S # 20\",\"uid\":\"312341\",\"birthday\":\""
            "1994-02-13\",\"birthtime\":\"1994-02-13T14:01:54.9571247Z\"}],\"hiredAt"
            "\":\"Sun, 06 Nov 1994 08:49:37 GMT\",\"promotedAt\":1484719381},\"depend"
            "ents\":[{\"name\":\"Future Wife\",\"age\":5147483649,\"address\":\"H # 5"
            "31, S # 20\",\"uid\":\"123412\",\"birthday\":\"1994-02-13\",\"birthtime"
            "\":\"1994-02-13T14:01:54.9571247Z\"},{\"name\":\"Future Kid\",\"age\":51"
            "47483648,\"address\":\"H # 531, S # 20\",\"uid\":\"312341\",\"birthday\""
            ":\"1994-02-13\",\"birthtime\":\"1994-02-13T14:01:54.9571247Z\"}],\"hired"
            "At\":\"Sun, 06 Nov 1994 08:49:37 GMT\"}]",
            Employee.from_dictionary,
        )
        options["strings"] = "abc"

        # Perform the API call through the SDK function
        result = self.controller.send_multipart_with_json(
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

