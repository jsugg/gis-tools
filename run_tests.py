import unittest
import glob

# Define the test loader
loader = unittest.TestLoader()

# Use glob to find all test files in the 'tests' directory
test_files = glob.glob('tests/test_*.py')

# Create test suites for each test file and load them
suites = [loader.loadTestsFromName(f'tests.{file[:-3]}') for file in test_files]

# Create a test suite that combines all test suites
all_tests_suite = unittest.TestSuite(suites)

# Run the tests
unittest.TextTestRunner().run(all_tests_suite)
