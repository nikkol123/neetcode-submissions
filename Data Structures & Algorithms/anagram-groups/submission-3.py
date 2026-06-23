from collections import defaultdict

class Solution:
    #there are only 26 letters
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res: defaultdict[tuple, list[str]] = defaultdict(list)
        for word in strs:
            counter = [0] * 26
            for char in word:
                counter[ord(char)-ord('a')] +=1
            res[tuple(counter)].append(word)
        return list(res.values())