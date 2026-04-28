import time
from sorter import Sorter
from searcher import Searcher

class Experiment:
    def __init__(self):
        self.s = Sorter()
        self.sh = Searcher()

    def measure_sort_time(self, arr, t):
        copy = arr.copy()

        start = time.perf_counter_ns()

        if t == "basic":
            self.s.basic_sort(copy)
        else:
            self.s.advanced_sort(copy)

        end = time.perf_counter_ns()
        return end - start

    def measure_search_time(self, arr, target):
        start = time.perf_counter_ns()
        self.sh.search(arr, target)
        end = time.perf_counter_ns()
        return end - start

    def run_all(self):
        sizes = [10, 100, 1000]

        for size in sizes:
            print("\nArray size:", size)

            random_arr = self.s.generate_random_array(size)

            sorted_arr = random_arr.copy()
            self.s.advanced_sort(sorted_arr)

            target = random_arr[size // 2]

            print("\nRandom array")

            b1 = self.measure_sort_time(random_arr, "basic")
            m1 = self.measure_sort_time(random_arr, "advanced")

            self.s.advanced_sort(random_arr)
            s1 = self.measure_search_time(random_arr, target)

            print("Bubble:", b1, "ns")
            print("Merge:", m1, "ns")
            print("Binary:", s1, "ns")

            print("\nSorted array")

            b2 = self.measure_sort_time(sorted_arr, "basic")
            m2 = self.measure_sort_time(sorted_arr, "advanced")
            s2 = self.measure_search_time(sorted_arr, target)

            print("Bubble:", b2, "ns")
            print("Merge:", m2, "ns")
            print("Binary:", s2, "ns")