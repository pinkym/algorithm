class MinStack:
    index = 0
    stack = []
    sorted_list = []

    def __init__(self):
        # do intialization if necessary
        # min = None
        index = 0
        stack = []
        sorted_list = []

    """
    @param: number: An integer
    @return: nothing
    """

    def push(self, number):
        # write your code here
        self.stack.append(number)
        self.index += 1

        if not self.sorted_list:
            self.sorted_list.append(number)
        else:

            # elif number > self.sorted_list[index]:
            #     self.sorted_list.insert(index, number)
            # elif number < self.sorted_list[0]:
            #     self.sorted_list.insert(0, number)
            # else:
            i = 0
            while self.sorted_list[i] < number:
                i += 1
            self.sorted_list.insert(i, number)

    """
    @return: An integer
    """

    def pop(self):
        # write your code here
        if not self.stack:
            return None
        self.index -= 1
        self.sorted_list.remove(self.stack[self.index])
        return self.stack[self.index]

    """
    @return: An integer
    """

    def min(self):
        # write your code here
        return self.sorted_index[0]


ms = MinStack()
print(ms.push(3))
print(ms.pop())