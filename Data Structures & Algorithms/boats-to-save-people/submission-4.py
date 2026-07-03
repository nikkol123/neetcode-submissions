class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        print(people)
        out=0
        left, right = 0, len(people)-1
        while left<right:
            print(people[left])
            print(people[right])
            if people[left]==limit:
                left+=1
                out+=1
            elif people[right]==limit:
                right-=1
                out+=1
            elif people[left]+people[right]>limit:
                out+=1
                right-=1
            elif people[left]+people[right]<=limit:
                left+=1
                right-=1
                out+=1
            
        if left==right:
            out+=1
        return out