from pydantic_sequence import BaseListModel


def test_int_list():
    ins = BaseListModel[int].parse_obj([1, 2, 3])
    assert bool(ins) is True
    assert len(ins) == 3
    resp = ins.map(lambda x: x * 2.0)
    assert sum(resp) == 12.0
