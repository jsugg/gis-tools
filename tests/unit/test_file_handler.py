import unittest
from unittest.mock import patch

from utils import file_handler


class TestFileHandler(unittest.TestCase):

    @patch('os.makedirs')
    def test_create_directories(self, mock_makedirs):
        file_handler.create_directories()
        self.assertEqual(mock_makedirs.call_count, 1)

if __name__ == '__main__':
    unittest.main()
