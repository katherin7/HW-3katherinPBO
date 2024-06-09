class InsertionSort:
    def __init__(self, data):
        self.data = data

    def sort(self):
        for i in range(1, len(self.data)):
            key = self.data[i]
            j = i - 1
            while j >= 0 and key < self.data[j]:
                self.data[j + 1] = self.data[j]
                j -= 1
            self.data[j + 1] = key

    def get_sorted_data(self):
        return self.data

    def print_step_by_step(self):

        for i in range(1, len(self.data)):
            key = self.data[i]
            j = i - 1
            while j >= 0 and key < self.data[j]:
                self.data[j + 1] = self.data[j]
                j -= 1
            self.data[j + 1] = key
            print(f"Step {i}: {self.data}")

    def is_sorted(self):

        return all(self.data[i] <= self.data[i + 1] for i in range(len(self.data) - 1))
