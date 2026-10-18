class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        current_max = arr[-1]

        for index, item in reversed(list(enumerate(arr))):
            if current_max  > item:
                arr[index] = current_max
            else:
                arr[index] = current_max
                current_max = item
        arr[-1] = -1

        return arr

