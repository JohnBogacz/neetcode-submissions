class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        temp = dict()


        for c in s:
            if c not in temp:
                temp[c] = 1
            else:
                temp[c] += 1
        
        for c in t:
            if c not in temp:
                return False
            else:
                temp[c] -= 1

                if temp[c] == 0:
                    temp.pop(c)
        
        if len(temp) != 0:
            return False
        else:
            return True

