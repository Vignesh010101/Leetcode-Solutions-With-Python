from collections import OrderedDict

# sort x and returning it
def mySort(x):
        x.sort()
        return x

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # get unique words from list
        uniqueWords = tuple(words);
        
        dict = {}
        # initializing dict = 0
        for i in uniqueWords :
            dict[i] = 0 ;

        # counting no of words
        for i in words:
            dict[i] += 1 ;    

        # sorting dict in decending order
        dict = {key: value for key, value in sorted(dict.items(), key=lambda item: item[1]  , reverse = True ) }

        keys = list(dict.keys())
        values = list(dict.values())
        i , j  = 0 , 0 
        output = []

        # sorting the words with same count Lexicographically
        while i != len(values) and j != len(values):
            if( values[i] == values[j] ):
                j += 1
            else:
                output = output + mySort(keys[i:j]) 
                i = j
        output = output + mySort(keys[i:j]) 
        
        return output[0:k]                  