class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_hash = {}
        for word in strs:
            alphabet_counts = [0]*26
            for letter in word:
                alphabet_counts[ord(letter)-ord('a')] +=1
            alphabet_counts_tuple = tuple(alphabet_counts)
            if alphabet_counts_tuple in word_hash:
                word_hash[alphabet_counts_tuple].append(word)
                continue
            word_hash[alphabet_counts_tuple] = [word]
        
        return list(word_hash.values())


            