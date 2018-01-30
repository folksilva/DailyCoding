"""
This problem was asked by Google.

Given the root to a binary tree, implement serialize(root), which serializes the tree into a string,
and deserialize(s), which deserializes the string back into the tree.

"""

import pytest

class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

class Tree:
    def __init__(self):
        self.root = None

    def addNode(self, node, value):
        if node == None:
            self.root = Node(value)
        else:
            if value < node.value:
                if not node.left:
                    node.left = Node(value)
                else:
                    self.addNode(node.left, value)
            else:
                if not node.right:
                    node.right = Node(value)
                else:
                    self.addNode(node.right, value)


def serialize(root):
    values = []
    def serializer(node):
        if not node:
            values.append('?')
        else:
            values.append(str(node.value))
            serializer(node.left)
            serializer(node.right)
    serializer(root)
    return ','.join(values)

def deserialize(s):
    values = iter(s.split(','))
    def deserializer():
        val = next(values)
        if val == '?':
            return None
        else:
            node = Node(int(val))
            node.left = deserializer()
            node.right = deserializer()
            return node
    return deserializer()


@pytest.fixture
def tree():
    numbers = [1, 3, 4, 2, 6, 7]
    theTree = Tree()
    for number in numbers:
        theTree.addNode(theTree.root, number)
    return theTree


def test_serialize(tree):
    s1 = serialize(tree.root)
    assert s1 == '1,?,3,2,?,?,4,?,6,?,7,?,?'


def test_deserialize(tree):
    s1 = serialize(tree.root)
    s2 = deserialize(s1)
    assert s2.__class__ == Node