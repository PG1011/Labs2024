'''
Pramodh Guduru
KUID: 3114377
Date: 9/30/24
Lab: lab 3
Last modified: 9/29/24
Purpose: Sets up nodes, stacks from nodes, and queues from nodes.
'''
#background.py
#node
class Node:
    def __init__(self, entry):
        self.entry = entry
        self.next = None

#linkedlist
class LinkedList:
    def __init__(self):
        self.front = None
        self.length = 0

    def insert(self, index, entry):
        if index < 0 or index > self.length:
            raise RuntimeError('Nope')
        new_node = Node(entry)
        if index == 0:
            new_node.next = self.front
            self.front = new_node
        else:
            jumper = self.front
            for i in range(index - 1):
                if jumper is None:
                    raise RuntimeError('Nah')
                jumper = jumper.next
            new_node.next = jumper.next
            jumper.next = new_node

        self.length += 1

    def length(self):
        return self.length

    def get_entry(self, index):
        if (self.length > index) and (index >= 0):
            jumper = self.front
            for i in range(index):
                jumper = jumper.next
            return jumper.entry
        else:
            raise RuntimeError('empty')

    def set_entry(self, index, new_entry):
        if (self.length > index) and (index >= 0):
            jumper = None
            for i in range(index):
                jumper = jumper.next
            jumper.entry = new_entry
        else:
            raise RuntimeError('empty')

    def remove(self, index):
        if self.length == 0:
            raise RuntimeError('Empty')

        if index < 0 or index >= self.length:
            raise RuntimeError('nah')

        if index == 0:
            temp = self.front
            self.front = self.front.next
        else:
            jumper = self.front
            for i in range(index - 1):
                jumper = jumper.next

            temp = jumper.next
            if temp is None:
                raise RuntimeError('Node to remove is None')
            jumper.next = temp.next
        self.length -= 1
        return temp.entry

#stack
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

#linkedqueue
class LinkedQueue:
    def __init__(self):
        self.front = None
        self.back = None

    def is_empty(self):
        return self._front is None and self._back  is None

    def enqueue(self, entry):
        if is_empty():
            self.first = Node(entry)
            self.last = self.first
        else:
            temp = self.last
            self.last = Node(entry)
            temp.next = self.last

    def dequeue(self):
        if self.is_empty:
            raise RuntimeError('rip')
        else:
            temp = self.first.entry
            self.first = self.first.next
            if self.first == None:
                self.last = None
            return temp



