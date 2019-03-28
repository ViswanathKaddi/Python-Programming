#Linked List

class node:
    def __init__(self, data=None):
        self.data=data
        self.next=None

class linked_list:
    def __init__(self):
        self.head=node()
        
    def append(self, data):
        new_node = node(data)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node
        
    def length(self):
        cur=self.head
        count=0
        while cur.next != None:
            count+=1
            cur=cur.next
        return count
    
    def display(self):
        elements=[]
        cur_node = self.head
        while cur_node.next!=None:
            cur_node=cur_node.next
            elements.append(cur_node.data)
        print(elements)
    
    def get(self, index):
       
        if (index >= self.length()):
            print("ERROR, Index out of Range")
            return None
        cur_inx = 0
        cur_node = self.head
        while True:
            cur_node = cur_node.next
            if cur_inx == index:
                return cur_node.data
            cur_inx+=1
            
    def erase(self, index):
        print(self.length())
        if index >= self.length():
            print("ERROR, Index out of Range")
            return 
        cur_inx=0
        cur_node=self.head
        while True:
            last_node = cur_node
            cur_node = cur_node.next
            if cur_inx==index:
                last_node.next = cur_node.next
                return
            cur_inx+=1

my_list =linked_list()

my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)
my_list.append(5)

my_list.length()
my_list.display()
my_list.erase(2)
my_list.display()

######## Stacks #################################################################

class Node:
    def __init__(self, data=None):
       self.data = data
       self.next = None
 
class Stack:
    def __init__(self):
        self.head = None
 
    def push(self, data):
        if self.head is None:           #if list is empty
            self.head = Node(data)
        else:                           #if list is non empty
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
 
    def pop(self):
        if self.head is None:
            return None
        else:
            popped = self.head.data
            self.head = self.head.next
            return popped
        
    def display(self):
        if self.head is None:
            print("Stack is Empty")
        else:
            elements=[]
            cur=self.head
            while cur!=None:
                elements.append(cur.data)
                cur=cur.next

            print(elements)
 
a_stack = Stack()
while True:
    print('push <value>')
    print('pop')
    print('quit')
    print('display list')
    do = input('What would you like to do? ').split()
 
    operation = do[0].strip().lower()
    if operation == 'push':
        a_stack.push(int(do[1]))
        a_stack.display()
    elif operation == 'display':
        a_stack.display()
    elif operation == 'pop':
        popped = a_stack.pop()
        a_stack.display()
        if popped is None:
            print('Stack is empty.')
        else:
            print('Popped value: ', int(popped))
    elif operation == 'quit':
        break
        

######## Queues #################################################################


class Node:
    def __init__(self, data):
       self.data = data
       self.next = None
 
class Queue:
    def __init__(self):
        self.head = None
        self.last = None
 
    def enqueue(self, data):
        if self.last is None:
            self.head = Node(data)
            self.last = self.head
        else:
            self.last.next = Node(data)
            self.last = self.last.next
 
    def dequeue(self):
        if self.head is None:
            return None
        else:
            to_return = self.head.data
            self.head = self.head.next
            return to_return
        
    def display(self):
        if self.head is None:
            print("Queue is Empty")
        else:
            elements=[]
            cur=self.head
            while cur!=None:
                elements.append(cur.data)
                cur=cur.next

            print(elements)
 
a_queue = Queue()
while True:
    print('enqueue <value>')
    print('dequeue')
    print('display')
    print('quit')
    do = input('What would you like to do? ').split()
 
    operation = do[0].strip().lower()
    if operation == 'enqueue':
        a_queue.enqueue(int(do[1]))
        a_queue.display()
        print('Added ', do[1], ' to queue')
    elif operation == 'display':
        a_queue.display()
    elif operation == 'dequeue':
        dequeued = a_queue.dequeue()
        if dequeued is None:
            print('Queue is empty.')
        else:
            print('Dequeued element: ', int(dequeued))
    elif operation == 'quit':
        break