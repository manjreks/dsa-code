class Node:
    def __init__(self,value):
        self.value = value
        self.next=None


class Stack:
    def __init__(self,value):
        new_node = Node(value)
        self.top = new_node
        self.height =1

    def print_stack(self):
        temp = self.top

        while temp != None:
            print(temp.value)
            temp = temp.next
    
    def push(self,value):
        new_node = Node(value)

        if self.top is None:
            self.top = new_node
            self.height =1
        else:
            temp = self.top
            self.top = new_node
            new_node.next =temp
            self.height += 1
    
    def pop(self):
        if self.top is None:
            return None
        else:
            temp = self.top
            self.top = self.top.next
            self.height -= 1
            return temp




    




if __name__ == "__main__":
    my_stack = Stack(6)
    my_stack.print_stack()        

        