# !/usr/bin/env python
# -*- coding: utf-8 -*-

#from peewee import *
from peewee import SqliteDatabase, Model, IntegerField, CharField, TextField, DateTimeField
from datetime import datetime

path = 'common/jinyong.sqlite'
db = SqliteDatabase(path)


class BaseModel(Model):
    class Meta:
        database = db


class Jinyong(BaseModel):
    id = IntegerField(primary_key=True, verbose_name='id')
    title = CharField(max_length=150, verbose_name='章节')
    name = CharField(max_length=20, verbose_name='小说')
    url = CharField(max_length=100, verbose_name='url')
    content = TextField(null=True, verbose_name='内容')
    created_at = DateTimeField(default=datetime.now, verbose_name='创建时间')


if __name__ == '__main__':
    try:
        Jinyong.create_table()
        print('created success : %s' % path)
    except Exception as err:
        print(err)
