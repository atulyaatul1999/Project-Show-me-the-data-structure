class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    def __repr__(self):
        return str(self.value)
class LinkedList:
    def __init__(self):
        self.head = None
    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        if len(out_string)==0:
            return "No common element in the Linked lists"
        return out_string

    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return
        node = self.head
        while node.next:
            node = node.next
        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next
        return size

def union(llist_1, llist_2):
    ll=LinkedList()
    size1=llist_1.size()
    size2=llist_2.size()
    head1=llist_1.head
    head2=llist_2.head
    a=set()
    i=0
    while i<size1:
        a.add(head1.value)
        head1=head1.next
        i+=1
    i=0
    while i<size2:
        a.add(head2.value)
        head2=head2.next
        i+=1
    for i in a:
        ll.append(i)
    return ll
def intersection(llist_1, llist_2):
    ll=LinkedList()
    size1=llist_1.size()
    size2=llist_2.size()
    head1=llist_1.head
    head2=llist_2.head
    a=set()
    i=0
    while i<size1:
        a.add(head1.value)
        head1=head1.next
        i+=1
    i=0
    while i<size2:
        if head2.value in a:
            ll.append(head2.value)
            a.remove(head2.value)
        head2=head2.next
        i+=1
    return ll
# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))
#its output is the union of both the linked lists i.e. 32,65,2,35,3,4,6,1,9,11,21
print (intersection(linked_list_1,linked_list_2))
#its output is 6, 4, 21

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))
#its output is-65, 2, 35, 3, 4, 6, 1, 7, 8, 9, 11, 21, 23
print (intersection(linked_list_3,linked_list_4))
# as there is no element in its intersection so the output is- "No common element in the Linked lists"

element_1 = [3]
element_2 = []
linked_list_5 = LinkedList()
linked_list_6 = LinkedList()
for i in element_1:
    linked_list_5.append(i)

for i in element_2:
    linked_list_6.append(i)

print (union(linked_list_5,linked_list_6))
# its output is 3
print (intersection(linked_list_5,linked_list_6))
# as there is no element in its intersection so the output is- "No common element in the Linked lists"


#we can also return a empty string instead of the message as we are showing in the return of empty string in the intersection .