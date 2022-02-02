def get_avail_letters(nums, prev = ""):
    if len(nums) == 0:
        yield prev
        return

    chars = ["", "", "abc", "def", "ghi", "jkl", "mno", \
             "pqrs", "tuv", "wxyz"]

    for c in chars[nums[0]]:
        yield from get_avail_letters(nums[1:], prev + c)

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        nums = [ int(i) for i in digits ]
        
        answers = list(get_avail_letters(nums))
        if len(answers) == 1:
            return []
        return answers
