class node:
    def __init__(self,data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.start = None
    def insertFirst(self,data):
        newnode = node(data)
        if self.start == None:
            self.start = newnode
        else:
            temp = self.start
            self.start = newnode
            newnode.next = temp
    def insertBtw(self, data, pos):
        newnode = node(data)
        count = 0
        temp = self.start
        while temp:
            count += 1
            prev = temp
            temp = temp.next
            if count == pos:
                prev.next = newnode
                newnode.next = temp
            
    def insertLast(self,data):
        newnode = node(data)
        if self.start == None:
            self.start = newnode
        else:
            temp = self.start
            while temp.next != None:
                temp = temp.next
            temp.next = newnode
    def getlength(self):
        l = 0
        temp = self.start
        while temp:
            l += 1
            temp = temp.next
        return l
        
    def viewList(self):
        if self.start == None:
            print("List is empty.")
        else:
            temp = self.start
            while temp:
                print(temp.data, end="->")
                temp = temp.next
    def viewListRev(self):
        if self.start:
            viewListRev(self.start.next)
            print(self.start.data)
                

    def deleteFirst(self):
        if self.start == None:
            self.start = None
        else:
            self.start = self.start.next
    def deleteNode(self, pos):
        temp = self.start
        count = 0
        if pos == 0:
            self.start = temp.next
            temp = None
        else:
            while count != (pos - 1):
                count += 1
                temp = temp.next
            cur = temp.next
            temp.next = cur.next
            cur = None
            
    def rotate(self, k):
    ## examine new logic of Leetcode
        if not self.start or not self.start.next or not k:
            self.start = self.start
        
        node1 = self.start
        length = 1
        while node1 and node1.next:
            node1 = node1.next
            length += 1
                    
        k %= length
        if not k:
            self.start = self.start
        i = 0
        node2 = self.start
        while i != length - k - 1:
            node2 = node2.next
            i += 1
            
        nextNode = node2.next
        node2.next = None
        
        node1.next = self.start
        
        self.start = nextNode
        
        #return nextNode
        
        '''length = 0
        node1 = self.start
        while node1:
            length += 1
            node1 = node1.next
     
        k %= length
        r = length - k
        i = 0
        node2 = self.start
        while i != r:
            node2 = node2.next
        nextnode = node2.next
        node2.next = None
        node1.next = self.start
        
        self.start = nextnode'''
        

list = LinkedList()
list.viewList()
print()
list.insertLast(10)
list.insertLast(20)
list.insertLast(30)
list.insertLast(40)
list.insertLast(50)
list.viewList()
list.deleteFirst()
print()
list.viewList()
list.rotate(2)
print()
list.viewList()
list.insertLast(100)
list.insertLast(200)
list.insertFirst(56)
list.insertFirst(32)
list.insertBtw(92, 3)
list.deleteNode(0)
list.deleteNode(4)
print()
list.viewList()
print()
list.viewListRev()