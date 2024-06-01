class Encrypter:
    def __init__(self, keys: List[str], values: List[str], dictionary: List[str]):
        self.key2value={}
        for k,v in zip(keys,values):
            self.key2value[k]=v
        self.dictionary=Counter()
        for d in dictionary:
            self.dictionary[self.encrypt(d)]+=1

    def encrypt(self, word1: str) -> str:
        res=[]
        for c in word1:
            if c in self.key2value:
                res.append(self.key2value[c])
            else:
                return ""
        return "".join(res)

    def decrypt(self, word2: str) -> int:
        return  self.dictionary[word2]

# Your Encrypter object will be instantiated and called as such:
# obj = Encrypter(keys, values, dictionary)
# param_1 = obj.encrypt(word1)
# param_2 = obj.decrypt(word2)