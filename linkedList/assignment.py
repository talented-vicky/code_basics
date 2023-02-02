#1- def insert_after_value(self, data_after, data_to_insert):
    #se
#2- creating double linked list

class Node:
    def __init__(self, data=None, nextData=None):
        self.data = data
        self.nextData = nextData
        
class LinkedList():
    def __init__(self):
        self.head = None

    def insert_at_start(self, data):
        self.head = Node(data, self.head)
        #print('ref gen for entry', data, 'is:' , self.head)

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        
        itr = self.head
        while itr.nextData:
            itr = itr.nextData

        itr.nextData = Node(data, None)

    def insert_array(self, value):
        # self.head = None
        for check in value:
            self.insert_at_end(check)

    def listLength(self):
        counter = 0
        itr = self.head
        
        while itr:
            #counter += 1
            itr = itr.nextData
            counter += 1
            
        return counter

    def remove_atSpecific(self, ind):
        if ind < 0 or ind >= self.listLength():
            raise Exception('invalid index')
        if ind == 0:
            self.head = self.head.nextData #if head is removed, let next element be new head
            return

        counter = 0
        itr = self.head
        while itr:
            if counter == ind - 1:
                itr.nextData = itr.nextData.nextData
                break
            
            # taking [4, 8, 1, 9, 3] as my current linkedList
            # I passed ind as 3, so I need to get to ref attached to 1 (which yields elem 9)
            # counter begins iteration from 0 and gets to 2 (ind - 1 => 3 - 1 => 2)
            # itr would have gotten to elem 1 (since it made three iterations)
            # then itr.nextData == ref attached to 1 (which points at elem 9)
            # and itr.nextData.nextData == ref attached to 9 (which points at elem 3)
            # now reference (attached to 1) that points at elem 9 now points at elem 3
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
            if counter == ind - 1: 
                itr.nextData = Node(data, itr.nextData) # simply modifying the pointer of prev elem

                # taking [4, 8, 1, 9, 3] as my current linkedList
                # I passed ind as 3, and data as 12 so I need to get to ref attached to 1 (which yields elem 9)
                # counter begins iteration from 0 and gets to 2 (ind - 1 => 3 - 1 => 2)
                # itr would have gotten to elem 1 (since it made three iterations)
                # then itr.nextData == ref attached to 1 (which points at elem 9)
                # and Node(data, itr.nextData) adding a node here
                
                # now reference (attached to 1) that points at elem 9 now points at elem 3
                # hence results in [4, 8, 1, 12, 9, 3]
                
            itr = itr.nextData
            counter += 1

    def insert_val_afterSpecific(self, data_after, data_insert):
        itr = self.head
        while itr:
            #print(itr.data, itr.nextData) #uncomment this for better understanding
            if itr.data == data_after:
                itr.nextData = Node(data_insert, itr.nextData)

                # taken [4, 8, 1, 9, 3] as my current linkedList
                # I passed data_after as 8 and data_insert as 26
                # counter begins iteration and gets to elem 8
                # then itr.nextData == (is not elem 1 but) Node reference to elem 1
                # and Node(data_insert, itr.nextData) == Node(26, Node reference to elem 1)
                # hence results in [4, 8, 26, 1, 9, 3]

            itr = itr.nextData
            
    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        
        itr = self.head 
        llstr = ''

        while itr:
            llstr += str(itr.data) + ' --> '
            itr = itr.nextData

        print(llstr)

if __name__ == '__main__':
    result = LinkedList()
    result.insert_at_start(6)
    result.insert_at_start(4)
    result.insert_at_start(1)
    #result.insert_array([4, 8, 1, 9, 3])
    #result.remove_atSpecific(3)
    #result.insert_val_afterSpecific(9, 26)
    #result.insert_val_atSpecific(3, 91)
    result.print()
