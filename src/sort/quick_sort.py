class Quicksort:
    def __init__(self,arr):
        self.arr = arr
        pass

    def quicksort(self, arr):
        """
        Fungsi ini mengurutkan array menggunakan algoritma quicksort.
        """
        if len(arr) <= 1:
            return arr
        else:
            pivot = arr[0]
            less_than_pivot = [x for x in arr[1:] if x <= pivot]
            greater_than_pivot = [x for x in arr[1:] if x > pivot]
            return self.quicksort(less_than_pivot) + [pivot] + self.quicksort(greater_than_pivot)
