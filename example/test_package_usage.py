from sort.insertion_sort import InsertionSort

def main():
    data = [64, 34, 25, 12, 22, 11, 90]
    sorter = InsertionSort(data)
    sorter.sort()
    sorted_data = sorter.get_sorted_data()
    print("Sorted data:", sorted_data)

    if sorter.is_sorted():
        print("The data is sorted.")
    else:
        print("The data is not sorted.")

if __name__ == "__main__":
    main()
