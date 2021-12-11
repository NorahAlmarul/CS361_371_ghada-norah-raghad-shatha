import time
counter = 1
def AStar():
    global counter
    expand = []# initialize axpand list
    fringe=[]# intialize fringe list
    fringe.append(source)# add the source node fringe
    flag = True
    while flag:
        node = fringe.pop(0)
        expand.append(node)
        if node.getname() == destination.getname():
            flag = False
            break
        for i in node.getchild():
            fringe.append(relation(i, node, i.cost))
            counter = counter+1
        sortfring(fringe) 
    pathAstr(expand)#to find the correct path
class Node():#to represent rooms
    def __init__(self, name, h):
        self.name = name
        self.h = h
        self.child = []
        self.parent = []
        self.cost = 0
          
    def getchild(self,i):#return a specific adjecent room
        return self.child[i]
    
    def getname(self):
        return str(self.name)

    def addchild(self, child):#add adjacent
        self.child.append(child)

    def getchild(self):#return all adjacent
        return self.child

    def evaluate_fun(self):#the evaluation function 
        return 0 + self.h
    
    def leng(self):#return the number of adjacent rooms
        return len(self.child)


class child():#each room will have an array of child which are all adjacent room 
    def __init__(self, name, parent, cost, h):#constructor
        self.name = name
        self.cost = cost
        self.h = h

    def getname(self):
        return self.name.getname()

    def evaluate_fun(self):
        return self.cost + self.h
    
    def getchild(self,i):#return specific adjacent room
        return self.name.child[i]
    
    def getchild(self):#return all adjacent rooms
        return self.name.getchild()

    def getparent(self):#return the previuos rooms the crew member visit
        return self.name.getparent()
    
    def leng(self):#the number of adjacent rooms
        return len(self.name.child)


class relation():#this class is used to retrieve the path of visited rooms 
    def __init__(self, name, parent, cost):
        self.name = name
        self.cost = cost
        self.parent = parent

    def function(self):
        return self.name.h + self.cost
    
    def getchild(self):
        return self.name.getchild()

    def getname(self):
        return self.name.getname()

"""""
#create object of each room heuristic_1 
Lower_Engine = Node('Lower_Engine', 4)
Upper_Engine = Node('Upper_Engine', 1)
Reactor = Node('Reactor', 2)
Security = Node('Security', 2)
Medbay = Node('Medbay', 1)
Electrical= Node('Electrical', 2)
Storage = Node('Storage', 1)
Admin = Node('Admin', 1)
Communication = Node('Communication', 3)
O2 = Node('O2', 2)
Shields = Node('Shields', 2)
Weapons = Node('Weapons', 1)
Navigation = Node('Navigation', 2)
Cafeteria = Node('Cafeteria', 0)

#add Lower_Engine adjacents
Lower_Engine.addchild(child(Upper_Engine,Lower_Engine, 1,1))
Lower_Engine.addchild(child(Reactor,Lower_Engine, 2,2))
Lower_Engine.addchild(child(Security, Lower_Engine,2,2))
Lower_Engine.addchild(child(Electrical, Lower_Engine,4,2))
Lower_Engine.addchild(child(Storage, Lower_Engine,3,1))
#add Upper_Engine adjacent
Upper_Engine.addchild(child(Cafeteria,Upper_Engine,1,0))
Upper_Engine.addchild(child(Medbay,Upper_Engine,2,1))
#add Reactor adjacent
Reactor.addchild(child(Security,Reactor,1,2))
Reactor.addchild(child(Upper_Engine,Reactor,2,1))
#add Security adjacent
Security.addchild(child(Upper_Engine, Security,2,1))
#add Medbay adjacent
Medbay.addchild(child(Cafeteria, Medbay,2,0))
#add Electrical adjacent
Electrical.addchild(child(Storage, Electrical,2,1))
# add Storage adjacent
Storage.addchild(child(Cafeteria,Storage, 1,0))
Storage.addchild(child(Admin,Storage, 2,1))
Storage.addchild(child(Communication, Storage,2,3))
Storage.addchild(child(Shields, Storage,1,2))
# add Admin adjacent 
Admin.addchild(child(Cafeteria, Admin,2,0))
# add Communication adjacent 
Communication.addchild(child(Shields, Communication,2,2))
# add O2 adjacent 
O2.addchild(child(Shields, O2,4,2))
O2.addchild(child(Weapons, O2,2,1))
O2.addchild(child(Navigation, O2,2,2))
# add Shields adjacent
Shields.addchild(child(Navigation, Shields,4,2))
Shields.addchild(child(Weapons, Shields,5,1))
# add Weapons adjacent 
Weapons.addchild(child(Navigation, Weapons,4,2))
Weapons.addchild(child(Cafeteria, Weapons,1,0))
# add Navigation adjacent 
Navigation.addchild(child(Shields, Navigation,4,2))
Navigation.addchild(child(Weapons, Navigation,4,1))
Navigation.addchild(child(O2, Navigation,3,2))
"""""

