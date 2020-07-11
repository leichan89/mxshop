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

        # 通过goods表中的category_id查询，只查询category_id为指定值的数据
        # 查询的是商品直接关联的类别信息
        # return queryset.filter(Q(category_id=value))

        # 通过外键category在goods_goodscategory表中查找parent_category_id等于指定值的数据
        # 查询的是商品的category_id对应的父id是指定值的商品，会将父id都一样的商品都查询出来
        # 二级目录相同的商品都查询出来，既parent_category_id等于指定值
        # return queryset.filter(Q(category__parent_category_id=value))

        # goods表的外键category通过goods_goodscategory的外键找到对应的id，在通过这个id找这个id的parent_category_id

        # SELECT goods_goods.name , goods_goodscategory.parent_category_id FROM `goods_goods`
        # INNER JOIN `goods_goodscategory` ON (`goods_goods`.`category_id` = `goods_goodscategory`.`id`)
        # return queryset.filter(Q(category__parent_category__parent_category_id=value))

        # 查询一级相同，或者二级相同，或者三级相同的类别id

        # 获取商品的目前关联的一级目录
        # SELECT parent_category_id from goods_goodscategory where id in
        # (SELECT DISTINCT(parent_category_id) from goods_goodscategory WHERE id in
        # (SELECT DISTINCT(category_id) FROM `goods_goods`))
        # 一级目录相同的商品都查询出来:比如parent_category_id=1

        # SELECT goods_goods.name , goods_goodscategory.parent_category_id, T3.parent_category_id FROM `goods_goods`
        # INNER JOIN `goods_goodscategory` ON (`goods_goods`.`category_id` = `goods_goodscategory`.`id`)
        # INNER JOIN `goods_goodscategory` T3 ON (`goods_goodscategory`.`parent_category_id` = T3.`id`) ;

        # 解释：先是goods表和goodscategory表inner join，join条件是goods的category_id等于goodscategory表的id，
        # 可以得到每个商品对应的父id，然后再和goodscategory inner join
        # join的条件是前面join的父id与goodscategory的id相同，就能得到每个商品的一级id
        return queryset.filter(Q(category_id=value) | Q(category__parent_category_id=value)
                               | Q(category__parent_category__parent_category_id=value))

    class Meta:
        model = Goods
        fields = ['price_min', 'price_max', 'name']











