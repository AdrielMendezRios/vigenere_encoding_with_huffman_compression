"""
Background to Using the Vigenere Square for Encryption

The rows are associated with the characters in the key and the columns 
are associated with the characters in the message to encrypt.  The key 
will be used over and over again matching the letters in the message 
with the letters in the key. 

Encryption: Find the ciphertext character in the Vigenere square 
matrix by the following steps:
a) Using the character from the key, find the row where it exists by 
   looking down column 0 until you find the correct row.
b) Using the character from the plaintext message, find column where 
   it exists by looking across row 0 until you find the correct column.
c) The ciphertext character will be the one in the in the matrix 
   having the row and column found above.
d) Add the ciphertext letter to the coded message.

Decryption: Find the plaintext character in the Vigenere square 
matrix by the following steps:
a) Find the ciphertext letter in the Vigenere square, using the key 
   letter row.
b) In that same column, get the character at row 0, this is the 
   plaintext letter.
c) Add the plaintext letter to the decoded message.
"""
class Vigenere:    
    def __init__(self,key):
        """
        Create Vigenere object: initialize key and matrix
        """
        ## Add code here ##
        self.key = key
        self.vig_squ = self.create_vig_square()
        
    def create_vig_square(self):
        """
        Create the vigenere square, using 128 rows and 128 columns
        Use a nested list for the matrix and a nested loop to create 
           each inner row and add it to the outer matrix.
        Each element of the inner row is one more in ASCII code value 
           than the previous element.  After getting to 128, you must
           go back to 0.
 
        """
        
        ## Add code here ##
        vigenere_square = []
        temp = [i for i in range(128)]  # creates list of first 127 ascii codes
        for i in range(128):
            row = [chr(num) for num in temp]  # creates a row of first 127 ascii chars from temp num list
            vigenere_square.append(row)
            temp.append(temp[0])
            temp = temp[1:]

        return vigenere_square


            
    def encrypt(self, msg):
        """
        Traverse the message getting each letter 
           and finding its encoding:
        Get the row index of the key char using get_row_index
        Get the column index of the message char using get_col_index
        Use the row and column indices to find the code character
           in the Vigenere square
        Add code character to encoded message    
        """
        ## Add code here ##

        msg_chars = msg
        key_chars = self.key
        coded_msg = ""
        i = 0
        j = 0
        while len(coded_msg) < len(msg_chars):
            if j >= len(key_chars):
                j = 0  # if true -> set j back to 0 if its larger then the length of key_chars string

            row = self.get_row_index(key_chars[j])
            column = self.get_col_index(msg_chars[i])

            if column != -1:
                coded_msg += self.vig_squ[row][column]
                j += 1
            else:
                coded_msg += msg_chars[i]

            i += 1

        return coded_msg
    
    
    def decrypt(self, coded_msg):
        """
        Traverse the code getting each letter 
           and finding its decoding:
        Get the message character using get_plain_text_char 
        Add message character to decoded message   
        """ 
        
        ## Add code here ##
        key_chars = self.key
        i = 0
        j = 0
        decoded_msg = ""
        while len(decoded_msg) < len(coded_msg): # while len(decoded_msg) < len(coded_msg):
            if j >= len(key_chars):
                j = 0  # if true -> set j back to 0 if its larger then the length of key_chars string

            if ord(coded_msg[i]) < 128:
                decoded_char = self.get_plain_text_char(coded_msg[i], key_chars[j])
                decoded_msg += decoded_char
                i += 1
                j += 1

        return decoded_msg
    
    def get_col_index(self, char):
        """
        The first row of the Vigenere square is vig_squ[0].
        This is used to match chars from the message to encrypt.
        Return the column index in row 0 containing the char
        """
        
        ## Add code here ##
        for i in self.vig_squ[0]:
            if ord(char) < 128:
                if i == char:
                    return self.vig_squ[0].index(i)
            else:
                return -1
        
    
    def get_row_index(self, key_char):
        """
        The first column of the Vigenere square is vig_squ[][0]
        This is used to match chars from the key.
        Return the row index in col 0 containing the key char
        """
        ## Add code here ##
        for row in self.vig_squ:
            if row[0] == key_char:
                return self.vig_squ.index(row)
    
    
    def get_plain_text_char(self, coded_char, key_char):
        """
        Use the row index of the key char and the column index of
        the coded message char in that row to locate the column in
        row 0 of the plaintext char and return that element value.
        """
        
        ## Add code here ##
        row = self.get_row_index(key_char)
        col_index = 0
        for char in self.vig_squ[row]:
            if char == coded_char:
                col_index = self.vig_squ[row].index(char)
                return self.vig_squ[0][col_index]
