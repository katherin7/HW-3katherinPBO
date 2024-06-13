<h3>Katherin monica pypi package and test</h3>
<hr>

## Introduction
This repository contains Python implementations of the quick sort algorithm and corresponding test cases. The quicksort.py file provides the sorting functionality, while the test_quicksort.py file contains unit tests to verify its correctness.

## Usage
To use the quick sort,bubble sort, insertion sort, implementation, follow these steps:

- Import the Quicksort class from quick_sort.py.
- Import the Bubblesort class from bubble_sort.py. 
- Import the Insertionsort class from insertion_sort.py.
- Create an instance of Quicksort.
- Create an instance of Bubblesort.
- Create an instance of Insertionsort.
- Call the quicksort() method on your input data.
- Call the bubblesort() method on your input data.
- Call the insertionsort() method on your input data.

## example 
from quicksort import Quicksort

data = [5, 2, 9, 1, 5, 6]
sorter = Quicksort()
sorted_data = sorter.quicksort(data)
print("Sorted data:", sorted_data)

## Unit Tests
The test_quick_sort.py, test_bubble_sort.py, test_insertion_sort.py, file contains test cases for the quick sort algorithm, bubble sort algorithm, insertion algorithm . It ensures that the sorting function produces the expected output for various input arrays.

## Running Tests
To run the tests, execute the following command in your terminal:

python -m unittest test_quicksort.py

## Conclusion
The quick sort algorithm, bubble sort algorithm, insertion algorithm  is a powerful sorting technique, and thorough testing ensures its correctness. Feel free to explore the code and experiment with different input data!
