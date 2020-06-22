#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
#
# dtype.py
#
# data type for the gugon
#

class Place(object):
    
    name = ""
    arch_type = None

    def __init__(self):
        super().__init__()

    def to_english(self):
        pass

    def to_pinyin(self):
        pass


class Gong(Place):

    def __init__(self):
        super().__init__()

        self.arch_type = "GONG"


class Dian(Place):

    def __init__(self):
        super().__init__()

        self.arch_type = "DIAN"

