class Node:
    def __init__(self, data=None, nextData=None):
        self.data = data
        self.nextData = nextData
        
    #   index=0          index=1           index=2          index=3
    #   banana|nextData-->mango|nextData-->grape|nextData-->orange|None
        
class LinkedList():
    def __init__(self):
        self.head = None

    def insert_at_start(self, data):
        node = Node(data, self.head)
        # instantiating Node class (1st param is inputData(data), 2nd is existing list(None at start => pointing at class variable))
        self.head = node
        # redifining class variable (initially node) to our linkedlist; with only one data

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        
        itr = self.head
        while itr.nextData: 
            itr = itr.nextData
            #at final step (NextData = None) i.e itr.nextData has no value, hence iteration ends

        itr.nextData = Node(data, None)

    def insert_array(self, value):
        # self.head = None
        for check in value:
            self.insert_at_end(check)

    def listLength(self):
        counter = 0
        itr = self.head
        
        while itr:
            counter += 1
            itr = itr.nextData
            
        return counter

    def remove_specific(self, ind):
        if ind < 0 or index >= self.listLength():
            raise Exception('invalid index')
        if ind == 0:
            self.head = self.head.nextData #if head is removed, let next element be new head
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1: #if the previous num to the passed index is attained             
                itr.nextData = itr.nextData.nextData #
                break
            
            itr = itr.nextData
            count += 1
            
    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        
        # hence linkedlist has something in it(which I already initialized to likedList), so...
        itr = self.head 
        llstr = ''

        while itr:
            llstr += str(itr.data) + ' --> '
            # itr.data returns the value of the first parma in the list
            itr = itr.nextData
            # at final step (itr = Null (no value present) hence iteration ends

        print(llstr)

if __name__ == '__main__':
    result = LinkedList()
    result.insert_at_start(73)
    result.insert_at_start(5)
    result.insert_at_start(9)
    result.insert_at_end(12)
    result.insert_at_end(901)
    result.insert_array([5, 7, 6])
    result.print()
    print('the length of the linkedList is: ' , result.listLength())
