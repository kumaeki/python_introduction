# -*- coding: utf-8 -*-
class MyDict(dict):

    def __init__(self , **kw):
        super().__init__(**kw)

    def __getattr__(self,key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self,key,value):
        self[key] = value


import unittest

class TestMyDict(unittest.TestCase):

    def setUp(self):
        print("setUp.......")

    def tearDown(self):
        print("tearDown")

    def test_init(self):
        d = MyDict(a=1,b="test")
        self.assertEqual(d.a,1)
        self.assertEqual(d.b,"test")
        self.assertTrue(isinstance(d,dict))

    def test_key(self):
        d = MyDict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')

    def test_attr(self):
        d = MyDict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')

    def test_keyerror(self):
        d = MyDict()
        with self.assertRaises(KeyError):
            value = d['empty']

    def test_attrerror(self):
        d = MyDict()
        with self.assertRaises(AttributeError):
            value = d.empty