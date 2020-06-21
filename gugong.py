#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
#
# gugong
#

import json
from proto import gugong_pb2 as ggpb

class GuGong(object):

    name = "故宫"

    def __init__(self):
        super().__init__();

        self.load_data()
    
    # load the data into the object
    def load_data(self):
        place1 = ggpb.Place(name="sdfsff")
