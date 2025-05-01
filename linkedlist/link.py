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





    
    
      


    
if __name__ == "__main__":
    myLinkedList = LinkedList(10)
    #test_append(myLinkedList)
    #test_pop(myLinkedList)
    #test_prepend(myLinkedList)
    test_popfirst(myLinkedList)








