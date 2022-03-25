import random

from MoveCalculator import MoveCalculator
from MoveCalculator import LinkedList

class TreeNode:
    def __init__(self, rank, x, y, xa, ya):
        self.rank = rank
        self.x = x
        self.y = y
        self.xa = xa
        self.ya = ya
        self.leftTreeNode = None
        self.rightTreeNode = None


class Tree:
    def __init__(self):
        self.head = None


    def addTreeNode(self, rank, x, y, xa, ya):
        newTreeNode = TreeNode(rank,x,y,xa,ya)
        if (self.head == None):
            self.head = newTreeNode
        else:
            current = self.head
            parent = None
            while (True):
                parent = current
                if (rank < current.rank):
                    current = current.leftTreeNode
                    if (current == None):
                        parent.leftTreeNode = newTreeNode
                        break


                else:
                    current = current.rightTreeNode
                    if (current == None):
                        parent.rightTreeNode = newTreeNode
                        break

class Engine:
    def __init__(self):
        self.treeList = []


    def moveVector(self, localRoot, base):
        if(localRoot != None):
            self.moveVector(localRoot.leftTreeNode, base)
            if(localRoot.rank == base):
                self.treeList.append(localRoot.x)
                self.treeList.append(localRoot.y)
                self.treeList.append(localRoot.xa)
                self.treeList.append(localRoot.ya)
            self.moveVector(localRoot.rightTreeNode, base)

    def returnRank(self, localRoot):

        if(localRoot != None):
            index = localRoot.rank
            self.returnRank(localRoot.rightTreeNode)
        else:
            return index

    def resolveMove(self, gameBoard):
        moveTree = Tree()

        calc = MoveCalculator()

        base = 0


        for e in range(0, 8):
            for i in range(0, 8):
                if(gameBoard.returnSquare(e, i).find("Black")):
                    list = calc.possibleSquares2DArray(e,i, gameBoard)
                    moveVector2 = list.returnWeightedVector()
                    for j in range(0, len(moveVector2), 3):
                        a = moveVector2[j]
                        b = moveVector2[j+1]
                        c = moveVector2[j+2]
                        if c > base:
                            base = c
                        if (c >= 0 and c <= 10):
                            moveTree.addTreeNode(c,e,i,a,b)


        self.moveVector(moveTree.head, base)


        if(len(self.treeList) > 4):
            test = int(len(self.treeList) / 4)
            choice = random.randint(1, test)
            choice = choice * 4
        else:
            choice = 0


        move = []
        move.append(self.treeList[int(choice)-4])
        move.append(self.treeList[int(choice)-3])
        move.append(self.treeList[int(choice)-2])
        move.append(self.treeList[int(choice)-1])

        return move

