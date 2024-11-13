class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
    
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True
    
    def pop(self):
        if self.length == 0:
            return None
        # this case when have 2 or more nodes in the linked list
        temp = self.head
        pre = self.head
        
        while(temp.next is not None):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        # case when have 1 nodes
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp
    
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True
    
    def pop_first(self):
        if self.length == 0:
            return None
       
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        # case 1 node in list
        if self.length == 0:
            self.tail = None
        return temp.value
    
    def get(self, index):
        if index >= 0 and index <= self.length - 1:
            temp = self.head
            i = 0
            while (i < index):
                temp = temp.next
                i += 1
            return temp
        else:
            return None
        
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index-1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        prev = self.get(index - 1)
        temp = prev.next
        # change the pointers
        prev.next = temp.next
        temp.next = None
        # decrease length
        self.length -= 1
        return temp
    
    def reverse(self):
        # first swap head and tail
        temp = self.head
        self.head = self.tail
        self.tail = temp
        # create 2 more pointers before and after to reverse linked list
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after
            
        
            
            
my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)

my_linked_list.reverse()
my_linked_list.print_list()

