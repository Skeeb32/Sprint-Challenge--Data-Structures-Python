import time

class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # The left sebtree of a node contains only nodes with keys lesser than the nodes key
    # The right sebtree of a node contains only nodes with keys legreatersser than the nodes key
    # The left and the right subtree each must also be a binary search tree. There must be no duplicate nodes.
    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        else: # Value is greater than or equal to 
            if self.right is None:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):        
        # if node is none
        # return false
        # if node.value == findvalue
        #     return True
        # else:
        #     if find < node.value
        #         find on left nodes
        #     else:
        #         find on right node
        if self.value == target:
            return True
        if target < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(target)
        else: 
            if self.right is None:
                return False
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        # if there's a right:
        if self.right:
        # get max on right
            return self.right.get_max()
        #else
        else:
            return self.value
        # return node.value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node == None:
            return
        self.in_order_print(node.left)
        print(node.value)
        self.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        Queue().enqueue(node)
        while Queue().len() > 0:
            temp = Queue().dequeue()
            print(temp.value)
            if temp.left:
                Queue().enqueue(temp.left)
            if temp.right:
                Queue().enqueue(temp.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        Stack().push(node)
        while Stack().len() > 0:
            temp = Stack().pop()
            print(temp.value)
            if temp.left:
                Stack().push(temp.left)
            if temp.right:
                Stack().push(temp.right)
start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
for name_1 in names_1:
    for name_2 in names_2:
        if name_1 == name_2:
            duplicates.append(name_1)

b = BinarySearchTree(names_1[0])

for i in range(1, len(names_1)):
    b.insert(names_1[i])

for j in names_2:
    if b.contains(j):
        duplicates.append(j)
end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
