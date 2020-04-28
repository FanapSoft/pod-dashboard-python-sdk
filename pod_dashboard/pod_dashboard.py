# coding=utf-8
from __future__ import unicode_literals

import json
from os import path
from sys import version_info

from pod_base import PodBase, ConfigException

from .exceptions import DashboardException

try:
    import urllib.parse as urllib
except ImportError:
    import urllib


class PodDashboard(PodBase):
    __slots__ = "__raw_response"

    def __init__(self, api_token, token_issuer="1", server_type="sandbox", config_path=None,
                 sc_api_key="", sc_voucher_hash=None):
        here = path.abspath(path.dirname(__file__))
        self.__raw_response = None
        self._services_file_path = path.join(here, "services.json")
        super(PodDashboard, self).__init__(api_token, token_issuer, server_type, config_path, sc_api_key,
                                           sc_voucher_hash, path.join(here, "json_schema.json"))

    def __get_private_call_address(self):
        """
        دریافت آدرس سرور پرداخت از فایل کانفیگ

        :return: str
        :raises: :class:`ConfigException`
        """
        private_call_address = self.config.get("private_call_address", self._server_type)
        if private_call_address:
            return private_call_address

        raise ConfigException("config `private_call_address` in {} not found".format(self._server_type))

    def _get_headers(self):
        headers = super(PodDashboard, self)._get_headers()
        headers["token"] = self._api_token
        return headers

    def create_dashboard(self, name, order=None, config=None, **kwargs):
        """
        ایجاد داشبورد

        :param str name: نام
        :param int|None order: مکان قرارگیری میان لیست داشبوردها
        :param dict|None config: تنظیمات داشبورد

        :return: int
        """
        data = {
            "name": name
        }
        if order is not None:
            data["order"] = order
        if config is not None:
            data["config"] = config

        self._validate(data, "createDashboard")
        if config is not None:
            data["config"] = json.dumps(config)

        data = {
            "content": json.dumps(data)
        }
        return self.__parse_response(self._request.call(
            super(PodDashboard, self)._get_sc_product_settings("/v1/dashboard", method_type="post"), params=data,
            headers=self._get_headers(), internal=False, **kwargs))

    def get_user_dashboards(self, page=0, size=10, **kwargs):
        """
        لیست داشبوردهای کاربر

        :param int page: شماره صفحه
        :param int size: تعداد رکورد در هر صفحه
        :return: dict
        """
        kwargs["page"] = page
        kwargs["size"] = size
        self._validate(kwargs, "getUserDashboards")
        return self.__parse_response(self._request.call(
            super(PodDashboard, self)._get_sc_product_settings("/v1/dashboard"), params=kwargs,
            headers=self._get_headers(), internal=False, **kwargs))

    def get_all_dashboards(self, **kwargs):
        """
        تمام داشبوردهای قابل مشاهده توسط کاربر
        :return: dict
        """

        self._validate(kwargs, "getAllDashboards")
        return self.__parse_response(self._request.call(
            super(PodDashboard, self)._get_sc_product_settings("/v1/dashboard/all"), params=kwargs,
            headers=self._get_headers(), internal=False, **kwargs))

    def update_dashboard(self, dashboard_id, name, order=None, config=None, **kwargs):
        """
        ویرایش داشبورد

        :param int dashboard_id: شناسه داشبورد
        :param str name: نام
        :param int|None order: مکان قرارگیری میان لیست داشبوردها
        :param dict|None config: تنظیمات داشبورد

        :return: int
        """
        data = {
            "name": name,
            "dashboard_id": dashboard_id
        }

        if order is not None:
            data["order"] = order
        if config is not None:
            data["config"] = config

        self._validate(data, "updateDashboard")
        if config is not None:
            data["config"] = json.dumps(config)

        del data["dashboard_id"]

        data = {
            "content": json.dumps(data),
            "id": dashboard_id
        }
        return self.__parse_response(self._request.call(
            super(PodDashboard, self)._get_sc_product_settings("/v1/dashboard", method_type="put"), params=data,
            headers=self._get_headers(), internal=False, **kwargs))

    def remove_dashboard(self, dashboard_id, **kwargs):
        """
        حذف داشبورد

        :param int dashboard_id: شناسه داشبورد

        :return: int
        """
        self._validate({"dashboard_id": dashboard_id}, "removeDashboard")

        data = {
            "id": dashboard_id
        }
        return self.__parse_response(self._request.call(
            super(PodDashboard, self)._get_sc_product_settings("/v1/dashboard", method_type="delete"), params=data,
            headers=self._get_headers(), internal=False, **kwargs))

    def get_all_collaborator_reports(self, name=None, page=0, size=10, **kwargs):
        """
        مشاهده همه گزارشات در دسترس

        :param str|None name: نام گزارش
        :param int page: شماره صفحه
        :param int size: تعداد رکورد در هر صفحه
        :return: dict
        """
        kwargs["page"] = page
        kwargs["size"] = size
        kwargs["name"] = name
        kwargs = self.__remove_empty_items(kwargs)
        self._validate(kwargs, "getAllCollaboratorReports")
        return self.__parse_response(self._request.call(
            super(PodDashboard, self)._get_sc_product_settings("/v1/report/CollaboratorReports"), params=kwargs,
            headers=self._get_headers(), internal=False, **kwargs))

    def get_collaborator_report(self, report_id, **kwargs):
        """
        مشاهده یک گزارش در دسترس با شناسه

        :param int report_id: شناسه گزارش
        :return: dict
        """

        self._validate({"report_id": report_id}, "getCollaboratorReport")
        kwargs["id"] = report_id
        return self.__parse_response(self._request.call(
            super(PodDashboard, self)._get_sc_product_settings("/v1/report/CollaboratorReport/{id}"), params=kwargs,
            headers=self._get_headers(), internal=False, **kwargs))

    def add_user_param(self, report_id, dashboard_id, name=None, params=None, **kwargs):
        """
        ایجاد یک نمونه از گزارش در داشبورد کاربر

        :param int report_id: شناسه گزارش
        :param int dashboard_id: شناسه داشبورد
        :param str|None name: نام
        :param list|None params: لیست پارامترهای گزارش

        :return: int
        """

        if name is None:
            name = ""

        if params is None:
            params = []

        data = {
            "report_id": report_id,
            "dashboard_id": dashboard_id,
            "name": name,
            "params": params
        }

        self._validate(data, "addUserParam")

        if version_info[0] == 2:
            name = urllib.quote(name.encode("utf-8"))
        else:
            name = urllib.quote(name)

        data = {
            "id": report_id,
            "dashboardId": dashboard_id,
            "name": name,
            "content": json.dumps(params)
        }

        return self.__parse_response(self._request.call(
            super(PodDashboard, self)._get_sc_product_settings("/v1/report/{id}/param", method_type="post"),
            params=data, headers=self._get_headers(), internal=False, **kwargs))

    def add_drill_down_user_param(self, report_id, user_report_id, params=None, **kwargs):
        """
        ایجاد یک نمونه از زیر گزارش

        :param int report_id: شناسه گزارش
        :param int user_report_id: شناسه گزارش کاربر
        :param list|None params: لیست پارامترهای گزارش

        :return: int
        """

        if params is None:
            params = []

        data = {
            "report_id": report_id,
            "user_report_id": user_report_id,
            "params": params
        }

        self._validate(data, "addDrillDownUserParam")

        data = {
            "id": report_id,
            "userReportId": user_report_id,
            "content": json.dumps(params)
        }

        return self.__parse_response(self._request.call(
            super(PodDashboard, self)._get_sc_product_settings("/v1/report/{id}/userreport/{userReportId}/param",
                                                               method_type="post"),
            params=data, headers=self._get_headers(), internal=False, **kwargs))

    def get_all_user_reports(self, page=0, size=10, **kwargs):
        """
        مشاهده همه گزارش های کاربر

        :param int page: شماره صفحه
        :param int size: تعداد رکورد در هر صفحه
        :return: dict
        """
        kwargs["page"] = page
        kwargs["size"] = size

        self._validate(kwargs, "getAllUserReports")
        return self.__parse_response(self._request.call(
            super(PodDashboard, self)._get_sc_product_settings("/v1/userreport"), params=kwargs,
            headers=self._get_headers(), internal=False, **kwargs))

    def get_user_report(self, user_report_id, **kwargs):
        """
        مشاهده گزارش کاربر با شناسه

        :param int user_report_id: شماره گزارش کاربر
        :return: dict
        """
        kwargs["id"] = user_report_id

        self._validate({"user_report_id": user_report_id}, "getUserReport")
        return self.__parse_response(self._request.call(
            super(PodDashboard, self)._get_sc_product_settings("/v1/userreport/{id}"), params=kwargs,
            headers=self._get_headers(), internal=False, **kwargs))

    def execute_user_report(self, user_report_id, page=0, size=10, load_from_cache=False, execute_params=None,
                            **kwargs):
        """
        اجرای گزارش کاربر

        :param int user_report_id: شماره گزارش کاربر
        :param int page: شماره صفحه
        :param int size: تعداد رکورد برگشتی
        :param bool load_from_cache: خروجی از کش بارگذاری شود یا مجددا کوئری اجرا شود؟
        :param dict|None execute_params: اطلاعات لازم برای اجرای گزارش
        :return: dict
        """
        kwargs["user_report_id"] = user_report_id
        kwargs["userReportId"] = user_report_id
        kwargs["loadFromCache"] = load_from_cache
        kwargs["execute_params"] = execute_params
        kwargs["page"] = page
        kwargs["size"] = size
        return self.__execute_user_report(url="exec", schema_name="executeUserReport", **kwargs)

    def get_xls(self, user_report_id, page=0, size=10, callback_url=None, force_save=False, execute_params=None,
                save_to=None, **kwargs):
        """
        دریافت خروجی اکسل گزارش

        :param int user_report_id: شماره گزارش کاربر
        :param int page: شماره صفحه
        :param int size: تعداد رکورد برگشتی
        :param str callback_url: آدرس کال بک، این آدرس پس از ایجاد خروجی فراخوانی می شود
        :param bool force_save: آیا خروجی حتما در پاد اسپیس ذخیره شود؟
        :param dict execute_params: اطلاعات لازم برای اجرای گزارش
        :param str save_to: آدرس محل ذخیره سازی خروجی
        :return: str|bool
        """
        kwargs["forceSave"] = force_save
        kwargs["callbackUrl"] = callback_url
        kwargs["user_report_id"] = user_report_id
        kwargs["id"] = user_report_id
        kwargs["execute_params"] = execute_params
        kwargs["page"] = page
        kwargs["size"] = size
        result = self.__execute_user_report(url="getXLS", schema_name="getExcelUserReport", is_stream=True, **kwargs)

        if save_to is None:
            return result

        with open(save_to, "w") as f:
            f.write(result)

        return True

    def get_csv(self, user_report_id, page=0, size=10, callback_url=None, force_save=False, execute_params=None,
                save_to=None, **kwargs):
        """
        دریافت خروجی csv گزارش

        :param int user_report_id: شماره گزارش کاربر
        :param int page: شماره صفحه
        :param int size: تعداد رکورد برگشتی
        :param str callback_url: آدرس کال بک، این آدرس پس از ایجاد خروجی فراخوانی می شود
        :param bool force_save: آیا خروجی حتما در پاد اسپیس ذخیره شود؟
        :param dict execute_params: اطلاعات لازم برای اجرای گزارش
        :param str save_to: آدرس محل ذخیره سازی خروجی
        :return: str|bool
        """
        kwargs["forceSave"] = force_save
        kwargs["callbackUrl"] = callback_url
        kwargs["user_report_id"] = user_report_id
        kwargs["id"] = user_report_id
        kwargs["execute_params"] = execute_params
        kwargs["page"] = page
        kwargs["size"] = size
        result = self.__execute_user_report(url="getCSV", schema_name="getCSVUserReport", is_stream=True, **kwargs)

        if save_to is None:
            return result

        with open(save_to, "w") as f:
            f.write(result)

        return True

    def __execute_user_report(self, url, schema_name, execute_params=None, is_stream=False, **kwargs):
        """
        مشاهده گزارش کاربر با شناسه

        :param str url: آدرس سرویس
        :param str schema_name: نام اسکیما اعتبارسنجی
        :param dict|None execute_params: اطلاعات لازم برای اجرای گزارش
        :param bool is_stream: آیا خروجی به صورت استریم است؟
        :return: dict
        """
        if execute_params is None or execute_params == {}:
            execute_params = self.__default_params()

        self._validate(kwargs, schema_name=schema_name)

        kwargs["content"] = json.dumps(execute_params)

        return self.__parse_response(
            self._request.call(super(PodDashboard, self)._get_sc_product_settings("/v1/userreport/{userReportId}/"+url,
                                                                                  method_type="post"),
                               params=kwargs, headers=self._get_headers(), internal=False, **kwargs),
            is_stream=is_stream)

    @staticmethod
    def __default_params():
        return {
            "filterVOS": [],
            "parentParams": [],
            "orderByElementVOS": [],
        }

    def get_user_report_hash(self, user_report_id, **kwargs):
        """
        دریافت هش گزارش کاربر

        :param int user_report_id: شماره گزارش کاربر
        :return: str
        """
        kwargs["id"] = user_report_id

        self._validate({"user_report_id": user_report_id}, "getUserReportHash")
        return self.__parse_response(self._request.call(
            super(PodDashboard, self)._get_sc_product_settings("/v1/userreport/{id}/hash"), params=kwargs,
            headers=self._get_headers(), internal=False, **kwargs))

    def get_public_user_report(self, user_report_id, user_report_hash, **kwargs):
        """
        مشاهده گزارش عمومی (مشاهده گزارش با هش)

        :param int user_report_id: شماره گزارش کاربر
        :param str user_report_hash: هش گزارش
        :return: dict
        """
        kwargs["id"] = user_report_id
        kwargs["hash"] = user_report_hash

        self._validate({"user_report_id": user_report_id, "hash": user_report_hash}, "getPublicUserReport")
        return self.__parse_response(self._request.call(
            super(PodDashboard, self)._get_sc_product_settings("/v1/userreport/{id}/publicGet"), params=kwargs,
            headers=self._get_headers(), internal=False, **kwargs))

    def public_execute(self, user_report_id, user_report_hash, page=0, size=10, load_from_cache=False,
                       execute_params=None, **kwargs):
        """
        اجرای گزارش عمومی (اجرای گزارش با هش)

        :param int user_report_id: شماره گزارش کاربر
        :param str user_report_hash: هش گزارش
        :param int page: شماره صفحه
        :param int size: تعداد رکورد در هر خروجی
        :param bool load_from_cache: آیا خروجی از کش لود شود؟
        :param dict execute_params: پارامترهای لازم برای اجرای گزارش
        :return: dict
        """
        kwargs["user_report_id"] = user_report_id
        kwargs["hash"] = user_report_hash
        kwargs["page"] = page
        kwargs["size"] = size
        kwargs["load_from_cache"] = load_from_cache
        kwargs["execute_params"] = execute_params

        self._validate(kwargs, "publicExecute")

        if execute_params is None or execute_params == {}:
            execute_params = self.__default_params()

        data = {
            "userReportId": user_report_id,
            "hash": user_report_hash,
            "page": page,
            "size": size,
            "loadFromCache": load_from_cache,
            "content": json.dumps(execute_params)
        }
        return self.__parse_response(self._request.call(
            super(PodDashboard, self)._get_sc_product_settings("/v1/userreport/{userReportId}/publicExec"),
            params=data, headers=self._get_headers(), internal=False, **kwargs))

    def remove_user_report(self, user_report_id, **kwargs):
        """
        حذف گزارش کاربر

        :param int user_report_id: شماره گزارش کاربر
        :return: int
        """
        kwargs["id"] = user_report_id

        self._validate({"user_report_id": user_report_id}, "removeUserReport")
        return self.__parse_response(self._request.call(
            super(PodDashboard, self)._get_sc_product_settings("/v1/userreport/{id}", method_type="delete"),
            params=kwargs, headers=self._get_headers(), internal=False, **kwargs))

    def share_dashboard(self, dashboard_id, identity, expire, edit_access_level, share_access_level, **kwargs):
        """
        اشتراک گذاری داشبورد

        :param int dashboard_id: شماره داشبورد
        :param str|list identity: نام کاربری، ایمیل و یا تلفن همراه کاربرانی که داشبورد با آن ها به اشتراک گذاشته می شود
        :param str expire: تاریخ اتمام اشتراک گذاری
        :param str edit_access_level: سطح دسترسی برای ویرایش داشبورد
        :param str share_access_level: سطح دسترسی برای اشتراک گذاری
        :return: dict
        """
        kwargs["dashboard_id"] = dashboard_id
        kwargs["identity"] = identity
        kwargs["expire"] = expire
        kwargs["edit_access_level"] = edit_access_level
        kwargs["share_access_level"] = share_access_level

        self._validate(kwargs, "shareDashboard")
        data = {
            "id": dashboard_id,
            "identity": identity,
            "editAccessLevel": edit_access_level,
            "shareAccessLevel": share_access_level,
            "expire": expire
        }
        return self.__parse_response(self._request.call(
            super(PodDashboard, self)._get_sc_product_settings("/v1/dashboard/{dashboardId}/share"), params=data,
            headers=self._get_headers(), internal=False, **kwargs))

    def get_dashboard_users(self, dashboard_id, **kwargs):
        """
        مشاهده افرادی که داشبورد با آن ها اشتراک گذاری شده

        :param int dashboard_id: شماره داشبورد
        :return: dict
        """
        kwargs["id"] = dashboard_id

        self._validate({"dashboard_id": dashboard_id}, "getDashboardUsers")

        return self.__parse_response(self._request.call(
            super(PodDashboard, self)._get_sc_product_settings("/v1/dashboard/{id}/users"), params=kwargs,
            headers=self._get_headers(), internal=False, **kwargs))

    def remove_shared_dashboard(self, shared_id, **kwargs):
        """
        لغو اشتراک گذاری داشبورد

        :param int shared_id: شناسه اشتراک
        :return: dict
        """
        kwargs["id"] = shared_id
        self._validate(kwargs, "removeSharedDashboard")
        return self.__parse_response(self._request.call(
            super(PodDashboard, self)._get_sc_product_settings("/v1/dashboard/shared/{id}", method_type="delete"),
            params=kwargs, headers=self._get_headers(), internal=False, **kwargs))

    def get_shared_dashboards(self, page=0, size=10, **kwargs):
        """
        مشاهده داشبوردهای به اشتراک گذاشته شده با کاربر

        :param int page: شماره صفحه
        :param int size: تعداد رکورد در هر صفحه
        :return: dict
        """
        kwargs["page"] = page
        kwargs["size"] = size

        self._validate(kwargs, "getSharedDashboards")

        return self.__parse_response(self._request.call(
            super(PodDashboard, self)._get_sc_product_settings("/v1/dashboard/shared"), params=kwargs,
            headers=self._get_headers(), internal=False, **kwargs))

    def update_shared_dashboard(self, dashboard_id, config, order=None, **kwargs):
        """
        تغییر داشبورد اشتراک گذاری شده با کاربر

        :param int dashboard_id: شناسه داشبورد
        :param dict config: تنظیمات داشبورد
        :param int order: مکان قرارگیری میان لیست داشبوردها
        :return: int
        """

        self._validate({
            "dashboard_id": dashboard_id,
            "config": config,
            "order": order
        }, "updateSharedDashboard")

        data = {
            "id": dashboard_id,
            "content": json.dumps({
                "config": config,
                "order": order
            })
        }

        return self.__parse_response(self._request.call(
            super(PodDashboard, self)._get_sc_product_settings("/v1/dashboard/shared/{id}", method_type="put"),
            params=data, headers=self._get_headers(), internal=False, **kwargs))

    def add_user_collaborator(self, report_id, identity, **kwargs):
        """
        مشاهده داشبوردهای به اشتراک گذاشته شده با کاربر

        :param int report_id: شناسه گزارش
        :param str identity: نام کاربری، ایمیل و یا تلفن همراه کاربرانی که داشبورد با آن ها به اشتراک گذاشته می شود
        :return: dict
        """
        kwargs["id"] = report_id
        kwargs["identity"] = identity

        self._validate({"report_id": report_id, "identity": identity}, "addUserCollaborator")

        return self.__parse_response(self._request.call(
            super(PodDashboard, self)._get_sc_product_settings("/v1/report/{id}/addUser"), params=kwargs,
            headers=self._get_headers(), internal=False, **kwargs))

    def get_user_collaborators(self, report_id, **kwargs):
        """
        مشاهده افرادی که به یک گزارش دسترسی دارند

        :param int report_id: شناسه گزارش

        :return: dict
        """
        kwargs["id"] = report_id

        self._validate({"report_id": report_id}, "getUserCollaborators")

        return self.__parse_response(self._request.call(
            super(PodDashboard, self)._get_sc_product_settings("/v1/report/{id}/users"), params=kwargs,
            headers=self._get_headers(), internal=False, **kwargs))

    def remove_collaborator(self, report_id, user_id, **kwargs):
        """
        لغو دسترسی کاربر به یک گزارش

        :param int report_id: شناسه گزارش
        :param int user_id: شناسه کاربر
        :return: int
        """
        kwargs["id"] = report_id
        kwargs["userId"] = user_id

        self._validate({
            "report_id": report_id,
            "user_id": user_id
        }, "removeCollaborator")

        return self.__parse_response(self._request.call(
            super(PodDashboard, self)._get_sc_product_settings("/v1/report/{id}/removeUser", method_type="delete"),
            params=kwargs, headers=self._get_headers(), internal=False, **kwargs))

    @staticmethod
    def __convert_list_to_str(items, index, delimiter=","):
        if index in items:
            items[index] = [str(val) for val in items[index]]
            return delimiter.join(items[index])
        return ""

    @staticmethod
    def __remove_empty_items(items):
        return {key: value for key, value in items.items() if value != "" and value is not None and value != {}}

    def raw_response(self):
        """
        جواب دریافتی از سرور داشبورد

        :return: dict
        """
        return self.__raw_response

    def __parse_response(self, raw_response, is_stream=False):
        if is_stream:
            self.__raw_response = {
                "content": raw_response,
                "is_stream": True
            }

            return raw_response

        self.__raw_response = json.loads(raw_response)
        if "code" in self.__raw_response:
            if self.__raw_response["code"] == 200:
                return self.__raw_response["result"]

        data = self.__raw_response
        data["reference_number"] = self._request._reference_number
        data["error_code"] = self._request.error_code

        raise DashboardException(**data)
