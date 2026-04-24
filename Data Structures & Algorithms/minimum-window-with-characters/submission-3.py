class Solution:
    def minWindow(self, s: str, t: str) -> str:
        s_len = len(s)
        t_len = len(t)
        t_hash: dict[str, int] = {}
        for t_char in t:
            t_hash[t_char] = t_hash.get(t_char, 0) + 1

        # we update haves when the count matches t_hash
        have = 0
        left = 0
        need = len(t_hash)
        window_hash = {}
        smallest_sub = ""
        for right in range(s_len):
            char = s[right]
            window_hash[char] = window_hash.get(char, 0) + 1
            if char in t_hash and window_hash[char] == t_hash[char]:
                have += 1
            while have == need:
                curr_valid_sub = s[left : right + 1]
                if not smallest_sub or len(curr_valid_sub) < len(smallest_sub):
                    smallest_sub = curr_valid_sub
                if s[left] in window_hash:
                    window_hash[s[left]] -= 1
                
                if s[left] in t_hash and window_hash[s[left]]<t_hash[s[left]]:
                    have-=1
                left += 1
        return smallest_sub
