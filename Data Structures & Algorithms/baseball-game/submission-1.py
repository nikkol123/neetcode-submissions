class Solution:
    def calPoints(self, operations: List[str]) -> int:
        out=[]
        for i in range(len(operations)):
            if operations[i] == "+":
                res = out[-1]+out[-2]
                out.append(res)
            elif operations[i] == "D":
                res=out[-1]*2
                out.append(res)
            elif operations[i] == "C":
                out.pop()  
            else:
                out.append(int(operations[i]))    
        scoretotal=0
        for score in out:
            scoretotal+=score
        return scoretotal
