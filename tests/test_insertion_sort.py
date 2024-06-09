from src.sort import InsertionSort

def main():
    data = [64, 34, 25, 12, 22, 11, 90, 88, 76, 55, 43, 21, 99, 77, 66]
    insertion_sort = InsertionSort(data)
    print("Sorting steps:")
    insertion_sort.print_step_by_step()
    insertion_sort.sort()
    sorted_data = insertion_sort.get_sorted_data()
    print("\nSorted data:", sorted_data)
    is_sorted = insertion_sort.is_sorted()
    print("Is data sorted?", is_sorted)
if __name__ == "__main__":
    main()
