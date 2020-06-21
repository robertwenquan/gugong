#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
#
# gugong
#

import json
import time
import random
from proto import gugong_pb2 as ggpb

class Place(object):
    pass

class Palace(Place):

    def __init__(self):
        super().__init__()

class GuGong(object):

    # name of the object
    name = "故宫"

    # open-schema profile
    profile = {}

    # a list of places in Gugong
    places = []

    def __init__(self):
        super().__init__();

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
        with open("data/gugong.json", "r") as fd:
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

    def get_faq_answer(self, question):
        return {
            '你是谁？': '我是你的故宫小帮手。',
            '故宫什么时候成立的': '故宫是xxxx成立的。',
            '故宫有多大': '故宫长900多米，宽700多米。',
            '故宫里有御猫吗': '你去找找看？',
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


def main():
    gugong = GuGong()
    print(gugong.ask('故宫有多大?'))

if __name__ == "__main__":
    main()

