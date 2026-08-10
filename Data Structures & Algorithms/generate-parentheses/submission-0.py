class Solution:
    def generate_paranthesis(self, valid_paranthesis: str, open_paranthesis_count: int, closed_paranthesis_count: int, n: int)->None:

        if closed_paranthesis_count == n:
            # main exit condition, i.e. a valid iteration
            self.res.append(valid_paranthesis)
            return None

        if open_paranthesis_count<n:
            self.generate_paranthesis(
                valid_paranthesis=valid_paranthesis + "(",
                open_paranthesis_count=open_paranthesis_count+1,
                closed_paranthesis_count=closed_paranthesis_count,
                n=n
            )

        if open_paranthesis_count!=closed_paranthesis_count:
            self.generate_paranthesis(
                valid_paranthesis=valid_paranthesis + ")",
                open_paranthesis_count=open_paranthesis_count,
                closed_paranthesis_count=closed_paranthesis_count+1,
                n=n
            )


    def generateParenthesis(self, n: int) -> List[str]:
        self.res = []
        self.generate_paranthesis(valid_paranthesis="",
        open_paranthesis_count=0, 
        closed_paranthesis_count=0,
         n=n)
        return self.res