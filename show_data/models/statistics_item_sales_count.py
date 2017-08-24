# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.

class ItemSalesSixMonthModel(models.Model):
    id = models.BigIntegerField(max_length=20)
    goods_id = models.IntegerField(max_length=11)
    item_number = models.CharField(max_length=20)
    category_id = models.IntegerField(max_length=11)
    total_sales = models.BigIntegerField(max_length=20)

    class Meta:
        db_table = 'statistics_item_sales_count_180'
