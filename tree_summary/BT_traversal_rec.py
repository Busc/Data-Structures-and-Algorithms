'''
example:
              3
             / \
            2   4
           /     \
          1       6
                 / \
                5   7
                     \
                      8
'''

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class recTraversal(object):
    def preOrder(self, root):
        if root is None:
            return
        else:
            print("%d " % root.val),
            self.preOrder(root.left)
            self.preOrder(root.right)

    def inOrder(self, root):
        if root is None:
            return
        else:
            self.inOrder(root.left)
            print("%d " % root.val),
            self.inOrder(root.right)

    def postOrder(self, root):
        if root is None:
            return
        else:
            self.postOrder(root.left)
            self.postOrder(root.right)
            print("%d " % root.val),


if __name__ == "__main__":
    node1 = TreeNode(3)
    node2 = TreeNode(2)
    node3 = TreeNode(4)
    node4 = TreeNode(1)
    node5 = TreeNode(6)
    node6 = TreeNode(5)
    node7 = TreeNode(7)
    node8 = TreeNode(8)
    node1.left = node2
    node1.right = node3
    node2.left = node4
    node3.right = node5
    node5.left = node6
    node5.right = node7
    node7.right = node8
    # python2.7 'print' auto linefeed
    print("\n*****DLR*****")
    recTraversal().preOrder(node1)
    print("\n*****LDR*****")
    recTraversal().inOrder(node1)
    print("\n*****LRD*****")
    recTraversal().postOrder(node1)
