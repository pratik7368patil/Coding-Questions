class node:
    def __init__(self,data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.start = None
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
    def deleteFirst(self):
        if self.start == None:
            self.start = None
        else:
            self.start = self.start.next
            
            
    def remove(self, val):
    ### this will remove all the elements from list which is equal to val
        if self.start is None:
            return None
        if self.start.next is None and val == self.start.data:
            return None
         
        cur, prev = self.start, None
        
        while cur:
            if cur.data == val:
                if prev is not None:
                    prev.next = cur.next
                else:
                    self.start = self.start.next
            else:
                prev = cur
            cur = cur.next
            
  
        
    
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
list.insertLast(30)
list.remove(30)
print()
list.viewList()