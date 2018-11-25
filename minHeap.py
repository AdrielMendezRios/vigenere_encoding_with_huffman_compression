class MinHeap:
    """
    This MinHeap class uses a Python list to store 
    the integer elements of the complete binary tree
    """ 
    def __init__(self):
        """
        Create an empty heap from a Python list
        """
        self._heap_list = []
   
    def __len__(self):
        return len(self._heap_list)
        
    def heapify(self, index):
        """
        Restore the Min Heap order starting 
        with the element at the given index
        """
        left_index = self.get_left_child(index)
        right_index = self.get_right_child(index)
        smallest = index
        
        if (left_index < len(self)) and \
             self._heap_list[left_index] < self._heap_list[index]:
            smallest = left_index
          
        if (right_index < len(self)) and \
             self._heap_list[right_index] < self._heap_list[smallest]:
            smallest = right_index 
   
        if smallest != index:
            temp = self._heap_list[index]
            self._heap_list[index] = self._heap_list[smallest]
            self._heap_list[smallest] = temp
            
            self.heapify(smallest) 
  
    
    def get_parent(self, index):
        """
        Return the parent index of the element at the given index
        """
        return (index-1) // 2 
  
    
    def get_left_child(self, index):
        """
        Return the left child index of the element at the given index
        """
        return 2*index + 1
        
    
    def get_right_child(self, index):
        """
        Return the right child index of the element at the given index
        """
        return 2*index + 2
         
    
    def extract_min(self):
        """
        Remove the root element which has the minimum value
        """
        if len(self) == 0:
            return None
        
        if len(self) == 1:
            root = self._heap_list[0]
            self._heap_list = []
            return root
     
        root = self._heap_list[0]
        self._heap_list[0] = self._heap_list[len(self)-1]
        del self._heap_list[len(self)-1]

        self.heapify(0)
        return root
    

    def set_value(self, index, new_value):
        """
        Sets the value of the element 
        at the given index to the new_value
        """ 
        self._heap_list[index] = new_value 
        
        # Swap the element at the given index with its parent, 
        # until the parent is smaller than that element
        
        while index != 0 and \
               self._heap_list[self.get_parent(index)] > self._heap_list[index]: 
     
            temp = self._heap_list[index] 
            self._heap_list[index] = self._heap_list[self.get_parent(index)]
            self._heap_list[self.get_parent(index)] = temp
             
            index = self.get_parent(index)

    def get_min(self):
        """
        Returns the element with minimum value (root element)
        """ 
        return self._heap_list[0]
            

    def insert_elem(self, element): 
        """
        Inserts a new element into the min heap at the bottom
        Then restore the heap order 
        """
        self._heap_list.append(element)
        index = len(self) - 1
        
        # Swap the element at the given index with its parent, 
        # until the parent is smaller than that element

        while index != 0 and \
              self._heap_list[self.get_parent(index)] > self._heap_list[index]:
            
            temp = self._heap_list[index] 
            self._heap_list[index] = self._heap_list[self.get_parent(index)]
            self._heap_list[self.get_parent(index)] = temp
            
            index = self.get_parent(index)

    def __str__(self):
        str_heap = ""
        for i in range(len(self)):
            str_heap += " || " + str(self._heap_list[i])
            if (i+1) % 8 == 0:
                str_heap += "\n"
        return str_heap
