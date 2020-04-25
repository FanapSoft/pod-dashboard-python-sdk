# coding=utf-8
from __future__ import unicode_literals

import json

from pod_base import APIException, PodException
from examples.config import *
from pod_dashboard import PodDashboard, DashboardException

try:
    pod_dashboard = PodDashboard(api_token=API_TOKEN, server_type=SERVER_MODE)
    print(pod_dashboard.get_all_user_reports())

    # OUTPUT
    # {
    #   "currentPage": 0,
    #   "data": [
    #     {
    #       "dashboardId": 335,
    #       "id": 705,
    #       "name": "گزارش پایتونی",
    #       "report": {
    #         "config": "{\"refreshInterval\":0}",
    #         "created": "2019-09-03T10:22:41.934Z[UTC]",
    #         "drillDownId": -1,
    #         "id": 45,
    #         "name": "گزارش های POD Space - مجموع حجم فایل های موجود",
    #         "publicized": False,
    #         "query": {
    #           "dataSource": {
    #             "id": 0,
    #             "type": "SQL"
    #           },
    #           "metadata": "{\"default_order\":\"\",\"template\":\"\"}",
    #           "queryFilters": [],
    #           "queryParams": []
    #         },
    #         "type": "SCALAR",
    #         "updated": "2019-12-10T08:02:22.032Z[UTC]"
    #       },
    #       "userPodParams": []
    #     }
    #   ],
    #   "endIndex": 1,
    #   "hasNextPage": False,
    #   "startIndex": 0,
    #   "totalPages": 1,
    #   "totalSize": 1
    # }

    # print(pod_dashboard.raw_response())

except DashboardException as e:
    print("Dashboard Exception :", e)

except APIException as e:
    print("API Exception\nError {}\nError Code : {}\nReference Number : {}".format(e.message, e.error_code,
                                                                                   e.reference_number))
except PodException as e:
    print("Pod Exception: ", e.message)
