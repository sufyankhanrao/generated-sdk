
"""
tester

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

from tester.api_helper import APIHelper
from tests.controllers.controller_test_base import (
    ControllerTestBase,
)


class ResponseTypesControllerTests(ControllerTestBase):
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
        cls.controller = cls.client.response_types
        cls.response_catcher = cls.controller.http_call_back

    def test_get_date_array(self):
        """
        Api call test for `test_get_date_array`.
        """
        # Perform the API call through the SDK function
        result = self.controller.get_date_array()
        # Test response code
        assert self.response_catcher.response.status_code == 200
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize(
            "[\"1994-02-13\",\"1994-02-13\"]",
        )
        received_body = APIHelper.json_deserialize(
            self.response_catcher.response.text,
        )
        assert ComparisonHelper.match_body(
            expected_body,
            received_body,
        )

    def test_get_date(self):
        """
        Api call test for `test_get_date`.
        """
        # Perform the API call through the SDK function
        result = self.controller.get_date()
        # Test response code
        assert self.response_catcher.response.status_code == 200
        # Test whether the captured response is as we expected
        assert result is not None
        assert self.response_catcher.response.text ==\
            "1994-02-13"

    def test_return_company_model(self):
        """
        Api call test for `test_return_company_model`.
        """
        # Perform the API call through the SDK function
        result = self.controller.return_company_model()
        # Test response code
        assert self.response_catcher.response.status_code == 200
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize(
            "{\"company name\":\"APIMatic\",\"address\":\"nust\",\"cell number\":\"09"
            "0078601\"}",
        )
        received_body = APIHelper.json_deserialize(
            self.response_catcher.response.text,
        )
        assert ComparisonHelper.match_body(
            expected_body,
            received_body,
            check_values = True,
        )

    def test_return_boss_model(self):
        """
        Api call test for `test_return_boss_model`.
        """
        # Perform the API call through the SDK function
        result = self.controller.return_boss_model()
        # Test response code
        assert self.response_catcher.response.status_code == 200
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize(
            "{\"company name\":\"APIMatic\",\"address\":\"nust\",\"cell number\":\"09"
            "0078601\",\"first name\":\"Adeel\",\"last name\":\"Ali\",\"address_boss"
            "\":\"nust\"}",
        )
        received_body = APIHelper.json_deserialize(
            self.response_catcher.response.text,
        )
        assert ComparisonHelper.match_body(
            expected_body,
            received_body,
            check_values = True,
        )

    def test_return_employee_model(self):
        """
        Api call test for `test_return_employee_model`.
        """
        # Perform the API call through the SDK function
        result = self.controller.return_employee_model()
        # Test response code
        assert self.response_catcher.response.status_code == 200
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize(
            "{\"company name\":\"APIMatic\",\"address\":\"nust\",\"cell number\":\"09"
            "0078601\",\"first name\":\"Nauman\",\"last name\":\"Ali\",\"id\":\"12345"
            "6\"}",
        )
        received_body = APIHelper.json_deserialize(
            self.response_catcher.response.text,
        )
        assert ComparisonHelper.match_body(
            expected_body,
            received_body,
            check_values = True,
        )

    def test_return_developer_model(self):
        """
        Api call test for `test_return_developer_model`.
        """
        # Perform the API call through the SDK function
        result = self.controller.return_developer_model()
        # Test response code
        assert self.response_catcher.response.status_code == 200
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize(
            "{\"company name\":\"APIMatic\",\"address\":\"nust\",\"cell number\":\"09"
            "0078601\",\"first name\":\"Nauman\",\"last name\":\"Ali\",\"id\":\"12345"
            "6\",\"team\":\"CORE\",\"designation\":\"Manager\",\"role\":\"Team Lead\""
            "}",
        )
        received_body = APIHelper.json_deserialize(
            self.response_catcher.response.text,
        )
        assert ComparisonHelper.match_body(
            expected_body,
            received_body,
            check_values = True,
        )

    def test_return_tester_model(self):
        """
        Api call test for `test_return_tester_model`.
        """
        # Perform the API call through the SDK function
        result = self.controller.return_tester_model()
        # Test response code
        assert self.response_catcher.response.status_code == 200
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize(
            "{\"company name\":\"APIMatic\",\"address\":\"nust\",\"cell number\":\"09"
            "0078601\",\"first name\":\"Muhammad\",\"last name\":\"Farhan\",\"id\":\""
            "123456\",\"team\":\"Testing\",\"designation\":\"Tester\",\"role\":\"Test"
            "ing\"}",
        )
        received_body = APIHelper.json_deserialize(
            self.response_catcher.response.text,
        )
        assert ComparisonHelper.match_body(
            expected_body,
            received_body,
            check_values = True,
        )

    def test_return_complex_1_object(self):
        """
        Api call test for `test_return_complex_1_object`.
        """
        # Perform the API call through the SDK function
        result = self.controller.return_complex_1_object()
        # Test response code
        assert self.response_catcher.response.status_code == 200
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize(
            "{\"medications\":[{\"aceInhibitors\":[{\"name\":\"lisinopril\",\"strengt"
            "h\":\"10 mg Tab\",\"dose\":\"1 tab\",\"route\":\"PO\",\"sig\":\"daily\","
            "\"pillCount\":\"#90\",\"refills\":\"Refill 3\"}],\"antianginal\":[{\"nam"
            "e\":\"nitroglycerin\",\"strength\":\"0.4 mg Sublingual Tab\",\"dose\":\""
            "1 tab\",\"route\":\"SL\",\"sig\":\"q15min PRN\",\"pillCount\":\"#30\",\""
            "refills\":\"Refill 1\"}],\"anticoagulants\":[{\"name\":\"warfarin sodium"
            "\",\"strength\":\"3 mg Tab\",\"dose\":\"1 tab\",\"route\":\"PO\",\"sig\""
            ":\"daily\",\"pillCount\":\"#90\",\"refills\":\"Refill 3\"}],\"betaBlocke"
            "r\":[{\"name\":\"metoprolol tartrate\",\"strength\":\"25 mg Tab\",\"dose"
            "\":\"1 tab\",\"route\":\"PO\",\"sig\":\"daily\",\"pillCount\":\"#90\",\""
            "refills\":\"Refill 3\"}],\"diuretic\":[{\"name\":\"furosemide\",\"streng"
            "th\":\"40 mg Tab\",\"dose\":\"1 tab\",\"route\":\"PO\",\"sig\":\"daily\""
            ",\"pillCount\":\"#90\",\"refills\":\"Refill 3\"}],\"mineral\":[{\"name\""
            ":\"potassium chloride ER\",\"strength\":\"10 mEq Tab\",\"dose\":\"1 tab"
            "\",\"route\":\"PO\",\"sig\":\"daily\",\"pillCount\":\"#90\",\"refills\":"
            "\"Refill 3\"}]}],\"labs\":[{\"name\":\"Arterial Blood Gas\",\"time\":\"T"
            "oday\",\"location\":\"Main Hospital Lab\"},{\"name\":\"BMP\",\"time\":\""
            "Today\",\"location\":\"Primary Care Clinic\"},{\"name\":\"BNP\",\"time\""
            ":\"3 Weeks\",\"location\":\"Primary Care Clinic\"},{\"name\":\"BUN\",\"t"
            "ime\":\"1 Year\",\"location\":\"Primary Care Clinic\"},{\"name\":\"Cardi"
            "ac Enzymes\",\"time\":\"Today\",\"location\":\"Primary Care Clinic\"},{"
            "\"name\":\"CBC\",\"time\":\"1 Year\",\"location\":\"Primary Care Clinic"
            "\"},{\"name\":\"Creatinine\",\"time\":\"1 Year\",\"location\":\"Main Hos"
            "pital Lab\"},{\"name\":\"Electrolyte Panel\",\"time\":\"1 Year\",\"locat"
            "ion\":\"Primary Care Clinic\"},{\"name\":\"Glucose\",\"time\":\"1 Year\""
            ",\"location\":\"Main Hospital Lab\"},{\"name\":\"PT/INR\",\"time\":\"3 W"
            "eeks\",\"location\":\"Primary Care Clinic\"},{\"name\":\"PTT\",\"time\":"
            "\"3 Weeks\",\"location\":\"Coumadin Clinic\"},{\"name\":\"TSH\",\"time\""
            ":\"1 Year\",\"location\":\"Primary Care Clinic\"}],\"imaging\":[{\"name"
            "\":\"Chest X-Ray\",\"time\":\"Today\",\"location\":\"Main Hospital Radio"
            "logy\"},{\"name\":\"Chest X-Ray\",\"time\":\"Today\",\"location\":\"Main"
            " Hospital Radiology\"},{\"name\":\"Chest X-Ray\",\"time\":\"Today\",\"lo"
            "cation\":\"Main Hospital Radiology\"}]}",
        )
        received_body = APIHelper.json_deserialize(
            self.response_catcher.response.text,
        )
        assert ComparisonHelper.match_body(
            expected_body,
            received_body,
            check_values = True,
        )

    def test_return_response_with_enum_object(self):
        """
        Api call test for `test_return_response_with_enum_object`.
        """
        # Perform the API call through the SDK function
        result = self.controller.return_response_with_enums()
        # Test response code
        assert self.response_catcher.response.status_code == 200
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize(
            "{\"paramFormat\":\"Template\",\"optional\":false,\"type\":\"Long\",\"con"
            "stant\":false,\"isArray\":false,\"isStream\":false,\"isAttribute\":false"
            ",\"isMap\":false,\"attributes\":{\"exclusiveMaximum\":false,\"exclusiveM"
            "inimum\":false,\"id\":\"5a9fcb01caacc310dc6bab51\"},\"nullable\":false,"
            "\"id\":\"5a9fcb01caacc310dc6bab50\",\"name\":\"petId\",\"description\":"
            "\"ID of pet to update\"}",
        )
        received_body = APIHelper.json_deserialize(
            self.response_catcher.response.text,
        )
        assert ComparisonHelper.match_body(
            expected_body,
            received_body,
            check_values = True,
        )

    def test_return_complex_2_object(self):
        """
        Api call test for `test_return_complex_2_object`.
        """
        # Perform the API call through the SDK function
        result = self.controller.return_complex_2_object()
        # Test response code
        assert self.response_catcher.response.status_code == 200
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize(
            "{\"glossary\":{\"title\":\"example glossary\",\"GlossDiv\":{\"title\":\""
            "S\",\"GlossList\":{\"GlossEntry\":{\"ID\":\"SGML\",\"SortAs\":\"SGML\","
            "\"GlossTerm\":\"Standard Generalized Markup Language\",\"Acronym\":\"SGM"
            "L\",\"Abbrev\":\"ISO 8879:1986\",\"GlossDef\":{\"para\":\"A meta-markup "
            "language, used to create markup languages such as DocBook.\",\"GlossSeeA"
            "lso\":[\"GML\",\"XML\"]},\"GlossSee\":\"markup\"}}}}}",
        )
        received_body = APIHelper.json_deserialize(
            self.response_catcher.response.text,
        )
        assert ComparisonHelper.match_body(
            expected_body,
            received_body,
            check_values = True,
        )

    def test_return_complex_3_object(self):
        """
        Api call test for `test_return_complex_3_object`.
        """
        # Perform the API call through the SDK function
        result = self.controller.return_complex_3_object()
        # Test response code
        assert self.response_catcher.response.status_code == 200
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize(
            "{\"documentId\":\"099cceda-38a8-4b01-87b9-a8f2007675d6\",\"signers\":[{"
            "\"id\":\"1bef97d1-0704-4eb2-a490-a8f2007675db\",\"url\":\"https://sign-t"
            "est.idfy.io/start?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzM4NCJ9.eyJrdmVyc2lvb"
            "iI6IjdmNzhjNzNkMmQ1MjQzZWRiYjdiNDI0MmI2MDE1MWU4IiwiZG9jaWQiOiIwOTljY2VkY"
            "S0zOGE4LTRiMDEtODdiOS1hOGYyMDA3Njc1ZDYiLCJhaWQiOiJjMGNlMTQ2OC1hYzk0LTRiM"
            "zQtODc2ZS1hODg1MDBjMmI5YTEiLCJsZyI6ImVuIiwiZXJyIjpudWxsLCJpZnIiOmZhbHNlL"
            "CJ3Ym1zZyI6ZmFsc2UsInNmaWQiOiIxYmVmOTdkMS0wNzA0LTRlYjItYTQ5MC1hOGYyMDA3N"
            "jc1ZGIiLCJ1cmxleHAiOm51bGwsImF0aCI6bnVsbCwiZHQiOiJUZXN0IGRvY3VtZW50Iiwid"
            "mYiOmZhbHNlLCJhbiI6IklkZnkgU0RLIGRlbW8iLCJ0aCI6IlBpbmsiLCJzcCI6IkN1YmVzI"
            "iwiZG9tIjpudWxsLCJyZGlyIjpmYWxzZSwidXQiOiJ3ZWIiLCJ1dHYiOm51bGwsInNtIjoid"
            "GVzdEB0ZXN0LmNvbSJ9.Dyy2RSeR6dmU8qxOEi-2gEX3Gg7wry6JhkZIWOuADDdu5jJWidQL"
            "cxfJn_qAHNpb\",\"links\":[],\"externalSignerId\":\"uoiahsd321982983jhrmn"
            "ec2wsadm32\",\"redirectSettings\":{\"redirectMode\":\"donot_redirect\"},"
            "\"signatureType\":{\"mechanism\":\"pkisignature\",\"onEacceptUseHandWrit"
            "tenSignature\":false},\"ui\":{\"dialogs\":{\"before\":{\"useCheckBox\":f"
            "alse,\"title\":\"Info\",\"message\":\"Please read the contract on the ne"
            "xt pages carefully. Pay some extra attention to paragraph 5.\"}},\"langu"
            "age\":\"EN\",\"styling\":{\"colorTheme\":\"Pink\",\"spinner\":\"Cubes\"}"
            "},\"tags\":[],\"order\":0,\"required\":false}],\"status\":{\"documentSta"
            "tus\":\"unsigned\",\"completedPackages\":[],\"attachmentPackages\":{}},"
            "\"title\":\"Test document\",\"description\":\"This is an important docum"
            "ent\",\"externalId\":\"ae7b9ca7-3839-4e0d-a070-9f14bffbbf55\",\"dataToSi"
            "gn\":{\"fileName\":\"sample.txt\",\"convertToPDF\":false},\"contactDetai"
            "ls\":{\"email\":\"test@test.com\",\"url\":\"https://idfy.io\"},\"advance"
            "d\":{\"tags\":[\"develop\",\"fun_with_documents\"],\"attachments\":0,\"r"
            "equiredSignatures\":0,\"getSocialSecurityNumber\":false,\"timeToLive\":{"
            "\"deadline\":\"2018-06-29T14:57:25Z\",\"deleteAfterHours\":1}}}",
        )
        received_body = APIHelper.json_deserialize(
            self.response_catcher.response.text,
        )
        assert ComparisonHelper.match_body(
            expected_body,
            received_body,
            check_values = True,
        )

    def test_get_long(self):
        """
        Api call test for `test_get_long`.
        """
        # Perform the API call through the SDK function
        result = self.controller.get_long()
        # Test response code
        assert self.response_catcher.response.status_code == 200
        # Test whether the captured response is as we expected
        assert result is not None
        assert self.response_catcher.response.text ==\
            "5147483647"

    def test_get_model(self):
        """
        Api call test for `test_get_model`.
        """
        # Perform the API call through the SDK function
        result = self.controller.get_model()
        # Test response code
        assert self.response_catcher.response.status_code == 200
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize(
            "{\"name\":\"Shahid Khaliq\",\"age\":5147483645,\"address\":\"H # 531, S "
            "# 20\",\"uid\":\"123321\",\"birthday\":\"1994-02-13\",\"birthtime\":\"19"
            "94-02-13T14:01:54.9571247Z\",\"salary\":20000,\"department\":\"Software "
            "Development\",\"joiningDay\":\"Saturday\",\"workingDays\":[\"Monday\",\""
            "Tuesday\",\"Friday\"],\"boss\":{\"personType\":\"Boss\",\"name\":\"Zeesh"
            "an Ejaz\",\"age\":5147483645,\"address\":\"H # 531, S # 20\",\"uid\":\"1"
            "23321\",\"birthday\":\"1994-02-13\",\"birthtime\":\"1994-02-13T14:01:54."
            "9571247Z\",\"salary\":20000,\"department\":\"Software Development\",\"jo"
            "iningDay\":\"Saturday\",\"workingDays\":[\"Monday\",\"Tuesday\",\"Friday"
            "\"],\"dependents\":[{\"name\":\"Future Wife\",\"age\":5147483649,\"addre"
            "ss\":\"H # 531, S # 20\",\"uid\":\"123412\",\"birthday\":\"1994-02-13\","
            "\"birthtime\":\"1994-02-13T14:01:54.9571247Z\"},{\"name\":\"Future Kid\""
            ",\"age\":5147483648,\"address\":\"H # 531, S # 20\",\"uid\":\"312341\","
            "\"birthday\":\"1994-02-13\",\"birthtime\":\"1994-02-13T14:01:54.9571247Z"
            "\"}],\"hiredAt\":\"Sun, 06 Nov 1994 08:49:37 GMT\",\"promotedAt\":148471"
            "9381},\"dependents\":[{\"name\":\"Future Wife\",\"age\":5147483649,\"add"
            "ress\":\"H # 531, S # 20\",\"uid\":\"123412\",\"birthday\":\"1994-02-13"
            "\",\"birthtime\":\"1994-02-13T14:01:54.9571247Z\"},{\"name\":\"Future Ki"
            "d\",\"age\":5147483648,\"address\":\"H # 531, S # 20\",\"uid\":\"312341"
            "\",\"birthday\":\"1994-02-13\",\"birthtime\":\"1994-02-13T14:01:54.95712"
            "47Z\"}],\"hiredAt\":\"Sun, 06 Nov 1994 08:49:37 GMT\"}",
        )
        received_body = APIHelper.json_deserialize(
            self.response_catcher.response.text,
        )
        assert ComparisonHelper.match_body(
            expected_body,
            received_body,
            check_values = True,
        )

    def test_get_void_model(self):
        """
        Api call test for `test_get_void_model`.
        """
        # Perform the API call through the SDK function
        result = self.controller.get_void_model()
        # Test response code
        assert self.response_catcher.response.status_code == 200
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize(
            "{\"id\":100,\"message\":\"passed\"}",
        )
        received_body = APIHelper.json_deserialize(
            self.response_catcher.response.text,
        )
        assert ComparisonHelper.match_body(
            expected_body,
            received_body,
            check_values = True,
        )

    def test_get_string_enum_array(self):
        """
        Api call test for `test_get_string_enum_array`.
        """
        # Perform the API call through the SDK function
        result = self.controller.get_string_enum_array()
        # Test response code
        assert self.response_catcher.response.status_code == 200
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize(
            "[\"Tuesday\",\"Saturday\",\"Wednesday\",\"Monday\",\"Sunday\"]",
        )
        received_body = APIHelper.json_deserialize(
            self.response_catcher.response.text,
        )
        assert ComparisonHelper.match_body(
            expected_body,
            received_body,
        )

    def test_get_string_enum(self):
        """
        Api call test for `test_get_string_enum`.
        """
        # Perform the API call through the SDK function
        result = self.controller.get_string_enum()
        # Test response code
        assert self.response_catcher.response.status_code == 200
        # Test whether the captured response is as we expected
        assert result is not None
        assert self.response_catcher.response.text ==\
            "Monday"

    def test_get_model_array(self):
        """
        Api call test for `test_get_model_array`.
        """
        # Perform the API call through the SDK function
        result = self.controller.get_model_array()
        # Test response code
        assert self.response_catcher.response.status_code == 200
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize(
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
        )
        received_body = APIHelper.json_deserialize(
            self.response_catcher.response.text,
        )
        assert ComparisonHelper.match_body(
            expected_body,
            received_body,
            check_values = True,
        )

    def test_get_int_enum(self):
        """
        Api call test for `test_get_int_enum`.
        """
        # Perform the API call through the SDK function
        result = self.controller.get_int_enum()
        # Test response code
        assert self.response_catcher.response.status_code == 200
        # Test whether the captured response is as we expected
        assert result is not None
        assert self.response_catcher.response.text ==\
            "3"

    def test_get_int_enum_array(self):
        """
        Api call test for `test_get_int_enum_array`.
        """
        # Perform the API call through the SDK function
        result = self.controller.get_int_enum_array()
        # Test response code
        assert self.response_catcher.response.status_code == 200
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize(
            "[1,3,4,2,3]",
        )
        received_body = APIHelper.json_deserialize(
            self.response_catcher.response.text,
        )
        assert ComparisonHelper.match_body(
            expected_body,
            received_body,
        )

    def test_get_precision(self):
        """
        Api call test for `test_get_precision`.
        """
        # Perform the API call through the SDK function
        result = self.controller.get_precision()
        # Test response code
        assert self.response_catcher.response.status_code == 200
        # Test whether the captured response is as we expected
        assert result is not None
        assert self.response_catcher.response.text ==\
            "4.999"

    def test_get_binary(self):
        """
        Api call test for `test_get_binary`.
        """
        # Perform the API call through the SDK function
        result = self.controller.get_binary()
        # Test response code
        assert self.response_catcher.response.status_code == 200
        # Test whether the captured response is as we expected
        assert result is not None
        assert self.response_catcher.response.text ==\
            FileHelper.get_file("http://localhost:3000/response/image").read()

    def test_get_integer(self):
        """
        Api call test for `test_get_integer`.
        """
        # Perform the API call through the SDK function
        result = self.controller.get_integer()
        # Test response code
        assert self.response_catcher.response.status_code == 200
        # Test whether the captured response is as we expected
        assert result is not None
        assert self.response_catcher.response.text ==\
            "4"

    def test_get_integer_array(self):
        """
        Api call test for `test_get_integer_array`.
        """
        # Perform the API call through the SDK function
        result = self.controller.get_integer_array()
        # Test response code
        assert self.response_catcher.response.status_code == 200
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize(
            "[1,2,3,4,5]",
        )
        received_body = APIHelper.json_deserialize(
            self.response_catcher.response.text,
        )
        assert ComparisonHelper.match_body(
            expected_body,
            received_body,
        )

    def test_get_dynamic(self):
        """
        Api call test for `test_get_dynamic`.
        """
        # Perform the API call through the SDK function
        result = self.controller.get_dynamic()
        # Test response code
        assert self.response_catcher.response.status_code == 200
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize(
            "{\"method\":\"GET\",\"body\":{},\"uploadCount\":0}",
        )
        received_body = APIHelper.json_deserialize(
            self.response_catcher.response.text,
        )
        assert ComparisonHelper.match_body(
            expected_body,
            received_body,
            check_values = True,
        )

    def test_get_dynamic_array(self):
        """
        Api call test for `test_get_dynamic_array`.
        """
        # Perform the API call through the SDK function
        result = self.controller.get_dynamic_array()
        # Test response code
        assert self.response_catcher.response.status_code == 200
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize(
            "{\"method\":\"GET\",\"body\":{},\"uploadCount\":0}",
        )
        received_body = APIHelper.json_deserialize(
            self.response_catcher.response.text,
        )
        assert ComparisonHelper.match_body(
            expected_body,
            received_body,
            check_values = True,
        )

    def test_get_3339_datetime(self):
        """
        Api call test for `test_get_3339_datetime`.
        """
        # Perform the API call through the SDK function
        result = self.controller.get_3339_datetime()
        # Test response code
        assert self.response_catcher.response.status_code == 200
        # Test whether the captured response is as we expected
        assert result is not None
        assert self.response_catcher.response.text ==\
            "2016-03-13T12:52:32.123Z"

    def test_get_3339_datetime_array(self):
        """
        Api call test for `test_get_3339_datetime_array`.
        """
        # Perform the API call through the SDK function
        result = self.controller.get_3339_datetime_array()
        # Test response code
        assert self.response_catcher.response.status_code == 200
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize(
            "[\"2016-03-13T12:52:32.123Z\",\"2016-03-13T12:52:32.123Z\",\"2016-03-13T"
            "12:52:32.123Z\"]",
        )
        received_body = APIHelper.json_deserialize(
            self.response_catcher.response.text,
        )
        assert ComparisonHelper.match_body(
            expected_body,
            received_body,
        )

    def test_get_boolean(self):
        """
        Api call test for `test_get_boolean`.
        """
        # Perform the API call through the SDK function
        result = self.controller.get_boolean()
        # Test response code
        assert self.response_catcher.response.status_code == 200
        # Test whether the captured response is as we expected
        assert result is not None
        assert self.response_catcher.response.text ==\
            "true"

    def test_get_boolean_array(self):
        """
        Api call test for `test_get_boolean_array`.
        """
        # Perform the API call through the SDK function
        result = self.controller.get_boolean_array()
        # Test response code
        assert self.response_catcher.response.status_code == 200
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize(
            "[true,false,true,true,false]",
        )
        received_body = APIHelper.json_deserialize(
            self.response_catcher.response.text,
        )
        assert ComparisonHelper.match_body(
            expected_body,
            received_body,
        )

    def test_get_headers_allow_extra(self):
        """
        Api call test for `test_get_headers_allow_extra`.
        """
        # Perform the API call through the SDK function
        self.controller.get_headers()
        # Test response code
        assert self.response_catcher.response.status_code == 200
        # Test headers
        expected_headers = {
            "naumanali": None,
            "waseemhasan": None,
        }

        assert ComparisonHelper.match_headers(
            expected_headers,
            self.response_catcher.response.headers,
        )

    def test_get_1123_date_time(self):
        """
        Api call test for `test_get_1123_date_time`.
        """
        # Perform the API call through the SDK function
        result = self.controller.get_1123_date_time()
        # Test response code
        assert self.response_catcher.response.status_code == 200
        # Test whether the captured response is as we expected
        assert result is not None
        assert self.response_catcher.response.text ==\
            "Sun, 06 Nov 1994 08:49:37 GMT"

    def test_get_unix_date_time(self):
        """
        Api call test for `test_get_unix_date_time`.
        """
        # Perform the API call through the SDK function
        result = self.controller.get_unix_date_time()
        # Test response code
        assert self.response_catcher.response.status_code == 200
        # Test whether the captured response is as we expected
        assert result is not None
        assert self.response_catcher.response.text ==\
            "1484719381"

    def test_get_1123_date_time_array(self):
        """
        Api call test for `test_get_1123_date_time_array`.
        """
        # Perform the API call through the SDK function
        result = self.controller.get_1123_date_time_array()
        # Test response code
        assert self.response_catcher.response.status_code == 200
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize(
            "[\"Sun, 06 Nov 1994 08:49:37 GMT\",\"Sun, 06 Nov 1994 08:49:37 GMT\"]",
        )
        received_body = APIHelper.json_deserialize(
            self.response_catcher.response.text,
        )
        assert ComparisonHelper.match_body(
            expected_body,
            received_body,
        )

    def test_get_unix_date_time_array(self):
        """
        Api call test for `test_get_unix_date_time_array`.
        """
        # Perform the API call through the SDK function
        result = self.controller.get_unix_date_time_array()
        # Test response code
        assert self.response_catcher.response.status_code == 200
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize(
            "[1484719381,1484719381]",
        )
        received_body = APIHelper.json_deserialize(
            self.response_catcher.response.text,
        )
        assert ComparisonHelper.match_body(
            expected_body,
            received_body,
        )

    def test_get_content_type_in_response(self):
        """
        Api call test for `test_get_content_type_in_response`.
        """
        # Perform the API call through the SDK function
        self.controller.get_content_type_headers()
        # Test response code
        assert self.response_catcher.response.status_code == 200
        # Test headers
        expected_headers = {
            "content-type": "application/responseType",
            "accept": "application/noTerm",
            "accept-encoding": "UTF-8",
        }

        assert ComparisonHelper.match_headers(
            expected_headers,
            self.response_catcher.response.headers,
        )

