import unittest
from sort.bubble_sort import bubblesort

data=  [5, 2, 9, 1, 5, 6]

class TestBubbleSort(unittest.TestCase):
    def test_bubble_sort(self, data):
        data = [5, 2, 9, 1, 5, 6]
        expected = [1, 2, 5, 5, 6, 9]
        sorter = bubblesort(data) 
        sorter.bubbleSort()
        sorted_data = sorter.bubbleSort()
        self.assertEqual(sorted_data, expected)
    


if __name__ == '__main__':
    unittest.main()

