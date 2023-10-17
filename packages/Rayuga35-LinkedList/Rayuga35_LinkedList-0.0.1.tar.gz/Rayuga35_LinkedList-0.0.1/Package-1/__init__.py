

#Create Node

class createnode:
    def __init__(self,data) -> None:
        self.data = data
        self.next = None


class linkedlist:
    def __init__(self) -> None:
        self.head = None


# INSERT AT TAIL OF A NODE
    def insert_at_tail(self,value):
        new_node = createnode(value)
        if(self.head is None):
            self.head = new_node
            print("Node Inserted Sucessfully At The Tail!")
            return
        iterater = self.head
        while(iterater.next !=None):
            iterater = iterater.next
        
        iterater.next = new_node
        print("Node Inserted Sucessfully At The Tail!")

# INSERT AT HEAD OF A NODE
    def insert_at_head(self, value):
        new_node= createnode(value)
        new_node.next = self.head 
        self.head = new_node
        print("Node Inserted Sucessfully At The Head!")

# INSERT AT PARTICULAR INDEX OF A NODE
    def insert_at_index(self, loc, value):
        if self.head is None:  # check if the Linked List is empty or not
            print("LinkedList is empty")
            return

        new_node = createnode(value)  # Create new node & Put in the data

        if loc == self.head:  # If loc is at the first position
            new_node.next = self.head.next
            self.head.next = new_node
            print("Node Inserted Sucessfully At The Index!")
            return

        temp = self.head  # Check if the given loc exists
        while temp.data != loc:
            temp = temp.next
            if temp == None:
                print("Index Doesn't Exist In Linkedlist!")
                return

        new_node.next = temp.next
        temp.next = new_node
        print("Node Inserted Sucessfully At The Index!")

# DELETE THE START OF A  NODE
    def delete_at_head(self):
        if self.head is None:
            print("LinkedList is empty")
            return 
        self.head = self.head.next
        print("Node Deleted Sucessfully At The Head")

# DELETE THE LAST OF A NODE
    def delete_at_tail(self):
        if self.head is None:
            print("LinkedList is empty")
            return
        else:
            temp = self.head
            while(temp.next.next is not None):
                temp = temp.next

            temp.next = None
            print("Node Deleted Sucessfully At The Tail")

# DELETE THE NODE BY VALUE
    def delete_by_value(self , value):

        if self.head is None:
            print("LinkedList is empty")
            return
        
        while self.head is not None and self.head.data == value:
            self.head = self.head.next

        currentNode = self.head
        while currentNode is not None:
            while currentNode.next and currentNode.next.data == value:
                currentNode.next = currentNode.next.next
            currentNode = currentNode.next
              

# TO FIND LENGTH OF LINKEDLIST
    def length(self,head):
        if head is None:
            print("LinkedList is Empty")
        else:
            temp = head
            c = 0
            while temp != None:
                c = c + 1
                temp = temp.next
            return c

# TO REVERSE THE LINKEDLIST
    def reverse(self):
        prev = None
        current = self.head

        while current is not None:
            temp = current.next
            current.next = prev
            prev = current
            current = temp

        self.head = prev
        print("Reverse Done Successfully!")

# TO SEARCH NODE IN A LINKEDLIST
    def search(self, find):
        if self.head is None:
            print("LinkedList is Empty so Your value " + str(find) + " is not present")
        else:
            temp = self.head
            flag = False
            location = 0
            counter = 0
            while temp != None:
                counter = counter + 1
                if temp.data == find:
                    flag = True
                    location = counter
                    break
                else:
                    temp = temp.next

        if flag == True:
            print("Your Value Found!..." + "at index " + str(location))
            return location
        else:
            print("Your Value Is Not Present In LinkedList")
            return -1

# PRINT MIDDLE OF A LINKEDLIST
    def middle(self):
        counter = 0
        if(self.head is None):
            print("Linkedlist is empty so middle is zero")
            return
        
        temp = self.head
        while(temp.next!=None):
            counter = counter + 1
            temp = temp.next

        if(counter%2==0):
            middle = counter//2
            c = 1
            temp = self.head
            while(c!=(middle+1)):
                temp = temp.next
                c = c + 1
            
            return temp.data , -1
        else:
            middle = counter//2
            c = 1
            temp = self.head
            while(c!=middle):
                temp = temp.next
                c = c +  1
            
            return temp.data , temp.next.data

#  function that counts the number of times a given int occurs in a Linked List
    def occurence(self,key):
        res = 0
        if(self.head is None):
            print("linkedlist is empty..!")
        else:
            temp = self.head
            while(temp!=None):
                if(temp.data == key):
                    res = res + 1
                temp = temp.next 
            
            return res
 
# Intersection of two linkedlist

    def intersection(self,h1,h2):
        temp1 = h1
        temp2 = h2
        object = linkedlist()
        while(temp1 is not None):
            while(temp2 is not None):
                if(temp1.data == temp2.data):
                    object.insert_at_last(temp1.data)
                    temp2 = temp2.next
                    break
                else:
                    temp2 = temp2.next
            temp1 = temp1.next
            temp2 = h2
        return object.head


# TO DISPLAY LINKEDLIST JUST BY SENDING HEAD OF LINKEDLIST
    def display(self,head):
        if(head is None):
            print("linkedlist is empty")
        
        temp = head
        while(temp is not None):
            print(temp.data,end="===>")
            temp = temp.next
        print("None")