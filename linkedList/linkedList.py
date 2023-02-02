class Node:
    def __init__(self, data=None, nextData=None):
        self.data = data
        self.nextData = nextData
        
    #   0x00500         0x00A1         0x00C5         0x00D7          0x00C0
    #   banana|0x00A1-->avocado|0x00C5-->sherry|0x00D7-->orange|0x00C0-->pineapple|Null
    
    #   banana|nextData-->avocado|nextData-->sherry|nextData-->orange|nextData-->pineapple|None
    #   data[0]     |     data[1]   |        data[2]    |      data[3]      |    data[4]    |
    #               |               |                   |                   |               |
    #           callsAvocado      callsSherry          callsOrange          callsPine        noCall
    
    # self.data always yields VALUE of data while self.nextData (doesn't yield value
    # of next element data) actually yields REFERENCE to next elem data
        
class LinkedList():
    def __init__(self):
        self.head = None

    def insert_at_start(self, data):
        self.head = Node(data, self.head)
        # self.head moves from None, to elem first inserted, to complete linkedList

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

    def remove_atSpecific(self, ind):
        if ind < 0 or ind >= self.listLength():
            raise Exception('invalid index')
        if ind == 0:
            self.head = self.head.nextData #if head is the target, let next element be new head
            return

        counter = 0
        itr = self.head
        while itr:
            if counter == ind - 1:
                itr.nextData = itr.nextData.nextData
                break
            # taken [4, 8, 1, 9, 3] as my current linkedList
            # I passed ind as 3, so I need to get to elem 9
            # counter begins iteration and gets to 2 (ind - 1 => 3 - 1 => 2)
            # itr would have gotten to (elem 1 since it made three iterations)
            # then itr.nextData == 9 // and itr.nextData.nextData == 3
            # hence results in [4, 8, 1, 3]
            
            itr = itr.nextData
            counter += 1

    def insert_val_atSpecific(self, ind, data):
        if ind < 0 or ind >= self.listLength():
            raise Exception('invalid index')
        
        if ind == 0:
            self.head = Node(data, self.head)
            return
        
        counter = 0
        itr = self.head
        while itr:
            if counter == ind - 1: # we'll always do ind-1 to reach actual elem
                # remember position starts from zero, so we're always 1 behind
                itr.nextData = Node(data, itr.nextData)
                
            itr = itr.nextData
            counter += 1

        #1- itr = self.head
        #2- while itr:
            #3- itr = itr.nextData
        # the three lines are simple iterations through the linked list, noteD
            
            
    def output(self):
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
    result.output()
    #result.remove_atSpecific(0)
    result.output()
    result.insert_val_atSpecific(3, 7)
    result.output()
    print('the length of the linkedList is: ' , result.listLength())
