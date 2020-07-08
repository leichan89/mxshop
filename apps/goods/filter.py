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
    # 定义进行过滤的参数，CharFilter 是过滤参数的类型，过滤器参数类型还有很多，包括
    # BooleanFilter，ChoiceFilter，DateFilter，NumberFilter，RangeFilter..等等
    # field_name 为筛选的参数名，需要和你 model 中的一致，lookup_expr 为筛选参数的条件
    # 例如 icontains 为 忽略大小写包含，例如 NumberFilter 则可以有 gte，gt，lte，lt，
    # year__gt，year__lt 等
    price_min = django_filters.NumberFilter(field_name='shop_price', lookup_expr='gte')
    price_max = django_filters.NumberFilter(field_name='shop_price', lookup_expr='lte')
    # lookup_expr参考 https://docs.djangoproject.com/en/3.1/topics/db/queries/
    # 单独通过名称搜索
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')

    class Meta:
        model = Goods
        fields = ['price_min', 'price_max', 'name']











