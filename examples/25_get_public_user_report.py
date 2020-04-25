# coding=utf-8
from __future__ import unicode_literals

import json

from pod_base import APIException, PodException
from examples.config import *
from pod_dashboard import PodDashboard, DashboardException

try:
    pod_dashboard = PodDashboard(api_token=API_TOKEN, server_type=SERVER_MODE)
    user_report_hash = "0a59b4c32768be2248a0181c2ec8e43e4755d43144e453f8bd6ce289eae54749"
    print(pod_dashboard.get_public_user_report(user_report_id=715, user_report_hash=user_report_hash))

    # OUTPUT
    # {
    #   "dashboardId": 335,
    #   "drillDownId": 716,
    #   "id": 715,
    #   "report": {
    #     "config": "{\"refreshInterval\":0,\"options\":{\"title\":{\"show\":True,\"text\":\"تست - ن...}}",
    #     "created": "2020-01-20T12:39:00.867Z[UTC]",
    #     "drillDownId": 181,
    #     "id": 180,
    #     "name": "تست - نوع عملیات روی فایل ها",
    #     "publicized": False,
    #     "query": {
    #       "dataSource": {
    #         "id": 0,
    #         "type": "SQL"
    #       },
    #       "metadata": "{\"default_order\":\"\",\"template\":\"\"}",
    #       "queryFilters": [],
    #       "queryParams": []
    #     },
    #     "type": "PIE",
    #     "updated": "2020-01-21T08:23:16.736Z[UTC]"
    #   },
    #   "userPodParams": []
    # }

    # print(pod_dashboard.raw_response())

except DashboardException as e:
    print("Dashboard Exception :", e)

except APIException as e:
    print("API Exception\nError {}\nError Code : {}\nReference Number : {}".format(e.message, e.error_code,
                                                                                   e.reference_number))
except PodException as e:
    print("Pod Exception: ", e.message)
