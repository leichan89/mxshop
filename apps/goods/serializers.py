# -*- coding: utf-8 -*-
# @Time    : 2020-07-01 18:38
# @Author  : OG·chen
# @File    : serializers.py

from rest_framework import serializers
from .models import GoodsCategory, Goods

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = GoodsCategory
        fields = "__all__"


class GoodsSerializer(serializers.ModelSerializer):

    # 覆盖外键，用外键对应的所有内容来替代
    category = CategorySerializer()

    class Meta:
        model = Goods
        fields = "__all__"









