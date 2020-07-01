# -*- coding: utf-8 -*-
# @Time    : 2020-06-29 11:00
# @Author  : OG·chen
# @File    : adminx.py

import xadmin
from .models import Goods, GoodsCategory, GoodsImage, GoodsCategoryBrand, Banner, HotSearchWords
from .models import IndexAd

class GoodsAdmin(object):
    """
    导航栏：商品管理-商品信息
    """
    # 显示的列，获取数据库中所有商品的信息
    list_display = ["name", "click_num", "sold_num", "fav_num", "goods_num", "market_price",
                    "shop_price", "goods_brief", "goods_desc", "is_new", "is_hot", "add_time"]

    # 可以搜索的字段:使用这个属性列出来的字段关键字来搜索数据
    search_fields = ["name"]

    # 列表页可以直接编辑的
    list_editable = ["is_hot", ]

    # 过滤器
    list_filter = ["name", "click_num", "sold_num", "fav_num", "goods_num", "market_price",
                   "shop_price", "is_new", "is_hot", "add_time", "category__name"]

    # 富文本编辑器
    style_fields = {"goods_desc": "ueditor"}

    # 在添加商品的时候可以添加商品图片（商品轮播GoodsImage）
    class GoodsImagesInline(object):
        model = GoodsImage
        exclude = ["add_time"]
        # 默认显示的条目数
        extra = 1
        # 对应文件中xadmin/plugins/inline.py
        # 显示上传图片的按钮的样式，没有其他作用：accordion，tab，one
        style = "tab"

    inlines = [GoodsImagesInline]

class GoodsCategoryAdmin(object):
    """
    导航栏：商品管理-商品类别
    """
    list_display = ["name", "category_type", "parent_category", "add_time"]
    list_filter = ["category_type", "parent_category", "name"]
    search_fields = ["name", ]

class GoodsBrandAdmin(object):
    """
    导航栏：商品管理-宣传品牌
    """
    list_display = ["category", "image", "name", "desc"]

    def get_context(self):
        context = super(GoodsBrandAdmin, self).get_context()
        if 'form' in context:
            # 商品类目下拉框只显示类别是1的类别
            context['form'].fields['category'].queryset = GoodsCategory.objects.filter(category_type=1)
        return context

class BannerGoodsAdmin(object):
    """
    导航栏：商品管理-首页轮播商品
    """
    list_display = ["goods", "image", "index"]

class HotSearchAdmin(object):
    """
    导航栏：商品管理-热搜排行
    """
    list_display = ["keywords", "index", "add_time"]

class IndexAdAdmin(object):
    """
    导航栏：商品管理-首页广告
    """
    list_display = ["category", "goods"]


xadmin.site.register(Goods, GoodsAdmin)
xadmin.site.register(GoodsCategory, GoodsCategoryAdmin)
xadmin.site.register(Banner, BannerGoodsAdmin)
xadmin.site.register(GoodsCategoryBrand, GoodsBrandAdmin)
xadmin.site.register(HotSearchWords, HotSearchAdmin)
xadmin.site.register(IndexAd, IndexAdAdmin)




