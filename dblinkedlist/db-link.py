from node import Node

class DbLinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length =1
    
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
    
    def append(self,value):
        new_node = Node(value)

        temp = self.head

        if temp == None:
            self.head = new_node
            self.tail = new_node
                   
        else:

            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            
        self.length += 1
        return True
    
    def pop(self):

        if self.length == 0:
            return None
        
        temp = self.tail
             

        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next =None
            temp.prev = None
        self.length -= 1
        return temp
    
    def prepend(self,value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail= new_node
                    
        else:
            temp = self.head
            new_node.next = temp
            temp.prev = new_node
            self.head = new_node
        
        self.length +=1
        return True
    
    def popFirst(self):
        if self.head is None:
            return None
        
        if self.length ==1:
            temp = self.head
            self.head = None
            self.tail = None
            self.length =0
            return temp
        else:
            temp = self.head
            self.head = self.head.next
            self.head.prev = None
            self.length -= 1
            return temp
    
    def get(self,index):
        if self.head is None or index < 0 or index >= self.length:
            return None
        else:
            temp = self.head
            i = index
            while i > 0:
                temp=temp.next
                i -= 1
            return temp
    
    def set_value(self,index,value):
        temp = self.get(index)

        if temp is not None:
            temp.value = value
            return True
        else:
            return False
    
    def insert(self,index,value):
        if self.head is None or index < 0 or index >= self.length:
            return False
        
        else:
            current = self.head
            prev = current.prev
            next = current.next

            for _ in range(index):
                current = current.next
                prev = current.prev
                next = current.next
            
            new_node = Node(value)
            new_node.next = next
            current.next = new_node
            new_node.prev = current





        



        






            






if __name__ == "__main__":
    my_list = DbLinkedList(7)
    my_list.print_list()

    print("***tested constructor***")
    my_list.append(10)
    my_list.append(11)
    my_list.print_list()
    print("***tested append***")

    tail_node =my_list.pop()
    #print(tail_node.value)
    my_list.print_list()
    print("***tested pop***")


    my_list.prepend(99)
    #print(tail_node.value)
    my_list.print_list()
    print("***tested prepend***")

    my_list.popFirst()
    #print(tail_node.value)
    my_list.print_list()
    print("***tested popfirst***")

    my_node = my_list.get(1)
    print(my_node.value)
    
    print("***tested get***")

    my_list.set_value(1,100)
    my_list.print_list()
    print("***tested set***")




    



        
