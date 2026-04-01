class Solution:
    def isValid(self, s: str) -> bool:
        l = list()

        while len(s) > 0:
            val = s[0]
            s = s[1:]

            if val in ['(', '[', '{']:
                l.append(val)
            elif val not in ['(', '[', '{'] and len(l) == 0:
                return False
            else:
                l_val = l.pop()

                if l_val == '(' and val != ')':
                    return False
                elif l_val == '[' and val != ']':
                    return False
                elif l_val == '{' and val != '}':
                    return False
        
        return len(s) == 0 and len(l) == 0