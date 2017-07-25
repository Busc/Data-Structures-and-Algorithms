# -*-coding:utf-8 -*-

'''
二叉排序树(Binary Sort Tree)/二叉查找(搜索)树(Binary Search Tree):
1) 若左子树不空，则左子树上所有结点的值均小于(不大于)它的根结点的值
2) 若右子树不空，则右子树上所有结点的值均大于(不小于)它的根结点的值
3) 非空的左右子树也都是二叉排序树
'''

# 二叉树节点类
class BST_Node(object):
    def __init__(self, value):
        self.val = value
        self.l_child = None
        self.r_child = None

# 二叉查找树类
class BSTree(object):
    def __init__(self, root):
        self.root = root

    def create_tree(self):
        # 怎样把树先建起来？？
        pass

    def levelorder(self):
        '''
        层次顺序遍历(广度优先:从上倒下+从左到右)
        :return:遍历结果
        '''
        travResult=[]
        if not self.root:
            return travResult
        curr_level = [self.root]
        while curr_level:
            travResult.append(curr_level)
            next_level = []
            for tempNode in curr_level:
                if tempNode.l_child:
                    next_level.append(tempNode.l_child)
                if tempNode.r_child:
                    next_level.append(tempNode.r_child)
            curr_level = next_level
        return travResult
    def preorder_rec(self):

        return
    def inorder_rec(self):
    def postorder_rec(self):
    def preorder_nonrec(self):
    def inorder_nonrec(self):
    def postorder_nonrec(self):





