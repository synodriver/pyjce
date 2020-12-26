# -*- coding: utf-8 -*-
from typing import TypeVar, TYPE_CHECKING

if TYPE_CHECKING:
    from .reader import JceReader
    from .writer import JceWriter
    from .struct import IJceStruct
    from .buffer import ByteBuffer
    from .head import HeadData

JceReader = TypeVar("JceReader", bound="JceReader")

JceWriter = TypeVar("JceWriter", bound="JceWriter")

IJceStruct = TypeVar("IJceStruct", bound="IJceStruct")

ByteBuffer = TypeVar("ByteBuffer", bound="ByteBuffer")

HeadData = TypeVar("HeadData", bound="HeadData")
