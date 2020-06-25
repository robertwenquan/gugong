#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
#
# dtype.py
#
# data type for the gugon
#

from peewee import *

db = SqliteDatabase(':memory:'

class Place(Model):
    id = CharField()
    name = CharField()
    arch_type = CharField()

    class Meta:
        database = db