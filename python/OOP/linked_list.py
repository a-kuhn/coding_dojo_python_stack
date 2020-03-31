class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class LList():
    def __init__(self):
        self.head = None


    def print_values(self):
        values = []
        runner = self.head
        while runner.next != None:
            values.append(runner.data)
            runner = runner.next
        values.append(runner.data)
        print(f"current list: {values}")
        return self


    def add_to_end(self, data):
        #create new_node
        new_node = Node(data)

        #check for existance of head
        if self.head == None:
            self.head = new_node
            print(f"CREATING: new_node, data= {data} is the first object in the list")
            return self

        #use runner to traverse list and find last node
        runner = self.head
        while runner.next != None:
            runner = runner.next 

        #set last node's next to new_node
        runner.next = new_node
        print(f"CREATING: new_node, data= {data} is now the end of the list")
        return self


    def add_to_front(self, data):
        #create new node
        new_node = Node(data)

        #test for existance of head
        if self.head == None:
            self.head = new_node
            return self
        
        #change new_node.next to point to current head
        new_node.next = self.head

        #change head to new_node
        self.head = new_node
        print(f"CREATING: new_node, data= {data} is now the front of the list")
        return self


    def remove_from_front(self):
        #identify node to be removed from list
        del_node = self.head

        #redirect head to next node in list
        self.head = del_node.next

        #remove link from node to be deleted
        del_node.next = None

        print(f"REMOVED: {del_node.data} from the front of the list")
        return del_node

    def remove_from_end(self):
        pass




stuff = LList()

stuff.add_to_end('mammalia')
stuff.print_values()

# stuff.add_to_end('primates')
# stuff.print_values()

# stuff.add_to_end('human')
# stuff.print_values()

# stuff.add_to_front('chordata')
# stuff.print_values()

# stuff.add_to_front('animalia')
# stuff.print_values()

# stuff.remove_from_front()
# stuff.remove_from_front()
# stuff.print_values()
