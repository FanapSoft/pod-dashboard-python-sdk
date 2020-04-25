# coding=utf-8
from __future__ import unicode_literals

from pod_base import APIException, PodException
from examples.config import *
from pod_dashboard import PodDashboard, DashboardException

try:
    pod_dashboard = PodDashboard(api_token=API_TOKEN, server_type=SERVER_MODE)
    print(pod_dashboard.get_dashboard_users(dashboard_id=335))

    # OUTPUT
    # {
    #   "currentPage": 0,
    #   "data": [
    #     {
    #       "created": "2020-04-25T08:53:08.177Z[UTC]",
    #       "editable": False,
    #       "expire": "2020-12-29T23:59:59.999Z[UTC]",
    #       "id": 642,
    #       "user": {
    #         "id": 122,
    #         "username": "som*******ani"
    #       }
    #     },
    #     {
    #       "created": "2020-04-25T09:35:18.085Z[UTC]",
    #       "editable": False,
    #       "expire": "2020-12-29T23:59:59.999Z[UTC]",
    #       "id": 643,
    #       "user": {
    #         "id": 112,
    #         "username": "re.zare"
    #       }
    #     }
    #   ],
    #   "endIndex": 0,
    #   "hasNextPage": True,
    #   "startIndex": 0,
    #   "totalPages": 0,
    #   "totalSize": 0
    # }

    # print(pod_dashboard.raw_response())

except DashboardException as e:
    print("Dashboard Exception :", e)

except APIException as e:
    print("API Exception\nError {}\nError Code : {}\nReference Number : {}".format(e.message, e.error_code,
                                                                                   e.reference_number))
except PodException as e:
    print("Pod Exception: ", e.message)
