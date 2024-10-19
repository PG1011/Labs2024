'''
Pramodh Guduru
KUID: 3114377
Date: 9/25/24
Lab: lab 2
Last modified: 9/25/24
Purpose: Sets up nodes, stacks from nodes, and queues from nodes.
Also defines what a function can do and what call and return methods do.
'''
from function import Function

class Process:
    def __init__(self, name): #initializes class and stack, and adds functions
        self.name = name
        self.stack = Stack()
        self.add_call(Function("main", handle_exceptions = True))

    def add_call(self, function): #adds a call function
        self.stack.push(function)
        print(f"Function {function.name} added to the call stack of process {self.name}.")

    def return_from_call(self): #returns stored calls
        if not self.stack.is_empty():
            function = self.stack.pop()
            print(f"Process {self.name} returning from function: {function.name}")
            if function.name == "main" and self.stack.is_empty():
                print(f"Process {self.name} has completed.")
                return True
            else:
                return False
        else:
            raise RuntimeError("No calls in stack.")

    def handle_exception(self): #if function can handle exception (if there is one), keeps, else pops it
        print(f"Exception raised in process {self.name}")
        while not self.stack.is_empty():
            function = self.stack.peek()
            if function.handle_exceptions:
                print(f"Exception handled by function: {function.name} in process {self.name}")
                return False
            else:
                print(f"Popping func: {function.name} from process {self.name}")
                self.stack.pop()

        print(f"Process {self.name} complete")
        return True

#code from lecture below
class Node:
    def __init__(self, entry):
        self.entry = entry
        self.next = None

class Stack:
    def __init__(self):
        self._top = None

    def push(self, entry):
        temp = self._top
        self._top = Node(entry)
        self._top.next = temp

    def pop(self):
        if self.is_empty():
            raise RuntimeError('Stack Empty')
        else:
            temp = self._top.entry
            self._top = self._top.next
            return temp

    def peek(self):
        if not self.is_empty():
            return self._top.entry
            print (self._top.entry)
        else:
            raise RuntimeError('Stack Empty')

    def is_empty(self):
        return(self._top == None)

class LinkedQueue:
    def __init__(self):
        self.front = None
        self.back = None

    def is_empty(self):
        return self.front is None and self.back  is None

    def enqueue(self, entry):
        new_node = Node(entry)
        if self.is_empty():
            self.front = new_node
            self.back = self.front
        else:
            self.back.next = new_node
            self.back = new_node

    def dequeue(self):
        if self.is_empty():
            raise RuntimeError('Queue Empty')
        else:
            temp = self.front.entry
            self.front = self.front.next
            if self.front == None:
                self.back = None
            return temp


