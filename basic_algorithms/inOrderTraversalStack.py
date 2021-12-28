"""
Inorder: left -> mid -> right
1) Create an empty stack S
2) Initialize current node as root
3) Push the current node to S and set current = current->left until current is NULL
4) If current is Null and stack is not empty then
  a) Pop the top item from stack
  b) Print the popped item, set current = popped_item->right
  c) Go to step 3
5) if current is null and stack is empty then we are done
"""
class Node:
  def __init__(self,data):
    self.data = data
    self.left = None
    self.right = None

def inorderTreeStack(root):
  inorder = []
  s = []
  curr = root
  while True:
    if curr is not None:
      s.append(curr)
      curr = curr.left
    elif len(s) > 0:
      top = s.pop(-1)
      inorder.append(top.data)
      curr = top.right
    else:
      return inorder
  return

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

res = inorderTreeStack(root)
print(res)

