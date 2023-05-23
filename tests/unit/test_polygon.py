import unittest
from unittest.mock import patch, Mock
from pytest_html import extras
from ...polygon.polygon import read_data, write_results, calculate_area, calculate_perimeter
import pandas as pd

class TestFunctions(unittest.TestCase):
#    @patch('requests.get')
#    def test_read_data_url(self, mock_get):
#        mock_get.return_value.ok = True
#        mock_get.return_value.text = 'longitude,latitude\n-73.98,40.75\n-73.99,40.75\n-73.99,40.74\n-73.98,40.74\n-73.98,40.75'
#        data = read_data(url='http://test.com/test.csv')
#        self.assertEqual(data.shape, (5, 2))

#    def test_calculate_area(self):
#        data = pd.DataFrame({'longitude': [-73.98, -73.99, -73.99, -73.98, -73.98], 'latitude': [40.75, 40.75, 40.74, 40.74, 40.75]})
#        area = calculate_area(data, "cm")
#        self.assertAlmostEqual(area, 0.88, places=2)

#    def test_calculate_perimeter(self):
#        data = pd.DataFrame({'longitude': [-73.98, -73.99, -73.99, -73.98, -73.98], 'latitude': [40.75, 40.75, 40.74, 40.74, 40.75]})
#        perimeter = calculate_perimeter(data, "cm")
#        self.assertAlmostEqual(perimeter, 3.51, places=2)

    @patch('json.dump')
    def test_write_results(self, mock_dump):
        write_results('1234', '2023-05-19 12:00:00', 'coordenadas.csv', None, 0.88, 3.51, 'km')
        mock_dump.assert_called()

    # More tests to come ...

if __name__ == '__main__':
    unittest.main()
