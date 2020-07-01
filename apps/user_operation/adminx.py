# -*- coding: utf-8 -*-
# @Time    : 2020-07-01 11:39
# @Author  : OG·chen
# @File    : xadmin.py

import xadmin
from .models import UserFav, UserLeavingMessage, UserAddress

class UserFavAdmin(object):
    list_display = ["user", "goods", "add_time"]


class UserLeavingMessageAdmin(object):
    list_display = ["user", "message_type", "message", "add_time"]


class UserAddressAdmin(object):
    list_display = ["signer_name", "signer_mobile", "district", "address"]


xadmin.site.register(UserFav, UserFavAdmin)
xadmin.site.register(UserAddress, UserAddressAdmin)
xadmin.site.register(UserLeavingMessage, UserLeavingMessageAdmin)










