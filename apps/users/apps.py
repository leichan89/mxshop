from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'
    # 设置app在xadmin中显示为中文
    verbose_name = "用户管理"
