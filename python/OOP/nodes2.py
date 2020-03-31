class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class SLList():
    def __init__(self):
        self.head = None

    def add_to_front(self, data):
        new_node = Node(data)
        if self.head != None:
            current_head = self.head
            new_node.next = current_head
            self.head = new_node
            return self
        else:
            self.head = new_node
            return self

        
    def add_to_back(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            return self

        runner = self.head
        while runner.next != None:
            runner = runner.next
        runner.next = new_node
        return self


    def print_values(self):
        if self.head == None:
            print("this list is empty")
            return self
        runner = self.head
        while runner.next != None:
            print(runner.data)
            runner = runner.next
        return self 


pets = SLList()

pets.print_values()

pets.add_to_back("1-buttercup")

pets.print_values()

print(pets.head.data)

pets.add_to_front("2-mia")
pets.add_to_front("3-bubbles")
pets.add_to_back("4-logan")
pets.add_to_front("5-lenny")
pets.add_to_front("6-tia")
pets.add_to_front("7-popsy")
pets.add_to_front("8-franny")

pets.print_values()



# 8
# 7
# 6
# 5
# 3
# 2
# 1
# 4