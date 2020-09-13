import math
import copy

Board = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],\
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],\
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],\
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],\
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

Boards = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, Board] #board 12 in slot 11 is always blank

Pieces = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

Finished = 0

level = 11

Pieces[0] = [[1, 0], [1, 1], [0, 1]]
Pieces[1] = [[1, 0], [1, 1]]
Pieces[2] = [[1, 0], [1, 0], [1, 1]]
Pieces[3] = [[1, 0], [1, 1], [1, 0]]
Pieces[4] = [[1, 1], [1, 0], [1, 1]]
Pieces[5] = [[1, 0], [1, 1], [1, 1]]
Pieces[6] = [[1, 0, 0], [1, 0, 0], [1, 1, 1]]
Pieces[7] = [[0, 1, 0], [1, 1, 0], [0, 1, 1]]
Pieces[8] = [[1, 0], [1, 1], [0, 1], [0, 1]]
Pieces[9] = [[1, 1], [1, 0], [1, 0], [1, 0]]
Pieces[10] = [[1, 0, 0], [1, 1, 0], [0, 1, 1]]
Pieces[11] = [[1, 0], [1, 1], [1, 0], [1, 0]]

PieceIndex = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, Pieces]

def AddList(Board, Piece, Position):        #adds the piece to the boarf and returns a copy of the original board
    Board_1 = copy.deepcopy(Board)
    width = 12 - len(Piece[0])     #defining the furthest along the board we should consider
    Column = Position % width
    Row = math.floor(Position / width)
    #print("piece width2")
    #print(range(len(Piece)))
    #print("piece height2")
    #print(len(Piece))
    for RowIndex in range(len(Piece)):
        for ColumnIndex in range(len(Piece[0])):
            #print("Row")
            #print(Row)
            #print("column")
            #print(Column)
            #print(RowIndex)
            #print(ColumnIndex)
            Board_1[Row + RowIndex][Column + ColumnIndex] += Piece[RowIndex][ColumnIndex]
    return Board_1

def tryAllPieces(Boards, Pieces, PieceIndex, Finished, level):
    for PieceNumber in range(len(Pieces)):         #go through each piece
        PieceOk = 0
        for direction in range
        for Position in range((12-len(Pieces[PieceNumber][0]))*(6-len(Pieces[PieceNumber]))):  #go through each position
            print("piece")
            print(PieceNumber)
            #print("piece width")
            #print(len(Pieces[PieceNumber][0]))
            #print("piece height")
            #print(len(Pieces[PieceNumber]))
            #print("level")
            print(level)
            Boards[level] = AddList(Boards[level+1], Pieces[PieceNumber], Position)
            NotFit = 0
            for i in range(5):
                if 2 in Boards[level][i]:  #piece cannot go here
                    print("didnt go")
                    print(Boards[level+1])
                    print(Boards[level])
                    NotFit = 1
                    break           #try another position
            if NotFit == 0:                   #piece fits in
                print("worked")
                PieceOk = 1
                level -= 1
                PieceIndex[level] = copy.deepcopy(PieceIndex[level+1])
                PieceIndex[level].remove(PieceIndex[level][PieceNumber])
                print(Boards[level+2])
                print(Boards[level+1])
                if Finished == 1:
                    return Boards
                tryAllPieces(Boards, Pieces, PieceIndex, Finished, level)
                if level == 0:
                    Finished = 1
                if Finished == 1:
                    return Boards
                tryAllPieces(Boards, Pieces, PieceIndex, Finished, level)
            #if Position == ((12-len(Pieces[PieceNumber][0]))*(6-len(Pieces[PieceNumber])))-1 and PieceNumber == len(Pieces)-1: #gone through every option



Board = tryAllPieces(Boards, Pieces, PieceIndex, Finished, level)

print(Boards[0])
