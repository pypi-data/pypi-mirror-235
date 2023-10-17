"""
Validates the package
copyright: (c) 2023 by Kourosh Parsa.
"""
import unittest
import az_sights
from unittest.mock import patch


class TestInsights(unittest.TestCase):
    """ tests app insights result conversion """

    @patch('az_sights.check_extensions')
    @patch('az_sights.execute', return_value=('{"tables": [{"columns": [{"name": "id"}, {"name": "label"}], "rows": ["a", "b"]}]}', '', 0))
    def test_query_today(self, mock_check_extensions, mock_execute):
        res = az_sights.query_today('app_id', 'some query')
        self.assertEqual(res, [{'id': 'a'}, {'id': 'b'}])


if __name__ == '__main__':
    unittest.main()
