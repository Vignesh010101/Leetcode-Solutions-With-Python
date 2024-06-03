class TextEditor:

    def __init__(self):
        self.tex=""
        self.pos=0

    def addText(self, text: str) -> None:
        self.tex=self.tex[:self.pos]+text+self.tex[self.pos:]
        self.pos+=len(text)

    def deleteText(self, k: int) -> int:
        de=max(self.pos-k,0)
        d=min(self.pos,k)
        self.tex=self.tex[:de]+self.tex[self.pos:]
        self.pos=de
        return d

    def cursorLeft(self, k: int) -> str:
        self.pos=max(0,self.pos-k)
        return self.tex[max(0,self.pos-10):self.pos]

    def cursorRight(self, k: int) -> str:
        self.pos=min(len(self.tex),self.pos+k)
        return self.tex[max(0,self.pos-10):self.pos]

# Your TextEditor object will be instantiated and called as such:
# obj = TextEditor()
# obj.addText(text)
# param_2 = obj.deleteText(k)
# param_3 = obj.cursorLeft(k)
# param_4 = obj.cursorRight(k)