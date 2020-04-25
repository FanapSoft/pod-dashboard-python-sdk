# coding=utf-8
from __future__ import unicode_literals

import json

from pod_base import APIException, PodException
from examples.config import *
from pod_dashboard import PodDashboard, DashboardException

try:
    pod_dashboard = PodDashboard(api_token=API_TOKEN, server_type=SERVER_MODE)
    user_report_hash = "0a59b4c32768be2248a0181c2ec8e43e4755d43144e453f8bd6ce289eae54749"
    print(pod_dashboard.public_execute(user_report_id=715, user_report_hash=user_report_hash))

    # OUTPUT
    # {
    #   "cols": [
    #     {
    #       "index": 1,
    #       "key": "نوع عملیات",
    #       "type": "VARCHAR2"
    #     },
    #     {
    #       "index": 2,
    #       "key": "تعداد",
    #       "type": "NUMBER"
    #     }
    #   ],
    #   "rows": [
    #     {
    #       "cols": [
    #         "EDIT",
    #         329
    #       ]
    #     },
    #     {
    #       "cols": [
    #         "PUBLIC",
    #         239
    #       ]
    #     },
    #     {
    #       "cols": [
    #         "UNSHARE",
    #         12
    #       ]
    #     },
    #     {
    #       "cols": [
    #         "MOVE",
    #         66
    #       ]
    #     },
    #     {
    #       "cols": [
    #         "SHARE",
    #         93
    #       ]
    #     },
    #     {
    #       "cols": [
    #         "DOWNLOAD",
    #         78560
    #       ]
    #     },
    #     {
    #       "cols": [
    #         "UPLOAD",
    #         11950
    #       ]
    #     },
    #     {
    #       "cols": [
    #         "WIPE",
    #         24
    #       ]
    #     },
    #     {
    #       "cols": [
    #         "EDIT",
    #         54
    #       ]
    #     },
    #     {
    #       "cols": [
    #         "TRASH",
    #         1541
    #       ]
    #     }
    #   ],
    #   "totalCount": 24
    # }

    # print(pod_dashboard.raw_response())

except DashboardException as e:
    print("Dashboard Exception :", e)

except APIException as e:
    print("API Exception\nError {}\nError Code : {}\nReference Number : {}".format(e.message, e.error_code,
                                                                                   e.reference_number))
except PodException as e:
    print("Pod Exception: ", e.message)
