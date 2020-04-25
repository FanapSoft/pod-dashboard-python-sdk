# coding=utf-8
from __future__ import unicode_literals

import json

from pod_base import APIException, PodException
from examples.config import *
from pod_dashboard import PodDashboard, DashboardException

try:
    pod_dashboard = PodDashboard(api_token=API_TOKEN, server_type=SERVER_MODE)
    print(pod_dashboard.remove_user_report(user_report_id=705))

    # OUTPUT
    # {
    #   "dashboardId": 335,
    #   "drillDownId": 716,
    #   "id": 715,
    #   "report": {
    #     "config": "{\"refreshInterval\":0,\"options\":{\"title\":{\"show\":True,\"text\":\"تست - نوع عملیات روی...}",
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
