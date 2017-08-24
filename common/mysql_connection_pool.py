# encoding: utf-8

"""

@author: kevin

@contact: kevin_678@126.com

@file: mysql_connection_pool.py

@time: 2017/8/12 11:17

@desc:

@Software: kevin_test

"""
import sqlalchemy.pool as pool
import django.db.backends.mysql
from django.db import connection


class MysqlConnectionPool(object):
    this = None
    pool = None

    def __init__(self):
        """
        """
        self.pool = pool.QueuePool(self.getConnection(), max_overflow=10, pool_size=5)

    @staticmethod
    def getInstance(self):
        if (MysqlConnectionPool.this == None):
            this = MysqlConnectionPool()
        return this

    def getConnection(self):
        return None
