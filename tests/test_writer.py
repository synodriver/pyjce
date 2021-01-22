# -*- coding: utf-8 -*-
import unittest
from typing import Union

from pydantic import Field

from pyjce import JceReader, IAutoDecodeJceStruct


class SsoServerInfo(IAutoDecodeJceStruct):
    server: str = Field(None, jce_id=1)  # string `jceId:"1"`
    port: int = Field(None, jce_id=2)  # int32  `jceId:"2"`
    location: str = Field(None, jce_id=8)  # string `jceId:"8"`


class TestWriter(unittest.TestCase):
    def test_writer(self):
        data = SsoServerInfo(server="rcnb", port="8000", location="rcnb")
        reader = JceReader(data.to_bytes())
        sso = SsoServerInfo()
        sso.read_from(reader)
        self.assertEqual(sso.server, "rcnb")
        self.assertEqual(sso.port, 8000)
        self.assertEqual(sso.location, "rcnb")
        pass


if __name__ == "__main__":
    unittest.main()
