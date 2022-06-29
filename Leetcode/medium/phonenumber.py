class Solution:
    def letterCombinations(self, digits: str):
        mapper = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        mapped_letters = []
        output_len = len(digits)
        for i in digits:
            mapped_letters.append(mapper.get(i))

        if output_len == 1:
            return self.find_combo(mapped_letters[0], [])
        combo = []

        for i in range(len(mapped_letters) - 1, -1, -1):
            if i == 0:
                return combo
            combo = self.find_combo(mapped_letters[i - 1], combo or mapped_letters[i])
        return combo

    def find_combo(self, first_letter, other_letters):
        combo = []
        for i in first_letter:
            if not other_letters:
                combo.append(i)
                continue
            for j in other_letters:
                combo.append(i+j)
        return combo


op = Solution().letterCombinations("3568")

print(op)

