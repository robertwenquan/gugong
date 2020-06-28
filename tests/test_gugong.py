import os
import json
from gugong import GuGong
from gugong.proto import gugong_pb2 as ggpb
from gugong.models import db

def test_init():
    gg = GuGong()
    assert gg.name == "故宫"

def test_protos():
    place = ggpb.Place(name="Abc", other_names=["bbb", "ccc"], arch_type = ggpb.DIAN)
    assert place.name == "Abc"
    assert len(place.other_names) == 2
    assert place.other_names[0] == "bbb"
    assert place.other_names[1] == "ccc"
    assert place.arch_type == ggpb.DIAN

def test_data_models():
    # test the data models
    db.init_db()

    # test arch_type table
    #arch_types = db.ArchType.select()
    #assert len(arch_types) > 0

    # test place table
    places = db.Place.select()
    assert len(places) > 0

    # test empire table
    empires = db.Empire.select().where(db.Empire.dynasty == 'QING')
    assert len(empires) > 0
    for empire in empires:
        assert empire.dynasty == 'QING'

def test_data_integrity():
    # verify data integrity after loading
    gg = GuGong()
    assert (len(gg.places) > 0)
    for place in gg.places:
        assert (isinstance(place, ggpb.Place))
        if place.arch_type == ggpb.MEN:
            assert (place.name.endswith('门'))
        elif place.arch_type == ggpb.DIAN:
            assert (place.name.endswith('殿'))
        elif place.arch_type == ggpb.GONG:
            assert (place.name.endswith('宫'))
        elif place.arch_type == ggpb.TING:
            assert (place.name.endswith('亭'))
        elif place.arch_type == ggpb.QIAO:
            assert (place.name.endswith('桥'))
        elif place.arch_type == ggpb.GE:
            assert (place.name.endswith('阁'))
        elif place.arch_type == ggpb.ZHAI:
            assert (place.name.endswith('斋'))
        elif place.arch_type == ggpb.HUAYUAN:
            assert (place.name.endswith('花园'))
        elif place.arch_type == ggpb.TANG:
            assert (place.name.endswith('堂'))
        elif place.arch_type == ggpb.GUAN:
            assert (place.name.endswith('馆'))
        elif place.arch_type == ggpb.LOU:
            assert (place.name.endswith('楼'))
 
def test_history_integrity():
    # verify if the data checks with simple historic facts
    gg = GuGong()

    empires = gg.empires
    assert (len(empires) == 24)
