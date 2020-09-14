import math
import copy
from tkinter import *
import tkinter.messagebox
import time

Board = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],\
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],\
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],\
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],\
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]      #0. @     1. @      2. @        3.@         4. @@         5. @
                                                 #   @@       @@        @          @@           @             @@
                                                 #             @        @@         @            @@            @@

                                                 #6. @     7.  @     8. @        9. @@      10. @        11. @
                                                 #   @        @@        @@          @           @@           @@
                                                 #   @@@       @@        @          @            @@          @
                                                 #                       @          @                        @
                                                 # PIECE KEY
Pieces = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

Finished = 0

Pieces[0] = [[[1, 0], [1, 1], [0, 1]], [[0, 1], [1, 1], [1, 0]], [[0, 1, 1], [1, 1, 0]], [[1, 1, 0], [0, 1, 1]]]
Pieces[1] = [[[1, 0], [1, 1]], [[0, 1], [1, 1]], [[1, 1], [0, 1]], [[1, 1], [0, 1]]]
Pieces[2] = [[[1, 0], [1, 0], [1, 1]], [[0, 1], [0, 1], [1, 1]], [[1, 1], [1, 0], [1, 0]], [[1, 1], [0, 1], [0, 1]],\
             [[1, 0, 0], [1, 1, 1, 1]], [[1, 1, 1], [1, 0, 0]], [[1, 1, 1], [0, 0, 1]], [[0, 0, 1], [1, 1, 1]]]
Pieces[3] = [[[1, 0], [1, 1], [1, 0]], [[0, 1], [1, 1], [0, 1]], [[0, 1, 0], [1, 1, 1]], [[1, 1, 1], [0, 1, 0]]]
Pieces[4] = [[[1, 1], [1, 0], [1, 1]], [[1, 1], [0, 1], [1, 1]], [[1, 0, 1], [1, 1, 1]], [[1, 1, 1], [1, 0, 1]]]
Pieces[5] = [[[1, 0], [1, 1], [1, 1]], [[0, 1], [1, 1], [1, 1]], [[1, 1], [1, 1], [1, 0]], [[1, 1], [1, 1], [0, 1]],\
             [[0, 1, 1], [1, 1, 1]], [[1, 1, 0], [1, 1, 1]], [[1, 1, 1], [0, 1, 1]], [[1, 1, 1], [1, 1, 0]]]
Pieces[6] = [[[1, 0, 0], [1, 0, 0], [1, 1, 1]], [[1, 1, 1], [1, 0, 0], [1, 0, 0]], [[1, 1, 1], [0, 0, 1], [0, 0, 1]],\
             [[0, 0, 1], [0, 0, 1], [1, 1, 1]]]
Pieces[7] = [[[0, 1, 0], [1, 1, 0], [0, 1, 1]], [[0, 0, 1], [1, 1, 1], [0, 1, 0]], [[1, 1, 0], [0, 1, 1], [0, 1, 0]],\
             [[0, 1, 0], [1, 1, 1], [1, 0, 0]], [[0, 1, 0], [1, 1, 1], [0, 0, 1]], [[0, 1, 0], [0, 1, 1], [1, 1, 0]],\
             [[1, 0, 0], [1, 1, 1], [0, 1, 0]], [[0, 1, 1], [1, 1, 0], [0, 1, 0]]]
Pieces[8] = [[[1, 0], [1, 1], [0, 1], [0, 1]], [[0, 1], [1, 1], [1, 0], [1, 0]], [[1, 0], [1, 0], [1, 1], [0, 1]],\
             [[0, 1], [0, 1], [1, 1], [1, 0]], [[1, 1, 0, 0], [0, 1, 1, 1]], [[0, 0, 1, 1], [1, 1, 1, 0]],\
             [[0, 1, 1, 1], [1, 1, 0, 0]], [[1, 1, 1, 0], [0, 0, 1, 1]]]
Pieces[9] = [[[1, 1], [1, 0], [1, 0], [1, 0]], [[1, 1], [0, 1], [0, 1], [0, 1]], [[1, 0], [1, 0], [1, 0], [1, 1]],\
             [[0, 1], [0, 1], [0, 1], [1, 1]], [[1, 0, 0, 0], [1, 1, 1, 1]], [[1, 1, 1, 1], [1, 0, 0, 0]],\
             [[1, 1, 1, 1], [0, 0, 0, 1]], [[0, 0, 0, 1], [1, 1, 1, 1]]]
Pieces[10] = [[[1, 0, 0], [1, 1, 0], [0, 1, 1]], [[0, 0, 1], [0, 1, 1], [1, 1, 0]], [[0, 1, 1], [1, 1, 0], [1, 0, 0]],\
              [[1, 1, 0], [0, 1, 1], [0, 0, 1]]]
Pieces[11] = [[[1, 0], [1, 1], [1, 0], [1, 0]], [[0, 1], [1, 1], [0, 1], [0, 1]], [[1, 0], [1, 0], [1, 1], [1, 0]],\
              [[0, 1], [0, 1], [1, 1], [0, 1]], [[0, 1, 0, 0], [1, 1, 1, 1]], [[1, 1, 1, 1], [0, 1, 0, 0]],\
              [[0, 0, 1, 0], [1, 1, 1, 1]], [[1, 1, 1, 1], [0, 0, 1, 0]]]

