class BinarySearchTree:

    """
    This defines the node class. The children can be individually declared or stored
    in a list. We are adding a pos value to help with visualization
    """
# 123
    class node:
        def __init__(self):
            self.element = None
            self.leftchild = None
            self.rightchild = None
            self.parent = None

    """
    This initializes the binary search tree. ht is the height of the tree, sz is the
    number of nodes. You may define this appropriately.
    """

    def __init__(self):
        self.sz = 0
        self.root = None
        self.ht = 0

    """
        This method implements the functionality of finding an element in the tree. The function
        findElement(e) finds the node in the current tree, whose element is e. Depending on the
        value of e and in relation to the current element visited, the algorithm visits the left
        or the right child till the element is found, or an external node is visited. Your
        algorithm can be iterative or recursive

        Output: True if tree contains e or False if e not present in T
    """

    def findElement(self, e, v):
        if(v.element == e):
            print("True")
            return
        elif(v.element > e):
            if(v.leftchild != None):
                self.findElement(e, v.leftchild)
            else:
                print("False")
                return
        else:
            if(v.rightchild != None):
                self.findElement(e, v.rightchild)
            else:
                print("False")
                return
        return

    def returnbalancefac(self, v):
        return self.findHeight(v.leftchild) - self.findHeight(v.rightchild)
    

    def findinEleParent(self, e, v):
        if(v.element >= e):
            if(v.leftchild == None):
                return v

            else:
                t = self.findinEleParent(e, v.leftchild)
        else:
            if(v.rightchild == None):
                return v

            else:
                t = self.findinEleParent(e, v.rightchild)
        return t

    def insertElement(self, e):
        v = self.findinEleParent(e, self.root)
        curnode = self.node()
        # print(1)
        curnode.element = e
        if(v.element > e):
            v.leftchild = curnode
            curnode.parent = v
        else:
            v.rightchild = curnode
            curnode.parent = v
        return

    def restructure(self, x):
        y = x.parent
        z = y.parent
        t = z.parent

        # a, b, c = x, y, z
        # T0, T1, T2, T3 = x.leftchild, x.rightchild, y.rightchild, z.rightchild
        if(z.leftchild == y):
            if(y.leftchild == x):
                a, b, c = x, y, z
                T0, T1, T2, T3 = x.leftchild, x.rightchild, y.rightchild, z.rightchild
            elif(y.rightchild == x):
                a, b, c = y, x, z
                T0, T1, T2, T3 = y.leftchild, x.leftchild, x.rightchild, z.rightchild
        elif(z.rightchild == y):

            if(y.leftchild == x):
                print(1)
                a, b, c = z, x, y
                T0, T1, T2, T3 = z.leftchild, x.leftchild, x.rightchild, y.rightchild
            else:
                l = 2
                print(2)
                a, b, c = z, y, x
                T0, T1, T2, T3 = z.leftchild, y.leftchild, x.leftchild, x.rightchild
        print(l)
        if(z != self.root):
            if(t.leftchild == z):
                t.leftchild = b
            else:
                t.rightchild = b
            b.parent = t
        else:
            self.root = b

        b.leftchild = a
        a.parent = b
        b.rightchild = c
        c.parent = b
        a.leftchild = T0
        if(T0 != None):
            T0.parent = a
        a.rightchild = T1
        if(T1 != None):
            T1.parent = a
        c.leftchild = T2
        if(T2 != None):
            T2.parent = c
        c.rightchild = T3
        if(T3 != None):
            T3.parent = c
        # self.printTree()

    def insertElementAVL(self, e):
        self.insertElement(e)
        w = self.getnode(e, self.root)
        t = w
        while(t != self.root):
            while(t != self.root and (abs(self.returnbalancefac(t)) <= 1)):
                t = t.parent
            if(abs(self.returnbalancefac(t)) > 1):
                z = t
                if(self.findHeight(z.leftchild) > self.findHeight(z.rightchild)):
                    y = z.leftchild
                else:
                    y = z.rightchild
                if(self.findHeight(y.leftchild) > self.findHeight(y.rightchild)):
                    x = y.leftchild
                else:
                    x = y.rightchild
                if(t != self.root):
                    t = t.parent
                self.restructure(x)

        return

    """
        This method inorderTraverse(self,v) performs an inorder traversal of the BST, starting
        from node v which is initially the root and prints the elements of the nodes as they
        are visited. Remember the inorder traversal first visits the left child, followed by
        the parent, followed by the right child. This could be used to print the tree.
    """

    def inorderTraverse(self, v, count, k):
        curnode = v
        if (curnode.leftchild != None):
            self.inorderTraverse(curnode.leftchild, count, k)
        count += 1
        if(count == k):
            print(curnode.element)

        print(curnode.element, end=' ')
        if (curnode.rightchild != None):
            self.inorderTraverse(curnode.rightchild, count, k)

    """
        Given a node v this will return the next element that should be visited after v in the
        inorder traversal.
    """

    def returnNextInorder(self, v):
        v = v.rightchild
        while(v.leftchild != None):
            v = v.leftchild
        return v

    """
        This method deleteElement(self, e), removes the node with element e from the tree T.
        There are three cases:
            1. Deleting a leaf or external node:Just remove the node
            2. Deleting a node with one child: Remove the node and replace it with its child
            3. Deleting a node with two children: Instead of deleting the node replace with
                a) its inorder successor node or b)Inorder predecessor node
	 For AVL call the basic BST delete and do the rotation
    """

    def getnode(self, e, v):
        if(v.element == e):
            return v
        elif(v.element > e):
            return self.getnode(e, v.leftchild)
        elif(v.element < e):
            return self.getnode(e, v.rightchild)

    def deleteElement(self, e):
        v = self.getnode(e, self.root)
        c = self.getChildren(v)
        if(c[0] == None and c[1] == None):
            if(v.parent.leftchild == v):
                v.parent.leftchild = None
            else:
                v.parent.rightchild = None

        elif(c[0] == None and c[1] != None):
            if(v != self.root):
                if(v.parent.leftchild == v):
                    v.parent.leftchild = c[1]
                    c[1].parent = v.parent
                else:
                    v.parent.rightchild = c[1]
                    c[1].parent = v.parent
            else:
                self.root = c[1]
                self.root.parent = None
        elif(c[0] != None and c[1] == None):
            if(v != self.root):
                if(v.parent.leftchild == v):
                    v.parent.leftchild = c[0]
                    c[0].parent = v.parent
                else:
                    v.parent.rightchild = c[0]
                    c[0].parent = v.parent
            else:
                self.root = c[0]
                self.root.parent = None
        else:
            nxt = self.returnNextInorder(v)
            if(nxt.parent.leftchild == nxt):
                nxt.parent.leftchild = nxt.rightchild
            else:
                nxt.parent.rightchild = nxt.rightchild

            v.element = nxt.element
        return

    def deleteElementAVL(self, e):
        x = self.getnode(e, self.root)
        t = self.returnNextInorder(x)
        if(t == None):
            if(x.leftchild == None):
                t = self.getnode(e, self.root).parent
            else:
                t = x.leftchild
        self.deleteElement(e)

        while(t.parent != None):
            while(t != self.root and (abs(self.returnbalancefac(t)) <= 1)):
                t = t.parent
            if(abs(self.returnbalancefac(t)) > 1):
                z = t
                if(self.findHeight(z.leftchild) > self.findHeight(z.rightchild)):
                    y = z.leftchild
                else:
                    y = z.rightchild
                if(self.findHeight(y.leftchild) > self.findHeight(y.rightchild)):
                    x = y.leftchild
                else:
                    x = y.rightchild
                if(t != self.root):
                    t = t.parent
                self.restructure(x)

        return
    """
        Given a list of elements construct a balanced binary search tree
    """

    def createTree(self, items):
        curnode = self.node()
        items.sort()
        if(len(items) == 1):
            curnode.element = items[0]
            return curnode
        if(len(items) % 2):
            mid = (len(items) // 2)
        else:
            mid = (len(items) // 2) - 1

        curnode.element = items[mid]
        if(mid):
            curnode.leftchild = self.createTree(items[:mid])
            # print(curnode.leftchild.element)
            curnode.leftchild.parent = curnode
        curnode.rightchild = self.createTree(items[(mid + 1):])
        # print(curnode.rightchild.element)
        curnode.rightchild.parent = curnode

        self.root = curnode
        return curnode
        """
        There are other support methods which maybe useful for implementing your functionalities.
        These include
            1. isExternal(self,v): which returns true if the node v is external
            2. printTree(self): to visualize the tree for your debugging purposes. You may print it
            using text formatting or use a turtle library given along with the file.
        """

    def isExternal(self, curnode):
        if (curnode.leftchild == None and curnode.rightchild == None):
            return True
        else:
            return False

    def getChildren(self, curnode):
        children = []

        # if curnode.leftchild!= None:
        children.append(curnode.leftchild)
        # if curnode.rightchild!= None:
        children.append(curnode.rightchild)
        return children

    def isExternal(self, curnode):
        if (curnode.leftchild == None and curnode.rightchild == None):
            return True
        else:
            return False

    def preorderTraverse(self, v):
        curnode = v
        print(curnode.element)
        if (curnode.leftchild != None):
            self.preorderTraverse(curnode.leftchild)
        if (curnode.rightchild != None):
            self.preorderTraverse(curnode.rightchild)
        return

    def postorderTraverse(self, v):
        curnode = v
        if (curnode.leftchild != None):
            self.postorderTraverse(curnode.leftchild)
        if (curnode.rightchild != None):
            self.postorderTraverse(curnode.rightchild)
        print(curnode.element)
        return

    def findDepthIter(self, v):
        if v == self.root:
            return 0
        else:
            return 1 + self.findDepthIter(v.parent)

    def findDepth(self, v):
        return self.findDepthIter(self.findElement(v.element, self.root))

    def findHeightIter(self, v):
        if self.isExternal(v):
            return 0

        else:
            h = 0
            if(v.leftchild != None):
                h = max(h, self.findHeightIter(v.leftchild))
            if(v.rightchild != None):
                h = max(h, self.findHeightIter(v.rightchild))
            return 1 + h

    def findHeight(self, v):
        if(v == None):
            return -1
        return self.findHeightIter(v)

    """
     Print the tree so that it can be visualized clearly.
    """

    def printTree(self, v):
        a = []
        a.append(v)
        while(len(a)):
            if(a[0] != None):
                a += self.getChildren(a[0])
            if(a[0] != None):
                print(a.pop(0).element, end=",")
            else:
                print("None", end=",")
                a.pop(0)
        return
