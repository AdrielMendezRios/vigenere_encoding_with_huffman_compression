from comparable import Comparable
from huffElement import HuffElement

class HuffNode(Comparable):
    """
    This class represents a node in a HuffTree, 
    where the node data is a HuffElement object
    The public instance variables are:
       - element: the HuffElement object
       - left: the root node of the left subtree off this node
       - right: the root node of the right subtree off this node
    """
    def __init__(self, element): # element is a HuffElement
        """
        Constructor: Create HuffNode object
         - initialize data with passed in HuffElement
         - initialize nodes to None
        """
        ## Add code here ##
        self.element = element
        self.left = None
        self.right = None

    def get_char(self):
        """
        Return the character from the HuffElement
        """
        ## Add code here ##
        return self.element.get_char()

    def get_freq(self):
        """
        Return the character count from the HuffElement
        """
        ## Add code here ##
        return self.element.get_freq()

    def set_freq(self, count):
        """
        Set the character count in the HuffElement
        """
        ## Add code here ##
        self.element.set_freq(count)

    def get_code(self):
        """
        Return the Huffman code from the HuffElement
        """
        ## Add code here ##
        return self.element.get_code()

    def set_code(self, code):
        """
        Set the character count in the HuffElement
        """
        ## Add code here ##
        self.element.set_code(code)

    def compare(self, other_node):
        """
        Use the character frequency count for comparison,
        by calling the HuffElement compare method 
        """
        ## Add code here ##
        return self.element.compare(other_node.element)

    def __str__(self):
        """
        Return the string representation of the HuffElement
        """
        ## Add code here ##
        return self.element.__str__()

class HuffTree(Comparable):
    """
    This class represents a Huffman Encoding Tree
    There are two types of HuffTrees that are built
      1. the leaf nodes: built with the HuffElements
      2. the internal nodes: built with two HuffTrees
    """

    def __init__(self, element = None, left_tree = None, right_tree = None):
        """
        Constructor:
        The constructor parameters have default values.
        The constructor must be called using these keyword arguments:
        1. when building the internal nodes for the Huffman Tree, the
           element parameter is None 
        2. when building the leaf nodes the left and right subtree 
           root nodes will be None
        Initialize the root HuffNode instance variable appropriately  
        a) for the leaf Node, root is initialized with a HuffNode 
           using the element parameter
        b) for the internal Node, root is initialized with a 
           HuffNode using a HuffElement where the character is EOF 
        """
        ## Add code here ##

        if element is None:
            l_root = left_tree.get_root()
            r_root = right_tree.get_root()
            freq = l_root.get_freq() + r_root.get_freq()
            internal_huff_elem = HuffElement(chr(3))
            internal_huff_elem.set_freq(freq)
            self.root = HuffNode(internal_huff_elem)
            self.root.left = l_root
            self.root.right = r_root

            # self.root = HuffNode(HuffElement(None))

        if left_tree is None and right_tree is None:
            self.root = HuffNode(element)




    def get_root(self):
        """
        Returns the root of the tree
        """
        ## Add code here ##
        return self.root
    

    def compare(self, other_huff_tree):
        """
        Compare the root node of this HuffTree 
        to that of the other HuffTree
        """
        ## Add code here ##
        return self.root.compare(other_huff_tree.get_root())

    def __str__(self):
        return self.root.__str__()







