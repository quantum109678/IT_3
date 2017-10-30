
class ListNode:
    def __init__(self):
        self.value=0
        self.next=None

class LinkedList:

  
    
    def __init__(self):
        self.head=ListNode()
        """Create a new list with a Sentinel Node"""
        #pass

    def insert(self,x,p):
        temp=ListNode()
        temp.value=x
        temp.next=p.next
        p.next=temp
    
        
    
        """Insert element x in the position after p"""
        #pass

    def delete(self,p):
        p.next=p.next.next

        """Delete the node following node p in the linked list."""
        #pass

    def printlist(self):
        tmp=self.head.next
        while tmp!=None:
            print(tmp.value, end=' ')
            tmp=tmp.next
        """ Print all the elements of a list in a row."""
        #pass

    def insertAtIndex(self,x,i):
        p=self.head
        while i>0:
            p=p.next
            i=i-1
        self.insert(x,p)


        """Insert value x at list position i. (The position of the first element is taken to be 0.)"""
        #pass

    def search(self,x):
        tmp=self.head
        while tmp!=None:
            if tmp.value==x:
                return(tmp.next)
            else:
                return(None)
            tmp=tmp.next


        """Search for value x in the list. Return a reference to the first node with value x; return None if no such node is found."""
        #pass

    def len(self):
        c=0
        tmp=self.head.next
        while tmp!=None:
            c=c+1
            tmp=tmp.next
        return(c)
        """Return the length (the number of elements) in the Linked List."""
        #pass

    def isEmpty(self):
        if self.head.next==None:
            return("True")
        else:
            return("False")
        """Return True if the Linked List has no elements, False otherwise."""
        #pass


class ListNode:
    def __init__(self):
        self.value=0
        self.next=None

def main():
    L = LinkedList()
    L.insert(10,L.head)
    print("List is :")
    L.printlist()
    print()
    L.insert(12,L.head.next)
    print("List is :")
    L.printlist()
    print()
    L.insert(2,L.head)
    print("List is :")
    L.printlist()
    print()
    l=L.len()
    print('Size of L is ', end='')
    print(l)
    L.delete(L.head)
    print("List is :")
    L.printlist()
    print()
    L.delete(L.head.next)
    print("List is :")
    L.printlist()
    print()
    e=L.isEmpty()
    print('List is empty?', end='')
    print(e)
    l=L.len()
    print('Size of L is ', end='')
    print(l)
    L.delete(L.head)
    e=L.isEmpty()
    print('List is empty?', end='')
    print(e)
    l=L.len()
    print('Size of L is ', end='')
    print(l)
    L.insertAtIndex(2,0)
    L.insertAtIndex(1,0)
    L.insertAtIndex(4,2)
    L.insertAtIndex(3,2)
    print('List is: ')
    L.printlist()
    print()
    p=L.search(1)
    print(p)

if __name__ == '__main__':
    main()