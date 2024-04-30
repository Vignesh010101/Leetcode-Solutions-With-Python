class Solution:
    def interpret(self, command: str) -> str:
        vy=[]
        for i in range(len(command)):
            if command[i]=="G":
                vy.append("G")
            elif command[i]=="(":
                if command[i+1]==")":
                    vy.append("o")
                elif command[i+1]=="a":
                    vy.append("al")
        
        return "".join(vy)
            