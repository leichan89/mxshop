# -*- coding: utf-8 -*-
# @Time    : 2020-07-08 14:59
# @Author  : OG·chen
# @File    : filter.py

import django_filters
from .models import Goods

class GoodsFilter(django_filters.rest_framework.FilterSet):
    """
    商品过滤的类，根据价格区间进行过滤
    """
    # 两个参数，name是要过滤的字段，lookup是执行的行为，‘小与等于本店价格’
    # Django 2.x开始NumberFilter中的参数name变为filed_name
    price_min = django_filters.NumberFilter(field_name="shop_price", lookup_expr='gte')
    price_max = django_filters.NumberFilter(field_name="shop_price", lookup_expr='lte')

    class Meta:
        model = Goods
        fields = ['price_min', 'price_max']











