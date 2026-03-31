class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        vals = list()

        for i in range(len(operations)):
            print(vals)
            e = None
            try:
                e = int(operations[i])
                vals.append(e)
                continue
            except:
                e = operations[i]

            if e == '+':
                vals.append(
                    vals[-1] + vals[-2]
                )
            elif e == 'D':
                vals.append(
                    vals[-1] * 2
                )
            elif e == 'C':
                vals.pop()
        
        return sum(vals)