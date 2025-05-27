#!/usr/bin/python3
"""
This module defines a class that print a notification message every time an
item is added (using the append or extend methods) or removed (using the
remove or pop methods)
"""


class VerboseList(list):
    """  A class that prints a message every time an item is added or removed
    """

    def append(self, item):
        """
        Prints a notification every time an item is added
        """
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, item):
        """
        Prints a notification every time an item is added
        """
        super().extend(item)
        # Calculates number of items added for the message using len()
        print("Extended the list with [{}] items.".format(len(item)))

    def remove(self, item):
        """
        Prints a notification every time an item is removed
        """
        # Prints notificatioin before removing item
        print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=None):
        """
        Prints a notification every time an item is removed
        If index is not specified, it pops the last item
        """

        # Checks if there is no index
        if index is None:
            if len(self) == 0:  # if list is empty
                raise Exception
            item_to_pop = self[-1]  # Gets the last item to be popped
            print("Popped [{}] from the list".format(item_to_pop))
            return super().pop()

        else:
            # Raises error if index is invalid
            if not index < len(self) and index >= -len(self):
                raise Exception
            item_to_pop = self[index]  # Gets the item at specified item
            print("Popped [{}] from the list".format(item_to_pop))
            return super().pop(index)  # Calls parent method with index
