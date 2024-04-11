class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        indx = []
        arr.sort()
        mabs = arr[1] - arr[0]
        for i in range(len(arr) - 1):
            min_abs = abs(arr[i + 1] - arr[i])

            if min_abs < mabs:
                mabs = min_abs
                indx.clear()
                indx.append([arr[i], arr[i + 1]])

            elif min_abs == mabs:
                indx.append([arr[i], arr[i + 1]])

        
        return indx