"""""
#create object of each room seconed heuristic_2 
Lower_Engine = Node('Lower_Engine', 4)
Upper_Engine = Node('Upper_Engine', 4)
Reactor = Node('Reactor', 3)
Security = Node('Security', 3)
Medbay = Node('Medbay', 1)
Electrical= Node('Electrical', 2)
Storage = Node('Storage', 1)
Admin = Node('Admin', 1)
Communication = Node('Communication', 3)
O2 = Node('O2', 2)
Shields = Node('Shields', 2)
Weapons = Node('Weapons', 1)
Navigation = Node('Navigation', 2)
Cafeteria = Node('Cafeteria', 0)

#add Lower_Engine adjacents
Lower_Engine.addchild(child(Upper_Engine,Lower_Engine, 1,4))
Lower_Engine.addchild(child(Reactor,Lower_Engine, 2,3))
Lower_Engine.addchild(child(Security, Lower_Engine,2,3))
Lower_Engine.addchild(child(Electrical, Lower_Engine,4,2))
Lower_Engine.addchild(child(Storage, Lower_Engine,3,1))
#add Upper_Engine adjacent
Upper_Engine.addchild(child(Cafeteria,Upper_Engine,1,0))
Upper_Engine.addchild(child(Medbay,Upper_Engine,2,1))
#add Reactor adjacent
Reactor.addchild(child(Security,Reactor,1,3))
Reactor.addchild(child(Upper_Engine,Reactor,2,4))
#add Security adjacent
Security.addchild(child(Upper_Engine, Security,2,4))
#add Medbay adjacent
Medbay.addchild(child(Cafeteria, Medbay,2,0))
#add Electrical adjacent
Electrical.addchild(child(Storage, Electrical,2,1))
# add Storage adjacent
Storage.addchild(child(Cafeteria,Storage, 1,0))
Storage.addchild(child(Admin,Storage, 2,1))
Storage.addchild(child(Communication, Storage,2,3))
Storage.addchild(child(Shields, Storage,1,2))
# add Admin adjacent 
Admin.addchild(child(Cafeteria, Admin,2,0))
# add Communication adjacent 
Communication.addchild(child(Shields, Communication,2,2))
# add O2 adjacent 
O2.addchild(child(Shields, O2,4,2))
O2.addchild(child(Weapons, O2,2,1))
O2.addchild(child(Navigation, O2,2,2))
# add Shields adjacent
Shields.addchild(child(Navigation, Shields,4,2))
Shields.addchild(child(Weapons, Shields,5,1))
# add Weapons adjacent 
Weapons.addchild(child(Navigation, Weapons,4,2))
Weapons.addchild(child(Cafeteria, Weapons,1,0))
# add Navigation adjacent 
Navigation.addchild(child(Shields, Navigation,4,2))
Navigation.addchild(child(Weapons, Navigation,4,1))
Navigation.addchild(child(O2, Navigation,3,2))
"""""

