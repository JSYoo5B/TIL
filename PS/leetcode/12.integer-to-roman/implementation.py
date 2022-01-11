class Solution:
    def intToRoman(self, num: int) -> str:
        answer = ""
        # Last digit
        if num % 10 == 9:
            answer += 'XI'
            num -= 9
        elif num % 10 == 4:
            answer += 'VI'
            num -= 4
        else:
            for _ in range(num % 5):
                answer += 'I'
            num -= (num % 5)
            if num % 10 == 5:
                answer += 'V'
                num -= 5
        # ten's digit
        num //= 10
        if num % 10 == 9:
            answer += 'CX'
            num -= 9
        elif num % 10 == 4:
            answer += 'LX'
            num -= 4
        else:
            for _ in range(num % 5):
                answer += 'X'
            num -= (num % 5)
            if num % 10 == 5:
                answer += 'L'
                num -= 5
        # hundred's digit
        num //= 10
        if num % 10 == 9:
            answer += 'MC'
            num -= 9
        elif num % 10 == 4:
            answer += 'DC'
            num -= 4
        else:
            for _ in range(num % 5):
                answer += 'C'
            num -= (num % 5)
            if num % 10 == 5:
                answer += 'D'
                num -= 5        
        # hundred's digit
        num //= 10
        for _ in range(num % 5):
            answer += 'M'
        num -= (num % 5)
        answer = answer[::-1]
        return answer
