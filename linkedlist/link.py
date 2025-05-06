#linkedlist ds code
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
    

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head=new_node
        self.tail=new_node
        self.length =1
    
    def append(self,value):
        new_node = Node(value)

        if self.head == None:
            self.head=new_node
            self.tail=new_node
        else:
            temp = self.tail
            temp.next = new_node
            self.tail = new_node
        self.length += 1

        return True
    
    def prepend(self,value):

        new_node = Node(value)
        if self.head == None:
            self.head=new_node
            self.tail=new_node   
        else:
            temp = self.head
            self.head = new_node
            new_node.next = temp
    
        self.length +=1


    
    def printlist(self):
        temp = self.head

        while temp is not None:
            print(temp.value)
            temp = temp.next
    
    def pop(self):
        if self.head == None:
            return None
        
        temp = self.head
        pre= None

        while temp.next != None:
            pre = temp
            temp = temp.next
        self.tail = pre
        pre.next=None

        self.length -= 1

        return temp
    
    def popfirst(self):
        if self.length == 0:
            return None
        else:
            temp = self.head
            self.head = self.head.next
            temp.next = None
            self.length -= 1
            if self.length == 0:
                self.tail = None

            return temp
    
    def get(self, index):
        if self.length ==0 or index < 0 or index >= self.length:
            return None
        else:
            index_node = self.head
            for _ in range(index):
                index_node = index_node.next
            return index_node
    
    def set_value(self, index, value):
        if index < 0 or index >= self.length:
            return False
        else:
            temp = self.head
            for _ in range(index):
                temp=temp.next
            temp.value = value
            return True

    def insert(self,index,value):
        if index < 0 or index > self.length:
            return False
        elif index ==0:
            return self.prepend(value)
        elif index == self.length:
            return self.append(value)
        else:
            new_node = Node(value)
            temp = self.get(index-1)
            new_node.next = temp.next
            temp.next= new_node
            self.length += 1
            return True
    
    def remove(self,index):
        if index < 0 or index >= self.length:
            return None
        if index ==0:
            return self.popfirst()
        if index == self.length -1:
            return self.pop()
        prev = self.get(index-1)
        temp = prev.next

        prev.next = temp.next
        temp.next = None
        self.length -= 1
        return temp
    
    def reverse(self):
        if self.length ==0 or self.length ==1 :
            return True
        else:
            temp = self.head
            self.head=self.tail
            self.tail = temp

            after = temp.next
            before = None

            for _ in range(self.length):
                after = temp.next
                temp.next = before
                before = temp
                temp = after
    
    def reverse(self):

        temp_head = self.head
        temp_tail = self.tail

        temp= self.head

        prev = None
        after = None

        while temp.next != None:
            after = temp.next
            temp.next = prev
            prev=temp
            temp=after
        
        self.head = temp_tail
        self.head.next = prev
        
    def binary_to_decimal(self):
        num = 0
        current = self.head
        while current:
            num = num * 2 + current.value
            current = current.next
        return num
    


def test_append(myLinkedList):

    myLinkedList.append(20)
    myLinkedList.append(30)
    myLinkedList.printlist()
    print("linkedlist appended")

    
def test_pop(myLinkedList):
    node = myLinkedList.pop()
    print("popped value",node.value)

def test_prepend(myLinkedList):
    node = myLinkedList.prepend(40)
    print("linked list prepend")
    myLinkedList.printlist()

def test_popfirst(myLinkedList):
    node =myLinkedList.popfirst()
    myLinkedList.printlist()
    print(node.value)

def test_get(myLinkedList):
    node =myLinkedList.get(0)
    myLinkedList.printlist()
    print(node.value)

def test_set(myLinkedList):
    myLinkedList.append(90)
    node =myLinkedList.set_value(1,99)
    myLinkedList.printlist()
    
def test_insert(myLinkedList):
    myLinkedList.append(90)
    node =myLinkedList.insert(1,99)
    myLinkedList.printlist()

def test_remove(myLinkedList):
    myLinkedList.append(90)
    myLinkedList.append(99)
    myLinkedList.printlist()
    print("contents of linked list")

    node =myLinkedList.remove(1)
    myLinkedList.printlist()

def test_reverse(myLinkedList):
    myLinkedList.append(90)
    myLinkedList.append(99)
    
    print("contents of linked list")
    myLinkedList.printlist()
    
    node =myLinkedList.reverse()
    print("contents after reverse")
    myLinkedList.printlist()











    
    
      


    
if __name__ == "__main__":
    myLinkedList = LinkedList(1)
    myLinkedList.append(1)
    myLinkedList.append(1)
    #test_append(myLinkedList)
    #test_pop(myLinkedList)
    #test_prepend(myLinkedList)
    #test_popfirst(myLinkedList)
    #test_get(myLinkedList)
    #test_set(myLinkedList)
    #test_insert(myLinkedList)
    #test_remove(myLinkedList)
    #test_reverse(myLinkedList)

    print(myLinkedList.binary_to_decimal())



    







