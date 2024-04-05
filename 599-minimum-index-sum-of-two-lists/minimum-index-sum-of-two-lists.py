class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        res, listDict_1 = {}, {}
        ans = []
        for i in range(len(list1)):
            listDict_1[list1[i]] = i
        for j in range(len(list2)):
            if list2[j] in listDict_1:
                res[list2[j]] = j + listDict_1[list2[j]]
        min_value = min(res.values())
        ans = [key for key, value in res.items() if value == min_value]
        return ans
        