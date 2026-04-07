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
inorder (root.right)
 def preorder (root):
if root:
 print(root.val,end=' ')
preorder (root.left)
def postorder (root):
preorder (root.right)
if root:
postorder (root.left)
postorder (root.right)
print(root.val,end=' ')
 #Example usage:
 r=node (50)
print(r.val)
inorder(root.right)
def preorder(root):
if root:
print(root.val, end='')
preorder(root.left)
preorder(root.pight)
def postorder(root)：
if root:
postorder(root.left)
postorder(root.right)
print(root.val, end='')
 #Example usage:
r=node(50)
 print(r.val)
p=insert(r, 30)+ r=insert(r, 20)+ print(r.val)+ r=insert(r, 40)+ r=insert(r, 70)+ r=insert(r, 60)+ print(r.val)+ r=insert(r, 80)
 print("Inorder traversal:")
inorder(r)
print("InPreorder traversal:")
preorder(r)
print("(nPostorder traversal:")
 postorder(r)
