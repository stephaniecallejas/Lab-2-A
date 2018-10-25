# CS2302
# NAME: Stephanie Callejas
# Assigment: Lab 2 Option A
# Instructor: Diego Aguirre
# T.A: Manoj Saha
# Date: October 24,2018
# Purpose: Merge two companies IDs using linked lists

import copy
class Node(object):
    item = -1
    next = None

    def __init__1(self,item):
        self.item = item
        self.next = None

    def __init__(self,item,next):
        self.item = item
        self.next = next

    def getID(self):
        return self.item

    def getNext(self):
        return self.next

    def setID(self, newdata):
        self.item = newdata

    def setNext(self, newnext):
        self.next = newnext


class linked_list:
    def __init__(self):
        self.head = None
        self.tail = None

    # Adds node at the tail #
    def append(self, item):
        new_Node = Node(item)

        if self.head is None:
            self.head = new_Node

        if self.tail is None:
            self.tail = new_Node

        self.tail.next = new_Node

    # Adds node as new head and attaches list #
    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def printL(self):
        current = self.head
        while current != None:
            print(current.getID())
            current = current.getNext()

#########################################################################


def find_duplicates(self, head):
    self.ptr1 = None
    self.ptr2 = None
    ptr1 = head

    # pick elements one by one
    while ptr1 is not None and ptr1.next is not None:
        ptr2 = ptr1

        # compare the picked element with the rest of the elements
        while ptr2.next is not None:
             # if duplicate then print it
            if ptr1.item == ptr2.next.item:
                print(ptr1.item)
            ptr2 = ptr2.next
        ptr1 = ptr1.next
    return head


a = find_duplicates(linked_list)
print('The duplicate IDs are:')
a.printL()


###################### BUBBLE SORT #####################################

def bubbleSort(self,a):
        # temp = a
    if a is None:
        return a
    for i in range(0, 6000):
        head = a
        for j in range(0, 6000):  # for(a is not None)
            if head.getID() == head.getNext().getID():
                head = head.getNext()
            elif head.getID() > head.getNext().getID():
                temp = head.getID()
                head.item = head.getNext().getID()
                head.next.item = temp

            head = head.getNext()
    return head


b = bubbleSort(linked_list)
print('The duplicate IDs are:')
b.printL()

###################### MERGE SORT ######################################


def midpoint(node):
        # pointers #
    fast = node.getNext()
    slow = node

    while fast is not None:
        fast = fast.getNext()
        if fast is not None:
            slow = slow.getNext()
            fast = fast.getNext()  # every time slow moves, fast moves twice
    return slow


def sort(leftN,rightN):
    head = Node(None)
    current = head
   
    while leftN is not None and rightN is not None:
        if leftN.getID() < = rightN.getID():  
            current.setNext(leftN)  # current points to left ID
            leftN = leftN.getNext()  # move it to the right
        else:
            current.setNext(rightN)  # current point to right ID
            temp = leftN.getID() # temp stores the left ID
            leftN.getID() = rightN.getID() 
            leftN.getNext().getID() = temp
    if leftN is None:  # if left is none, point to right
       current.setNext(rightN)
    else:
       current.setNext(leftN)  # if right is none, point to left
    return head.getNext()  # return correctly arranged items


def mergeSort(self, head):
   
    if head is None or head.getNext() is None:
        return head

    middle = midpoint(head)
    middleNext = middle.getNext()

    # recursive calls for left and right sides 
    left = self.mergeSort(head)
    right = self.mergeSort(middleNext)

    # Merge the lists 
    sortedList = sort(left, right)
    return sortedList


def s3(list):
    templist = copy.copy(list)  # make copy of original list
    merged = templist.mergeSort(templist.head)
    duplicates = linked_list()
    while merged.getNext() is not None:
        if merged.getID() == merged.getNext().getID():  # compare IDs
            duplicates.add(merged.getID())  # if they match, add them to list
        merged = merged.getNext()
    return duplicates


c = s3(linked_list)
print('The duplicate IDs are:')
c.printL()


#################################################################################

def s4(list):
    seen = [False]  # create a 1D boolean array of only False
    for i in range(6001):
        current = list.head
        duplicates = linked_list()

    while current.getNext() is not None:  # traverse the list
        item = current.getID()  # set 'item' to current ID
        if seen[item]:
            duplicates.add(item)  # if it's been seen before, add to list
        else:
            seen[item] = True  
        current = current.getNext()  # move on to next ID
    return duplicates


d = s4(linked_list)
print('The duplicate IDs are:')
d.printL()

#################################################################################


def combinelists(self):
    for i in range(0, 6000):
        list.append(my_linkedList1.head.item)
        my_linkedList1.head = my_linkedList1.head.next
    my_linkedList1.printL()


list = linked_list()
    # open the file
with open('activision.txt', 'r') as file:
        my_linkedList1 = linked_list()
        for line in file:
            my_linkedList1.append(line)
    # print(my_linkedList1.head.item)

with open('vivendi.txt', 'r') as file:
    my_linkedList2 = linked_list()
    for line in file:
        my_linkedList2.append(line)

my_linkedList1.tail.next = my_linkedList2.head



