# coding=utf-8
from __future__ import unicode_literals

from pod_base import APIException, PodException
from examples.config import *
from pod_dashboard import PodDashboard, DashboardException

try:
    pod_dashboard = PodDashboard(api_token=API_TOKEN, server_type=SERVER_MODE)
    print(pod_dashboard.get_shared_dashboards())

    # OUTPUT
    # {
    #   "currentPage": 0,
    #   "data": [
    #     {
    #       "actualDashboardId": 212,
    #       "id": 644,
    #       "name": "Elham21",
    #       "shared": True
    #     }
    #   ],
    #   "endIndex": 1,
    #   "hasNextPage": False,
    #   "startIndex": 0,
    #   "totalPages": 1,
    #   "totalSize": 1
    # }
    #
    # Process finished with exit code 0

    # print(pod_dashboard.raw_response())

except DashboardException as e:
    print("Dashboard Exception :", e)

except APIException as e:
    print("API Exception\nError {}\nError Code : {}\nReference Number : {}".format(e.message, e.error_code,
                                                                                   e.reference_number))
except PodException as e:
    print("Pod Exception: ", e.message)
