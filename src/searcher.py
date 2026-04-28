class Searcher:
    def search(self, arr, target):
        l = 0
        r = len(arr) - 1

        while l <= r:
            m = (l + r) // 2

            if arr[m] == target:
                return m
            elif arr[m] < target:
                l = m + 1
            else:
                r = m - 1

        return -1