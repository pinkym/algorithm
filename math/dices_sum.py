class Solution:
    # @param {int} n an integer
    # @return {tuple[]} a list of tuple(sum, probability)
    def dicesSum(self, n):
        if n <= 0:
            return []
        p = 1 / 6
        # total dices
        numbers = [1, 2, 3, 4, 5, 6]
        p_list = [p, p, p, p, p, p]

        # new dices
        numbers2 = [1, 2, 3, 4, 5, 6]

        i = 2
        while i <= n:
            new_numbers = []
            new_p = []
            for number in numbers:
                for num in numbers2:
                    new_sum = num + number
                    if new_sum in new_numbers:
                        new_p[new_numbers.index(new_sum)] += p * p_list[numbers.index(number)]
                    else:
                        new_numbers.append(new_sum)
                        new_p.append(p * p_list[numbers.index(number)])
            numbers = new_numbers
            p_list = new_p
            i += 1

        # merge
        sum_p_list = []
        for number, p in zip(numbers, p_list):
            sum_p_list.append([number, p])
        return sum_p_list


if __name__ == '__main__':
    s = Solution()
    print(s.dicesSum(2))
