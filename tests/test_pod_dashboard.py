# coding=utf-8
from __future__ import unicode_literals

import unittest

from pod_base import InvalidDataException
from random import randint
from pod_dashboard import PodDashboard, EditAccessLevel, ShareAccessLevel, DashboardException
from tests.config import *
from datetime import datetime


class TestPodDashboard(unittest.TestCase):
    __slots__ = ("__dashboard", "__name", "__dashboard_id")

    def setUp(self):
        self.__dashboard_id = 342
        self.__name = "PyDash {}".format(datetime.now().timestamp())
        self.__dashboard = PodDashboard(api_token=API_TOKEN, server_type=SERVER_MODE)

    def test_01_create_dashboard(self):
        result = self.__dashboard.create_dashboard(name=self.__name)
        self.assertIsInstance(result, int, msg="create dashboard : check instance")

    def test_01_create_dashboard_all_params(self):
        config = {
            "layout": [{
                "w": 20,
                "h": 43,
                "x": 0,
                "y": 0,
                "i": 356,
                "moved": True,
                "static": True
            }],
        }
        result = self.__dashboard.create_dashboard(name=self.__name+"_2", order=1, config=config)
        self.assertIsInstance(result, int, msg="create dashboard (all params): check instance")

    def test_01_create_dashboard_required_param(self):
        with self.assertRaises(TypeError, msg="create dashboard : required param"):
            self.__dashboard.create_dashboard()

    def test_01_create_dashboard_validation_error(self):
        with self.assertRaises(InvalidDataException, msg="create dashboard : validation error"):
            self.__dashboard.create_dashboard(name="", order="2", config="{'test': 'yes'}")

    def test_02_get_user_dashboards(self):
        result = self.__dashboard.get_user_dashboards()
        self.assertIsInstance(result, dict, msg="get user dashboards : check instance")

    def test_02_get_user_dashboards_all_params(self):
        result = self.__dashboard.get_user_dashboards(page=0, size=5)
        self.assertIsInstance(result, dict, msg="get user dashboards (all params): check instance")

    def test_02_get_user_dashboards_validation_error(self):
        with self.assertRaises(InvalidDataException, msg="get user dashboards : validation error"):
            self.__dashboard.get_user_dashboards(page="0", size="10")

    def test_03_get_all_dashboards(self):
        result = self.__dashboard.get_all_dashboards()
        self.assertIsInstance(result, list, msg="get all dashboards : check instance")

    def test_04_update_dashboard(self):
        result = self.__dashboard.update_dashboard(dashboard_id=self.__dashboard_id, name=self.__name+"_edited")
        self.assertIsInstance(result, int, msg="update dashboard : check instance")

    def test_04_update_dashboard_required_params(self):
        with self.assertRaises(TypeError, msg="update dashboard : required params"):
            self.__dashboard.update_dashboard()

    def test_04_update_dashboard_validation_error(self):
        with self.assertRaises(InvalidDataException, msg="update dashboard : validation error"):
            self.__dashboard.update_dashboard(dashboard_id="123456", name=456)

    def test_905_remove_dashboard(self):
        result = self.__dashboard.remove_dashboard(dashboard_id=self.__dashboard_id)
        self.assertIsInstance(result, int, msg="remove dashboard : check instance")

    def test_905_remove_dashboard_required_params(self):
        with self.assertRaises(TypeError, msg="remove dashboard : required params"):
            self.__dashboard.remove_dashboard()

    def test_905_remove_dashboard_validation_errors(self):
        with self.assertRaises(InvalidDataException, msg="remove dashboard : validation errors"):
            self.__dashboard.remove_dashboard(dashboard_id="123")

    def test_06_get_all_collaborator_reports(self):
        result = self.__dashboard.get_all_collaborator_reports()
        self.assertIsInstance(result, dict, msg="get all collaborator : check instance")

    def test_06_get_all_collaborator_reports_all_params(self):
        result = self.__dashboard.get_all_collaborator_reports(name="نسبت", page=0, size=10)
        self.assertIsInstance(result, dict, msg="get all collaborator (all params) : check instance")

    def test_06_get_all_collaborator_reports_validation_errors(self):
        with self.assertRaises(InvalidDataException, msg="get all collaborator : validation errors"):
            self.__dashboard.get_all_collaborator_reports(name="", page="0", size="10")

    def test_07_get_collaborator_report(self):
        result = self.__dashboard.get_collaborator_report(report_id=180)
        self.assertIsInstance(result, dict, msg="get collaborator report : check instance")

    def test_07_get_collaborator_report_required_params(self):
        with self.assertRaises(TypeError, msg="get collaborator report : required params"):
            self.__dashboard.get_collaborator_report()

    def test_07_get_collaborator_report_validation_errors(self):
        with self.assertRaises(InvalidDataException, msg="get collaborator report : validation errors"):
            self.__dashboard.get_collaborator_report(report_id="180")

    def test_08_add_user_param(self):
        result = self.__dashboard.add_user_param(report_id=180, dashboard_id=self.__dashboard_id)
        self.assertIsInstance(result, int, msg="add user param : check instance")

    def test_08_add_user_param_all_params(self):
        params = [{
            "key": "key_1",
            "value": "value_1"
        },{
            "key": "key_2",
            "value": "value_2"
        }]

        result = self.__dashboard.add_user_param(report_id=180, dashboard_id=self.__dashboard_id, name="گزارش دوم",
                                                 params=params)
        self.assertIsInstance(result, int, msg="add user param (all params) : check instance")

    def test_08_add_user_param_required_params(self):
        with self.assertRaises(TypeError, msg="add user param : required params"):
            self.__dashboard.add_user_param()

    def test_08_add_user_param_validation_errors(self):
        with self.assertRaises(InvalidDataException, msg="add user param : validation errors"):
            self.__dashboard.add_user_param(report_id="180", dashboard_id="123")

    def test_09_add_drill_down_user_param(self):
        user_report_id = self.__dashboard.add_user_param(report_id=180, dashboard_id=self.__dashboard_id,
                                                         name="تست زیر گزارش")

        result = self.__dashboard.add_drill_down_user_param(report_id=181, user_report_id=user_report_id, params=[{
            "key": "key_1",
            "value": "value_1"
        }])
        self.assertIsInstance(result, int, msg="add drill down user param : check instance")

    def test_09_add_drill_down_user_param_required_params(self):
        with self.assertRaises(TypeError, msg="add drill down user param : required params"):
            self.__dashboard.add_drill_down_user_param()

    def test_09_add_drill_down_user_param_validation_errors(self):
        with self.assertRaises(InvalidDataException, msg="add drill down user param : validation errors"):
            self.__dashboard.add_drill_down_user_param(report_id="181", user_report_id="123")

    def test_10_get_all_user_reports(self):
        result = self.__dashboard.get_all_user_reports()
        self.assertIsInstance(result, dict, msg="get all user reports : check instance")

    def test_10_get_all_user_reports_all_params(self):
        result = self.__dashboard.get_all_user_reports(page=0, size=10)
        self.assertIsInstance(result, dict, msg="get all user reports (all params) : check instance")

    def test_10_get_all_user_reports_validation_errors(self):
        with self.assertRaises(InvalidDataException, msg="get all user reports : validation errors"):
            self.__dashboard.get_all_user_reports(page="0", size="10")

    def test_11_get_user_report(self):
        user_reports = self.__dashboard.get_all_user_reports()
        if user_reports["totalSize"] < 1:
            self.skipTest("get user report : empty user reports")
        result = self.__dashboard.get_user_report(user_report_id=user_reports["data"][0]["id"])
        self.assertIsInstance(result, dict, msg="get user report : check instance")

    def test_11_get_user_report_required_params(self):
        with self.assertRaises(TypeError, msg="get user report : required params"):
            self.__dashboard.get_user_report()

    def test_11_get_user_report_validation_errors(self):
        with self.assertRaises(InvalidDataException, msg="get user report : validation errors"):
            self.__dashboard.get_user_report(user_report_id="123")

    def test_12_execute_user_report(self):
        user_reports = self.__dashboard.get_all_user_reports()
        if user_reports["totalSize"] < 1:
            self.skipTest("execute user report : empty user reports")

        result = self.__dashboard.execute_user_report(user_report_id=user_reports["data"][0]["id"])
        self.assertIsInstance(result, dict, msg="execute user report : check instance")

    def test_12_execute_user_report_all_params(self):
        user_reports = self.__dashboard.get_all_user_reports()
        if user_reports["totalSize"] < 1:
            self.skipTest("execute user report (all params) : empty user reports")

        result = self.__dashboard.execute_user_report(user_report_id=user_reports["data"][0]["id"], page=0, size=5,
                                                      load_from_cache=False, execute_params={})
        self.assertIsInstance(result, dict, msg="execute user report (all params) : check instance")

    def test_12_execute_user_report_required_params(self):
        with self.assertRaises(TypeError, msg="execute user report : required params"):
            self.__dashboard.execute_user_report()

    def test_12_execute_user_report_validation_errors(self):
        with self.assertRaises(InvalidDataException, msg="execute user report : validation errors"):
            self.__dashboard.execute_user_report(user_report_id="132", page="0", size="5", load_from_cache="True",
                                                 execute_params="{}")

    def test_13_get_xls(self):
        user_reports = self.__dashboard.get_all_user_reports()
        if user_reports["totalSize"] < 1:
            self.skipTest("get xls (all params) : empty user reports")

        result = self.__dashboard.get_xls(user_report_id=user_reports["data"][0]["id"], page=0, size=10,
                                          callback_url="http://localhost/test.php", force_save=True, execute_params={})
        self.assertIsInstance(result, str, msg="get xls : check instance")

    def test_13_get_xls_required_params(self):
        with self.assertRaises(TypeError, msg="get xls : required params"):
            self.__dashboard.get_xls()

    def test_13_get_xls_validation_errors(self):
        with self.assertRaises(InvalidDataException, msg="get xls : validation errors"):
            self.__dashboard.get_xls(user_report_id="123", page="0", size="10")

    def test_14_get_csv(self):
        user_reports = self.__dashboard.get_all_user_reports()
        if user_reports["totalSize"] < 1:
            self.skipTest("get csv (all params) : empty user reports")

        result = self.__dashboard.get_csv(user_report_id=user_reports["data"][0]["id"], page=0, size=10,
                                          callback_url="http://localhost/test.php", force_save=True, execute_params={})
        self.assertIsInstance(result, str, msg="get csv : check instance")

    def test_14_get_csv_required_params(self):
        with self.assertRaises(TypeError, msg="get csv : required params"):
            self.__dashboard.get_csv()

    def test_14_get_csv_validation_errors(self):
        with self.assertRaises(InvalidDataException, msg="get csv : validation errors"):
            self.__dashboard.get_csv(user_report_id="123", page="0", size="10")

    def test_9015_remove_user_report(self):
        user_reports = self.__dashboard.get_all_user_reports()
        if user_reports["totalSize"] < 1:
            self.skipTest("remove user report (all params) : empty user reports")

        result = self.__dashboard.remove_user_report(user_report_id=user_reports["data"][0]["id"])
        self.assertIsInstance(result, bool, msg="remove user report : check instance")

    def test_9015_remove_user_report_required_params(self):
        with self.assertRaises(TypeError, msg="remove user report : required params"):
            self.__dashboard.remove_user_report()

    def test_9015_remove_user_report_validation_errors(self):
        with self.assertRaises(InvalidDataException, msg="remove user report : validation errors"):
            self.__dashboard.remove_user_report(user_report_id="123")

    def test_16_share_dashboard(self):
        result = self.__dashboard.share_dashboard(dashboard_id=self.__dashboard_id,
                                                  identity=IDENTITY, expire=datetime.now().__format__("%Y-%m-%d"),
                                                  edit_access_level=EditAccessLevel.EDIT_SHARED_DASHBOARD_CONFIG,
                                                  share_access_level=ShareAccessLevel.SHARE)
        self.assertIsInstance(result, dict, msg="share dashboard : check instance")

    def test_16_share_dashboard_required_params(self):
        with self.assertRaises(TypeError, msg="share dashboard : required params"):
            self.__dashboard.share_dashboard()

    def test_16_share_dashboard_validation_errors(self):
        with self.assertRaises(InvalidDataException, msg="share dashboard : validation errors"):
            self.__dashboard.share_dashboard(dashboard_id="123", identity=123, expire=123, edit_access_level=123,
                                             share_access_level=123)

    def test_17_get_dashboard_users(self):
        result = self.__dashboard.get_dashboard_users(dashboard_id=self.__dashboard_id)
        self.assertIsInstance(result, dict, msg="get dashboard users : check instance")

    def test_17_get_dashboard_users_required_params(self):
        with self.assertRaises(TypeError, msg="get dashboard users : required params"):
            self.__dashboard.get_dashboard_users()

    def test_17_get_dashboard_users_validation_errors(self):
        with self.assertRaises(InvalidDataException, msg="get dashboard users : validation errors"):
            self.__dashboard.get_dashboard_users(dashboard_id="123")

    def test_18_remove_shared_dashboard(self):
        result = self.__dashboard.remove_shared_dashboard(shared_id=1)
        self.assertIsInstance(result, list, msg="remove shared dashboard : check instance")

    def test_18_remove_shared_dashboard_required_params(self):
        with self.assertRaises(TypeError, msg="remove shared dashboard : required params"):
            self.__dashboard.remove_shared_dashboard()

    def test_18_remove_shared_dashboard_validation_errors(self):
        with self.assertRaises(TypeError, msg="remove shared dashboard : validation errors"):
            self.__dashboard.remove_shared_dashboard(shared_id="123")

    def test_19_get_shared_dashboards(self):
        result = self.__dashboard.get_shared_dashboards()
        self.assertIsInstance(result, dict, msg="get shared dashboards : check instance")

    def test_19_get_shared_dashboards_all_params(self):
        result = self.__dashboard.get_shared_dashboards(page=0, size=10)
        self.assertIsInstance(result, dict, msg="get shared dashboards (all params) : check instance")

    def test_19_get_shared_dashboards_validation_errors(self):
        with self.assertRaises(InvalidDataException, msg="get shared dashboards : validation errors"):
            self.__dashboard.get_shared_dashboards(page="0", size="10")

    def test_20_update_shared_dashboard(self):
        dashboards = self.__dashboard.get_shared_dashboards()
        if dashboards["totalSize"] < 1:
            self.skipTest("update shared dashboard : empty shared dashboards")
        config = {
            "layout": [{
                "w": 20,
                "h": 43,
                "x": 0,
                "y": 0,
                "moved": False,
                "static": True
            }]
        }
        try:
            result = self.__dashboard.update_shared_dashboard(dashboard_id=dashboards["data"][0]["id"], config=config,
                                                              order=2)
            self.assertIsInstance(result, list, msg="update shared dashboard : check instance")
        except DashboardException as e:
            self.assertEqual(e.code, 105, msg="update shared dashboard : update access denied")

    def test_20_update_shared_dashboard_required_params(self):
        with self.assertRaises(TypeError, msg="update shared dashboard : required params"):
            self.__dashboard.update_shared_dashboard()

    def test_20_update_shared_dashboard_validation_errors(self):
        with self.assertRaises(InvalidDataException, msg="update shared dashboard : validation errors"):
            self.__dashboard.update_shared_dashboard(dashboard_id="123", order="5", config="test")

    def test_21_add_user_collaborator(self):
        try:
            result = self.__dashboard.add_user_collaborator(report_id=180, identity=IDENTITY)
            self.assertIsInstance(result, dict, msg="add user collaborator : check instance")
        except DashboardException as e:
            self.assertEqual(e.code, 105, msg="add user collaborator : access denied")

    def test_21_add_user_collaborator_required_params(self):
        with self.assertRaises(TypeError, msg="add user collaborator : required params"):
            self.__dashboard.add_user_collaborator()

    def test_21_add_user_collaborator_validation_errors(self):
        with self.assertRaises(InvalidDataException, msg="add user collaborator : validation errors"):
            self.__dashboard.add_user_collaborator(report_id="13", identity=123)

    def test_22_get_user_collaborators(self):
        try:
            result = self.__dashboard.get_user_collaborators(report_id=180)
            self.assertIsInstance(result, list, msg="get user collaborators : check instance")
        except DashboardException as e:
            self.assertEqual(e.code, 105, msg="get user collaborators : access denied")

    def test_22_get_user_collaborators_required_params(self):
        with self.assertRaises(InvalidDataException, msg="get user collaborators : required params"):
            self.__dashboard.get_user_collaborators()

    def test_22_get_user_collaborators_validation_errors(self):
        with self.assertRaises(InvalidDataException, msg="get user collaborators : validation errors"):
            self.__dashboard.get_user_collaborators(report_id="12345")

    def test_23_remove_collaborator(self):
        try:
            result = self.__dashboard.remove_collaborator(report_id=180, user_id=123)
            self.assertIsInstance(result, dict, msg="remove collaborator : check instance")
        except DashboardException as e:
            self.assertEqual(e.code, 105, msg="remove collaborator : access denied")

    def test_23_remove_collaborator_required_params(self):
        with self.assertRaises(TypeError, msg="remove collaborator : required params"):
            self.__dashboard.remove_collaborator()

    def test_23_remove_collaborator_validation_errors(self):
        with self.assertRaises(InvalidDataException, msg="remove collaborator : validation errors"):
            self.__dashboard.remove_collaborator(report_id="123", user_id="123")

    def test_24_get_user_report_hash(self):
        user_reports = self.__dashboard.get_all_user_reports()
        if user_reports["totalSize"] < 0:
            self.skipTest("get user report hash : empty user reports")

        result = self.__dashboard.get_user_report_hash(user_report_id=user_reports["data"][0]["id"])
        self.assertIsInstance(result, str, msg="get user report hash : check instance")

    def test_24_get_user_report_hash_required_params(self):
        with self.assertRaises(TypeError, msg="get user report hash : required params"):
            self.__dashboard.get_user_report_hash()

    def test_24_get_user_report_hash_validation_errors(self):
        with self.assertRaises(InvalidDataException, msg="get user report hash : validation errors"):
            self.__dashboard.get_user_report_hash(user_report_id="123")

    def test_25_get_public_user_report(self):
        user_reports = self.__dashboard.get_all_user_reports()
        if user_reports["totalSize"] < 0:
            self.skipTest("get public user report : empty user reports")

        user_report_id = user_reports["data"][0]["id"]
        user_report_hash = self.__dashboard.get_user_report_hash(user_report_id=user_report_id)

        result = self.__dashboard.get_public_user_report(user_report_id=user_report_id, user_report_hash=user_report_hash)
        self.assertIsInstance(result, dict, msg="get public user report : check instance")

    def test_25_get_public_user_report_required_params(self):
        with self.assertRaises(TypeError, msg="get public user report : required params"):
            self.__dashboard.get_public_user_report()

    def test_25_get_public_user_report_validation_errors(self):
        with self.assertRaises(InvalidDataException, msg="get public user report : validation errors"):
            self.__dashboard.get_public_user_report(user_report_id="123", user_report_hash=123456)

    def test_26_public_execute(self):
        user_reports = self.__dashboard.get_all_user_reports()
        if user_reports["totalSize"] < 0:
            self.skipTest("public execute : empty user reports")

        user_report_id = user_reports["data"][0]["id"]
        user_report_hash = self.__dashboard.get_user_report_hash(user_report_id=user_report_id)

        result = self.__dashboard.public_execute(user_report_id=user_report_id, user_report_hash=user_report_hash,
                                                 page=0, size=10, load_from_cache=False, execute_params={})
        self.assertIsInstance(result, dict, msg="public execute : check instance")

    def test_26_public_execute_required_params(self):
        with self.assertRaises(TypeError, msg="public execute : required params"):
            self.__dashboard.public_execute()

    def test_26_public_execute_validation_errors(self):
        with self.assertRaises(InvalidDataException, msg="public execute : validation errors"):
            self.__dashboard.public_execute(user_report_id="123", user_report_hash=123, page="0", size="10",
                                            load_from_cache="False", execute_params="{}")
