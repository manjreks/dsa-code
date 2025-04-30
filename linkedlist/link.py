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
    
    def printlist(self):
        temp = self.head

        while temp is not None:
            print(temp.value)
            temp = temp.next

    
if __name__ == "__main__":
    myLinkList = LinkedList(10)
    myLinkList.append(20)
    myLinkList.append(30)

    myLinkList.printlist()
