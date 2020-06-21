from gugong import GuGong
from proto import gugong_pb2 as ggpb

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
