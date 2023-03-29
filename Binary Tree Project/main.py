'''
Project:
Author: 
Course: 
Date: 

Description:

Lessons Learned:

'''
from pathlib import Path
from string import whitespace, punctuation
from bst import BST


class Pair:
    ''' Encapsulate letter,count pair as a single entity.
    
    Realtional methods make this object comparable
    using built-in operators. 
    '''
    def __init__(self, letter, count = 1):
        self.letter = letter
        self.count = count
    
    def __eq__(self, other):
        return self.letter == other.letter
    
    def __hash__(self):
        return hash(self.letter)

    def __ne__(self, other):
        return self.letter != other.letter

    def __lt__(self, other):
        return self.letter < other.letter

    def __le__(self, other):
        return self.letter <= other.letter

    def __gt__(self, other):
        return self.letter > other.letter

    def __ge__(self, other):
        return self.letter >= other.letter

    def __repr__(self):
        return f'({self.letter}, {self.count})'
    
    def __str__(self):
        return f'({self.letter}, {self.count})'

def make_tree():
    ''' A helper function to build the tree.
    
    The test code depends on this function being available from main.
    :param: None
    :returns: A binary search tree
    '''
    text_tree = BST()
    with open('Binary Tree Project/around-the-world-in-80-days-3.txt', 'r') as file:
        for line in file:
            for character in line:
                if character != '\n' and character != ' ':
                    text_tree.add(Pair(character))
    return text_tree
def main():
    ''' Program kicks off here.

    '''
    pass
    
if __name__ == "__main__":
    main()

# tree_test = make_tree()
# test_pair = Pair("s")
# print(tree_test.inorder())
# tree_test.remove(Pair('j',1))
# print(tree_test.inorder())
# print(len(tree_test.inorder()))
# print(tree_test._size)

test_bst = BST()

test_bst.add(9)
test_bst.add(10)
test_bst.add(11)
test_bst.add(7)
test_bst.add(8)
test_bst.add(1)
# test_bst.add(6)
# test_bst.add(2)
# test_bst.add(12)
# test_bst.add(3)
# test_bst.add(5)
# test_bst.add(20)
# test_bst.add(-10)
# test_bst.add(-9)
# test_bst.add(-3)
# test_bst.add(-14)
# test_bst.add(7)

print(test_bst.preorder())
test_bst.remove(9)
print(test_bst.preorder())