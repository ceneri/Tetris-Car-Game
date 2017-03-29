#Cesar Neri
#January 18, 2017

#Advance data structures to be used in future projects

#March 16, 2017 UPDATE: Iterator Added


#!/usr/bin/env python

class Node():

    def __init__(self, data):
        self.__data = data
        self.__nextNode = None
        self.__prevNode = None

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

    @property
    def nextNode(self):
        return self.__nextNode

    @nextNode.setter
    def nextNode(self, N):
        if not isinstance(N, Node) and N is not None:
            raise ValueError("nextNode obj must be of type Node or a None object")
        
        self.__nextNode = N

    @property
    def prevNode(self):
        return self.__prevNode

    @prevNode.setter
    def prevNode(self, N):
        if not isinstance(N, Node) and N is not None:
            raise ValueError("prevNode obj must be of type Node or a None object")
        
        self.__prevNode = N


class LinkedList():

    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__size = 0

    @property
    def head(self):
        if not self.isEmpty():
            return self.__head.data

    @property
    def tail(self):
        if not self.isEmpty():
            return self.__tail.data

    @property
    def size(self):
        return self.__size
        
    def isEmpty(self):
        if self.size == 0:
            return True

        return False
    

    def append(self, data):
        temp = Node(data)

        if self.isEmpty():
            self.__head = self.__tail = temp
        else:
            self.__tail.nextNode = temp
            temp.prevNode = self.__tail
            self.__tail = temp

        self.__size += 1

    def prepend(self, data):
        temp = Node(data)

        if self.isEmpty():
            self.__head = self.__tail = temp
        else:
            temp.nextNode = self.__head
            self.__head.prevNode = temp
            self.__head = temp

        self.__size += 1
    
    def removeHead(self):
        if not self.isEmpty():
        
            if self.__head == self.__tail:
                self.__head = self.__tail = None
            else:
                self.__head = self.__head.nextNode
                self.__head.prevNode = None
                
            self.__size -= 1
            
        
    def removeTail(self):
        if not self.isEmpty():
            
            if self.__head == self.__tail:
                self.__tail = self.__head = None
            else:
                self.__tail = self.__tail.prevNode
                self.__tail.nextNode = None
                
            self.__size -= 1

    def __str__(self):

        string = ""

        for n in self:
            string += str(n)

        return string

    def __iter__(self):
        self.__index = -1
        self.__current = self.__head
        return self

    def __next__(self):
        if self.__index == self.size - 1:
            raise StopIteration()

        self.__index += 1
        result = self.__current.data
        self.__current = self.__current.nextNode

        return result


class Stack():

    def __init__(self):
        self.__list = LinkedList()

    def isEmpty(self):
        return self.__list.isEmpty()

    def push(self, data):
        self.__list.prepend(data)

    def peek(self):
        return self.__list.head

    def pop(self):
        data = self.__list.head
        self.__list.removeHead()    

        return data

class Queue():

    def __init__(self):
        self.__list = LinkedList()

    def isEmpty(self):
        return self.__list.isEmpty()

    def enqueue(self, data):
        self.__list.append(data)

    def peek(self):
        return self.__list.head

    def dequeue(self):
        data = self.__list.head
        self.__list.removeHead()
        
        return data

#Iterator Test
if __name__ == "__main__":

    l = LinkedList()

    l.append(3)
    l.append(4)
    l.append(5)
    l.append(7)

    for i in l:
        print(i)
