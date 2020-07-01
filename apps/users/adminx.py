# -*- coding: utf-8 -*-
# @Time    : 2020-06-28 17:31
# @Author  : OG·chen
# @File    : adminx.py

import xadmin
from xadmin import views
from .models import VerifyCode

class BaseSetting(object):
    """
    添加主题功能
    """
    enable_themes = True
    use_bootswatch = True

class GlobalSetting(object):
    """
    全局配置，后台管理标题和页脚
    """
    site_title = "OG大哥大"
    site_footer = "https://github.com/derek-zhang123/MxShop"
    # 菜单收缩
    menu_style = "accordion"

class VerifyCodeAdmin(object):
    """
    导航栏：用户管理-短信验证
    """
    list_display = ['code', 'mobile', 'add_time']


xadmin.site.register(VerifyCode, VerifyCodeAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSetting)





