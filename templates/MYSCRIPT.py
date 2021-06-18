from vpython import *
import math
# display(background=color.white)
class BinarySearchTree:
    class node:
        def init(self):
            self.element = None
            self.leftchild = None
            self.rightchild = None
            self.parent = None
            self.shape=None
            self.cordinates=None
            self.label=None
    def __init__(self):
        self.rightstartteta=0
        self.leftstartteta=pi
        self.dict={}
    
    def findinEleParent(self, e, v,lvl):
        #print(v.element, lvl)
        
        if(v.element >= e):
            try:
                if(v.leftchild == None):
                    return [v,lvl+1]

                else:
                    t = self.findinEleParent(e, v.leftchild,lvl+1)
            except:
                return [v,lvl+1]
        else:
            #print(v.element)
            try:
                #print(v.rightchild)
                if(v.rightchild == None):
                    return [v,lvl+1]

                else:
                    t = self.findinEleParent(e, v.rightchild,lvl+1)
            except:
                return [v,lvl+1]
        return t
    
    def insertElement(self, e):
        lvl=0
        #print("------------------------------------")
#         print(self.root.element)
        v,lvl = self.findinEleParent(e, self.root,lvl)
        #print("------------------------------------")
#         print(v[0],v[1])
        #print(v.element,lvl)
        curnode = self.node()
        # print(1)
        curnode.element = e
        if(v.element > e):
            r=5
            v.leftchild = curnode
            curnode.parent = v
            parentx=v.cordinates.x
            parenty=v.cordinates.y
            temp=self.leftstartteta+(lvl*pi*28/180)
            
            rootpos=vector(parentx,parenty,0)
            pos1=vector(parentx+r*cos(temp),parenty+r*sin(temp),0)
            c = curve(rootpos,pos1)
            rate(1)
            curnode.shape=sphere(pos=pos1,radius=0.5,color=color.red)
            
            curnode.cordinates=pos1
           
            curnode.label=label(pos=curnode.cordinates,
                  text=str(curnode.element), xoffset=0,
                  yoffset=0, space=30,
                  height=12, border=4,
                  font='sans')
             
            
        else:
            r=5
            v.rightchild = curnode
            curnode.parent = v
            
            parentx=v.cordinates.x
            parenty=v.cordinates.y
            
            temp=self.rightstartteta-(lvl*pi*28/180)
            
            rootpos=vector(parentx,parenty,0)
            pos1=vector(parentx+r*cos(temp),parenty+r*sin(temp),0)
          
            c = curve(rootpos,pos1)
            rate(1)
            curnode.shape=sphere(pos=pos1,radius=0.5,color=color.red)
            curnode.cordinates=pos1
           
            curnode.label=label(pos=curnode.cordinates,
                  text=str(curnode.element), xoffset=0,
                  yoffset=0, space=30,
                  height=12, border=4,
                  font='sans')
             
            
        return
    def createTree(self, items,pos,lvl,parentnode=None,r=5):
        curnode = self.node()
        rootpos=pos
        
        if parentnode!=None:
            rate(1)
            c = curve(parentnode.cordinates, rootpos)
        rate(1)
        curnode.shape=sphere(pos=rootpos,radius=0.5,color=color.red)
        curnode.cordinates=rootpos
        items.sort()
        if(len(items) == 1):
            curnode.element = items[0]
            curnode.label= label(pos=curnode.cordinates,
                  text=str(curnode.element), xoffset=0,
                  yoffset=0, space=30,
                  height=12, border=4,
                  font='sans')
            return curnode
        if(len(items) % 2):
            mid = (len(items) // 2)
        else:
            mid = (len(items) // 2) - 1

        curnode.element = items[mid]
        self.dict[curnode.element]=lvl
        #print(curnode.element)
        curnode.label= label(pos=curnode.cordinates,
                  text=str(curnode.element), xoffset=0,
                  yoffset=0, space=30,
                  height=12, border=4,
                  font='sans')
        if(mid):
            parentx=curnode.cordinates.x
            parenty=curnode.cordinates.y
            temp=self.leftstartteta+(lvl*pi*28/180)
            #self.leftstartteta=
            pos=vector(parentx+r*cos(temp),parenty+r*sin(temp),0)
            curnode.leftchild = self.createTree(items[:mid],pos,lvl+1,curnode)
            # print(curnode.leftchild.element)
            curnode.leftchild.parent = curnode
        temp1=self.rightstartteta-(lvl*pi*28/180)
        parentx=curnode.cordinates.x
        parenty=curnode.cordinates.y
        #print(lvl)
        #print(math.degrees(self.leftstartteta),math.degrees(self.rightstartteta))
        pos=vector(parentx+r*cos(temp1),parenty+r*sin(temp1),0)
        curnode.rightchild = self.createTree(items[(mid + 1):],pos,lvl+1,curnode)
        # print(curnode.rightchild.element)
        curnode.rightchild.parent = curnode
        
        
        self.root = curnode
        return curnode
    
    def returnbalancefac(self, v):
        return self.findHeight(v.leftchild) - self.findHeight(v.rightchild)
    
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


bst = BinarySearchTree()
a=[1,2,4,5,6,7]
pos=vector(0,0,0)
leftstartteta=pi
rightstartteta=0
bst.createTree(a,pos,1)
bst.insertElement(3)

