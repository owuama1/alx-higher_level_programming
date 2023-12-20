#!/usr/bin/python3
"""Defines classes for singly linked list."""


class Node:
    """Represents a node of a singly linked list."""
    def __init__(self, data, next_node=None):
        """Initializes a new Node.

        Args:
            data: Integer, the data for the node.
            next_node: Node, the next node in the linked list.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Retrieves the data of the node."""
        return self.__data

    @data.setter
    def data(self, value):
        """Sets the data of the node.

        Args:
            value: Integer, the data for the node.

        Raises:
            TypeError: If data is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Retrieves the next node in the linked list."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Sets the next node in the linked list.

        Args:
            value: Node or None, the next node in the linked list.

        Raises:
            TypeError: If next_node is not a Node object.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Represents a singly linked list."""
    def __init__(self):
        """Initializes an empty singly linked list."""
        self.head = None

    def sorted_insert(self, value):
        """Inserts a new Node into the correct sorted position in the list.

        Args:
            value: Integer, the data for the new node.
        """
        new_node = Node(value)
        if self.head is None or self.head.data >= value:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next_node is not None and current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """Returns a string representation of the linked list."""
        result = ""
        current = self.head
        while current:
            result += str(current.data)
            if current.next_node:
                result += "\n"
            current = current.next_node
        return result


# Example usage:
if __name__ == "__main__":
    linked_list = SinglyLinkedList()
    linked_list.sorted_insert(5)
    linked_list.sorted_insert(3)
    linked_list.sorted_insert(8)
    linked_list.sorted_insert(1)

    print(linked_list)
