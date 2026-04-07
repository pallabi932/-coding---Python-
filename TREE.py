class node:
def__init_(self, key):
self.left=None
self.right=None
self.val=key
def insert(root, key):
if root is None:
return node(key)
else:
if root.val<key:
root.right=insert(root.right, key)
else:
root.left=insert(root.left, key)
return root
 def inorder(root)：
if root:
inorder(root.left)
print(root.val, end=' ')
