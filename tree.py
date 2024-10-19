from pokemon import *

#Khaled Esmail,cs302,Karla Fant

#This is my tree class where I implemented my node class and my avl tree

#node class
class node():
    #constructor 
    def __init__(self, PokeObj):
        self.__left = None
        self.__right = None
        self.__PokeObj = PokeObj
        self.duplicate = [] #list of duplicate data

    def get_left(self):
        return self.__left
    
    def get_right(self):
        return self.__right
    
    def get_data(self):
        return self.__PokeObj
    
    def set_left(self,new_left):
        self.__left = new_left
    
    def set_right(self,new_right):
        self.__right = new_right
    
    def set_data(self,new_data):
        self.__PokeObj = new_data



    
    
class tree():
    def __init__(self): 
        self.__root = None
    
    #finds the height
    def __height(self,root):
        if root is None:
            return 0
        left_height = self.height(root.get_left())
        right_height = self.height(root.get_right())
        return max(left_height,right_height) + 1
    
    #finds the balance factor 
    def getBalance(self,root):
        if root is None:
            return 0
        return self.__height(root.get_left()) - self.__height(root.get_right())
    
    #this rotates the tree left
    def leftrotate(self,root:node):
        if root is None:
            return False
        if root.get_right() is None:
            return False

        temp = root.get_right()
        root.set_right(temp.get_left())
        temp.set_left(root)
        return True

    #this rotates the tree right
    def rightrotate(self,root:node):
        if root is None:
            return False
        
        if root.get_left() is None:
            return False
                
        temp = root.get_left()
        root.set_left(temp.get_right())
        temp.set_right(root)
        return True
    

    def left_rightrotate(self,root:node):
        if self.leftrotate(root.get_left()):
            self.rightrotate(root)
        
          
    def right_leftrotate(self,root:node):
        if self.rightrotate(root.get_right()):
            self.leftrotate(root)

    # wrapper add
    def add(self,PokeObj):
        if self.__root is None:
            self.__root = node(PokeObj)
            return
        self.__root = self.__add(self.__root,PokeObj) 
        self.__fix_tree(self.__root)

    #recursive add 
    def __add(self,root,PokeObj):
        if root is None:
            root = node(PokeObj)

        if PokeObj < root.get_data():
            root.set_left(self.__add(root.get_left(),PokeObj))
            return root
        
        elif PokeObj > root.get_data():
            root.set_right(self.__add(root.get_right(),PokeObj))
            return root
        
        else:
            root.duplicate.append(PokeObj)
            return root
        
    # wrapper display  
    def display(self,PokeObj):
        if self.__root is None:
            return 
        self.__display(self.__root,PokeObj)

    #recursive display
    def __display(self,root:node,PokeObj:Pokemon, depth = 0):
        if root is None:
            return
        self.__display(root.get_left(),PokeObj, depth + 1)
        PokeObj.Pokemon_display()
        print("level:", depth)
        self.__display(root.get_right(),PokeObj, depth + 1)

    def retrieve(self,PokeObj):
        if self.root is None:
            return
        self.__retrieve(self.__root,PokeObj)

    def __retrieve(self,root,PokeObj):
        if root is None:
            return
        
    #this adjusts the tree based on the balance factor
    def __fix_tree(self,root:node):   
        balance = self.getBalance(root)
        
        if abs(balance) < 2: # if balance is 1,0,-1
            return

        if balance > 2:
            self.__fix_tree(root.get_left())

        elif balance < -2:
            self.__fix_tree(root.get_right())
    
        balance = self.getBalance(root)

        if balance == 2:
            if self.getBalance(root.get_left()) < 0:
                self.right_leftrotate(root) 
            
            else:
                self.rightrotate(root)     

        if balance == -2:
            if self.getBalance(root.get_right()) > 0:
                self.left_rightrotate(root) 
            
            else:
                self.leftrotate(root) 


    
        
    
    
    
    
