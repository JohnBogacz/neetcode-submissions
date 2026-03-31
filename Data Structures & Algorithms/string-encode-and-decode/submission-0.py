class Solution:
    def encode(self, strs: List[str]) -> str:
        s_send = ''
        for s in strs:
            s_send += f'{len(s)}' + '#' + s

        return s_send

    def decode(self, s: str) -> List[str]:
        strs = list()

        print(s)

        while len(s) > 0:
            i_hash = s.find('#')
            l = int(s[:i_hash])

            s_sub = s[i_hash+1:i_hash+1+l]
            strs.append(s_sub)

            s = s[i_hash+1+l:]
            print(strs)

        return strs

