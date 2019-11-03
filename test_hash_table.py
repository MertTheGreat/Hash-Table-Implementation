import unittest
from HashTable import *


class HashTableTest(unittest.TestCase):

    def test_insert(self):
        '''
        Test Hash Table class for setting, getting and itteration
        :return:
        '''
        self.my_hash = HashTable(10)
        self.my_hash.set('ali', 100)
        self.my_hash.set('kadir', 200)
        self.my_hash.set('halil', 300)
        self.my_hash.set('hayri', 400)
        self.my_hash.set('cevdet', 500)
        self.my_hash.set('celal', 600)
        # Test for values
        self.assertEqual(100, self.my_hash.get('ali'))
        self.assertEqual(200, self.my_hash.get('kadir'))
        self.assertEqual(300, self.my_hash.get('halil'))
        self.assertEqual(400, self.my_hash.get('hayri'))
        self.assertEqual(500, self.my_hash.get('cevdet'))
        self.assertEqual(600, self.my_hash.get('celal'))
        # Test for keys
        self.assertEqual('ali', self.my_hash.index(100))
        self.assertEqual('kadir', self.my_hash.index(200))
        self.assertEqual('halil', self.my_hash.index(300))
        self.assertEqual('hayri', self.my_hash.index(400))
        self.assertEqual('cevdet', self.my_hash.index(500))
        self.assertEqual('celal', self.my_hash.index(600))
        # Test for iteration
        self.new_hash = HashTable(3)
        self.new_hash.set('a', 1)
        self.new_hash.set('b', 2)
        self.new_hash.set('c', 3)
        iterable = iter(self.new_hash)
        self.assertEqual(next(iterable), 3)
        self.assertEqual(next(iterable), 1)
        self.assertEqual(next(iterable), 2)
        self.assertRaises(StopIteration, next, iterable)


if __name__ == '__main__':
    unittest.main()
