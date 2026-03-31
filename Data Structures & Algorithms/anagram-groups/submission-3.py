class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        temp = dict()

        for s in strs:
            y = [0 for _ in range(0, 26)]
            for c in s:
                y[ord(c)-ord('a')] += 1
            y = tuple(y)
            
            if y not in temp:
                temp[y] = [s]
            else:
                temp[y].append(s)
        
        result_list = list()
        for v in temp.values():
            result_list.append(v)
        
        return result_list