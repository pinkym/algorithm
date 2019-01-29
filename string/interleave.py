class Solution:
    """
    @param s1: A string
    @param s2: A string
    @param s3: A string
    @return: Determine whether s3 is formed by interleaving of s1 and s2

    Example:
        For s1 = "aabcc", s2 = "dbbca"
        When s3 = "aadbbcbcac", return true.
        When s3 = "aadbbbaccc", return false.
    """

    def isInterleave(self, s1, s2, s3):
        i = j = 0
        start_from_s1 = True
        while start_from_s1 and i < len(s1) and s1[i] == s3[i + j] or j < len(s2) and s2[j] == s3[i + j]:

            delta = 0
            if start_from_s1:
                # find the most equal string in s1
                while i < len(s1) and s3[i + j] == s1[i]:
                    i += 1
                    delta += 1

                # if the char of s2 in (most equal string index + 1) is not equal to s3[i + j]，
                # but the char of s2 in (most equal string index ) is equal to s3[i + j]
                # and the delta is bigger than 1
                # let the most equal string shorter, in order to interleave string
                while 1 < delta and (i + j) < len(s3) and j < len(s2) and not s3[i + j] == s2[j]:
                    delta -= 1
                    i -= 1
                start_from_s1 = False
            else:
                # find the most equal string in s2
                while j < len(s2) and s3[i + j] == s2[j]:
                    j += 1
                    delta += 1

                while 1 < delta and (i + j) < len(s3) and i < len(s1) and not s3[i + j] == s1[i]:
                    delta -= 1
                    j -= 1

                start_from_s1 = True

        if (i + j) == len(s3):
            return True
        else:
            return False


if __name__ == '__main__':
    s = Solution()
    print(s.isInterleave(
        "abbcddef",
        "accbbbcd",
        "abbcddefaccbbbdc"))
