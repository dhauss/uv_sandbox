class BST_Node:
    def __init__(self, val:int = None):
        self.val = val

        #dummy node for all valid BST_Nodes simplifies insertion
        if(val):
            self.left = BST_Node()
            self.right = BST_Node()
        else:
            self.left = None
            self.right = None

    def insert(self, new_val:int):
        while(self.val):
            if(new_val < self.val):
                self = self.left
            elif(new_val > self.val):
                self = self.right
            else: # new_val == self.val so ignore duplicate val
                return

        self.val = new_val
        self.left = BST_Node()
        self.right = BST_Node()
    
    def insert_list(self, new_vals: list[int]):
        for val in new_vals:
            self.insert(val)
    
    def lookup_val(self, val:float) -> bool:
        while(self.val):
            if(self.val == val):
                return True
            elif(val < self.val):
                self = self.left
            else: # val > self.val
                self = self.right
        
        return False

    def min_val(self):
        if(not self or not self.left):
            return None
        
        if(not self.left.val):
            return self.val
        
        return self.left.min_val()