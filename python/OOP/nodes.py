class SLNode:
    def __init__(self, val):
        self.value = val
        self.next = None

class SLList:
    def __init__(self):
        self.head = None
    
    def addToFront(self, val):
        new_node = SLNode(val)
        if self.head != None:
            current_head = self.head
            new_node.next = current_head
            self.head = new_node
        else: 
            self.head = new_node
        return self

    def print_values(self):
        runner = self.head
        while runner != None:
            print(runner.value)
            runner = runner.next
        return self

    def add_to_back(self, val):
        new_node = SLNode(val)
        if self.head == None:
            self.head = new_node
            return self
        runner = self.head
        while runner.next != None:
            runner = runner.next
        runner.next = new_node
        return self

    def remove_from_front(self):
        pass 

    def remove_from_back(self):
        pass 

    def remove_val(self, val):
        pass 

    def insert_at(self, val, n):
        # new_node = SLNode(val)
        # runner = self.head
        # for node in range(0, n+1, 1):
        #     runner = runner.next
        #     temp_next = 

        

pets = SLList()

pets.addToFront("1-buttercup")
pets.addToFront("2-mia")
pets.addToFront("3-bubbles")
pets.addToFront("4-logan")
pets.addToFront("5-lenny")
pets.addToFront("6-tia")

pets.add_to_back("7-popsy")
pets.add_to_back("8-franny")

pets.print_values()



# 6
# 5
# 4
# 3
# 2
# 1
# 7
# 8