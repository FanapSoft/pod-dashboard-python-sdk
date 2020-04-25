# coding=utf-8
from __future__ import unicode_literals
from pod_base import APIException, PodException
from examples.config import *
from pod_dashboard import PodDashboard, DashboardException

try:
    pod_dashboard = PodDashboard(api_token=API_TOKEN, server_type=SERVER_MODE)

    print(pod_dashboard.get_all_dashboards())
    # OUTPUT
    # {
    #   "currentPage": 0,
    #   "data": [
    #     {
    #       "id": 128,
    #       "name": "dashboard 1",
    #       "order": 0,
    #       "shared": False
    #     },
    #     {
    #       "id": 132,
    #       "name": "my dashboard",
    #       "order": 2,
    #       "shared": False
    #     },
    #     {
    #       "id": 133,
    #       "name": "my dashboard",
    #       "order": 2,
    #       "shared": False
    #     },
    #     {
    #       "id": 134,
    #       "name": "testDashboard",
    #       "shared": False
    #     },
    #     {
    #       "id": 335,
    #       "name": "PyDashboard",
    #       "shared": False
    #     }
    #   ],
    #   "endIndex": 5,
    #   "hasNextPage": False,
    #   "startIndex": 0,
    #   "totalPages": 1,
    #   "totalSize": 5
    # }

    # print(pod_dashboard.raw_response())

except DashboardException as e:
    print("Dashboard Exception :", e)

except APIException as e:
    print("API Exception\nError {}\nError Code : {}\nReference Number : {}".format(e.message, e.error_code,
                                                                                   e.reference_number))
except PodException as e:
    print("Pod Exception: ", e.message)
