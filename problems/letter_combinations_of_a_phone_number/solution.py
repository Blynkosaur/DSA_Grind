class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        num_to_letter = {"2":["a","b", "c"], "3":["d","e", "f"],"4":["g","h","i"],"5":["j","k", "l"],"6":["m","n", "o"],"7":["p","q", "r", "s"],"8":["t","u", "v"],"9":["w","x", "y","z"]}
        sols = []
        n = len(digits)
        def backtrack(i, curr):
            if i == n:
                sols.append(curr)
                return
            digit = digits[i]
            for letter in num_to_letter[digit]:
                backtrack(i+1, curr + letter)
        backtrack(0,"")
        return sols
            
        