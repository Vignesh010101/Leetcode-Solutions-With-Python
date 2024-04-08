class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        # initially we split the given sentence based on the delimiter as space
        # and make it into two separate lists
        list1 = s1.split(' ')
        list2 = s2.split(' ')
        hashMap = defaultdict(int)
        answerList = []
        # counting the ocuurences of all words of sentence1
        for i in list1:
            hashMap[i] = hashMap[i] + 1

        # counting the ocuurences of all words of sentence2
        for i in list2:
            hashMap[i] = hashMap[i] + 1

        # those words that appears once are considers as not present in both the sentences
        for i in hashMap:
            if hashMap[i] == 1:
                answerList.append(i)

        return answerList