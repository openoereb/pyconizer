# -*- coding: utf-8 -*-


def encode_correctly(string):
    if isinstance(string, unicode):
        string = string.encode('utf8')
    elif isinstance(string, str):
        # Must be encoded in UTF-8
        string.decode('utf8')
    return string
