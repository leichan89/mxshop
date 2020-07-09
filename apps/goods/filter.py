# -*- coding: utf-8 -*-
# @Time    : 2020-07-08 14:59
# @Author  : OG·chen
# @File    : filter.py

import django_filters
from .models import Goods
from django.db.models import Q

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

    # 通过商品对应的category_id查询，会将该category_id相同父id的类别查询出来
    top_category = django_filters.NumberFilter(field_name='category', method='top_category_filter')

    def top_category_filter(self, queryset, name, value):
        # Q 对象使用 https://docs.djangoproject.com/zh-hans/3.0/topics/db/queries/
        # 不管当前点击的是一级分类二级分类还是三级分类，都能找到。
        # SELECT COUNT(*) AS `__count` FROM `goods_goods` INNER JOIN `goods_goodscategory` ON
        # (`goods_goods`.`category_id` = `goods_goodscategory`.`id`) LEFT OUTER JOIN `goods_goodscategory` T3
        # ON (`goods_goodscategory`.`parent_category_id` = T3.`id`)
        # WHERE (`goods_goods`.`category_id` = 7
        # OR `goods_goodscategory`.`parent_category_id` = 7
        # OR T3.`parent_category_id` = 7); args=(7, 7, 7)

        # goods表通过category表的id找到响应类别数据，再通过父id找父id，再通过父id的父id找数据
        return queryset.filter(Q(category_id=value) | Q(category__parent_category_id=value)
                               | Q(category__parent_category__parent_category_id=value))

    class Meta:
        model = Goods
        fields = ['price_min', 'price_max', 'name']











