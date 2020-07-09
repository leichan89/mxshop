# -*- coding: utf-8 -*-
# @Time    : 2020-07-01 18:38
# @Author  : OG·chen
# @File    : serializers.py

from rest_framework import serializers
from rest_framework.serializers import Field
from .models import GoodsCategory, Goods
from common.tools import Tools


class TimestampField(Field):
    """
    修改模型中的某个字段，在模型序列化类中需要知道字段的来源
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

class CategorySerializer3(serializers.ModelSerializer):
    """
    三级分类
    """
    addtime = TimestampField(source='add_time')
    class Meta:
        model = GoodsCategory
        exclude = ['add_time']

class CategorySerializer2(serializers.ModelSerializer):
    """
    二级分类
    """
    sub_cat = CategorySerializer3(many=True)
    addtime = TimestampField(source='add_time')
    class Meta:
        model = GoodsCategory
        exclude = ['add_time']

class CategorySerializer(serializers.ModelSerializer):
    """
    商品一级类别目录序列化
    """
    sub_cat = CategorySerializer2(many=True)
    # 修改时间为时间戳
    addtime = TimestampField(source='add_time')
    class Meta:
        model = GoodsCategory
        # fields = "__all__"
        exclude = ['add_time']

class GoodsSerializer(serializers.ModelSerializer):

    # 外键id对应的category信息
    category = CategorySerializer()
    addtime = TimestampField(source='add_time')

    class Meta:
        model = Goods
        # fields = "__all__"
        exclude = ['add_time']










