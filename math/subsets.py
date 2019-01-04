class Solution:
    """
    @param nums: A set of numbers
    @return: A list of lists
    """

    def subsets_recursive(self, nums):
        if len(nums) == 0:
            return [[]]

        subsets_list = []
        for subset in self.subsets_recursive(nums[:-1]):
            if not len(subset) == 0:
                subsets_list.append(sorted(subset + [nums[-1]]))
        subsets_list.append([nums[-1]])

        return subsets_list + self.subsets_recursive(nums[:-1])

    def subsets(self, nums):
        subsets = [[]]
        if len(nums) == 0:
            return subsets

        i = 0
        while i < len(nums):
            subsets_list = []
            for subset in subsets:
                if not subset == []:
                    subsets_list.append(sorted(subset + [nums[i]]))
            subsets_list.append([nums[i]])
            subsets += subsets_list
            i += 1

        return subsets


if __name__ == '__main__':
    data = [1, 2, 3]
    s = Solution()
    print(s.subsets(data))
    print(len(s.subsets(data)))

    print(s.subsets_recursive(data))
    print(len(s.subsets_recursive(data)))

