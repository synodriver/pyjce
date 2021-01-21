# -*- coding: utf-8 -*-
import sys
from pprint import pprint

from pyjce import JceReader


def to_dict(data: bytes):
    reader = JceReader(data)
    ret: dict = {}
    try:
        while True:
            head_data, length = reader.peak_head()
            ret[head_data.tag] = reader.read_any_with_tag(head_data.tag)
    except BufferError:
        return ret


def main():
    data: bytes = bytes.fromhex(sys.argv[1])
    pprint(to_dict(data))


if __name__ == "__main__":
    main()
