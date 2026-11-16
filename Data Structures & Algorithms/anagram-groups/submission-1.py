from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagrams = defaultdict(list)

        for word in strs:
            key = "".join(sorted(word))

            if key in anagrams:
                anagrams[key].append(word)

            else:
                anagrams[key] = [word]

        
        return list(anagrams.values())
