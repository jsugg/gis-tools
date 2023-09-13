import unittest
from unittest.mock import patch

from main import main as main_func


class TestIntegration(unittest.TestCase):

    @patch('features.polygon_calculation.polygon.main')
    @patch('utils.logger.setup_logger')
    @patch('utils.file_handler.create_directories')
    def test_main_integration(self, mock_create_directories, mock_setup_logger, mock_polygon_main):
        main_func()
        mock_create_directories.assert_called_once()
        mock_setup_logger.assert_called_once()
        mock_polygon_main.assert_called_once()

if __name__ == '__main__':
    unittest.main()
