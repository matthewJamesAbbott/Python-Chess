
class Node:

  def __init__(self, data, next=None):
    self.data = data
    self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def addNode(self, data):
        newNode = Node(data)
        if (self.head):
            current = self.head
            while (current.next):
                current = current.next
            current.next = newNode
        else:
            self.head = newNode

# of course were returning a python list here but to keep naming the same I have kept the function name.:)
    def returnVector(self):
        temp = self.head
        moveList = []
        while (temp != None)
            moveList.append(temp.x)
            moveList.append(temp.y)
            temp = temp.next

        return moveList


class MoveCalculator:

    def __init__(self):

    def __del__(self):

