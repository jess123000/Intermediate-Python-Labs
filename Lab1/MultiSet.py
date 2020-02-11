#!/usr/bin/env python3

# ----------------------------------------------------------------------
# MultiSet.py
# Alex Harris
# CS 161 12pm
# ----------------------------------------------------------------------

class MultiSet:

    # ------------------------------------------------------------------

    def __init__(self):
        """
        create the MultiSet
        """
        self.set = []

    # ------------------------------------------------------------------

    def insert(self, value) -> None:
        """
        inserts value into the MultiSet
        :param value: item to insert into the MultiSet
        :return: None
        """
        #appends the value into the MultiSet
        self.set.append(value)

    # ------------------------------------------------------------------

    def remove(self, value) -> None:
        """
        remove one copy of value from the MultiSet; if value is not in the MultiSet, nothing happens
        :param value: item to remove one copy of from the MultiSet
        :return: None
        """
        #uses the built in remove method for a list type
        self.set.remove(value)

    # ------------------------------------------------------------------

    def removeAll(self, value) -> None:
        """
        remove all copies of value from the MultiSet; if value is not in the MultiSet, nothing happens
        :param value: item to remove all copies of from the MultiSet
        :return: None
        """
        #goes through the loop multiple times to make sure every instance of the value is deleted
        while value in self.set:
            self.set.remove(value)

    # ------------------------------------------------------------------

    def count(self, value) -> int:
        """
        :param value: value to get the count of in the MultiSet
        :return: number of copies of value in the MultiSet
        """
        #counts the number of values using the list method of count
        amount = self.set.count(value)
        return amount

    # ------------------------------------------------------------------

    def __len__(self) -> int:
        """
        :return: total number of values in the MultiSet
        """
        #uses the len() function to calculate the length
        length = len(self.set)
        return length

    # ------------------------------------------------------------------

# ----------------------------------------------------------------------

def main():
    #creates the MultiSet
    vowels = MultiSet()

    #Adds to the MulitSet
    vowels.insert('a')
    vowels.insert('e')
    vowels.insert('i')
    vowels.insert('o')
    vowels.insert('u')
    vowels.insert('a')
    vowels.insert('a')
    vowels.insert('a')

    #counts the number of a's found in the MultiSet
    print(vowels.count('a'))

    #prints the length of the MultiSet
    print(len(vowels))

    #removes e and prints the new length
    vowels.remove('e')
    print(len(vowels))

    #removes all a's and prints the new length
    vowels.removeAll('a')
    print(len(vowels))

# ----------------------------------------------------------------------

if __name__ == '__main__':
    main()
