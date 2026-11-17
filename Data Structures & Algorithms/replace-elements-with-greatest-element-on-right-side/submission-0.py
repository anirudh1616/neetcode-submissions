class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # 1. Traverse the array in reverse order
        # 2. compare the current index, to the current set num and set that position to equal that.
        max_elem = -1
        for i in range(len(arr) -1, -1, -1):
            newMax = max(max_elem, arr[i])
            arr[i] = max_elem
            max_elem = newMax

        return arr