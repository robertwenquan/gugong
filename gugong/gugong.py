#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
#
# gugong
#

import os
import json
import time
import random
import pypinyin
from .proto import gugong_pb2 as ggpb

class GuGong(object):

    # name of the object
    name = "故宫"

    # open-schema profile
    profile = {}

    # a list of places in Gugong
    places = []

    # a list of empires that lived at GuGong
    empires = []

    cwd, _ = os.path.split(__file__)
    DATA_PATH = os.path.join(cwd, "data", "gugong.json")

    def __init__(self):
        super().__init__();

        if not self.profile and not self.places:
            self.load_data()
    
    # load the data into the main object
    def load_data(self):

        def map_arch_type(arch_type_string):
            return {
                'bridge': ggpb.QIAO,
                'qiao': ggpb.QIAO,
                'garden': ggpb.HUAYUAN,
                'huayuan': ggpb.HUAYUAN,
                'gate': ggpb.MEN,
                'men': ggpb.MEN,
                'guan': ggpb.GUAN,
                'hall': ggpb.DIAN,
                'dian': ggpb.DIAN,
                'kiosk': ggpb.TING,
                'ting': ggpb.TING,
                'lou': ggpb.LOU,
                'palace': ggpb.GONG,
                'gong': ggpb.GONG,
                'pavilion': ggpb.GE,
                'ge': ggpb.GE,
                'tang': ggpb.TANG,
                'xuan': ggpb.XUAN,
                'zhai': ggpb.ZHAI
            }.get(arch_type_string, ggpb.UNDEFINED_ARCH_TYPE)

        def map_orientation(orientation_string):
            return {
                'north': ggpb.NORTH,
                'south': ggpb.SOUTH,
                'east': ggpb.EAST,
                'west': ggpb.WEST
            }.get(orientation_string, ggpb.UNDEFINED_ORIENTATION)

        data_parsed = None
        with open(self.DATA_PATH, "r") as fd:
            data = fd.read()
            data_parsed = json.loads(data)

        if data_parsed is None:
            raise Exception("Data Parsing Error!!")

        places = data_parsed['places']
        for place in places:
            p = ggpb.Place(name=place['name'])
            if place.get('arch_type'):
                p.arch_type = map_arch_type(place['arch_type'])

            if place.get('orientation'):
                p.orientation = map_orientation(place['orientation'])

            self.places.append(p)

        empires = data_parsed['empires']
        for empire in empires:
            emp = ggpb.Empire(name=empire['name'])

            if empire.get('epoch_name'):
                emp.epoch_name = empire['epoch_name']

            if empire.get('temple_name'):
                emp.temple_name = empire['temple_name']

            self.empires.append(emp)

    def get_faq_answer(self, question):
        return {
            '你是谁？': '我是你的故宫小帮手。',
            '故宫什么时候成立的': '故宫是xxxx成立的。',
            '故宫有多大': '故宫长961多米，宽753多米。',
            '故宫里有御猫吗': '你去找找看？',
            '城门': '紫禁城有四座城门，南面为午门，北面为神武门，东面为东华门，西面为西华门。',
            '外朝': '外朝的中心为太和殿、中和殿、保和殿，统称三大殿',
            '内廷': '乾清宫、交泰殿、坤宁宫，统称后三宫',
            '故宫的入口在哪里？': '故宫目前只能从东华门进入。',
            '故宫里有餐厅么？': '故宫里有简餐，冰窖提供简餐。'
        }.get(question, '对不起，你的问题太难了。我暂时还帮不了你:(')

    # just kidding QA system here for fun.
    def ask(self, question):
        question = question.replace('?', '')
        print("你是想知道" + question + "吗？让我想一想", end='', flush=True)

        # AI假装在思考
        for i in range(random.randint(1, 3)):
            print('.', end='', flush=True)
            time.sleep(random.random())

        print('.', flush=True)

        return self.get_faq_answer(question)

    def du(self, query):
        return pypinyin.pinyin(query)
