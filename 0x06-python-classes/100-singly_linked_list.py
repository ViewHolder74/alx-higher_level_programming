#!/usr/bin/python3
"""
7. Singly linked list
"""


class Node:
    """"Class that defines a node"""

    def __init__(self, data, next_node=None):
        """ function that instantiate attributes: data & next_node"""

        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Function that returns data attribute"""

        return (self.__data)

    @data.setter
    def data(self, value):
        """
        Define private instance attribute: value
        Raise TypeError if value is not an integer
        """

        if not isinstance(value, int):
            raise TypeError('data must be an integer')

        self.__data = value

    @property
    def next_node(self):
        """Define private instance attribute: next_node"""

        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        """
        Define private instance attribute: value
        Raise TypeError if value is not an integer or None/NULL
        """

        if (value is not None and not isinstance(value, Node)):
            raise TypeError('next_node must be a Node object')

        self.__next_node = value


class SinglyLinkedList:
    """Class that defines a singly linked list"""

    def __init__(self):
        """ function that instantiate attribute: head"""

        self.head = None

    def __str__(self):
        """Define private instance attributes: print_data & curr"""

        print_data = ""
        curr = self.head
        while curr:
            print_data += str(curr.data) + "\n"
            curr = curr.next_node

        return (print_data[:-1])

    def sorted_insert(self, value):
        """Function that inserts new node into correct sorted position"""

        tmp_node = Node(value)
        if not self.head:
            self.head = tmp_node
            return

        if value < self.head.data:
            tmp_node.next_node = self.head
            self.head = tmp_node
            return

        curr = self.head
        while curr.next_node and curr.next_node.data < value:
            curr = curr.next_node

        if curr.next_node:
            tmp_node.next_node = curr.next_node

        curr.next_node = tmp_node
