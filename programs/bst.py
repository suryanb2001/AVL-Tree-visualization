from vpython import *
# GlowScript 3.1 VPython
#import math
#import copy

#from vpython import *
#import math
#import copy


class node:
    def __init__(self):
        self.element = None
        self.leftchild = None
        self.rightchild = None
        self.lvl = None
        self.parent = None
        self.shape = None
        self.pos = None
        self.label = None
        self.lefta = None
        self.righta = None


class BinarySearchTree:
    def __init__(self):
        self.rightstartteta = 0
        self.leftstartteta = pi
        self.dict = {}
        self.root = node()
        self.glist = []
        self.spheres = []

    def searchpath(self, e, v):
        if v.element == e:
            v.shape.color = color.blue
        elif v.element > e:
            v.shape.color = color.green
            self.searchpath(e, v.leftchild)
        else:
            v.shape.color = color.green
            self.searchpath(e, v.rightchild)

    def getfull(self, x):
        curnode = x
        self.glist.append(curnode.shape)
        if curnode.leftchild != None:
            self.glist.append(curnode.lefta)
        if curnode.rightchild != None:
            self.glist.append(curnode.righta)
        if (curnode.leftchild != None):
            self.getfull(curnode.leftchild)
        if (curnode.rightchild != None):
            self.getfull(curnode.rightchild)

    def levelorder(self, root):
        if root is None:
            return

        queue = []
        nodes = [root.shape, root.label]
        queue.append(root)

        while(len(queue) > 0):
            curr = queue.pop(0)

            if curr.leftchild is not None:
                nodes.append(curr.leftchild.shape)
                nodes.append(curr.leftchild.label)
                nodes.append(curr.lefta)
                queue.append(curr.leftchild)

            if curr.rightchild is not None:
                nodes.append(curr.rightchild.shape)
                nodes.append(curr.rightchild.label)
                nodes.append(curr.righta)
                queue.append(curr.rightchild)
        return nodes

    def print(self, x):
        curnode = x
        #print(curnode.shape.pos)
        if (curnode.leftchild != None):
            self.print(curnode.leftchild)
        if (curnode.rightchild != None):
            self.print(curnode.rightchild)

    def restu(self, x):
        y = x.parent
        z = y.parent
        t = z.parent
        #print(x.element)
        #print(y.element)
        #print(z.element)
        T1, T2, T3, T4 = None, None, None, None

        # leftleftcase
        if z.leftchild == y and y.leftchild == x:
            if z.rightchild == None:
                z.lefta.length = 0
                z.lefta = None
                for i in range(10):
                    z.shape.pos += vector(0.3, -0.4, 0)
                    z.label.pos += vector(0.3, -0.4, 0)
                    rate(7)
            else:
                z.lefta.length = 0
                z.lefta = None
                zsub = [z.shape, z.label, z.righta] + \
                    self.levelorder(z.rightchild)

                for j in range(10):
                    for i in zsub:
                        i.pos += vector(0.3, -0.4, 0)
                    rate(7)
            if y.rightchild == None:
                ysub = self.levelorder(y)
                for j in range(10):
                    for i in ysub:
                        i.pos += vector(0.3, 0.4, 0)
                    rate(7)
                y.righta = arrow(pos=y.shape.pos, axis=z.shape.pos -
                                 y.shape.pos, shaftwidth=0.2, length=5)
            else:
                y.righta.length = 0
                y.righta = None
                ysub = [y.shape, y.label, y.lefta] + \
                    self.levelorder(y.leftchild)
                for j in range(10):
                    for i in ysub:
                        i.pos += vector(0.3, 0.4, 0)
                    rate(7)
                y.righta = arrow(pos=y.shape.pos, axis=z.shape.pos -
                                 y.shape.pos, shaftwidth=0.2, length=5)
                z.lefta = arrow(
                    pos=z.shape.pos, axis=y.rightchild.shape.pos - z.shape.pos, shaftwidth=0.2, length=5)
            temp = z.parent
            z.leftchild = y.rightchild
            if(z.leftchild != None):
                z.leftchild.parent = z
            y.rightchild = z
            z.parent = y
            if(z == self.root):
                self.root = y
                y.parent = None
            else:
                y.parent = temp
                if temp.element > y.element:
                    y.parent.leftchild = y
                else:
                    y.parent.rightchild = y

        # leftrightcase
        elif z.leftchild == y and y.rightchild == x:
            if y.leftchild == None:
                y.righta.length = 0
                y.righta = None
                for j in range(10):
                    y.shape.pos += vector(-0.3, -0.4, 0)
                    y.label.pos += vector(-0.3, -0.4, 0)
                rate(7)
            else:
                y.righta.length = 0
                y.righta = None
                ysub = [y.shape, y.label, y.lefta] + \
                    self.levelorder(y.leftchild)
                for j in range(10):
                    for i in ysub:
                        i.pos += vector(-0.3, -0.4, 0)
                    rate(7)
            if x.rightchild == None:
                if x.leftchild == None:
                    for j in range(10):
                        x.shape.pos += vector(-0.3, 0.4, 0)
                        x.label.pos += vector(-0.3, 0.4, 0)
                        rate(7)
                else:
                    x.lefta.length = 0
                    x.lefta = None
                    for j in range(10):
                        x.shape.pos += vector(-0.3, 0.4, 0)
                        x.label.pos += vector(-0.3, 0.4, 0)
                        rate(7)
                x.lefta = arrow(pos=x.shape.pos, axis=y.shape.pos -
                                x.shape.pos, shaftwidth=0.2, length=5)
            else:
                if x.leftchild == None:
                    xsub = [x.shape, x.label, x.righta] + \
                        self.levelorder(x.rightchild)
                    for j in range(10):
                        for i in xsub:
                            i.pos += vector(-0.3, 0.4, 0)
                        rate(7)
                else:
                    x.lefta.length = 0
                    x.lefta = None
                    xsub = [x.shape, x.label, x.righta] + \
                        self.levelorder(x.rightchild)
                    for j in range(10):
                        for i in xsub:
                            i.pos += vector(-0.3, 0.4, 0)
                        rate(7)
                x.lefta = arrow(pos=x.shape.pos, axis=y.shape.pos -
                                x.shape.pos, shaftwidth=0.2, length=5)
            if x.leftchild != None:
                #print(y)
                #print(x.leftchild)
                y.righta = arrow(
                    pos=y.shape.pos, axis=x.leftchild.shape.pos - y.shape.pos, shaftwidth=0.2, length=5)
            z.leftchild = x
            x.parent = z
            temp = x.leftchild
            if x.leftchild != None:
                y.rightchild = temp
                temp.parent = y
            else:
                y.rightchild = None
            x.leftchild = y
            y.parent = x
            # after this
            x, y = y, x
            if z.rightchild == None:
                z.lefta.length = 0
                z.lefta = None
                for j in range(10):
                    z.shape.pos += vector(0.3, -0.4, 0)
                    z.label.pos += vector(0.3, -0.4, 0)
                    rate(7)
            else:
                z.lefta.length = 0
                z.lefta = None
                zsub = [z.shape, z.label, z.righta] + \
                    self.levelorder(z.rightchild)
                for j in range(10):
                    for i in zsub:
                        i.pos += vector(0.3, -0.4, 0)
                        rate(7)
            if y.rightchild == None:
                ysub = self.levelorder(y)
                for j in range(10):
                    for i in ysub:
                        i.pos += vector(0.3, 0.4, 0)
                    rate(7)
                y.righta = arrow(pos=y.shape.pos, axis=z.shape.pos -
                                 y.shape.pos, shaftwidth=0.2, length=5)
            else:
                y.righta.length = 0
                y.righta = None
                ysub = [y.shape, y.label, y.lefta] + \
                    self.levelorder(y.leftchild)
                for j in range(10):
                    for i in ysub:
                        i.pos += vector(0.3, 0.4, 0)
                    rate(7)
                y.righta = arrow(pos=y.shape.pos, axis=z.shape.pos -
                                 y.shape.pos, shaftwidth=0.2, length=5)
                z.lefta = arrow(
                    pos=z.shape.pos, axis=y.rightchild.shape.pos - z.shape.pos, shaftwidth=0.2, length=5)
            temp = z.parent
            z.leftchild = y.rightchild
            if(z.leftchild != None):
                z.leftchild.parent = z
            y.rightchild = z
            z.parent = y
            if(z == self.root):
                self.root = y
                y.parent = None
            else:
                y.parent = temp
                if temp.element > y.element:
                    y.parent.leftchild = y
                else:
                    y.parent.rightchild = y

        # RightRightCase
        elif z.rightchild == y and y.rightchild == x:
            if z.leftchild == None:
                z.righta.length = 0
                z.righta = None
                for j in range(10):
                    z.shape.pos += vector(-0.3, -0.4, 0)
                    # label direction changing
                    z.label.pos += vector(-0.3, -0.4, 0)
                    rate(7)
            else:
                z.righta.length = 0
                z.righta = None
                zsub = [z.shape, z.label, z.lefta] + \
                    self.levelorder(z.leftchild)
                for j in range(10):
                    for i in zsub:
                        i.pos += vector(-0.3, -0.4, 0)
                    rate(7)
            if y.leftchild == None:
                ysub = self.levelorder(y)
                for j in range(10):
                    for i in ysub:
                        i.pos += vector(-0.3, 0.4, 0)
                    rate(7)
                y.lefta = arrow(pos=y.shape.pos, axis=z.shape.pos -
                                y.shape.pos, shaftwidth=0.2, length=5)
            else:
                y.lefta.length = 0
                y.lefta = None
                ysub = [y.shape, y.label, y.righta] + \
                    self.levelorder(y.rightchild)
                for j in range(10):
                    for i in ysub:
                        i.pos += vector(-0.3, 0.4, 0)
                    rate(7)
                y.lefta = arrow(pos=y.shape.pos, axis=z.shape.pos -
                                y.shape.pos, shaftwidth=0.2, length=5)
                z.righta = arrow(
                    pos=z.shape.pos, axis=y.leftchild.shape.pos - z.shape.pos, shaftwidth=0.2, length=5)
            temp = z.parent
            z.rightchild = y.leftchild
            if z.rightchild != None:
                z.rightchild.parent = z
            y.leftchild = z
            z.parent = y
            if z == self.root:
                self.root = y
                y.parent = None
            else:
                y.parent = temp
                if temp.element > y.element:
                    y.parent.leftchild = y
                else:
                    y.parent.rightchild = y

        # RightLeftCase
        elif z.rightchild == y and y.leftchild == x:
            if y.rightchild == None:
                y.lefta.length = 0
                y.lefta = None
                for j in range(10):
                    y.shape.pos += vector(0.3, -0.4, 0)
                    y.label.pos += vector(0.3, -0.4, 0)
                    rate(7)
            else:
                y.lefta.length = 0
                y.lefta = None
                ysub = [y.shape, y.label, y.righta] + \
                    self.levelorder(y.rightchild)
                for j in range(10):
                    for i in ysub:
                        i.pos += vector(0.3, -0.4, 0)
                    rate(7)
            if x.leftchild == None:
                if x.rightchild == None:
                    for j in range(10):
                        x.shape.pos += vector(0.3, 0.4, 0)
                        x.label.pos += vector(0.3, 0.4, 0)
                        rate(7)
                else:
                    x.righta.length = 0
                    x.righta = None
                    for j in range(10):
                        x.shape.pos += vector(0.3, 0.4, 0)
                        x.label.pos += vector(0.3, 0.4, 0)
                        rate(7)
                x.righta = arrow(pos=x.shape.pos, axis=y.shape.pos -
                                 x.shape.pos, shaftwidth=0.2, length=5)
            else:
                if x.rightchild == None:
                    xsub = [x.shape, x.label, x.lefta] + \
                        self.levelorder(x.leftchild)
                    for j in range(10):
                        for i in xsub:
                            i.pos += vector(0.3, 0.4, 0)
                        rate(7)
                else:
                    x.righta.length = 0
                    x.righta = None
                    xsub = [x.shape, x.label, x.lefta] + \
                        self.levelorder(x.leftchild)
                    for j in range(10):
                        for i in xsub:
                            i.pos += vector(0.3, 0.4, 0)
                        rate(7)
                x.righta = arrow(pos=x.shape.pos, axis=y.shape.pos -
                                 x.shape.pos, shaftwidth=0.2, length=5)
            if x.rightchild != None:
                y.lefta = arrow(
                    pos=y.shape.pos, axis=x.rightchild.pos - y.shape.pos, shaftwidth=0.2, length=5)
            z.rightchild = x
            x.parent = z
            temp = x.rightchild
            if x.rightchild != None:
                y.leftchild = temp
                temp.parent = y
            else:
                y.leftchild = None
            x.rightchild = y
            y.parent = x
            # starts here
            if z.leftchild == None:
                z.righta.length = 0
                z.righta = None
                for j in range(10):
                    z.shape.pos += vector(-0.3, -0.4, 0)
                    z.label.pos += vector(-0.3, -0.4, 0)
                    rate(7)
            else:
                z.righta.length = 0
                z.righta = None
                zsub = [z.shape, z.label, z.lefta] + \
                    self.levelorder(z.leftchild)
                for j in range(10):
                    for i in zsub:
                        i.pos += vector(-0.3, -0.4, 0)
                    rate(7)
            if x.leftchild == None:
                xsub = self.levelorder(x)
                for j in range(10):
                    for i in xsub:
                        i.pos += vector(-0.3, 0.4, 0)
                    rate(7)
                x.lefta = arrow(pos=x.shape.pos, axis=z.shape.pos -
                                x.shape.pos, shaftwidth=0.2, length=5)
            else:
                x.lefta.length = 0
                x.lefta = None
                xsub = [x.shape, x.label, x.righta] + \
                    self.levelorder(x.rightchild)
                for j in range(10):
                    for i in xsub:
                        i.pos += vector(-0.3, 0.4, 0)
                    rate(7)
                x.lefta = arrow(pos=x.shape.pos, axis=z.shape.pos -
                                x.shape.pos, shaftwidth=0.2, length=5)
                z.righta = arrow(
                    pos=z.shape.pos, axis=x.leftchild.shape.pos - z.shape.pos, shaftwidth=0.2, length=5)
            temp = z.parent
            z.rightchild = x.leftchild
            if z.rightchild != None:
                z.rightchild.parent = z
            x.leftchild = z
            z.parent = x
            if z == self.root:
                self.root = x
                x.parent = None
            else:
                x.parent = temp
                if temp.element > x.element:
                    x.parent.leftchild = x
                else:
                    x.parent.rightchild = x

    def findinEleParent(self, e, v, lvl):
        if(v.element >= e):
            try:
                if(v.leftchild == None):
                    return [v, lvl + 1]

                else:
                    t = self.findinEleParent(e, v.leftchild, lvl + 1)
            except:
                return [v, lvl + 1]
        else:
            try:
                if(v.rightchild == None):
                    return [v, lvl + 1]

                else:
                    t = self.findinEleParent(e, v.rightchild, lvl + 1)
            except:
                return [v, lvl + 1]
        return t

    def getnode(self, e, v):
        if(v.element == e):
            return v
        elif(v.element > e):
            return self.getnode(e, v.leftchild)
        elif(v.element < e):
            return self.getnode(e, v.rightchild)

    def insertElementAVL(self, e):
        t = self.insertElement(e)

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
                self.restu(x)

    def insertElement(self, e):
        curnode = self.root
        #print("the curnode", curnode.element)
        while(True):
            #print("425 node is", curnode.element)
            if curnode.element > e:

                if curnode.leftchild == None:
                    break
                else:
                    curnode = curnode.leftchild
            else:
                #print(432)
                if curnode.rightchild == None:
                    break
                else:
                    curnode = curnode.rightchild
        rootpos = curnode.shape.pos
        if curnode.element > e:
            pos1 = vector(rootpos.x - 3, rootpos.y - 4, 0)
        else:
            pos1 = vector(rootpos.x + 3, rootpos.y - 4, 0)
        newnode = node()
        newnode.element = e
        newnode.parent = curnode
        if curnode.element > e:
            newnode.parent.leftchild = newnode
            curnode.lefta = arrow(
                pos=curnode.shape.pos, axis=pos1 - curnode.shape.pos, length=5, shaftwidth=0.2)
        else:
            curnode.righta = arrow(
                pos=curnode.shape.pos, axis=pos1 - curnode.shape.pos, length=5, shaftwidth=0.2)
            newnode.parent.rightchild = newnode
        rate(7)
        newnode.shape = sphere(pos=pos1, radius=1, color=color.red)
        newnode.label = label(pos=newnode.shape.pos, text=str(
            newnode.element), xoffset=0, yoffset=0, height=10, border=3, font='sans')
        self.spheres.append(newnode)
        return newnode

    def isExternal(self, curnode):
        if (curnode.leftchild == None and curnode.rightchild == None):
            return True
        else:
            return False

    def createTree(self, items, pos, r=5):
        curnode = node()
        rootpos = pos

        rate(1)
        curnode.shape = sphere(pos=rootpos, radius=1, color=color.red)
        curnode.pos = rootpos

        items.sort()
        if(len(items) == 1):
            curnode.element = items[0]
            curnode.label = label(pos=curnode.shape.pos, text=str(
                curnode.element), xoffset=0, yoffset=0, height=10, border=3, font='sans')
            #print(items[0])
            self.spheres.append(curnode)
            return curnode
        if(len(items) % 2):
            mid = (len(items) // 2)
        else:
            mid = (len(items) // 2) - 1

        curnode.element = items[mid]
        curnode.label = label(pos=curnode.shape.pos, text=str(
            curnode.element), xoffset=0, yoffset=0, height=10, border=3, font='sans')
        self.spheres.append(curnode)
        #print(curnode.element)
        # labelling done here

        if(mid):
            parentx = curnode.pos.x
            parenty = curnode.pos.y
            pos = vector(parentx - 3, parenty - 4, 0)
            curnode.leftchild = self.createTree(items[:mid], pos)
            if curnode.leftchild != None:
                curnode.lefta = arrow(
                    pos=curnode.pos, axis=curnode.leftchild.pos - curnode.pos, shaftwidth=0.2, length=5)
            curnode.leftchild.parent = curnode

        parentx = curnode.pos.x
        parenty = curnode.pos.y
        pos = vector(parentx + 3, parenty - 4, 0)
        curnode.rightchild = self.createTree(items[(mid + 1):], pos)
        if curnode.rightchild != None:
            curnode.righta = arrow(
                pos=curnode.pos, axis=curnode.rightchild.pos - curnode.pos, shaftwidth=0.2, length=5)
        curnode.rightchild.parent = curnode
        self.root = curnode
        return curnode

    def returnbalancefac(self, v):
        return self.findHeight(v.leftchild) - self.findHeight(v.rightchild)

    def findHeightIter(self, v):
        if v.leftchild == None and v.rightchild == None:
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

    def returnNextInorder(self, v):
        v = v.rightchild
        if(v == None):
            return v
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

    def getChildren(self, curnode):
        children = []

        # if curnode.leftchild!= None:
        children.append(curnode.leftchild)
        # if curnode.rightchild!= None:
        children.append(curnode.rightchild)
        return children

    def getnode(self, e, v):
        if(v.element == e):
            return v
        elif(v.element > e):
            return self.getnode(e, v.leftchild)
        elif(v.element < e):
            return self.getnode(e, v.rightchild)

    def del1(self, e):
        v = self.getnode(e, self.root)

        c = self.getChildren(v)
        """v.shape.radius=0
        v.label.height=0
        v.label.border=0
        v.label=None"""
        """if(v.lefta!=None):
            v.lefta.length=0
            v.lefta=None
        if(v.righta!=None):
            v.righta.length=0
            v.righta=None"""
        if(c[0] == None and c[1] == None):
            if(v.parent.leftchild == v):
                v.shape.radius = 0
                v.label.height = 0
                v.label.border = 0
                v.label = None
                v.parent.leftchild = None
                v.parent.lefta.length = 0
                v.parent.lefta = None

            else:
                v.shape.radius = 0
                v.label.height = 0
                v.label.border = 0
                v.label = None
                v.parent.rightchild = None
                v.parent.righta.length = 0
                v.parent.righta = None
        elif(c[0] == None and c[1] != None):
            if(v != self.root):
                if(v.parent.leftchild == v):
                    v.shape.radius = 0
                    v.label.height = 0
                    v.label.border = 0
                    v.label = None
                    v.parent.leftchild = c[1]
                    v.righta.length = 0
                    v.righta = None
                    c[1].parent = v.parent
                    # -3,+4
                    ysub = self.levelorder(c[1])
                    for i in ysub:
                        i.pos += vector(-3, 4, 0)
                    #c[1].parent.lefta=    c[1] and itself
                else:
                    v.shape.radius = 0
                    v.label.height = 0
                    v.label.border = 0
                    v.label = None
                    v.parent.rightchild = c[1]
                    v.righta.length = 0
                    v.righta = None
                    c[1].parent = v.parent
                    ysub = self.levelorder(c[1])
                    for i in ysub:
                        i.pos += vector(-3, 4, 0)

            else:
                v.shape.radius = 0
                v.label.height = 0
                v.label.border = 0
                v.label = None
                v.righta.length = 0
                v.righta = None

                self.root = c[1]
                self.root.parent = None

                ysub = self.levelorder(c[1])
                for i in ysub:
                    i.pos += vector(-3, 4, 0)
        elif(c[0] != None and c[1] == None):
            # +3,+4
            if(v != self.root):
                if(v.parent.leftchild == v):
                    v.shape.radius = 0
                    v.label.height = 0
                    v.label.border = 0
                    v.label = None
                    v.lefta.length = 0
                    v.lefta = None

                    v.parent.leftchild = c[0]
                    c[0].parent = v.parent
                    ysub = self.levelorder(c[0])
                    for i in ysub:
                        i.pos += vector(3, 4, 0)
                    #c[0].parent.lefta=    c[0] and itself
                else:
                    v.shape.radius = 0
                    v.label.height = 0
                    v.label.border = 0
                    v.label = None
                    v.lefta.length = 0
                    v.lefta = None

                    v.parent.rightchild = c[0]
                    c[0].parent = v.parent
                    ysub = self.levelorder(c[0])
                    for i in ysub:
                        i.pos += vector(3, 4, 0)

            else:
                v.shape.radius = 0
                v.label.height = 0
                v.label.border = 0
                v.label = None
                v.lefta.length = 0
                v.lefta = None

                self.root = c[0]
                self.root.parent = None
                # here remove both arrows
                ysub = self.levelorder(c[0])
                for i in ysub:
                    i.pos += vector(3, 4, 0)
        else:
            nxt = self.returnNextInorder(v)
            if nxt.parent.leftchild == nxt:
                if nxt.rightchild == None:
                    nxt.parent.lefta.length = 0
                    nxt.parent.lefta = None
                    v.shape.radius = 0
                    v.label.height = 0
                    v.label.border = 0
                    v.label = None
                    nxt.shape.pos = v.shape.pos
                    nxt.label.pos = v.shape.pos
                    nxt.rightchild = v.rightchild
                    if nxt.rightchild != None:
                        v.righta.length = 0
                        v.righta = None
                        nxt.righta = arrow(
                            pos=nxt.shape.pos, axis=nxt.rightchild.shape.pos - nxt.shape.pos, shaftwidth=0.2, length=5)
                        nxt.rightchild.parent = nxt
                    nxt.leftchild = v.leftchild
                    if nxt.leftchild != None:
                        v.lefta.length = 0
                        v.lefta = None
                        nxt.lefta = arrow(
                            pos=nxt.shape.pos, axis=nxt.leftchild.shape.pos - nxt.shape.pos, shaftwidth=0.2, length=5)
                        nxt.leftchild.parent = nxt
                    nxt.parent.leftchild = None
                    nxt.parent = v.parent
                    if v.parent == None:
                        self.root = nxt
                    else:
                        if v.parent.rightchild == v:
                            v.parent.rightchild = nxt
                        else:
                            v.parent.leftchild = nxt
                else:
                    nxt.righta.length = 0
                    nxt.righta = None
                    v.shape.radius = 0
                    v.label.height = 0
                    v.label.border = 0
                    v.label = None
                    ysub = self.levelorder(nxt.rightchild)
                    for i in ysub:
                        i.pos += vector(-3, 4, 0)
                    x = nxt.rightchild
                    x.parent = nxt.parent
                    x.parent.leftchild = x
                    nxt.shape.pos = v.shape.pos
                    nxt.label.pos = v.shape.pos
                    nxt.rightchild = v.rightchild
                    if nxt.rightchild != None:
                        v.righta.length = 0
                        v.righta = None
                        nxt.righta = arrow(
                            pos=nxt.shape.pos, axis=nxt.rightchild.shape.pos - nxt.shape.pos, shaftwidth=0.2, length=5)
                        nxt.rightchild.parent = nxt
                    nxt.leftchild = v.leftchild
                    if nxt.leftchild != None:
                        v.lefta.length = 0
                        v.lefta = None
                        nxt.lefta = arrow(
                            pos=nxt.shape.pos, axis=nxt.leftchild.shape.pos - nxt.shape.pos, shaftwidth=0.2, length=5)
                        nxt.leftchild.parent = nxt
                    nxt.parent = v.parent
                    if v.parent == None:
                        self.root = nxt
                    else:
                        if v.parent.rightchild == v:
                            v.parent.rightchild = nxt
                        else:
                            v.parent.leftchild = nxt
            else:
                if nxt.rightchild == None:
                    nxt.parent.righta.length = 0
                    nxt.parent.righta = None
                    v.shape.radius = 0
                    v.label.height = 0
                    v.label.border = 0
                    v.label = None
                    nxt.shape.pos = v.shape.pos
                    nxt.label.pos = v.shape.pos
                    nxt.rightchild = None
                    if nxt.rightchild != None:
                        v.righta.length = 0
                        v.righta = None
                        nxt.righta = arrow(
                            pos=nxt.shape.pos, axis=nxt.rightchild.shape.pos - nxt.shape.pos, shaftwidth=0.2, length=5)
                        nxt.rightchild.parent = nxt
                    nxt.leftchild = v.leftchild
                    if nxt.leftchild != None:
                        v.lefta.length = 0
                        v.lefta = None
                        nxt.lefta = arrow(
                            pos=nxt.shape.pos, axis=nxt.leftchild.shape.pos - nxt.shape.pos, shaftwidth=0.2, length=5)
                        nxt.leftchild.parent = nxt
                    nxt.parent = v.parent
                    if v.parent == None:
                        self.root = nxt
                    else:
                        if v.parent.rightchild == v:
                            v.parent.rightchild = nxt
                        else:
                            v.parent.leftchild = nxt
                else:
                    nxt.righta.length = 0
                    nxt.righta = None
                    v.shape.radius = 0
                    v.label.height = 0
                    v.label.border = 0
                    v.label = None
                    ysub = self.levelorder(nxt.rightchild)
                    for i in ysub:
                        i.pos += vector(-3, 4, 0)
                    x = nxt.rightchild
                    x.parent = nxt.parent
                    x.parent.rightchild = x
                    nxt.shape.pos = v.shape.pos
                    nxt.label.pos = v.shape.pos
                    nxt.rightchild = v.rightchild
                    if nxt.rightchild != None:
                        v.righta.length = 0
                        v.righta = None
                        nxt.righta = arrow(
                            pos=nxt.shape.pos, axis=nxt.rightchild.shape.pos - nxt.shape.pos, shaftwidth=0.2, length=5)
                        nxt.rightchild.parent = nxt
                    nxt.leftchild = v.leftchild
                    if nxt.leftchild != None:
                        v.lefta.length = 0
                        v.lefta = None
                        nxt.lefta = arrow(
                            pos=nxt.shape.pos, axis=nxt.leftchild.shape.pos - nxt.shape.pos, shaftwidth=0.2, length=5)
                        nxt.leftchild.parent = nxt
                    nxt.parent = v.parent
                    if v.parent == None:
                        self.root = nxt
                    else:
                        if v.parent.rightchild == v:
                            v.parent.rightchild = nxt
                        else:
                            v.parent.leftchild = nxt

        return

    def dell(self, e):
        x = self.getnode(e, self.root)
        z = x.parent
        #print(x.element)
        t = self.returnNextInorder(x)
        # y=t.element
        self.del1(e)
        if t == None:
            t = z
        else:
            y = t.element
            t = self.getnode(y, self.root)

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
                self.restu(x)

        if t == self.root:
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
                self.restu(x)
            return

        return


bst = BinarySearchTree()
a = list(map(float, input("Enter the initial array: ").split(" ")))
# a=[1,2,4,5,6,7]
pos = vector(0, 0, 0)
bst.createTree(a, pos, 5)
# bst.dell(5)
print("Delete(D) Insert(I) Search(S) StopGettingInput(X)")
while True:
    inputs = input("Enter the operation: ").split(" ")
    if inputs[0] == "S":
        try:
            val = float(inputs[1])
        except:
            print("Invalid input")
            continue
        bst.searchpath(val, bst.root)
        
    elif inputs[0] == "I":
        try:
            val = float(inputs[1])
        except:
            print("invalid input")
            continue
        bst.insertElementAVL(val)
#        print()
    elif inputs[0] == "D":
        try:
            val = float(inputs[1])
        except:
            print("invalid input")
            continue
#        print(val)
        try:
            bst.dell(val)
        except:
            print("Element " + str(val) + " is not present in the AVL")

    elif inputs[0] == "X":
        break
    else:
        print("invalid input")
