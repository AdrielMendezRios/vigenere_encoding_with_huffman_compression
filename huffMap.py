from map import Map
from huffElement import HuffElement


class HuffMap(Map): 
    """
    This class inherits from Map with methods tailored
    to Huffman encoding
    """
    def __init__(self):
        """
        Create the HuffMap object by calling
        the parent constructor
        """
        ## Code this ##
        super().__init__()

    def contains_char(self, ch):
        """
        Checks for previous existence of character in HuffMap
        Returns True, when found, otherwise returns False
        """
        ## Code this ##
        return ch in self
                
    def add_char(self, char): # shouldn't this be add_MapEntry instead?
        """
        Add a new character to the HuffMap
        """
        ## Code this ##
        huff_elem = HuffElement(char)
        huff_elem.set_freq(1)
        self.add(char, huff_elem)

    def get_huff_elem(self, char):
        """
        Returns the HuffElement for a passed in character
        """
        ## Code this ##
        if char in self:
            return self.get_value(char)

    def get_char_set(self):
        """
        Returns the set of characters in the HuffMap
        """
        ## Code this ##
        return self.get_key_set()

    def __str__(self):
        """
        return string representation of the huffmap
        """
        entries = self.get_entry_set()
        map_str = ""
        for entry in entries:
            if entry.key is not "\n":
                map_str += "Char: " + str(entry.key) + "  Code: " + str(entry.value.get_code()) \
                       + " Count: " + str(entry.value.get_freq()) + "\n"
            else:
                map_str += "Char: " + "\\n" + " Code: " + str(entry.value.get_code()) \
                       + " Count: " + str(entry.value.get_freq()) + "\n"
        return map_str


