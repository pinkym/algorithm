class Solution:
    """
    @param: nums: A list of integers.
    @return: A list of permutations.
    """
    def permute(self, nums):
        if len(nums) == 0:
            return [[]]
        permute_list = [[nums[0]]]

        i = 1
        while i < len(nums):
            tmp_list = []
            for permute in permute_list:
                for index in range(len(permute) + 1):
                    # python list copy uses a lot of time, use it carefully
                    tmp_list.append(permute[:index] + [nums[i]] + permute[index:])
            permute_list = tmp_list
            i += 1

        return permute_list


if __name__ == '__main__':
    data = [1, 2, 3, 4]
    s = Solution()
    print(s.permute(data))
    print(len(s.permute(data)))
