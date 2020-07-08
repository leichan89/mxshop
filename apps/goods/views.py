from goods.serializers import GoodsSerializer
from .models import Goods
from rest_framework import viewsets, mixins
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination
from .filter import GoodsFilter
from django_filters.rest_framework import DjangoFilterBackend


class GoodsPagination(PageNumberPagination):
    """
    商品列表自定义分页
    """

    # 默认每页显示的条数
    page_size = 10
    # 动态修改每页显示的个数
    page_size_query_param = 'page_size'
    # 页码参数
    page_query_param = 'page_num'
    # 最多能显示多少页
    max_page_size = 100

# class GoodsListView(generics.ListAPIView):
#     """
#     商品列表也
#     1.使用该序列化器的时候，需要在当前目录下创建一个url.py文件，参考url.py.bak
#     2.再在root目录下的url中注册路由
#     urlpatterns = [
#     ...
#         商品信息
#         path('', include('goods.urls')),
#     ]
#     """
#
#     pagination_class = GoodsPagination
#     queryset = Goods.objects.all()
#     serializer_class = GoodsSerializer
#     filter_backends = [filters.OrderingFilter]
#     # 可以通过以下字段进行排序参数ordering=market_price或者ordering=-market_price
#     ordering_fields = ['market_price', 'shop_price', 'add_time']

class GoodsListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    商品列表页
    如果不继承ListModelMixin的话，就无法将get和商品的列表关联起来，另外还有其中的分页等等，都无法实现
    ViewSet类与View类其实几乎是相同的,但提供的是read或update这些操作,而不是get或put 等HTTP动作。
    同时，ViewSet为我们提供了默认的URL结构, 使得我们能更专注于API本身。
    """

    pagination_class = GoodsPagination
    # 默认按照id排序
    queryset = Goods.objects.all().order_by('id')
    serializer_class = GoodsSerializer

    filter_backends = (filters.OrderingFilter, DjangoFilterBackend, filters.SearchFilter)

    # 设置filter的类为我们自己定义的类
    filter_class = GoodsFilter

    # 可以通过以下字段进行排序参数orderby=market_price或者orderby=-market_price
    # orderby可以在setting.py中修改
    ordering_fields = ('sold_num', 'add_time')

    # '^'开始搜索。
    # '='完全匹配。
    # '@'全文搜索。(目前只支持 Django 的 MySQL 后端。)
    # '$'正则表达式搜索。
    # 默认情况下，搜索参数被命名为 'search'，但这可能会被 SEARCH_PARAM 设置覆盖。
    # name和goods_brief是goods模型中的字段
    search_fields = ('=name', 'goods_brief')