#create object of each room seconed heuristic_3
Lower_Engine = Node('Lower_Engine', 4)
Upper_Engine = Node('Upper_Engine', 5)
Reactor = Node('Reactor', 4)
Security = Node('Security', 4)
Medbay = Node('Medbay', 1)
Electrical= Node('Electrical', 1)
Storage = Node('Storage', 3)
Admin = Node('Admin', 1)
Communication = Node('Communication', 3)
O2 = Node('O2', 2)
Shields = Node('Shields', 2)
Weapons = Node('Weapons', 1)
Navigation = Node('Navigation', 2)
Cafeteria = Node('Cafeteria', 0)

#add Lower_Engine adjacents
Lower_Engine.addchild(child(Upper_Engine,Lower_Engine, 1,5))
Lower_Engine.addchild(child(Reactor,Lower_Engine, 2,4))
Lower_Engine.addchild(child(Security, Lower_Engine,2,4))
Lower_Engine.addchild(child(Electrical, Lower_Engine,4,1))
Lower_Engine.addchild(child(Storage, Lower_Engine,3,3))
#add Upper_Engine adjacent
Upper_Engine.addchild(child(Cafeteria,Upper_Engine,1,0))
Upper_Engine.addchild(child(Medbay,Upper_Engine,2,1))
#add Reactor adjacent
Reactor.addchild(child(Security,Reactor,1,4))
Reactor.addchild(child(Upper_Engine,Reactor,2,5))
#add Security adjacent
Security.addchild(child(Upper_Engine, Security,2,5))
#add Medbay adjacent
Medbay.addchild(child(Cafeteria, Medbay,2,0))
#add Electrical adjacent
Electrical.addchild(child(Storage, Electrical,2,3))
# add Storage adjacent
Storage.addchild(child(Cafeteria,Storage, 1,0))
Storage.addchild(child(Admin,Storage, 2,1))
Storage.addchild(child(Communication, Storage,2,3))
Storage.addchild(child(Shields, Storage,1,2))
# add Admin adjacent 
Admin.addchild(child(Cafeteria, Admin,2,0))
# add Communication adjacent 
Communication.addchild(child(Shields, Communication,2,2))
# add O2 adjacent 
O2.addchild(child(Shields, O2,4,2))
O2.addchild(child(Weapons, O2,2,1))
O2.addchild(child(Navigation, O2,2,2))
# add Shields adjacent
Shields.addchild(child(Navigation, Shields,4,2))
Shields.addchild(child(Weapons, Shields,5,1))
# add Weapons adjacent 
Weapons.addchild(child(Navigation, Weapons,4,2))
Weapons.addchild(child(Cafeteria, Weapons,1,0))
# add Navigation adjacent 
Navigation.addchild(child(Shields, Navigation,4,2))
Navigation.addchild(child(Weapons, Navigation,4,1))
Navigation.addchild(child(O2, Navigation,3,2))


source = Lower_Engine
destination = Cafeteria



def sortfring(fringe):# bubble sort to sort the fringe in decreasing order
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(fringe) - 1):
            if fringe[i].function() > fringe[i + 1].function():
                fringe[i], fringe[i + 1] = fringe[i + 1], fringe[i]
                swapped = True   
        
    
    
                
def pathAstr(expand):#backtracking to find the path
    expand.reverse()
    pathA = []
    pathA.append(expand[0])
    flage=True
    while flage:
        if len(expand)<=1:
            break
        current=expand[0].parent
        if current.getname()== expand[1].getname():
            pathA.append(current)
            expand.pop(0)
            
        else:
            expand.pop(1)
            pathA.reverse()   
    costA=0
    path = []
    for i in pathA:
        costA+=i.cost
        path.append(i.getname())
    path.reverse()
    print('Path: {}'.format(path))
    print('cost = ', costA)
    #print('space complexity= ', counter)



start = time.time()
AStar() #call A star
end = time.time()
time_n = end - start 
print('time complexity= ',time_n)
print('space complexity= ', counter)