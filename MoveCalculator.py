
class Node:

  def __init__(self, x, y, squareRank, next=None):
    self.x = x
    self.y = y
    self.squareRank = squareRank
    self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def addNode(self, x, y, squareRank):
        newNode = Node(x, y, squareRank)
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
        while (temp != None):
            moveList.append(temp.x)
            moveList.append(temp.y)
            temp = temp.next

        return moveList

    def returnWeightedVector(self):
        temp = self.head
        moveList= []
        while (temp != None):
            moveList.append(temp.x)
            moveList.append(temp.y)
            moveList.append(temp.squareRank)
            temp = temp.next

        return moveList


class MoveCalculator:

#    def __init__(self):

#    def __del__(self):

    def evaluatePiece(self, x, y, moveBoard):

        if (moveBoard.returnSquare(x, y) == "Black Pawn"):
            return 2

        elif (moveBoard.returnSquare(x, y) == "Black Left Knight" or moveBoard.returnSquare(x, y) == "Black Right Knight"):
            return 3
        elif (moveBoard.returnSquare(x, y) == "Black Left Bishop" or moveBoard.returnSquare(x, y) == "Black Right Bishop"):
            return 4
        elif (moveBoard.returnSquare(x, y) == "Black Left Rook" or moveBoard.returnSquare(x, y) == "Black Right Rook"):
            return 5
        elif (moveBoard.returnSquare(x, y) == "Black Queen"):
            return 9
        elif (moveBoard.returnSquare(x, y) == "Black King"):
            return 10
        elif (moveBoard.returnSquare(x, y) == "Empty"):
            return 0


    def possibleSquares2DArray(self, x, y, moveBoard):
        piece = moveBoard.returnSquare(x, y)

        switchedPiece = 0
        if (piece == "White Left Rook"):
            switchedPiece = 1
        if (piece == "White Left Knight"):
            switchedPiece = 2
        if (piece == "White Left Bishop"):
            switchedPiece = 3
        if (piece == "White Queen"):
            switchedPiece = 4
        if (piece == "White King"):
            switchedPiece = 5
        if (piece == "White Right Bishop"):
            switchedPiece = 6
        if (piece == "White Right Knight"):
            switchedPiece = 7
        if (piece == "White Right Rook"):
            switchedPiece = 8
        if (piece == "White Pawn"):
            switchedPiece = 9
        if (piece == "Black Left Rook"):
            switchedPiece = 10
        if (piece == "Black Left Knight"):
            switchedPiece = 11
        if (piece == "Black Left Bishop"):
            switchedPiece = 12
        if (piece == "Black Queen"):
            switchedPiece = 13
        if (piece == "Black King"):
            switchedPiece = 14
        if (piece == "Black Right Bishop"):
            switchedPiece = 15
        if (piece == "Black Right Knight"):
            switchedPiece = 16
        if (piece == "Black Right Rook"):
            switchedPiece = 17
        if (piece == "Black Pawn"):
            switchedPiece = 18
        if (piece == "Empty"):
            switchedPiece = 19

        list = LinkedList()
        match switchedPiece:

            case 1: # White Left Rook Moves
                for i in range(x+1, 8):
                    if (moveBoard.returnSquare(i, y) == "Empty"):
                        list.addNode(i, y, self.evaluatePiece(i,y, moveBoard))
                    elif ((x < 8) and (moveBoard.returnSquare(i, y).find("Black") == False)):
                        list.addNode(i, y, self.evaluatePiece(i,y, moveBoard))
                        break
                    elif (moveBoard.returnSquare(i, y) != "Empty"):
                        break
                for i in range(x - 1, -1, -1):
                    if (moveBoard.returnSquare(i, y) == "Empty"):
                        list.addNode(i, y, self.evaluatePiece(i,y, moveBoard))
                    elif ((x >= 0 ) and (moveBoard.returnSquare(i, y).find("Black") == False)):
                        list.addNode(i, y, self.evaluatePiece(i,y, moveBoard))
                        break
                    elif (moveBoard.returnSquare(i, y) != "Empty"):
                        break
                for i in range(y + 1, 8):
                    if (moveBoard.returnSquare(x, i) == "Empty"):
                        list.addNode(x, i, self.evaluatePiece(x,i, moveBoard))
                    elif ((x >= 0 ) and (moveBoard.returnSquare(x, i).find("Black") == False)):
                        list.addNode(x, i, self.evaluatePiece(x,i, moveBoard))
                        break
                    elif (moveBoard.returnSquare(x, i) != "Empty"):
                        break
                for i in range(y - 1, -1, -1):
                    if (moveBoard.returnSquare(x, i) == "Empty"):
                        list.addNode(x, i, self.evaluatePiece(x,i, moveBoard))
                    elif ((x >= 0 ) and (moveBoard.returnSquare(x, i).find("Black") == False)):
                        list.addNode(x, i, self.evaluatePiece(x,i, moveBoard))
                        break
                    elif (moveBoard.returnSquare(x, i) != "Empty"):
                        break

                return list

            case 2: # White Left Knight Moves
                if (x < 6 and y < 7 and moveBoard.returnSquare(x + 2, y + 1) == "Empty"):
                    list.addNode(x + 2, y + 1, self.evaluatePiece(x+2,y+1, moveBoard))
                elif (x < 6 and y < 7 and (moveBoard.returnSquare(x+2, y+1).find("Black") == False)):
                    list.addNode(x + 2, y + 1, self.evaluatePiece(x+2,y+1, moveBoard))
                if (x < 6 and y > 0 and moveBoard.returnSquare(x + 2, y - 1) == "Empty"):
                    list.addNode(x + 2, y - 1, self.evaluatePiece(x+2,y-1, moveBoard))
                elif (x < 6 and y > 0 and (moveBoard.returnSquare(x+2, y-1).find("Black") == False)):
                    list.addNode(x + 2, y - 1, self.evaluatePiece(x+2,y-1, moveBoard))
                if (x < 7 and y < 6 and moveBoard.returnSquare(x + 1, y + 2) == "Empty"):
                    list.addNode(x + 1, y + 2, self.evaluatePiece(x+1,y+2, moveBoard))
                elif (x < 7 and y < 6 and (moveBoard.returnSquare(x+1, y+2).find("Black") == False)):
                    list.addNode(x + 1, y + 2, self.evaluatePiece(x+1,y+2, moveBoard))
                if (x < 7 and y > 1 and moveBoard.returnSquare(x + 1, y - 2) == "Empty"):
                    list.addNode(x + 1, y - 2, self.evaluatePiece(x+1,y-2, moveBoard))
                elif (x < 7 and y > 1 and (moveBoard.returnSquare(x+1, y-2).find("Black") == False)):
                    list.addNode(x + 1, y - 2, self.evaluatePiece(x+1,y-2, moveBoard))
                if (x > 1 and y < 7 and moveBoard.returnSquare(x - 2, y + 1) == "Empty"):
                    list.addNode(x - 2, y + 1, self.evaluatePiece(x-2,y+1, moveBoard))
                elif (x > 1 and y < 7 and (moveBoard.returnSquare(x-2, y+1).find("Black") == False)):
                    list.addNode(x - 2, y + 1, self.evaluatePiece(x-2,y+1, moveBoard))
                if (x > 1 and y < 0 and moveBoard.returnSquare(x - 2, y - 1) == "Empty"):
                    list.addNode(x - 2, y - 1, self.evaluatePiece(x-2,y-1, moveBoard))
                elif (x > 1 and y > 0 and (moveBoard.returnSquare(x-2, y-1).find("Black") == False)):
                    list.addNode(x - 2, y - 1, self.evaluatePiece(x-2,y-1, moveBoard))
                if (x > 0 and y < 6 and moveBoard.returnSquare(x - 1, y + 2) == "Empty"):
                    list.addNode(x - 1, y + 2, self.evaluatePiece(x-1,y+2, moveBoard))
                elif (x > 0 and y < 6 and (moveBoard.returnSquare(x-1, y+2).find("Black") == False)):
                    list.addNode(x - 1, y + 2, self.evaluatePiece(x-1,y+2, moveBoard))
                if (x > 0 and y > 1 and moveBoard.returnSquare(x - 1, y - 2) == "Empty"):
                    list.addNode(x - 1, y - 2, self.evaluatePiece(x-1,y-2, moveBoard))
                elif (x > 0 and y > 1 and (moveBoard.returnSquare(x-1, y-2).find("Black") == False)):
                    list.addNode(x - 1, y - 2, self.evaluatePiece(x-1,y-2, moveBoard))
                return list

            case 3: # White Left Bishop Moves
                for e, i in zip(range(x+1, 8), range(y+1, 8)):
                    if (moveBoard.returnSquare(e, i) == "Empty"):
                        list.addNode(e, i, self.evaluatePiece(e,i, moveBoard))
                    elif (e < 8 and i < 8 and (moveBoard.returnSquare(e, i).find("Black") == False)):
                        list.addNode(e, i, self.evaluatePiece(e,i, moveBoard))
                        break
                    elif (moveBoard.returnSquare(e, i) != "Empty"):
                        break
                for e, i in zip(range(x+1, 8), range(y-1, -1, -1)):
                    if (moveBoard.returnSquare(e, i) == "Empty"):
                        list.addNode(e, i, self.evaluatePiece(e,i, moveBoard))
                    elif (e < 8 and i < 8 and (moveBoard.returnSquare(e, i).find("Black") == False)):
                        list.addNode(e, i, self.evaluatePiece(e,i, moveBoard))
                        break
                    elif (moveBoard.returnSquare(e, i) != "Empty"):
                        break
                for e, i in zip(range(x-1, -1, -1), range(y+1, 8)):
                    if (moveBoard.returnSquare(e, i) == "Empty"):
                        list.addNode(e, i, self.evaluatePiece(e,i, moveBoard))
                    elif (e < 8 and i < 8 and (moveBoard.returnSquare(e, i).find("Black") == False)):
                        list.addNode(e, i, self.evaluatePiece(e,i, moveBoard))
                        break
                    elif (moveBoard.returnSquare(e, i) != "Empty"):
                        break
                for e, i in zip(range(x-1, -1, -1), range(y-1, -1, -1)):
                    if (moveBoard.returnSquare(e, i) == "Empty"):
                        list.addNode(e, i, self.evaluatePiece(e,i, moveBoard))
                    elif (e < 8 and i < 8 and (moveBoard.returnSquare(e, i).find("Black") == False)):
                        list.addNode(e, i, self.evaluatePiece(e,i, moveBoard))
                        break
                    elif (moveBoard.returnSquare(e, i) != "Empty"):
                        break
                return list

            case 4: # White Queen Moves
                for i in range(x+1, 8):
                    if (moveBoard.returnSquare(i, y) == "Empty"):
                        list.addNode(i, y, self.evaluatePiece(i,y, moveBoard))
                    elif ((x < 8) and (moveBoard.returnSquare(i, y).find("Black") == False)):
                        list.addNode(i, y, self.evaluatePiece(i,y, moveBoard))
                        break
                    elif (moveBoard.returnSquare(i, y) != "Empty"):
                        break
                for i in range(x-1, -1, -1):
                    if (moveBoard.returnSquare(i, y) == "Empty"):
                        list.addNode(i, y, self.evaluatePiece(i,y, moveBoard))
                    elif ((x >= 0 ) and (moveBoard.returnSquare(i, y).find("Black") == False)):
                        list.addNode(i, y, self.evaluatePiece(i,y, moveBoard))
                        break
                    elif (moveBoard.returnSquare(i, y) != "Empty"):
                        break
                for i in range(y+1, 8):
                    if (moveBoard.returnSquare(x, i) == "Empty"):
                        list.addNode(x, i, self.evaluatePiece(x,i, moveBoard))
                    elif ((x >= 0 ) and (moveBoard.returnSquare(x, i).find("Black") == False)):
                        list.addNode(x, i, self.evaluatePiece(x,i, moveBoard))
                        break
                    elif (moveBoard.returnSquare(x, i) != "Empty"):
                        break
                for i in range(y-1, -1, -1):
                    if (moveBoard.returnSquare(x, i) == "Empty"):
                        list.addNode(x, i, self.evaluatePiece(x,i, moveBoard))
                    elif ((x >= 0 ) and (moveBoard.returnSquare(x, i).find("Black") == False)):
                        list.addNode(x, i, self.evaluatePiece(x,i, moveBoard))
                        break
                    elif (moveBoard.returnSquare(x, i) != "Empty"):
                        break
                for e, i in zip(range(x+1, 8), range(y+1, 8)):
                    if (moveBoard.returnSquare(e, i) == "Empty"):
                        list.addNode(e, i, self.evaluatePiece(e,i, moveBoard))
                    elif (e < 8 and i < 8 and (moveBoard.returnSquare(e, i).find("Black") == False)):
                        list.addNode(e, i, self.evaluatePiece(e,i, moveBoard))
                        break
                    elif (moveBoard.returnSquare(e, i) != "Empty"):
                        break
                for e, i in zip(range(x+1, 8), range(y-1, -1, -1)):
                    if (moveBoard.returnSquare(e, i) == "Empty"):
                        list.addNode(e, i, self.evaluatePiece(e,i, moveBoard))
                    elif (e < 8 and i >= 0 and (moveBoard.returnSquare(e, i).find("Black") == False)):
                        list.addNode(e, i, self.evaluatePiece(e,i, moveBoard))
                        break
                    elif (moveBoard.returnSquare(e, i) != "Empty"):
                        break
                for e, i in zip(range(x-1, -1, -1), range(y+1, 8)):
                    if (moveBoard.returnSquare(e, i) == "Empty"):
                        list.addNode(e, i, self.evaluatePiece(e,i, moveBoard))
                    elif ( e >= 0 and i < 8 and (moveBoard.returnSquare(e, i).find("Black") == False)):
                        list.addNode(e, i, self.evaluatePiece(e,i, moveBoard))
                        break
                    elif (moveBoard.returnSquare(e, i) != "Empty"):
                        break
                for e, i in zip(range(x-1, -1, -1), range(y-1, -1, -1)):
                    if (moveBoard.returnSquare(e, i) == "Empty"):
                        list.addNode(e, i, self.evaluatePiece(e,i, moveBoard))
                    elif (e > 0 and i > 0 and (moveBoard.returnSquare(e, i).find("Black") == False)):
                        list.addNode(e, i, self.evaluatePiece(e,i, moveBoard))
                        break
                    elif (moveBoard.returnSquare(e, i) != "Empty"):
                        break
                return list

            case 5: # White King Moves
                if (x < 8 and moveBoard.returnSquare(x + 1, y) == "Empty"):
                    list.addNode(x + 1, y, self.evaluatePiece(x+1,y, moveBoard))
                elif (x < 8 and (moveBoard.returnSquare(x+1, y).find("Black") == False)):
                    list.addNode(x + 1, y, self.evaluatePiece(x+1,y, moveBoard))
                if (x > 0 and moveBoard.returnSquare(x - 1, y) == "Empty"):
                    list.addNode(x - 1, y, self.evaluatePiece(x-1,y, moveBoard))
                elif (x > 0 and (moveBoard.returnSquare(x-1, y).find("Black") == False)):
                    list.addNode(x - 1, y, self.evaluatePiece(x-1,y, moveBoard))
                if (y < 8 and moveBoard.returnSquare(x, y + 1) == "Empty"):
                    list.addNode(x, y + 1, self.evaluatePiece(x,y+1, moveBoard))
                elif (y < 8 and (moveBoard.returnSquare(x, y+1).find("Black") == False)):
                    list.addNode(x, y + 1, self.evaluatePiece(x,y+1, moveBoard))
                if (y > 0 and moveBoard.returnSquare(x, y - 1) == "Empty"):
                    list.addNode(x, y - 1, self.evaluatePiece(x,y-1, moveBoard))
                elif (y > 0 and (moveBoard.returnSquare(x, y-1).find("Black") == False)):
                    list.addNode(x, y - 1, self.evaluatePiece(x,y-1, moveBoard))
                if (x < 8 and y < 8 and moveBoard.returnSquare(x + 1, y + 1) == "Empty"):
                    list.addNode(x + 1, y + 1, self.evaluatePiece(x+1,y+1, moveBoard))
                elif (x < 8 and y < 8 and (moveBoard.returnSquare(x+1, y+1).find("Black") == False)):
                    list.addNode(x + 1, y + 1, self.evaluatePiece(x+1,y+1, moveBoard))
                if (x < 8 and y > 0 and moveBoard.returnSquare(x + 1, y - 1) == "Empty"):
                    list.addNode(x + 1, y - 1, self.evaluatePiece(x+1,y-1, moveBoard))
                elif (x < 8 and y > 0 and (moveBoard.returnSquare(x+1, y-1).find("Black") == False)):
                    list.addNode(x + 1, y - 1, self.evaluatePiece(x+1,y-1, moveBoard))
                if (x > 0 and y < 8 and moveBoard.returnSquare(x - 1, y + 1) == "Empty"):
                    list.addNode(x - 1, y + 1, self.evaluatePiece(x-1,y+1, moveBoard))
                elif (x > 0 and y < 8 and (moveBoard.returnSquare(x-1, y+1).find("Black") == False)):
                    list.addNode(x - 1, y + 1, self.evaluatePiece(x-1,y+1, moveBoard))
                if (x > 0 and y > 0 and moveBoard.returnSquare(x - 1, y - 1) == "Empty"):
                    list.addNode(x - 1, y - 1, self.evaluatePiece(x-1,y-1, moveBoard))
                elif (x > 0 and y > 0 and (moveBoard.returnSquare(x-1, y-1).find("Black") == False)):
                    list.addNode(x - 1, y - 1, self.evaluatePiece(x-1,y-1, moveBoard))
                return list

            case 6: # White Right Bishop
                for e, i in zip(range(x + 1, 8), range(y + 1, 8)):
                    if (moveBoard.returnSquare(e, i) == "Empty"):
                        list.addNode(e, i, self.evaluatePiece(e, i, moveBoard))
                    elif (e < 8 and i < 8 and (moveBoard.returnSquare(e, i).find("Black") == False)):
                        list.addNode(e, i, self.evaluatePiece(e, i, moveBoard))
                        break
                    elif (moveBoard.returnSquare(e, i) != "Empty"):
                        break
                for e, i in zip(range(x + 1, 8), range(y - 1, -1, -1)):
                    if (moveBoard.returnSquare(e, i) == "Empty"):
                        list.addNode(e, i, self.evaluatePiece(e, i, moveBoard))
                    elif (e < 8 and i < 8 and (moveBoard.returnSquare(e, i).find("Black") == False)):
                        list.addNode(e, i, self.evaluatePiece(e, i, moveBoard))
                        break
                    elif (moveBoard.returnSquare(e, i) != "Empty"):
                        break
                for e, i in zip(range(x - 1, -1, -1), range(y + 1, 8)):
                    if (moveBoard.returnSquare(e, i) == "Empty"):
                        list.addNode(e, i, self.evaluatePiece(e, i, moveBoard))
                    elif (e < 8 and i < 8 and (moveBoard.returnSquare(e, i).find("Black") == False)):
                        list.addNode(e, i, self.evaluatePiece(e, i, moveBoard))
                        break
                    elif (moveBoard.returnSquare(e, i) != "Empty"):
                        break
                for e, i in zip(range(x - 1, -1, -1), range(y - 1, -1, -1)):
                    if (moveBoard.returnSquare(e, i) == "Empty"):
                        list.addNode(e, i, self.evaluatePiece(e, i, moveBoard))
                    elif (e < 8 and i < 8 and (moveBoard.returnSquare(e, i).find("Black") == False)):
                        list.addNode(e, i, self.evaluatePiece(e, i, moveBoard))
                        break
                    elif (moveBoard.returnSquare(e, i) != "Empty"):
                        break
                return list

  

            case 7: # White Right Knight Moves
                if (x < 6 and y < 7 and moveBoard.returnSquare(x + 2, y + 1) == "Empty"):
                    list.addNode(x + 2, y + 1, self.evaluatePiece(x+2,y+1, moveBoard))
                elif (x < 6 and y < 7 and (moveBoard.returnSquare(x+2, y+1).find("Black") == False)):
                    list.addNode(x + 2, y + 1, self.evaluatePiece(x+2,y+1, moveBoard))
                if (x < 6 and y > 0 and moveBoard.returnSquare(x + 2, y - 1) == "Empty"):
                    list.addNode(x + 2, y - 1, self.evaluatePiece(x+2,y-1, moveBoard))
                elif (x < 6 and y > 0 and (moveBoard.returnSquare(x+2, y-1).find("Black") == False)):
                    list.addNode(x + 2, y - 1, self.evaluatePiece(x+2,y-1, moveBoard))
                if (x < 7 and y < 6 and moveBoard.returnSquare(x + 1, y + 2) == "Empty"):
                    list.addNode(x + 1, y + 2, self.evaluatePiece(x+1,y+2, moveBoard))
                elif (x < 7 and y < 6 and (moveBoard.returnSquare(x+1, y+2).find("Black") == False)):
                    list.addNode(x + 1, y + 2, self.evaluatePiece(x+1,y+2, moveBoard))
                if (x < 7 and y > 1 and moveBoard.returnSquare(x + 1, y - 2) == "Empty"):
                    list.addNode(x + 1, y - 2, self.evaluatePiece(x+1,y-2, moveBoard))
                elif (x < 7 and y > 1 and (moveBoard.returnSquare(x+1, y-2).find("Black") == False)):
                    list.addNode(x + 1, y - 2, self.evaluatePiece(x+1,y-2, moveBoard))
                if (x > 1 and y < 7 and moveBoard.returnSquare(x - 2, y + 1) == "Empty"):
                    list.addNode(x - 2, y + 1, self.evaluatePiece(x-2,y+1, moveBoard))
                elif (x > 1 and y < 7 and (moveBoard.returnSquare(x-2, y+1).find("Black") == False)):
                    list.addNode(x - 2, y + 1, self.evaluatePiece(x-2,y+1, moveBoard))
                if (x > 1 and y < 0 and moveBoard.returnSquare(x - 2, y - 1) == "Empty"):
                    list.addNode(x - 2, y - 1, self.evaluatePiece(x-2,y-1, moveBoard))
                elif (x > 1 and y > 0 and (moveBoard.returnSquare(x-2, y-1).find("Black") == False)):
                    list.addNode(x - 2, y - 1, self.evaluatePiece(x-2,y-1, moveBoard))
                if (x > 0 and y < 6 and moveBoard.returnSquare(x - 1, y + 2) == "Empty"):
                    list.addNode(x - 1, y + 2, self.evaluatePiece(x-1,y+2, moveBoard))
                elif (x > 0 and y < 6 and (moveBoard.returnSquare(x-1, y+2).find("Black") == False)):
                    list.addNode(x - 1, y + 2, self.evaluatePiece(x-1,y+2, moveBoard))
                if (x > 0 and y > 1 and moveBoard.returnSquare(x - 1, y - 2) == "Empty"):
                    list.addNode(x - 1, y - 2, self.evaluatePiece(x-1,y-2, moveBoard))
                elif (x > 0 and y > 1 and (moveBoard.returnSquare(x-1, y-2).find("Black") == False)):
                    list.addNode(x - 1, y - 2, self.evaluatePiece(x-1,y-2, moveBoard))
                return list

            case 8: # White Right Rook Moves
                for i in range(x + 1, 8):
                    if (moveBoard.returnSquare(i, y) == "Empty"):
                        list.addNode(i, y, self.evaluatePiece(i, y, moveBoard))
                    elif ((x < 8) and (moveBoard.returnSquare(i, y).find("Black") == False)):
                        list.addNode(i, y, self.evaluatePiece(i, y, moveBoard))
                        break
                    elif (moveBoard.returnSquare(i, y) != "Empty"):
                        break
                for i in range(x - 1, -1, -1):
                    if (moveBoard.returnSquare(i, y) == "Empty"):
                        list.addNode(i, y, self.evaluatePiece(i, y, moveBoard))
                    elif ((x >= 0) and (moveBoard.returnSquare(i, y).find("Black") == False)):
                        list.addNode(i, y, self.evaluatePiece(i, y, moveBoard))
                        break
                    elif (moveBoard.returnSquare(i, y) != "Empty"):
                        break
                for i in range(y + 1, 8):
                    if (moveBoard.returnSquare(x, i) == "Empty"):
                        list.addNode(x, i, self.evaluatePiece(x, i, moveBoard))
                    elif ((x >= 0) and (moveBoard.returnSquare(x, i).find("Black") == False)):
                        list.addNode(x, i, self.evaluatePiece(x, i, moveBoard))
                        break
                    elif (moveBoard.returnSquare(x, i) != "Empty"):
                        break
                for i in range(y - 1, -1, -1):
                    if (moveBoard.returnSquare(x, i) == "Empty"):
                        list.addNode(x, i, self.evaluatePiece(x, i, moveBoard))
                    elif ((x >= 0) and (moveBoard.returnSquare(x, i).find("Black") == False)):
                        list.addNode(x, i, self.evaluatePiece(x, i, moveBoard))
                        break
                    elif (moveBoard.returnSquare(x, i) != "Empty"):
                        break

                return list
                
            case 9: # White Pawn Moves
                if (x != 7 and moveBoard.returnSquare(x + 1, y) == "Empty"):
                    list.addNode(x + 1, y, self.evaluatePiece(x+1,y, moveBoard))
                if (x == 1 and moveBoard.returnSquare(x + 1, y) == "Empty" and moveBoard.returnSquare(x + 2, y) == "Empty"):
                    list.addNode(x + 2, y, self.evaluatePiece(x+2,y, moveBoard))
                if (x != 7 and y != 7 and (moveBoard.returnSquare(x+1, y+1).find("Black") == False)):
                    list.addNode(x + 1, y + 1, self.evaluatePiece(x+1,y+1, moveBoard))
                if (x != 7 and y != 0 and (moveBoard.returnSquare(x+1, y-1).find("Black") == False)):
                    list.addNode(x + 1, y - 1, self.evaluatePiece(x+1,y-1, moveBoard))
                return list


            case 10: # Black Left Rook Moves
                for i in range(x + 1, 8):
                    if (moveBoard.returnSquare(i, y) == "Empty"):
                        list.addNode(i, y, self.evaluatePiece(i, y, moveBoard))
                    elif ((x < 8) and (moveBoard.returnSquare(i, y).find("White") == False)):
                        list.addNode(i, y, self.evaluatePiece(i, y, moveBoard))
                        break
                    elif (moveBoard.returnSquare(i, y) != "Empty"):
                        break
                for i in range(x - 1, -1, -1):
                    if (moveBoard.returnSquare(i, y) == "Empty"):
                        list.addNode(i, y, self.evaluatePiece(i, y, moveBoard))
                    elif ((x >= 0) and (moveBoard.returnSquare(i, y).find("White") == False)):
                        list.addNode(i, y, self.evaluatePiece(i, y, moveBoard))
                        break
                    elif (moveBoard.returnSquare(i, y) != "Empty"):
                        break
                for i in range(y + 1, 8):
                    if (moveBoard.returnSquare(x, i) == "Empty"):
                        list.addNode(x, i, self.evaluatePiece(x, i, moveBoard))
                    elif ((x >= 0) and (moveBoard.returnSquare(x, i).find("White") == False)):
                        list.addNode(x, i, self.evaluatePiece(x, i, moveBoard))
                        break
                    elif (moveBoard.returnSquare(x, i) != "Empty"):
                        break
                for i in range(y - 1, -1, -1):
                    if (moveBoard.returnSquare(x, i) == "Empty"):
                        list.addNode(x, i, self.evaluatePiece(x, i, moveBoard))
                    elif ((x >= 0) and (moveBoard.returnSquare(x, i).find("White") == False)):
                        list.addNode(x, i, self.evaluatePiece(x, i, moveBoard))
                        break
                    elif (moveBoard.returnSquare(x, i) != "Empty"):
                        break

                return list

            case 11: # Black Left Knight Moves
                if (x < 6 and y < 7 and moveBoard.returnSquare(x + 2, y + 1) == "Empty"):
                    list.addNode(x + 2, y + 1, self.evaluatePiece(x + 2, y + 1, moveBoard))
                elif (x < 6 and y < 7 and (moveBoard.returnSquare(x + 2, y + 1).find("White") == False)):
                    list.addNode(x + 2, y + 1, self.evaluatePiece(x + 2, y + 1, moveBoard))
                if (x < 6 and y > 0 and moveBoard.returnSquare(x + 2, y - 1) == "Empty"):
                    list.addNode(x + 2, y - 1, self.evaluatePiece(x + 2, y - 1, moveBoard))
                elif (x < 6 and y > 0 and (moveBoard.returnSquare(x + 2, y - 1).find("White") == False)):
                    list.addNode(x + 2, y - 1, self.evaluatePiece(x + 2, y - 1, moveBoard))
                if (x < 7 and y < 6 and moveBoard.returnSquare(x + 1, y + 2) == "Empty"):
                    list.addNode(x + 1, y + 2, self.evaluatePiece(x + 1, y + 2, moveBoard))
                elif (x < 7 and y < 6 and (moveBoard.returnSquare(x + 1, y + 2).find("White") == False)):
                    list.addNode(x + 1, y + 2, self.evaluatePiece(x + 1, y + 2, moveBoard))
                if (x < 7 and y > 1 and moveBoard.returnSquare(x + 1, y - 2) == "Empty"):
                    list.addNode(x + 1, y - 2, self.evaluatePiece(x + 1, y - 2, moveBoard))
                elif (x < 7 and y > 1 and (moveBoard.returnSquare(x + 1, y - 2).find("White") == False)):
                    list.addNode(x + 1, y - 2, self.evaluatePiece(x + 1, y - 2, moveBoard))
                if (x > 1 and y < 7 and moveBoard.returnSquare(x - 2, y + 1) == "Empty"):
                    list.addNode(x - 2, y + 1, self.evaluatePiece(x - 2, y + 1, moveBoard))
                elif (x > 1 and y < 7 and (moveBoard.returnSquare(x - 2, y + 1).find("White") == False)):
                    list.addNode(x - 2, y + 1, self.evaluatePiece(x - 2, y + 1, moveBoard))
                if (x > 1 and y < 0 and moveBoard.returnSquare(x - 2, y - 1) == "Empty"):
                    list.addNode(x - 2, y - 1, self.evaluatePiece(x - 2, y - 1, moveBoard))
                elif (x > 1 and y > 0 and (moveBoard.returnSquare(x - 2, y - 1).find("White") == False)):
                    list.addNode(x - 2, y - 1, self.evaluatePiece(x - 2, y - 1, moveBoard))
                if (x > 0 and y < 6 and moveBoard.returnSquare(x - 1, y + 2) == "Empty"):
                    list.addNode(x - 1, y + 2, self.evaluatePiece(x - 1, y + 2, moveBoard))
                elif (x > 0 and y < 6 and (moveBoard.returnSquare(x - 1, y + 2).find("White") == False)):
                    list.addNode(x - 1, y + 2, self.evaluatePiece(x - 1, y + 2, moveBoard))
                if (x > 0 and y > 1 and moveBoard.returnSquare(x - 1, y - 2) == "Empty"):
                    list.addNode(x - 1, y - 2, self.evaluatePiece(x - 1, y - 2, moveBoard))
                elif (x > 0 and y > 1 and (moveBoard.returnSquare(x - 1, y - 2).find("White") == False)):
                    list.addNode(x - 1, y - 2, self.evaluatePiece(x - 1, y - 2, moveBoard))
                return list


            case 12: # Black Left Bishop Moves
                for e, i in zip(range(x + 1, 8), range(y + 1, 8)):
                    if (moveBoard.returnSquare(e, i) == "Empty"):
                        list.addNode(e, i, self.evaluatePiece(e, i, moveBoard))
                    elif (e < 8 and i < 8 and (moveBoard.returnSquare(e, i).find("White") == False)):
                        list.addNode(e, i, self.evaluatePiece(e, i, moveBoard))
                        break
                    elif (moveBoard.returnSquare(e, i) != "Empty"):
                        break
                for e, i in zip(range(x + 1, 8), range(y - 1, -1, -1)):
                    if (moveBoard.returnSquare(e, i) == "Empty"):
                        list.addNode(e, i, self.evaluatePiece(e, i, moveBoard))
                    elif (e < 8 and i < 8 and (moveBoard.returnSquare(e, i).find("White") == False)):
                        list.addNode(e, i, self.evaluatePiece(e, i, moveBoard))
                        break
                    elif (moveBoard.returnSquare(e, i) != "Empty"):
                        break
                for e, i in zip(range(x - 1, -1, -1), range(y + 1, 8)):
                    if (moveBoard.returnSquare(e, i) == "Empty"):
                        list.addNode(e, i, self.evaluatePiece(e, i, moveBoard))
                    elif (e < 8 and i < 8 and (moveBoard.returnSquare(e, i).find("White") == False)):
                        list.addNode(e, i, self.evaluatePiece(e, i, moveBoard))
                        break
                    elif (moveBoard.returnSquare(e, i) != "Empty"):
                        break
                for e, i in zip(range(x - 1, -1, -1), range(y - 1, -1, -1)):
                    if (moveBoard.returnSquare(e, i) == "Empty"):
                        list.addNode(e, i, self.evaluatePiece(e, i, moveBoard))
                    elif (e < 8 and i < 8 and (moveBoard.returnSquare(e, i).find("White") == False)):
                        list.addNode(e, i, self.evaluatePiece(e, i, moveBoard))
                        break
                    elif (moveBoard.returnSquare(e, i) != "Empty"):
                        break
                return list

            case 13: # Black Queen Moves
                for i in range(x + 1, 8):
                    if (moveBoard.returnSquare(i, y) == "Empty"):
                        list.addNode(i, y, self.evaluatePiece(i, y, moveBoard))
                    elif ((x < 8) and (moveBoard.returnSquare(i, y).find("White") == False)):
                        list.addNode(i, y, self.evaluatePiece(i, y, moveBoard))
                        break
                    elif (moveBoard.returnSquare(i, y) != "Empty"):
                        break
                for i in range(x - 1, -1, -1):
                    if (moveBoard.returnSquare(i, y) == "Empty"):
                        list.addNode(i, y, self.evaluatePiece(i, y, moveBoard))
                    elif ((x >= 0) and (moveBoard.returnSquare(i, y).find("White") == False)):
                        list.addNode(i, y, self.evaluatePiece(i, y, moveBoard))
                        break
                    elif (moveBoard.returnSquare(i, y) != "Empty"):
                        break
                for i in range(y + 1, 8):
                    if (moveBoard.returnSquare(x, i) == "Empty"):
                        list.addNode(x, i, self.evaluatePiece(x, i, moveBoard))
                    elif ((x >= 0) and (moveBoard.returnSquare(x, i).find("White") == False)):
                        list.addNode(x, i, self.evaluatePiece(x, i, moveBoard))
                        break
                    elif (moveBoard.returnSquare(x, i) != "Empty"):
                        break
                for i in range(y - 1, -1, -1):
                    if (moveBoard.returnSquare(x, i) == "Empty"):
                        list.addNode(x, i, self.evaluatePiece(x, i, moveBoard))
                    elif ((x >= 0) and (moveBoard.returnSquare(x, i).find("White") == False)):
                        list.addNode(x, i, self.evaluatePiece(x, i, moveBoard))
                        break
                    elif (moveBoard.returnSquare(x, i) != "Empty"):
                        break
                for e, i in zip(range(x + 1, 8), range(y + 1, 8)):
                    if (moveBoard.returnSquare(e, i) == "Empty"):
                        list.addNode(e, i, self.evaluatePiece(e, i, moveBoard))
                    elif (e < 8 and i < 8 and (moveBoard.returnSquare(e, i).find("White") == False)):
                        list.addNode(e, i, self.evaluatePiece(e, i, moveBoard))
                        break
                    elif (moveBoard.returnSquare(e, i) != "Empty"):
                        break
                for e, i in zip(range(x + 1, 8), range(y - 1, -1, -1)):
                    if (moveBoard.returnSquare(e, i) == "Empty"):
                        list.addNode(e, i, self.evaluatePiece(e, i, moveBoard))
                    elif (e < 8 and i >= 0 and (moveBoard.returnSquare(e, i).find("White") == False)):
                        list.addNode(e, i, self.evaluatePiece(e, i, moveBoard))
                        break
                    elif (moveBoard.returnSquare(e, i) != "Empty"):
                        break
                for e, i in zip(range(x - 1, -1, -1), range(y + 1, 8)):
                    if (moveBoard.returnSquare(e, i) == "Empty"):
                        list.addNode(e, i, self.evaluatePiece(e, i, moveBoard))
                    elif (e >= 0 and i < 8 and (moveBoard.returnSquare(e, i).find("White") == False)):
                        list.addNode(e, i, self.evaluatePiece(e, i, moveBoard))
                        break
                    elif (moveBoard.returnSquare(e, i) != "Empty"):
                        break
                for e, i in zip(range(x - 1, -1, -1), range(y - 1, -1, -1)):
                    if (moveBoard.returnSquare(e, i) == "Empty"):
                        list.addNode(e, i, self.evaluatePiece(e, i, moveBoard))
                    elif (e > 0 and i > 0 and (moveBoard.returnSquare(e, i).find("White") == False)):
                        list.addNode(e, i, self.evaluatePiece(e, i, moveBoard))
                        break
                    elif (moveBoard.returnSquare(e, i) != "Empty"):
                        break
                return list
     
            case 14: # Black King Moves
                if (x < 8 and moveBoard.returnSquare(x + 1, y) == "Empty"):
                    list.addNode(x + 1, y, self.evaluatePiece(x + 1, y, moveBoard))
                elif (x < 8 and (moveBoard.returnSquare(x + 1, y).find("White") == False)):
                    list.addNode(x + 1, y, self.evaluatePiece(x + 1, y, moveBoard))
                if (x > 0 and moveBoard.returnSquare(x - 1, y) == "Empty"):
                    list.addNode(x - 1, y, self.evaluatePiece(x - 1, y, moveBoard))
                elif (x > 0 and (moveBoard.returnSquare(x - 1, y).find("White") == False)):
                    list.addNode(x - 1, y, self.evaluatePiece(x - 1, y, moveBoard))
                if (y < 8 and moveBoard.returnSquare(x, y + 1) == "Empty"):
                    list.addNode(x, y + 1, self.evaluatePiece(x, y + 1, moveBoard))
                elif (y < 8 and (moveBoard.returnSquare(x, y + 1).find("White") == False)):
                    list.addNode(x, y + 1, self.evaluatePiece(x, y + 1, moveBoard))
                if (y > 0 and moveBoard.returnSquare(x, y - 1) == "Empty"):
                    list.addNode(x, y - 1, self.evaluatePiece(x, y - 1, moveBoard))
                elif (y > 0 and (moveBoard.returnSquare(x, y - 1).find("White") == False)):
                    list.addNode(x, y - 1, self.evaluatePiece(x, y - 1, moveBoard))
                if (x < 8 and y < 8 and moveBoard.returnSquare(x + 1, y + 1) == "Empty"):
                    list.addNode(x + 1, y + 1, self.evaluatePiece(x + 1, y + 1, moveBoard))
                elif (x < 8 and y < 8 and (moveBoard.returnSquare(x + 1, y + 1).find("White") == False)):
                    list.addNode(x + 1, y + 1, self.evaluatePiece(x + 1, y + 1, moveBoard))
                if (x < 8 and y > 0 and moveBoard.returnSquare(x + 1, y - 1) == "Empty"):
                    list.addNode(x + 1, y - 1, self.evaluatePiece(x + 1, y - 1, moveBoard))
                elif (x < 8 and y > 0 and (moveBoard.returnSquare(x + 1, y - 1).find("White") == False)):
                    list.addNode(x + 1, y - 1, self.evaluatePiece(x + 1, y - 1, moveBoard))
                if (x > 0 and y < 8 and moveBoard.returnSquare(x - 1, y + 1) == "Empty"):
                    list.addNode(x - 1, y + 1, self.evaluatePiece(x - 1, y + 1, moveBoard))
                elif (x > 0 and y < 8 and (moveBoard.returnSquare(x - 1, y + 1).find("White") == False)):
                    list.addNode(x - 1, y + 1, self.evaluatePiece(x - 1, y + 1, moveBoard))
                if (x > 0 and y > 0 and moveBoard.returnSquare(x - 1, y - 1) == "Empty"):
                    list.addNode(x - 1, y - 1, self.evaluatePiece(x - 1, y - 1, moveBoard))
                elif (x > 0 and y > 0 and (moveBoard.returnSquare(x - 1, y - 1).find("White") == False)):
                    list.addNode(x - 1, y - 1, self.evaluatePiece(x - 1, y - 1, moveBoard))
                return list

            case 15: # Black Right Bishop
                for e, i in zip(range(x + 1, 8), range(y + 1, 8)):
                    if (moveBoard.returnSquare(e, i) == "Empty"):
                        list.addNode(e, i, self.evaluatePiece(e, i, moveBoard))
                    elif (e < 8 and i < 8 and (moveBoard.returnSquare(e, i).find("White") == False)):
                        list.addNode(e, i, self.evaluatePiece(e, i, moveBoard))
                        break
                    elif (moveBoard.returnSquare(e, i) != "Empty"):
                        break
                for e, i in zip(range(x + 1, 8), range(y - 1, -1, -1)):
                    if (moveBoard.returnSquare(e, i) == "Empty"):
                        list.addNode(e, i, self.evaluatePiece(e, i, moveBoard))
                    elif (e < 8 and i < 8 and (moveBoard.returnSquare(e, i).find("White") == False)):
                        list.addNode(e, i, self.evaluatePiece(e, i, moveBoard))
                        break
                    elif (moveBoard.returnSquare(e, i) != "Empty"):
                        break
                for e, i in zip(range(x - 1, -1, -1), range(y + 1, 8)):
                    if (moveBoard.returnSquare(e, i) == "Empty"):
                        list.addNode(e, i, self.evaluatePiece(e, i, moveBoard))
                    elif (e < 8 and i < 8 and (moveBoard.returnSquare(e, i).find("White") == False)):
                        list.addNode(e, i, self.evaluatePiece(e, i, moveBoard))
                        break
                    elif (moveBoard.returnSquare(e, i) != "Empty"):
                        break
                for e, i in zip(range(x - 1, -1, -1), range(y - 1, -1, -1)):
                    if (moveBoard.returnSquare(e, i) == "Empty"):
                        list.addNode(e, i, self.evaluatePiece(e, i, moveBoard))
                    elif (e < 8 and i < 8 and (moveBoard.returnSquare(e, i).find("White") == False)):
                        list.addNode(e, i, self.evaluatePiece(e, i, moveBoard))
                        break
                    elif (moveBoard.returnSquare(e, i) != "Empty"):
                        break
                return list

            case 16: # Black Right Knight Moves
                if (x < 6 and y < 7 and moveBoard.returnSquare(x + 2, y + 1) == "Empty"):
                    list.addNode(x + 2, y + 1, self.evaluatePiece(x + 2, y + 1, moveBoard))
                elif (x < 6 and y < 7 and (moveBoard.returnSquare(x + 2, y + 1).find("White") == False)):
                    list.addNode(x + 2, y + 1, self.evaluatePiece(x + 2, y + 1, moveBoard))
                if (x < 6 and y > 0 and moveBoard.returnSquare(x + 2, y - 1) == "Empty"):
                    list.addNode(x + 2, y - 1, self.evaluatePiece(x + 2, y - 1, moveBoard))
                elif (x < 6 and y > 0 and (moveBoard.returnSquare(x + 2, y - 1).find("White") == False)):
                    list.addNode(x + 2, y - 1, self.evaluatePiece(x + 2, y - 1, moveBoard))
                if (x < 7 and y < 6 and moveBoard.returnSquare(x + 1, y + 2) == "Empty"):
                    list.addNode(x + 1, y + 2, self.evaluatePiece(x + 1, y + 2, moveBoard))
                elif (x < 7 and y < 6 and (moveBoard.returnSquare(x + 1, y + 2).find("White") == False)):
                    list.addNode(x + 1, y + 2, self.evaluatePiece(x + 1, y + 2, moveBoard))
                if (x < 7 and y > 1 and moveBoard.returnSquare(x + 1, y - 2) == "Empty"):
                    list.addNode(x + 1, y - 2, self.evaluatePiece(x + 1, y - 2, moveBoard))
                elif (x < 7 and y > 1 and (moveBoard.returnSquare(x + 1, y - 2).find("White") == False)):
                    list.addNode(x + 1, y - 2, self.evaluatePiece(x + 1, y - 2, moveBoard))
                if (x > 1 and y < 7 and moveBoard.returnSquare(x - 2, y + 1) == "Empty"):
                    list.addNode(x - 2, y + 1, self.evaluatePiece(x - 2, y + 1, moveBoard))
                elif (x > 1 and y < 7 and (moveBoard.returnSquare(x - 2, y + 1).find("White") == False)):
                    list.addNode(x - 2, y + 1, self.evaluatePiece(x - 2, y + 1, moveBoard))
                if (x > 1 and y < 0 and moveBoard.returnSquare(x - 2, y - 1) == "Empty"):
                    list.addNode(x - 2, y - 1, self.evaluatePiece(x - 2, y - 1, moveBoard))
                elif (x > 1 and y > 0 and (moveBoard.returnSquare(x - 2, y - 1).find("White") == False)):
                    list.addNode(x - 2, y - 1, self.evaluatePiece(x - 2, y - 1, moveBoard))
                if (x > 0 and y < 6 and moveBoard.returnSquare(x - 1, y + 2) == "Empty"):
                    list.addNode(x - 1, y + 2, self.evaluatePiece(x - 1, y + 2, moveBoard))
                elif (x > 0 and y < 6 and (moveBoard.returnSquare(x - 1, y + 2).find("White") == False)):
                    list.addNode(x - 1, y + 2, self.evaluatePiece(x - 1, y + 2, moveBoard))
                if (x > 0 and y > 1 and moveBoard.returnSquare(x - 1, y - 2) == "Empty"):
                    list.addNode(x - 1, y - 2, self.evaluatePiece(x - 1, y - 2, moveBoard))
                elif (x > 0 and y > 1 and (moveBoard.returnSquare(x - 1, y - 2).find("White") == False)):
                    list.addNode(x - 1, y - 2, self.evaluatePiece(x - 1, y - 2, moveBoard))
                return list

            case 17: # Black Right Rook Moves
                for i in range(x + 1, 8):
                    if (moveBoard.returnSquare(i, y) == "Empty"):
                        list.addNode(i, y, self.evaluatePiece(i, y, moveBoard))
                    elif ((x < 8) and (moveBoard.returnSquare(i, y).find("White") == False)):
                        list.addNode(i, y, self.evaluatePiece(i, y, moveBoard))
                        break
                    elif (moveBoard.returnSquare(i, y) != "Empty"):
                        break
                for i in range(x - 1, -1, -1):
                    if (moveBoard.returnSquare(i, y) == "Empty"):
                        list.addNode(i, y, self.evaluatePiece(i, y, moveBoard))
                    elif ((x >= 0) and (moveBoard.returnSquare(i, y).find("White") == False)):
                        list.addNode(i, y, self.evaluatePiece(i, y, moveBoard))
                        break
                    elif (moveBoard.returnSquare(i, y) != "Empty"):
                        break
                for i in range(y + 1, 8):
                    if (moveBoard.returnSquare(x, i) == "Empty"):
                        list.addNode(x, i, self.evaluatePiece(x, i, moveBoard))
                    elif ((x >= 0) and (moveBoard.returnSquare(x, i).find("White") == False)):
                        list.addNode(x, i, self.evaluatePiece(x, i, moveBoard))
                        break
                    elif (moveBoard.returnSquare(x, i) != "Empty"):
                        break
                for i in range(y - 1, -1, -1):
                    if (moveBoard.returnSquare(x, i) == "Empty"):
                        list.addNode(x, i, self.evaluatePiece(x, i, moveBoard))
                    elif ((x >= 0) and (moveBoard.returnSquare(x, i).find("White") == False)):
                        list.addNode(x, i, self.evaluatePiece(x, i, moveBoard))
                        break
                    elif (moveBoard.returnSquare(x, i) != "Empty"):
                        break

                return list

            case 18: # Black Pawn Moves
                if (x != 0 and moveBoard.returnSquare(x - 1, y) == "Empty"):
                    list.addNode(x - 1, y, self.evaluatePiece(x-1,y, moveBoard))
                if (x == 6 and moveBoard.returnSquare(x - 1, y) == "Empty" and moveBoard.returnSquare(x - 2, y) == "Empty"):
                    list.addNode(x - 2, y, self.evaluatePiece(x-2,y, moveBoard))
                if (x != 0 and y != 7 and moveBoard.returnSquare(x - 1, y + 1) != "Empty"):
                    list.addNode(x - 1, y + 1, self.evaluatePiece(x-1,y+1, moveBoard))
                if (x != 0 and y != 0 and moveBoard.returnSquare(x - 1, y - 1) != "Empty"):
                    list.addNode(x - 1, y - 1, self.evaluatePiece(x-1,y-1, moveBoard))
                return list
            case 19: # Empty Square
                return list

    def checkCalculator(self, x, y, moveBoard):
        temp = LinkedList()
        moveList = []
        returnList = []
        for e in range(0, 8):
            for i in range(0, 8):
                temp = self.possibleSquares2DArray(e, i, moveBoard)
                returnList = temp.returnVector()
                moveList.append(returnList)
        for i in range(0, len(moveList)):
            a = moveList[i]
            b = moveList[i+1]
            i = i+2
            if (x == a and y == b):
                return True
        return False