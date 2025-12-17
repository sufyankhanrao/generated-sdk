# -*- coding: utf-8 -*-

"""
testerfilesandmultipart

This file was automatically generated for Stamplay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

import json
import dateutil.parser

from tests.controllers.controller_test_base import ControllerTestBase
from apimatic_core.utilities.comparison_helper import ComparisonHelper
from apimatic_core.utilities.file_helper import FileHelper
from testerfilesandmultipart.api_helper import APIHelper
from testerfilesandmultipart.models.person import Employee


class MultipartParamsControllerTests(ControllerTestBase):

    controller = None

    @classmethod
    def setUpClass(cls):
        super(MultipartParamsControllerTests, cls).setUpClass()
        cls.controller = cls.client.multipart_params
        cls.response_catcher = cls.controller.http_call_back

    # Todo: Add description for test test_send_mixed_array
    def test_send_mixed_array(self):
        # Parameters for the API call
        options = {}
        options['file'] = FileHelper.get_file('http://localhost:3000/response/image')
        options['integers'] = 1
        options['models'] = APIHelper.json_deserialize('[{"name":"Shahid Khaliq","age":5147483645,"address":"H # 531, S # '
            '20","uid":"123321","birthday":"1994-02-13","birthtime":"1994-02-13'
            'T14:01:54.9571247Z","salary":20000,"department":"Software Developm'
            'ent","joiningDay":"Saturday","workingDays":["Monday","Tuesday","Fr'
            'iday"],"boss":{"personType":"Boss","name":"Zeeshan Ejaz","age":514'
            '7483645,"address":"H # 531, S # 20","uid":"123321","birthday":"199'
            '4-02-13","birthtime":"1994-02-13T14:01:54.9571247Z","salary":20000'
            ',"department":"Software Development","joiningDay":"Saturday","work'
            'ingDays":["Monday","Tuesday","Friday"],"dependents":[{"name":"Futu'
            're Wife","age":5147483649,"address":"H # 531, S # 20","uid":"12341'
            '2","birthday":"1994-02-13","birthtime":"1994-02-13T14:01:54.957124'
            '7Z"},{"name":"Future Kid","age":5147483648,"address":"H # 531, S #'
            ' 20","uid":"312341","birthday":"1994-02-13","birthtime":"1994-02-1'
            '3T14:01:54.9571247Z"}],"hiredAt":"Sun, 06 Nov 1994 08:49:37 GMT","'
            'promotedAt":1484719381},"dependents":[{"name":"Future Wife","age":'
            '5147483649,"address":"H # 531, S # 20","uid":"123412","birthday":"'
            '1994-02-13","birthtime":"1994-02-13T14:01:54.9571247Z"},{"name":"F'
            'uture Kid","age":5147483648,"address":"H # 531, S # 20","uid":"312'
            '341","birthday":"1994-02-13","birthtime":"1994-02-13T14:01:54.9571'
            '247Z"}],"hiredAt":"Sun, 06 Nov 1994 08:49:37 GMT"},{"name":"Shahid'
            ' Khaliq","age":5147483645,"address":"H # 531, S # 20","uid":"12332'
            '1","birthday":"1994-02-13","birthtime":"1994-02-13T14:01:54.957124'
            '7Z","salary":20000,"department":"Software Development","joiningDay'
            '":"Saturday","workingDays":["Monday","Tuesday","Friday"],"boss":{"'
            'personType":"Boss","name":"Zeeshan Ejaz","age":5147483645,"address'
            '":"H # 531, S # 20","uid":"123321","birthday":"1994-02-13","birtht'
            'ime":"1994-02-13T14:01:54.9571247Z","salary":20000,"department":"S'
            'oftware Development","joiningDay":"Saturday","workingDays":["Monda'
            'y","Tuesday","Friday"],"dependents":[{"name":"Future Wife","age":5'
            '147483649,"address":"H # 531, S # 20","uid":"123412","birthday":"1'
            '994-02-13","birthtime":"1994-02-13T14:01:54.9571247Z"},{"name":"Fu'
            'ture Kid","age":5147483648,"address":"H # 531, S # 20","uid":"3123'
            '41","birthday":"1994-02-13","birthtime":"1994-02-13T14:01:54.95712'
            '47Z"}],"hiredAt":"Sun, 06 Nov 1994 08:49:37 GMT","promotedAt":1484'
            '719381},"dependents":[{"name":"Future Wife","age":5147483649,"addr'
            'ess":"H # 531, S # 20","uid":"123412","birthday":"1994-02-13","bir'
            'thtime":"1994-02-13T14:01:54.9571247Z"},{"name":"Future Kid","age"'
            ':5147483648,"address":"H # 531, S # 20","uid":"312341","birthday":'
            '"1994-02-13","birthtime":"1994-02-13T14:01:54.9571247Z"}],"hiredAt'
            '":"Sun, 06 Nov 1994 08:49:37 GMT"}]', Employee.from_dictionary)
        options['strings'] = 'abc'

        # Perform the API call through the SDK function
        result = self.controller.send_multipart_with_json(options)

        # Test response code
        assert self.response_catcher.response.status_code == 200
        
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize('{"passed":true}')
        received_body = APIHelper.json_deserialize(self.response_catcher.response.text)
        assert ComparisonHelper.match_body(expected_body, received_body, check_values = True)

