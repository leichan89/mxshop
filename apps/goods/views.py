from goods.serializers import GoodsSerializer
from .models import Goods
from rest_framework import generics
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination


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

class GoodsListView(generics.ListAPIView):
    """
    商品列表也
    """

    pagination_class = GoodsPagination
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    filter_backends = [filters.OrderingFilter]
    # 可以通过以下字段进行排序参数ordering=market_price或者ordering=-market_price
    ordering_fields = ['market_price', 'shop_price', 'add_time']

