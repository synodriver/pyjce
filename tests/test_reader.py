# -*- coding: utf-8 -*-
import unittest
from typing import Union

from pydantic import Field

from pyjce import JceReader, IJceStruct, JceWriter, IAutoDecodeJceStruct

test_data = bytes.fromhex(
    "100129000b0a160e3139332e3131322e3233312e3630211f9030014c5c600870018602737a96066f74686572730b0a160d34322e38312e3137322e323135211f9030014c5c600870018602746a960374656c0b0a160b31342e32322e332e313134211f9030014c5c600870018602737a960374656c0b0a160e31342e3231352e3133382e3131302101bb30014c5c600870018602737a960374656c0b0a160d34322e38312e3136392e313030205030014c5c600870018602746a960374656c0b0a160e3131342e3232312e3134342e37362136b030014c5c6008700186027368960374656c0b0a160d3131332e39362e31322e3232342101bb30014c5c600870018602737a960374656c0b0a160d34322e38312e3137302e313232211f9030014c5c600870018602746a960374656c0b0a160e3131342e3232312e3134382e3637205030014c5c6008700186027368960374656c0b0a16116d7366776966692e33672e71712e636f6d211f9030014c5c60087c86066f746865727396066f74686572730b0a160c34322e38312e3137322e3633205030014c5c600870018602746a960374656c0b39000b0a160e3139332e3131322e3233312e3630211f9030014c5c600870018602737a96066f74686572730b0a160d34322e38312e3137322e323135211f9030014c5c600870018602746a960374656c0b0a160b31342e32322e332e313134211f9030014c5c600870018602737a960374656c0b0a160e31342e3231352e3133382e3131302101bb30014c5c600870018602737a960374656c0b0a160d34322e38312e3136392e313030205030014c5c600870018602746a960374656c0b0a160e3131342e3232312e3134342e37362136b030014c5c6008700186027368960374656c0b0a160d3131332e39362e31322e3232342101bb30014c5c600870018602737a960374656c0b0a160d34322e38312e3137302e313232211f9030014c5c600870018602746a960374656c0b0a160e3131342e3232312e3134382e3637205030014c5c6008700186027368960374656c0b0a16116d7366776966692e33672e71712e636f6d211f9030014c5c60087c86066f746865727396066f74686572730b0a160c34322e38312e3137322e3633205030014c5c600870018602746a960374656c0b425fe636545138406c7c80029005acbcc900050a160e3130392e3234342e3132392e3135205030014c500360087c8602737a96066f74686572730b0a160d34322e38312e3136392e313035205030014c500360087c8602746a960374656c0b0a160c3131332e39362e31332e3434205030014c500360087c8602737a960374656c0b0a160e3131342e3232312e3134342e3232205030014c500360087c86027368960374656c0b0a160d34322e38312e3136392e313035205030014c500360087c8602746a960374656c0bd900050a160e3130392e3234342e3132392e3135205030014c500360087c8602737a96066f74686572730b0a160d34322e38312e3136392e313035205030014c500360087c8602746a960374656c0b0a160c3131332e39362e31332e3434205030014c500360087c8602737a960374656c0b0a160e3131342e3232312e3134342e3232205030014c500360087c86027368960374656c0b0a160d34322e38312e3136392e313035205030014c500360087c8602746a960374656c0bed000cf90f0cf9100cf9110cf01202f113ff38f61428323032302d31322d32352032323a35383a32382064656c6976657279696e67206120706f6c6963790b")


class SsoServerInfo(IAutoDecodeJceStruct):
    server: str = Field(None, jce_id=1)  # string `jceId:"1"`
    port: int = Field(None, jce_id=2)  # int32  `jceId:"2"`
    location: str = Field(None, jce_id=8)  # string `jceId:"8"`

    # def read_from(self, reader: JceReader):
    #     self.server = reader.read_string(1)
    #     self.port = reader.read_int32(2)
    #     self.location = reader.read_string(8)

class TestReader(unittest.TestCase):
    def test_reader(self):
        reader = JceReader(test_data)
        s = SsoServerInfo()
        data = reader.read_list(SsoServerInfo, 2)
        self.assertEqual(len(data), 11)

        self.assertEqual(len(SsoServerInfo.decode_list(test_data, 2)), 11)


if __name__ == "__main__":
    unittest.main()
