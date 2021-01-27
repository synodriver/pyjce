# -*- coding: utf-8 -*-
import abc
from typing import Union

from pydantic import BaseModel

from .typing import JceReader


class IJceStruct(BaseModel, abc.ABC):
    """
    jce结构体的基础
    """

    @abc.abstractmethod
    def read_from(self, reader: JceReader) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def to_bytes(self) -> Union[bytes, bytearray]:
        raise NotImplementedError
