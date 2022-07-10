import json
import unittest
import time

import requests

from common import tool


class test_login(unittest.TestCase):

    def setUp(self):
        self.baseapi = "http://ihr-sit.yst.com.cn/backend"
        self.headers = {"Content-Type": "application/json"}
        time.sleep(1)

    def test_getPublicKey(self,case):
        print("测试用例:" + case)

        self.url = self.baseapi + "public-access/getPublicKey?t=1657441924565"
        response = requests.get(self.url, headers=self.headers,verify = False)
        #sid = tool.getValueTool().getvalue(response, "sid")
        res = json.loads(response)
        self.assertIn(res,"sid")

    def test_getPublicKey(self, case):
        print("测试用例:" + case)

        self.url = self.baseapi + "security/login?t=1657441924646"
        paramdict = {
            "username": "jliu142",
            "password": "123",
            "t":"1609913740008"
        }
        param = json.dumps(paramdict)
        response = requests.post(self.url,data=param,headers=self.headers,verify = False)
        res = json.loads(response)
        self.assertIsNotNone(res)




















