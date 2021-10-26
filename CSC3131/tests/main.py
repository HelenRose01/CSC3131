import unittest


class Test1(unittest.TestCase):
    def test1(self):
        from ./db.py import get_db, init_db
        self.assertEqual(True, True)  # add assertion here


if __name__ == '__main__':
    unittest.main()
