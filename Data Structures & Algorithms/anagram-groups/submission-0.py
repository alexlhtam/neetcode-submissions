class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}

        for string in strs:
            s = "".join(sorted(string))

            if s not in hashmap:
                hashmap[s] = []
            
            hashmap[s].append(string)


        res = []
        for key in hashmap:
            res.append(hashmap[key])

        return res