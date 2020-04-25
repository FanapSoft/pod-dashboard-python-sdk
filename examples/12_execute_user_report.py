# coding=utf-8
from __future__ import unicode_literals

import json

from pod_base import APIException, PodException
from examples.config import *
from pod_dashboard import PodDashboard, DashboardException

try:
    pod_dashboard = PodDashboard(api_token=API_TOKEN, server_type=SERVER_MODE)
    print(pod_dashboard.execute_user_report(user_report_id=715))

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
    #     ...
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
