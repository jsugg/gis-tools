import argparse
import unittest
from unittest.mock import patch

import pandas as pd

from features.polygon_calculation import polygon


class TestPolygon(unittest.TestCase):

    def setUp(self):
        self.data = pd.DataFrame({
            'longitude': [0, 1, 1, 0],
            'latitude': [0, 0, 1, 1]
        })
        self.results = {}
        self.unit = 'km'

    @patch('features.polygon_calculation.polygon.read_data')
    def test_calculate_area(self, mock_read_data):
        mock_read_data.return_value = self.data
        expected_area = 1.0  # For the given data
        actual_area = polygon.calculate_area(self.data, self.unit, self.results)
        self.assertEqual(expected_area, actual_area)

    @patch('features.polygon_calculation.polygon.read_data')
    def test_calculate_perimeter(self, mock_read_data):
        mock_read_data.return_value = self.data
        expected_perimeter = 4.0  # For the given data
        actual_perimeter = polygon.calculate_perimeter(self.data, self.unit, self.results)
        self.assertEqual(expected_perimeter, actual_perimeter)

    @patch('features.polygon_calculation.polygon.read_data')
    @patch('features.polygon_calculation.polygon.calculate_area')
    @patch('features.polygon_calculation.polygon.calculate_perimeter')
    @patch('features.polygon_calculation.polygon.display_and_write_results')
    def test_main(self, mock_display_and_write_results, mock_calculate_perimeter, mock_calculate_area, mock_read_data):
        mock_read_data.return_value = self.data
        mock_calculate_area.return_value = 1.0
        mock_calculate_perimeter.return_value = 4.0

        with patch('argparse.ArgumentParser.parse_args', return_value=argparse.Namespace(file='some_file.csv', url=None, area=True, perimeter=True, decimal_separator=',', unit='km')):
            polygon.main()

        mock_display_and_write_results.assert_called_once()

if __name__ == '__main__':
    unittest.main()
