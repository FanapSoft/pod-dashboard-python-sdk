# coding=utf-8
from __future__ import unicode_literals

import json

from pod_base import APIException, PodException
from examples.config import *
from pod_dashboard import PodDashboard, DashboardException

try:
    pod_dashboard = PodDashboard(api_token=API_TOKEN, server_type=SERVER_MODE)
    # print(pod_dashboard.get_all_collaborator_reports(name="نسبت"))
    print(pod_dashboard.get_all_collaborator_reports())

    # OUTPUT
    # {
    #   "currentPage": 0,
    #   "data": [
    #     {
    #       "canGiveAccess": True,
    #       "config": "{\"refreshInterval\":0}",
    #       "created": "2019-09-03T10:18:39.967Z[UTC]",
    #       "drillDownId": -1,
    #       "id": 42,
    #       "name": "گزارش های POD Space - نسبت دانلود به اپلود فایل",
    #       "publicized": False,
    #       "query": {
    #         "dataSource": {
    #           "id": 0,
    #           "type": "SQL"
    #         },
    #         "metadata": "{\"default_order\":\"\",\"template\":\"\"}",
    #         "queryFilters": [],
    #         "queryParams": []
    #       },
    #       "type": "SCALAR",
    #       "updated": "2019-12-10T07:49:20.268Z[UTC]"
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
