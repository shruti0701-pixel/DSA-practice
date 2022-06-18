class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        first_dif = -1
        sec_dif = -1
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                if first_dif  == -1:
                    first_dif = i
                elif sec_dif  == -1:
                    sec_dif = i    
                else:
                    return False
        return s1[first_dif] == s2[sec_dif] and s1[sec_dif] == s2[first_dif]