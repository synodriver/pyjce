import json
from typing import Union


class JceStructStatics:
    """
    jce 结构体的类型 由4位来表示
    """
    BYTE = 0  # 1byte
    SHORT = 1  # 2byte
    INT = 2  # 4byte
    LONG = 3  # 8byte
    FLOAT = 4  # 4byte
    DOUBLE = 5  # 8bytes
    STRING1 = 6  # 1byte len val
    STRING4 = 7  # 4byte len val
    MAP = 8
    LIST = 9
    STRUCT_BEGIN = 10
    STRUCT_END = 11
    ZERO_TAG = 12
    SIMPLE_LIST = 13
    JCE_MAX_STRING_LENGTH = 104857600


class JceStruct(object):

    def __init__(self):
        self.data = {}

    def __getitem__(self, key):
        return self.data[key]

    def __setitem__(self, key, value):
        self.data[key] = value

    def __iter__(self):
        return iter(self.data)

    def __contains__(self, item):
        return item in self.data

    def read_from(self, reader: Union[bytes, bytearray, "JceReader"]):
        self.data.clear()
        head_data, _ = reader.peak_head()
        while head_data.type != 11 and reader._buffer.position < len(reader._buffer.bytes):
            tag = head_data.tag
            value = reader.read_current(True)
            if isinstance(value, bytes) and len(value) > 0:
                try:
                    s = JceStruct()
                    from pyjce.reader import JceReader
                    s.read_from(JceReader(value))
                    self.data[tag] = s
                except:
                    self.data[tag] = value
            else:
                self.data[tag] = value
            if reader._buffer.position >= len(reader._buffer.bytes):
                break
            head_data, _ = reader.peak_head()

    def as_dict(self) -> dict:
        return json.loads(self.as_json())

    def as_json(self):
        return json.dumps(self, cls=JceStructEnconding, ensure_ascii=False)


class JceStructEnconding(json.JSONEncoder):
    def default(self, o):  # pylint: disable=E0202
        if isinstance(o, JceStruct):
            if len(o.data) == 1:
                return list(o.data.values())[0]
            else:
                return o.data
        if isinstance(o, (bytes, bytearray)):
            return str(o)
