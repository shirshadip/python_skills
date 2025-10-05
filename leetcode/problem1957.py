#deleting characters to make fancy string

class Solution(object):


    def makeFancyString(self, s: str) -> str:
        """
        :type s: str
        :rtype: str
        """
        result = []
        for c in s :
            if len(result)>=2 and result [-1] == result [-2] == c:
                continue 
            result.append(c)
        return "".join(result)

sol = Solution()
print(sol.makeFancyString("leeetcode"))
print(sol.makeFancyString("aaabaaaa"))
print(sol.makeFancyString("aab"))
