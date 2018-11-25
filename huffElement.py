from comparable import Comparable

class HuffElement(Comparable):
    """
    This class is used in conjunction with the HuffMap class.
    The HuffMap class is a dictionary for storing the frequency 
    counts of characters found in a string, and the Huffman code 
    for that character. The key for the HuffMap is the character 
    and the value is a HuffElement object, which contains the
    character, its frequency in the string, and its Huffman code.    
    """
    def __init__(self, char):
        """
        Create a HuffElement object for the passed in character.
        Initialize the character, the frequency to zero 
        and the code to the empty string.
        """
        ## Code this ##
        self._ch = char
        self._ch_freq = 0
        self._code = ""
        
    def inc_freq(self):
        """
        Increment the character frequency count
        """
        ## Code this ##
        self._ch_freq += 1
               
    def get_freq(self):
        """
        Return the character frequency count
        """
        ## Code this ##
        return self._ch_freq
        
    def set_freq(self, count):
        """
        Set the character frequency count
        """
        ## Code this ##
        self._ch_freq = count

    def get_char(self):
        """
        Return the character
        """
        return self._ch

    def set_char(self, char):
        """
        sets character
        """
        self._ch = char

    def get_code(self):
        """
        Return the Huffman code for the character
        """
        ## Code this ##
        return self._code

    def set_code(self, code):
        """
        Set the Huffman code for the character
        """
        ## Code this ##
        self._code = code
    
    def compare (self, other_huff_elem):
        """
        Use the character frequency count for comparison
        """
        ## Code this ##
        if self._ch_freq > other_huff_elem.get_freq():
            return 1
        elif self._ch_freq < other_huff_elem.get_freq():
            return -1
        return 0
        
    def __str__(self):
        """
        Returns a string representation of this HuffElement
        """
        ## Code this ##
        if self.get_char() is "\n":
            return "Char: " + "\\n" + " Code: " + str(self._code) + " Count: " + str(self.get_freq())
        return "Char: " + self.get_char() + "  Code: " + str(self._code) + " Count: " + str(self.get_freq())








