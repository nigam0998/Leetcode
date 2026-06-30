class Solution:
    def wordPattern(self, pattern, s):
        words = s.split()
        if len(pattern) != len(words):
            return False
        map1 = {}
        map2 = {}
        for i in range(len(pattern)):
            if pattern[i] in map1:
                if map1[pattern[i]] != words[i]:
                    return False
            else:
                map1[pattern[i]] = words[i]
            if words[i] in map2:
                if map2[words[i]] != pattern[i]:
                    return False
            else:
                map2[words[i]] = pattern[i]

        return True