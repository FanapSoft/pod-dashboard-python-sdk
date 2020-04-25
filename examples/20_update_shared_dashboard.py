# coding=utf-8
from __future__ import unicode_literals
from pod_base import APIException, PodException
from examples.config import *
from pod_dashboard import PodDashboard, DashboardException

try:
    pod_dashboard = PodDashboard(api_token=API_TOKEN, server_type=SERVER_MODE)
    config = {
        "layout": [{
            "w": 20,
            "h": 43,
            "x": 0,
            "y": 0,
            "moved": False,
            "static": True
        }]
    }
    print(pod_dashboard.update_shared_dashboard(dashboard_id=644, config=config, order=2))
    # OUTPUT
    # 644

    # print(pod_dashboard.raw_response())

except DashboardException as e:
    print("Dashboard Exception :", e)

except APIException as e:
    print("API Exception\nError {}\nError Code : {}\nReference Number : {}".format(e.message, e.error_code,
                                                                                   e.reference_number))
except PodException as e:
    print("Pod Exception: ", e.message)
