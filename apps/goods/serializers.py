# -*- coding: utf-8 -*-
# @Time    : 2020-07-01 18:38
# @Author  : OG·chen
# @File    : serializers.py

from rest_framework import serializers
from rest_framework.serializers import Field
from .models import GoodsCategory, Goods
from common.tools import Tools
# from datetime import datetime
# from pytz import timezone
# from MxShop.settings import TIME_ZONE


class TimestampField(Field):
    """
    修改模型中的某个字段
    """

    def to_representation(self, value):
        # 将Goods模型返回的add_time转换为时间戳
        # 重写它以支持序列化，用于读取操作。
        ts = Tools.datetime2timestamp(value)
        return ts

    # def to_internal_value(self, data):
    #     # 重写它以支持反序列化，以用于写入操作
    #     timestamp = float(data)
    #     no_tz = datetime.utcfromtimestamp(timestamp)
    #     return no_tz.astimezone(timezone(TIME_ZONE))

class CategorySerializer(serializers.ModelSerializer):

    # 修改时间为时间戳
    timestamp = TimestampField(source='add_time')
    class Meta:
        model = GoodsCategory
        # fields = "__all__"
        exclude = ['add_time']

class GoodsSerializer(serializers.ModelSerializer):

    # 外键id对应的category信息
    category = CategorySerializer()
    timestamp = TimestampField(source='add_time')

    class Meta:
        model = Goods
        # fields = "__all__"
        exclude = ['add_time']










