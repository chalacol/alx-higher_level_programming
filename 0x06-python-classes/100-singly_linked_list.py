#!/usr/bin/python3

"""Definition of class node"""


class Node:
    """Represent a node in a singly linked list"""

    def __init__(self, data, next_node=None):
        """Initialise a new node.
        Args:
            data (int): The data of the new node
            next_node (Node): The next node in the list
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Get/set the data of the Node"""
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Get/set the next_node of the Node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Represent a singly-linked list."""

    def __str__(self):
        """Define the print() representation of a singlylinkedlist."""
        rtn = ""
        ptr = self.__head

        while ptr is not None:
            rtn += str(ptr.data)
            if ptr.next_node is not None:
                rtn += "\n"
            ptr = ptr.next_node

        return rtn

    def __init__(self):
        """Initialize a new Singlylinked list."""
        self.__head = None

    def sorted_insert(self, value):
        """Insert a new Node to the singly linkedlist.
        Args:
            value (Node): The new Node to insert.
        """
        ptr = self.__head

        while ptr is not None:
            if ptr.data > value:
                break
            ptr_prev = ptr
            ptr = ptr.next_node

        newNode = Node(value, ptr)
        if ptr == self.__head:
            self.__head = newNode
        else:
            ptr_prev.next_node = newNode
