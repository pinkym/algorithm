class Solution:
    """
    Given a list of numbers with duplicate number in it. Find all unique permutations.
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
                    new_permute = permute[:index] + [nums[i]] + permute[index:]
                    if new_permute not in tmp_list:
                        tmp_list.append(new_permute)
            permute_list = tmp_list
            i += 1

        return permute_list


if __name__ == '__main__':
    data = [1, 2, 2, 4, 4]
    s = Solution()
    print(s.permute(data))
    print(len(s.permute(data)))
