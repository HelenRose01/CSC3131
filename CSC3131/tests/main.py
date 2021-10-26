import unittest


class Test1(unittest.TestCase):
    def test1(self):
        from CSC3131.flaskr.db import get_db, init_db
        self.assertEqual(True, True)  # add assertion here


if __name__ == '__main__':
    unittest.main()
