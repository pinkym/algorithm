class TreeNode:
    """
    Definition of TreeNode:
    """
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param root: An object of TreeNode, denote the root of the binary tree.
    This method will be invoked first, you should design your own algorithm
    to serialize a binary tree which denote by a root node to a string which
    can be easily deserialized by your own "deserialize" method later.
    """
    def serialize(self, root):
        string = ""
        if root is None:
            return string + "#"
        else:
            string += str(root.val)

        return string + "," + self.serialize(root.left) + "," + self.serialize(root.right)


    """
    @param data: A string serialized by your serialize method.
    This method will be invoked second, the argument data is what exactly
    you serialized at method "serialize", that means the data is not given by
    system, it's given by your own serialize method. So the format of data is
    designed by yourself, and deserialize it here as you serialize it in
    "serialize" method.
    """
    # this class variable remembers the index of the first unvisited node
    data_string = 0

    def deserialize(self, data):
        if type(data) == str:
            data = data.split(",")

        node_val = data[0]
        self.data_string = data[1:]

        if len(data) == 0 or node_val == "#":
            return None
        elif node_val != "#":
            n = TreeNode(node_val)
            n.left = self.deserialize(self.data_string)
            n.right = self.deserialize(self.data_string)

        return n


root = TreeNode(0)
n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)
n5 = TreeNode(5)
n6 = TreeNode(6)
n7 = TreeNode(7)

root.left = n1
root.right = n2
n1.right = n3
n2.left = n4
n2.right = n5
n4.left = n6
n4.right = n7

s = Solution()
# print(s.addquote(s.serialize(root)))
print(s.serialize(root))

# deserialize test
serialize_data = s.serialize(root)
deserialize_data = s.deserialize(serialize_data)

print(deserialize_data.val)
print(deserialize_data.left.val)
print(deserialize_data.left.right.val)
# print(s.deserialize(data).right.val)
print(s.serialize(deserialize_data))