Pieces2 = copy.deepcopy(Pieces)
NumberOfPieces = 12

root = Tk()
frames_list = []
btn_list = []

def create_frames_and_buttons():  #creating the board
    ndex = 0
    for i in range(5):
        for x in range(11):
            frames_list.append(Frame(root, width=100, height=100))
            frames_list[ndex].propagate(False)
            frames_list[ndex].grid(row=i, column=x, sticky="nsew", padx=2, pady=2)
            btn_list.append(Button(frames_list[ndex], text="", bg='white', font="Helvetica 16 bold",
                   command=lambda ndex=ndex: buttonClick(ndex)))
            btn_list[ndex].pack(expand=True, fill=BOTH)
            ndex += 1
    root.resizable(width=False, height=False)


def buttonClick(button_number):  #setting comand on click
    global btn_list
    row = math.floor(button_number / 11)
    column = button_number % 11
    if btn_list[button_number]["bg"] == 'white':
        btn_list[button_number]["bg"] = 'blue'
        Board[row][column] = 1
    elif btn_list[button_number]["bg"] == 'blue':
        btn_list[button_number]["bg"] = 'white'
        Board[row][column] = 0


create_frames_and_buttons()

root.mainloop()

root = Tk()
frames_list = []
btn_list = []


def create_frames_and_buttons2():  #Setting the pieces
    ndex = 0
    for x in range(12):
        frames_list.append(Frame(root, width=100, height=100))
        frames_list[ndex].propagate(False)
        frames_list[ndex].grid(row=1, column=x, sticky="nsew", padx=2, pady=2)
        btn_list.append(Button(frames_list[ndex], text=x, bg='white', font="Helvetica 16 bold",
              command=lambda ndex=ndex: buttonClick2(ndex)))
        btn_list[ndex].pack(expand=True, fill=BOTH)
        ndex += 1
    root.resizable(width=False, height=False)


def buttonClick2(button_number): #Command when button is pressed
    global btn_list
    global NumberOfPieces
    if btn_list[button_number]["bg"] == 'white':
        btn_list[button_number]["bg"] = 'blue'
        NumberOfPieces -= 1
        Pieces.remove(Pieces2[button_number])


create_frames_and_buttons2()
root.mainloop()

PieceIndex = []
Boards = []

for i in range(NumberOfPieces):
    PieceIndex.append(0)
    Boards.append(0)

PieceIndex.append(Pieces)
Boards.append(Board)

time.sleep(5)


level = len(PieceIndex)-1

start = time.time()

def AddList(Board, Piece, Position):        #adds the piece to the boarf and returns a copy of the original board
    Board_1 = copy.deepcopy(Board)
    width = 12 - len(Piece[0])     #defining the furthest along the board we should consider
    Column = Position % width
    Row = math.floor(Position / width)
    for RowIndex in range(len(Piece)):
        for ColumnIndex in range(len(Piece[0])):
            Board_1[Row + RowIndex][Column + ColumnIndex] += Piece[RowIndex][ColumnIndex]
    return Board_1

def tryAllPieces(Boards, PieceIndex):
    global level
    global Finished
    for PieceNumber in range(len(PieceIndex[level])):         #go through each piece
        PieceOk = 0
        for direction in range(len(PieceIndex[level][PieceNumber])):
            for Position in range((12-len(PieceIndex[level][PieceNumber][direction][0]))*(6-len(PieceIndex[level][PieceNumber][direction]))):  #go through each position
                if Finished == 5:
                    return Boards
                Boards[level-1] = AddList(Boards[level], PieceIndex[level][PieceNumber][direction], Position)
                NotFit = 0
                for i in range(5):
                    if 2 in Boards[level-1][i]:  #piece cannot go here
                        NotFit = 1
                        break           #try another position
                    elif 0 in Boards[level-1][i]:
                        Finished = 0
                    elif Finished == i:
                        Finished = i+1
                if NotFit == 0:                   #piece fits in
                    PieceOk = 1
                    level -= 1
                    PieceIndex[level] = copy.deepcopy(PieceIndex[level+1])
                    PieceIndex[level].remove(PieceIndex[level][PieceNumber])
                    if Finished == 5:
                        for j in range(NumberOfPieces+1):
                            print("Step")
                            #Boards[NumberOfPieces-j] = AddList(Boards[NumberOfPieces-j], Boards[NumberOfPieces-j+1], 0)
                            for k in range(5):
                                print(Boards[NumberOfPieces-j][k])
                        return Boards
                    tryAllPieces(Boards, PieceIndex)
                if Position == ((12-len(PieceIndex[level][PieceNumber][direction][0]))*(6-len(PieceIndex[level][PieceNumber][direction])))-1 \
                        and PieceNumber == len(PieceIndex[level])-1 and direction == len(PieceIndex[level][PieceNumber])-1: #gone through every option
                    #print("tried all combinations")
                    level += 1



Board = tryAllPieces(Boards, PieceIndex)

end = time.time() - start

print(end)