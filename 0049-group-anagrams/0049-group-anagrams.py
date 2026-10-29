class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        strstable={}
        for string in strs:
            sortedstring=''.join(sorted(string))
            if sortedstring not in strstable:
                strstable[sortedstring] = []
            strstable[sortedstring].append(string)
        return list(strstable.values())

        