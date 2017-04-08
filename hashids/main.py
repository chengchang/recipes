# coding: utf-8

import hashlib
from hashids import Hashids
# Hashids: generate short unique ids from integers


def int_hash_id(integer, salt='this is my salt'):
    """
    int <-> id
    :param salt: 
    :param integer: 
    :return:
    """
    hashids = Hashids(salt=salt)

    short_id = hashids.encode(integer)
    assert integer == hashids.decode(short_id)[0]
    print short_id


def str_hash_id(string):
    """
    str <-> id
    :param string: 
    :return:
    """
    hex_str = string.encode('hex')
    num = int(hex_str, 16)
    int_hash_id(num)

    assert string == hex_str.decode('hex')
    assert hex_str == format(num, 'x')


def md5_hash_id(string):
    """
    str -> md5 <-> id
    :param string: 
    :return: 
    """
    hex_str = hashlib.md5(string).hexdigest()
    num = int(hex_str, 16)
    int_hash_id(num)


if __name__ == '__main__':
    int_hash_id(1234)
    str_hash_id('hello world')
    str_hash_id('hello world, hello world, hello world')
    md5_hash_id('hello world')
    md5_hash_id('hello world, hello world, hello world')
