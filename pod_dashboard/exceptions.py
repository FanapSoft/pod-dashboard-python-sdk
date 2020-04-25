from pod_base import APIException


class DashboardException(APIException):
    __slots__ = ("code", "message", "status_code")

    def __init__(self, **kwargs):
        self.code = kwargs.pop("code", 0)
        self.message = kwargs.pop("message", "internal error")
        self.status_code = kwargs.pop("status_code", kwargs.pop("status", 0))

        super(DashboardException, self).__init__(message=self.message, **kwargs)

    def __str__(self):
        return "{}\nCode : {}\nStatus Code : {}\nReference Number : {}".\
            format(self.message, self.code, self.status_code, self.reference_number)
