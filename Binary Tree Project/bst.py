

class BST:
    
    class BSTNode:
        def __init__(self, key = None):
            self.key = key
            self.left_child = None
            self.right_child = None
            self.parent = None
    def __init__(self):
        self._root = None
        self._size = 0
        self._height = 0

    def find(self, value):
        def find_recursive(self, value, node):
            if node == None:
                raise ValueError("item isn't in the tree.")
            elif node.key == value:
                return node
            else:
                if value < node.key:
                    return find_recursive(self, value, node.left_child)
                else:
                    return find_recursive(self, value, node.right_child)
        return find_recursive(self, value, self._root)

    def add(self, value): 
        new_node = BST.BSTNode(value)
        #if statement if the bst is empty
        if self._size == 0:
            self._root = new_node
            self._size += 1
        else:
            current = self._root
            #runs this loop as long as the current node isn't empty; starts at the root
            while current != None:
                if current.key > new_node.key:
                    if current.left_child == None:
                        current.left_child = new_node
                        new_node.parent = current
                        current = None
                        self._size += 1
                    else:
                        current = current.left_child
                elif current.key < new_node.key:
                    if current.right_child == None:
                        current.right_child = new_node
                        new_node.parent = current
                        current = None
                        self._size += 1
                    else: 
                        current = current.right_child
                else:
                    if type(value) != int:
                        current.key.count = current.key.count + 1
                        current = None
                    else:
                        if current.right_child == None:
                            current.right_child = new_node
                            new_node.parent = current
                            current = None
                            self._size += 1
                        else: 
                            current = current.right_child
                    
        return self

    def print_tree(self, node):
          if node is not None:
            self.print_tree(node.left_child)
            print(node.key)
            self.print_tree(node.right_child)
    
    def remove(self, item):
        try:
            removal_node = self.find(item)
        except ValueError:
            return
        removal_node = self.find(item)
        if type(item) != int:
            
            removal_node.key.count = removal_node.key.count - 1
            return self
        #if node to remove has no children: 
        if removal_node.left_child == None and removal_node.right_child == None:
            #if node to remove is the root:
            if removal_node.parent == None:
                self._root = None
            elif removal_node.parent.left_child == removal_node:
                removal_node.parent.left_child = None
            elif removal_node.parent.right_child == removal_node:
                removal_node.parent.right_child = None
        #if node to remove has a left child:
        elif removal_node.left_child != None and removal_node.right_child == None:
            #if node to remove is the root:
            if removal_node.parent == None:
                self._root = removal_node.left_child
                removal_node.left_child.parent == None
            else:
                removal_node.parent.left_child = removal_node.left_child
        #if node to remove has a right child:
        elif removal_node.right_child != None and removal_node.left_child == None:
            #if node to remove is the root:
            if removal_node.parent == None:
                self._root = removal_node.right_child
                removal_node.right_child.parent == None
            else:
                removal_node.parent.right_child = removal_node.right_child
        #if node to remove has two children:
        else: 
        # Find successor
            current = removal_node.right_child
            while current.left_child is not None:
                current = current.left_child
            temp_key = current.key
            self.remove(current.key)
            removal_node.key = temp_key
        self._size = self._size -1
        return self
    
    def inorder(self):
        lyst = []
        def inorder_recurs(self, node, lyst):
            if node != None:
                inorder_recurs(self, node.left_child,lyst)
                lyst.append(node.key)
                inorder_recurs(self, node.right_child,lyst)
            return lyst
        inorder_recurs(self,self._root, lyst)
        return lyst

    def postorder(self):
        lyst = []
        def postorder_recurs(self, node, lyst):
            if node != None:
                postorder_recurs(self, node.left_child,lyst)
                postorder_recurs(self, node.right_child,lyst)
                lyst.append(node.key)
            return lyst
        postorder_recurs(self,self._root,lyst)
        return lyst


    def preorder(self):
        lyst = []
        def preorder_recurs(self, node, lyst):
            if node != None:
                lyst.append(node.key)
                preorder_recurs(self, node.left_child,lyst)
                preorder_recurs(self, node.right_child,lyst)
            return lyst
        preorder_recurs(self,self._root, lyst)
        return lyst

    def is_empty(self):
        if self._root == None:
            return True
        return False
    
    def height(self):
        if self.is_empty() == True:
            return -1
        def height_recurs(self, node):
            if node == None:
                return -1
            left_height = height_recurs(self,node.left_child)
            right_height = height_recurs(self,node.right_child)
            return 1 + max(left_height,right_height)
        return height_recurs(self, self._root)

    
            

        




