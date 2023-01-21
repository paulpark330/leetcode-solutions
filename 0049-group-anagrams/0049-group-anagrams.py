class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list) # mapping charCount to list of Anagrams
        
        for str in strs:
            count = [0] * 26
            for c in str:
                count[ord(c) - ord("a")] += 1
            hashmap[tuple(count)].append(str)
        return hashmap.values()
        
