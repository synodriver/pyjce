from typing import List, Union

from .buffer import ByteBuffer
from .writer import JceWriter
from .reader import JceReader
from .struct import IJceStruct

__all__ = ["ByteBuffer", "IJceStruct", "JceReader", "JceWriter", "AutoDecodeMixin"]

__version__ = "0.1.1"


class AutoDecodeMixin:
    @classmethod
    def decode_list(cls, data: Union[bytes, bytearray], tag: int) -> List["IJceStruct"]:
        """
        从一个bytes里面解码出List[自己]
        :param data:
        :param tag:
        :return:
        """
        reader = JceReader(data)
        return reader.read_list(cls, tag)
