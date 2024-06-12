import unittest
from sort.quick_sort import Quicksort 

class TestQuicksort(unittest.TestCase):
    def test_quicksort(self):
        data = [5, 2, 9, 1, 5, 6]
        expected = [1, 2, 5, 5, 6, 9]
        sorter = Quicksort()
        sorted_data = sorter.quicksort(data)
        self.assertEqual(sorted_data, expected)

if __name__ == '__main__':
    unittest.main()
