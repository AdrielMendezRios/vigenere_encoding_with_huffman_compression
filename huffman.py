from huffMap import HuffMap
from huffPQ import HuffPQ
from huffTree import HuffNode, HuffTree


class Huffman:
    """
    This Huffman class does the following:
      1. Compresses a passed in string of characters from a text file:
         - build the character frequency map of HuffElements
         - build the Huffman Tree using the HuffPQ of HuffTrees
         - recursively walk the Huffman tree assigning the 
           correct binary code to each leaf HuffNode which contain
           the HuffElement for the character  
         - build the Huffman encoded binary string by retrieving the
           correct code from the HuffElements for each character
           in the file string
      2. Decompresses the encoded binary string
         - each binary character (0 or 1) is retrieved from the
           binary encoded string and used to walk the Huffman tree 
         - traverse the Huffman tree starting from the root going left 
           with '0' and right with '1' until you find a leaf node
         - retrieve the file string character from the HuffElement 
           in the HuffNode and add it to the output string.
    """

    def __init__(self):
        """
        Constructor: Create the Huffman class object
        Initialize the huff_map instance variable to a HuffMap
        Initialize the huffTree instance variable to None
        """
        ## Add code here ##

        self.huff_map = HuffMap()
        self.huff_tree = None

    def build_huff_map(self, file_str):
        """
        Populate the huffMap from the passed in file string:
         - keys: file characters
         - values: HuffElements holding character frequency counts
         
        Loop though each character in the file string
          1. If the huffMap does not contain the character, 
             add the character to the map
          2. Retrieve the HuffElement from the map and increment 
             the frequency
        """
        ## Add code here ##
        for char in file_str:
            if char not in self.huff_map:
                self.huff_map.add_char(char)
            else:
                huff_elem = self.huff_map.get_huff_elem(char)
                huff_elem.inc_freq()

    def build_huff_tree(self):
        """
        1. Create an empty Huff Priority Queue: HuffPQ
        2. Create the set of character keys from the HuffMap
        3. Build a forest of HuffTrees one from each 
           HuffElement in the HuffMap using the character key 
           set to retrieve the HuffElements and enqueue each 
           single node HuffTree to the HuffPQ
        4. Loop through the HuffPQ min heap, dequeueing the two  
           lowest frequency count HuffTrees and combine them into 
           a new HuffTree, enqueueing the new single HuffTree back 
           to the HuffPQ and repeating until there is only one 
           HuffTree in the HuffPQ
        5. Dequeue the single HuffTree from the HuffPQ 
           and set it to the HuffTree instance variable
        """

        ## Add code here ##
        huffPQ = HuffPQ()
        key_set = self.huff_map.get_char_set()
        for key in key_set:
            huff_elem = self.huff_map.get_huff_elem(key)
            single_tree = HuffTree(element=huff_elem)
            huffPQ.enqueue(single_tree)

        finished = False
        while not finished:
            low_node_1 = huffPQ.dequeue()
            low_node_2 = huffPQ.dequeue()
            internal_node = HuffTree(left_tree=low_node_1, right_tree=low_node_2)
            huffPQ.enqueue(internal_node)
            if len(huffPQ) == 2:
                finished = True
                final_low_1 = huffPQ.dequeue()
                final_low_2 = huffPQ.dequeue()
                final_tree = HuffTree(left_tree=final_low_1, right_tree=final_low_2)
                huffPQ.enqueue(final_tree)

        full_huff_tree = huffPQ.dequeue()
        self.huff_tree = full_huff_tree

    def build_huff_codes(self, root):
        """
        This is the helper function for the recursive assign_code
        method that walks the Huffman Tree (self.huff_tree)
        building the code for each character in the file string
        starting from the root of the Huffman Tree.
        
        If the passed in root is not None, call assign_code
        """
        ## Add code here ##

        if root is not None:
            self.assign_code(root)

    def assign_code(self, root):
        """
        Recursively get the binary bits for the code as you
        walk the Huffman Tree to the leaf node.
        The base case is when the left subtree of the root is None
        1. Get the code from the root HuffNode and add '0' to it
           Set this new code in the HuffNode of the left subtree 
           of root, and then call assign_code passing in the
           left subtree of root
        2. Get the code from the root HuffNode and add '1' to it
           Set this new code in the HuffNode of the right subtree 
           of root, and then call assign_code passing in the
           right subtree of root 
        """
        ## Add code here ##
        if root.left is None:
            return

        code = root.get_code()


        code += '0'
        root.left.set_code(code)
        self.assign_code(root.left)

        code = root.get_code()


        code += '1'
        root.right.set_code(code)
        self.assign_code(root.right)



    def build_binary_str(self, file_str):
        """
        Builds a binary string of ones and zeros by walking through 
        the passed in file_str and replacing each character with the 
        code in the HuffElement which is retrieved from the HuffMap
        Return the binary string
        """
        ## Add code here ##
        binary_str = ""
        for char in file_str:
            huff_elem = self.huff_map.get_huff_elem(char)
            code = huff_elem.get_code()
            binary_str += code
        return binary_str

    def compress(self, file_str):
        """
        Compresses a passed in string of characters from a text file:
        1. take the passed in file_str and add EOF marker
        1. build the character frequency map of HuffElements
        2. build the Huffman Tree using the HuffPQ of HuffTrees
        3. build the Huffman codes, recursively traversing the tree
        4. build the Huffman encoded binary string and return it
        """
        ## Add code here ##

        file_str += chr(129)
        self.build_huff_map(file_str)
        self.build_huff_tree()
        self.build_huff_codes(self.huff_tree.get_root())
        return self.build_binary_str(file_str)

    def decompress(self, binary_str):
        """
        1. Get the root node of the Huffman tree and set a 
           current node pointing to the root node
	    2. Loop through each character (0 or 1) in the binary_str:
           a. Traverse the Huffman tree starting from the root going
              left with '0' and right with '1' until you find a leaf 
              node
           b. When you find a leaf node (both left and right node
              pointers are None), retrieve the file string character 
              from the HuffNode 
           c. Check the character for the EOF char 
              and break when found
           d. Reset the current node pointer to root
        3. Return the decompressed string
        """
        ## Add code here ##r
        root = self.huff_tree.get_root()
        cur_node = root
        decomp_str = ""
        for i in binary_str:
            if i == '0':
                cur_node = cur_node.left
            if i == '1':
                cur_node = cur_node.right
            if (cur_node.right and cur_node.left) is None:
                char = cur_node.get_char()
                if char != chr(129):
                    decomp_str += char
                else:
                    break
                cur_node = root
        return decomp_str
