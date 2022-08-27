class Node:
    def __init__(self, data=None):
        self.left = None
        self.right = None
        self.data = data


def create_tree(l, root):
    tree = root
    for a, b in l:
        root = tree
        for pos, i in enumerate(b):
            if pos == (len(b) - 1):
                if i == "0":
                    root.left = Node(a)
                else:
                    root.right = Node(a)
            else:
                if i == "0":
                    if root.left is None:
                        root.left = Node()
                    root = root.left
                else:
                    if root.right is None:
                        root.right = Node()
                    root = root.right


k = int(input())
l = []

for i in range(k):
    a, b = [x for x in input().split(" ")]
    l.append((a, b))

sequence = input()

root_node = Node()

node = root_node


create_tree(l, root_node)

for i in sequence:
    if i == "0":
        node = node.left
    else:
        node = node.right
    if node.data is not None:
        print(node.data, end="")
        node = root_node
