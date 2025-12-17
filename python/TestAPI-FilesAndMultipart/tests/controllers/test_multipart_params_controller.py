
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

