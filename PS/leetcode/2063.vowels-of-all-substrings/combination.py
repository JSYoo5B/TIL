#!/usr/bin/env python3

class Solution:
    def countVowels(self, word: str) -> int:
        answer = 0
        for i in range(len(word)):
            c = word[i]
            if c in 'aeiou':
                answer += (i+1)*(len(word)-i)
        return answer
