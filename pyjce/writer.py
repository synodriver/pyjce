# -*- coding: utf-8 -*-
import struct
from typing import Tuple, List, Optional, Union

from pyjce.bytebuffer import ByteBuffer
from .head import HeadData


class JceWriter:
    _buffer: ByteBuffer = None
    encoding = 'utf-8'

    def __init__(self, buffer: Union[ByteBuffer, bytearray, bytes], i: int = 0, encoding="utf-8"):
        """
        准备写入缓冲区
        :param buffer:
        :param i:
        :param encoding:
        """
        self._buffer = buffer
        self.encoding = encoding
        if isinstance(buffer, ByteBuffer):
            self._buffer = buffer
        elif isinstance(buffer, (bytearray, bytes)):
            self._buffer = ByteBuffer(buffer)
            self._buffer.position = i
        else:
            raise TypeError("'buffer' argument must be bytes, bytesarray or ByteBuffer")

    def write_head(self, head: HeadData) -> None:
        self._buffer.write_bytes(head.as_bytes())

    def write_filed(self, tag: int, type_: int, data, length: Optional[int] = None):
        """
        写入jce消息段

        :param tag:
        :param type_:
        :param data:
        :param length: map类型就要这个了 字节数
        :return:
        """
        self.write_head(HeadData(tag, type_))
        if type_ == 0:
            if isinstance(data, int):
                self._buffer.write_bytes(bytes([data]))
            else:
                self._buffer.write_bytes(data)
        elif type_ == 1:
            self._buffer.write_int2(data)
        elif type_ == 2:
            self._buffer.write_int4(data)
        elif type_ == 3:
            self._buffer.write_int8(data)
        elif type_ == 4:
            self._buffer.write_float(data)
        elif type_ == 5:
            self._buffer.write_double(data)
        elif type_ == 6:
            data = data.encode(self.encoding)
            self._buffer.write_bytes(bytes([len(data)]) + data)
        elif type_ == 7:
            data = data.encode(self.encoding)
            self._buffer.write_bytes(struct.pack(">i", len(data)) + data)
        elif type_ == 8:  # map
            if not length:
                raise ValueError("write to jce buffer with map need length")
            self._write_map(length, data)
        elif type_ == 9:  # list
            if not length:
                raise ValueError("write to jce buffer with list need length")
            self._write_list(length, data)
        elif type_ == 10:
            self._write_struct(data)
        elif type_ == 11:
            raise ValueError("can't direct end user difined struct")
        pass

    def _write_map(self, length: int, data: list):  # [((tag,type,data),(tag,type,data)),...]
        self.write_filed(0, 2, length*2)
        for d in data:
            self.write_filed(*d[0])
            self.write_filed(*d[1])

    def _write_list(self, length: int, data: list):  # [(tag,type,value),...]
        self.write_filed(0, 2, length)
        for i in data:
            self.write_filed(*i)

    def _write_struct(self, data: list):
        for i in data:
            self.write_filed(*i)
        self.write_head(HeadData(0, 11))

    @property
    def bytes(self):
        return self._buffer.bytes
