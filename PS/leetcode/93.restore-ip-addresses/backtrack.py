class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        answers = []
        
        def get_valid_tokens(s: str):
            for i in range(1, 4):
                token = s[:i]
                if i > 1 and token[0] == '0':
                    return
                if i == 3 and int(token) > 255:
                    return
                yield token
        
        firsts = get_valid_tokens(s)
        for fir in firsts:
            offset = len(fir)
            if len(s) - offset < 1:
                break
            seconds = get_valid_tokens(s[offset:])
            for sec in seconds:
                offset = len(fir) + len(sec)
                if len(s) - offset < 1:
                    break
                thirds = get_valid_tokens(s[offset:])
                for thi in thirds:
                    offset = len(fir) + len(sec) + len(thi)
                    if len(s) - offset < 1:
                        break
                    last = s[offset:]
                    if len(last) > 1 and last[0] == '0':
                        continue
                    elif len(last) == 3 and int(last) > 255:
                        continue
                    elif len(last) > 3:
                        continue
                    answer = fir + '.' + sec + '.' + thi + '.' + last
                    answers.append(answer)
        return answers
