class Solution:
    def comb(self, digits: str, index: int, comb: str, phone_dict: dict[int, str]) -> None:
        if index == len(digits):
            self.res.append(comb)
            return None

        chars = phone_dict[int(digits[index])]

        for char in chars:
            self.comb(digits=digits, index=index + 1, comb=comb + char, phone_dict=phone_dict)


    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        phone_dict = {
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz",
        }
        self.res = []
        self.comb(digits=digits, index=0, comb="",phone_dict=phone_dict)

        return self.res
