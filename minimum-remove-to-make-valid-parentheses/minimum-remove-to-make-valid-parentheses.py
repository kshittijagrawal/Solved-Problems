class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        braces_n_pos = collections.deque()
        for pos, brace in enumerate(s):
            if brace.isalpha(): continue
            if brace == "(":
                braces_n_pos.append((brace, pos))
            else:
                if len(braces_n_pos) == 0 or braces_n_pos[-1][0] == ")":
                    braces_n_pos.append((brace, pos))
                else:
                    braces_n_pos.pop()
        
        indices = [i[1] for i in braces_n_pos]
        res = ""
        for pos, char in enumerate(s):
            if pos in indices:
                continue
            res += char
        return res