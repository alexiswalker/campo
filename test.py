# -*- coding: utf-8 -*-
import unittest

from campo import *


class Test(unittest.TestCase):

    pkf = None
    url = 'http://www.pkfsrl.com.ar/modules.php?name=News&new_topic=2'

    def setUp(self):
        self.pkf = PKF(self.url)

    def test_create_class(self):
        self.assertTrue(self.pkf is not None)


if __name__ == '__main__':
    unittest.main()