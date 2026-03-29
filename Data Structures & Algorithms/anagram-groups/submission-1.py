class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_dict = defaultdict(list)

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - count("a")] += 1

            my_dict[tup[le(count)].append(s)]
        return my_dict.values