import unittest
from unittest.mock import patch

from utils import logger


class TestLogger(unittest.TestCase):

    @patch('logging.getLogger')
    def test_setup_logger(self, mock_getLogger):
        logger.setup_logger("some_run_id")
        mock_getLogger.assert_called_once()

if __name__ == '__main__':
    unittest.main()
