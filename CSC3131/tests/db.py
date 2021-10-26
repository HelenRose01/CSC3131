import sqlite3

import unittest
from CSC3131.flaskr.db import get_db


class dbTest(unittest.TestCase):
    def test_get_close_db(app):
        db = get_db()
        assert db is get_db()

if __name__ == '__main__':
    unittest.main()
