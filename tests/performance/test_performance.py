import timeit
import unittest

from main import main as main_func


class TestPerformance(unittest.TestCase):

    def test_main_performance(self):
        exec_time = timeit.timeit(lambda: main_func(), number=10)
        self.assertLess(exec_time, 5.0)  # The function should execute within 5 seconds for 10 runs

if __name__ == '__main__':
    unittest.main()
