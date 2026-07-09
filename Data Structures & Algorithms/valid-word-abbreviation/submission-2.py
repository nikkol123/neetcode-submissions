class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        leftWord, leftAbbr = 0, 0

        while leftAbbr < len(abbr):
            if abbr[leftAbbr].isdigit():
                if abbr[leftAbbr] == "0":
                    return False
                count = 0
                while leftAbbr < len(abbr) and abbr[leftAbbr].isdigit():
                    count = count * 10 + int(abbr[leftAbbr])
                    leftAbbr += 1
                leftWord += count
                if leftWord > len(word):
                    return False
            else:
                if leftWord >= len(word) or abbr[leftAbbr] != word[leftWord]:
                    return False
                leftWord += 1
                leftAbbr += 1

        return leftWord == len(word)