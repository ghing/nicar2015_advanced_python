import unittest

import mock

from pycar_advanced.db import get_default_db
from pycar_advanced.decorators import run_query

class DecoratorTestCase(unittest.TestCase):
    # The Database class is actually defined in dataset.persistance.database,
    # but you should mock where it's used.  In this case, dataset (in the
    # connect() function).  For more on where to patch, see
    # http://mock.readthedocs.org/en/latest/patch.html#where-to-patch
    @mock.patch('dataset.Database')
    def test_run_query(self, MockDatabase):
        query = "SELECT * FROM results"
        
        def query_fn():
            return query

        # db should be an instance of MagicMock because of our patch decorator
        db = get_default_db()

        # Decorate the query function
        query_executing_fn = run_query(query_fn, db)
        # Run the decorated function
        query_executing_fn()

        # Test that db.query() was called with our SQL string
        db.query.assert_called_with(query)

    @mock.patch('__builtin__.print')
    @mock.patch('dataset.Database')
    def test_run_query_show_sql(self, MockDatabase, mock_print):
        query = "SELECT * FROM results"
        
        def query_fn():
            return query

        # db should be an instance of MagicMock because of our patch decorator
        db = get_default_db()

        # Decorate the query function
        query_executing_fn = run_query(query_fn, db)
        # Run the decorated function
        query_executing_fn(show_sql=True)

        # Test that db.query() was called with our SQL string
        db.query.assert_called_with(query)

        # Test that sys.stdout.write was called with our SQL string
        mock_print.assert_called_with(query)

    @mock.patch('dataset.Database')
    def test_run_dry_run(self, MockDatabase):
        query = "SELECT * FROM results"
        
        def query_fn():
            return query

        # db should be an instance of MagicMock because of our patch decorator
        db = get_default_db()

        # Decorate the query function
        query_executing_fn = run_query(query_fn, db)
        # Run the decorated function
        query_executing_fn(dry_run=True)

        self.assertEqual(db.query.called, False)
