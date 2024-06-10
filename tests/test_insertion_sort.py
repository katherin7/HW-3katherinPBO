import unittest
from sort.insertion_sort import InsertionSort

class TestInsertionSort(unittest.TestCase):

    def test_insertion_sort(self):
        data = [5, 2, 9, 1, 5, 6]
        expected = [1, 2, 5, 5, 6, 9]
        sorter = InsertionSort(data)
        sorter.sort()
        sorted_data = sorter.get_sorted_data()
        self.assertEqual(sorted_data, expected)

    def test_insertion_sort_is_sorted(self):
        data = [5, 2, 9, 1, 5, 6]
        sorter = InsertionSort(data)
        sorter.sort()
        self.assertTrue(sorter.is_sorted())


if __name__ == '__main__':
    unittest.main()

