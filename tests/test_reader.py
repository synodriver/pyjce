# -*- coding: utf-8 -*-
import unittest

from pyjce import JceReader, JceStruct, JceWriter


class TestReader(unittest.TestCase):
    def test_reader(self):
        with open("datas", "rb") as f:
            reader = JceReader(f.read())
        s = JceStruct()
        s.read_from(reader)
        print(s.as_dict())

    def test_writer(self):
        writer = JceWriter(b"")
        writer.write_filed(0, 2, 3)  # 4byte int 3
        writer.write_filed(1, 5, 3.8)  # 8byte double 3.8
        writer.write_filed(2, 6, "哈哈哈")  # string1
        writer.write_filed(3, 9, [(0, 2, 3), (1, 5, 3.8), (2, 6, "哈哈哈")], 27)

        def decode(data: bytes) -> dict:
            reader = JceReader(data)
            s = JceStruct()
            s.read_from(reader)
            return s.as_dict

        print(decode(writer.bytes))


if __name__ == "__main__":
    unittest.main()
