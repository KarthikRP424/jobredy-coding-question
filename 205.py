class Solution(object):
    def isIsomorphic(self, s, t):
        char_map = {}
        reverse_map = {}

        for i in range(len(s)):

            if s[i] in char_map:
                if char_map[s[i]] != t[i]:
                    return False

            else:
                if t[i] in reverse_map:
                    return False

                char_map[s[i]] = t[i]
                reverse_map[t[i]] = s[i]

        return True
    
    
print(Solution().isIsomorphic("egg", "add"))  # True