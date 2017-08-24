# encoding: utf-8

"""

@author: kevin

@contact: kevin_678@126.com

@file: sales_ranking_service.py

@time: 2017/8/19 11:21

@desc:

@Software: kevin_test

"""
from show_data.models.statistics_item_sales_count import ItemSalesSixMonthModel


class SalesRankingService(object):
    def __init__(self):
        """

        """

    def query_all_data(self):
        lis = ItemSalesSixMonthModel.objects.all()

        # 销量倒排
        lis_order_by_sales_desc = lis.order_by("-total_sales")
        # lis_order_by_sales_desc.aggregate()
        print lis.query
        return lis_order_by_sales_desc
