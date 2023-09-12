 #!/usr/bin/python3
"""
Module: 1-my_list

Description:
    Defines the MyList class that inherits the list.

    Public Methods:
        - print_sorted(self): Prints the list, but sorted in ascending order.
"""

class MyList(list):
    """Inherits list"""

    def print_sorted(self):
        """Prints the list, but sorted (ascending sort)"""
        sorted_list = sorted(self)
        print(sorted_list)
