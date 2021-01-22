from typing import List, Union

from .buffer import ByteBuffer
from .writer import JceWriter
from .reader import JceReader
from .struct import IJceStruct

__all__ = ["ByteBuffer", "IJceStruct", "JceReader", "JceWriter", "IAutoDecodeJceStruct"]

__version__ = "0.1.2"


class IAutoDecodeJceStruct(IJceStruct):
    """
    实现了一些标准方法的接口,当然要是序列化嵌套jce的话可能还是有问题
    """
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

    def read_from(self, reader: JceReader) -> None:
        for field_name, val in self.schema()["properties"].items():
            jce_id: int = val["jce_id"]
            setattr(self, field_name, reader.read_any(jce_id))

    def to_bytes(self) -> Union[bytes, bytearray]:
        writer = JceWriter()
        writer.write_jce_struct_raw(self)
        return writer.bytes()
