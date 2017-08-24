# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from show_data.service.sales_ranking_service import SalesRankingService
from show_data.service.test_service import TestService


def index(request):
    ts = TestService()
    dlist = ts.test()
    context = {"name": "my data test === ||| ===", "message": dlist}
    return render(request=request, template_name="show/show_data.html", context=context)


def sales_ranking(request):
    srs = SalesRankingService()
    lis = srs.query_all_data()
    context = {"name": "180天亚米自营商品销量", "data": lis}
    return render(request=request, template_name="show/selas_ranking.html", context=context)
