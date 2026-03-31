class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        problem_dict = dict()
        for word in strs:
            key = ''.join(sorted(word))
            print(key)
            
            if key not in problem_dict:
                problem_dict[key] = [word]
            
            else:
                problem_dict[key].append(word)
        
        return list(problem_dict.values())