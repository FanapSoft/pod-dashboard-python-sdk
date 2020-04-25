# coding=utf-8


class EditAccessLevel:
    """
    سطح دسترسی برای ویرایش
    """

    def __init__(self):
        pass

    """ بدون دسترسی ویرایش """
    NONE = "NONE"

    """ دسترسی ویرایش تنظیمات اشتراک گذاری داشبورد """
    EDIT_SHARED_DASHBOARD_CONFIG = "EDIT_SHARED_DASHBOARD_CONFIG"

    """ دسترسی ویرایش تنظیمات گزارش کاربری """
    EDIT_USER_REPORTS_CONFIG = "EDIT_USER_REPORTS_CONFIG"

    """ دسترسی ویرایش تنظیمات داشبورد """
    EDIT_DASHBOARD_CONFIG = "EDIT_DASHBOARD_CONFIG"

    """ دسترسی حذف و اضافه گزارش کاربری """
    ADD_OR_REMOVE_USER_REPORTS = "ADD_OR_REMOVE_USER_REPORTS"


class ShareAccessLevel:
    """
    سطح دسترسی اشتراک گذاری
    """
    def __init__(self):
        pass

    NONE = "NONE"
    SHARE = "SHARE"
    UN_SHARE = "UNSHARE"

