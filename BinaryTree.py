# Binary Tree

# A Binary Tree is a tree that has a left branch and a right branch

# Fill the missing with an empty tree # An instance of tree must have two branches

# Binanry Search Tree

# Each entry larger than all entries on left and smaller than the rights

class Tree:

    def __init__(self, entry, branches = ()):
        self.entry = entry
        for branch in branches:
            assert isinstance(branch, Tree)
        self.branches = list(branches)
    

    def __repr__(self):
        if self.branches:
           branches_repr = ", " +repr(self.branches)
        else:
           branches_repr = ""
        return "Tree({0}{1})".format(self.entry,branches_repr)

class BinaryTree(Tree):
      empty = Tree(None)
      empty.is_empty = True 
      def __init__(self, entry, left = empty, right = empty):
          Tree.__init__(self,entry,(left,right))
          self.is_empty = False

      @property
      def left(self):
          return self.branches[0]
  
      @property
      def right(self):
          return self.branches[1]

Bin = BinaryTree

Bin(3, Bin(1),Bin(7,Bin(5),Bin(9,Bin.empty,Bin(11))))

'''set_contains travels the tree
-If the element is not the entry, it can only be either left or right
- Focusing on one branch, reduce the set about half the recursive call'''



def set_contains(s,v):
    'Check if the Bin contains the element v'
# Most Theata(hight of tree) on average
# Theata(log n) on average for balanced tree
# Order of growth  
    if s.is_empty:                    
       return False                          
    elif s.entry == v:
       return True
    elif s.entry < v:
       return set_contains(s.right,v)
    elif s.entry > v:
       return set_contains(s.left, v)
