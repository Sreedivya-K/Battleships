"""
Battleship Project
Name:
Roll No:
"""

import battleship_tests as test

project = "Battleship" # don't edit this

### SIMULATION FUNCTIONS ###

from tkinter import *
import random

EMPTY_UNCLICKED = 1
SHIP_UNCLICKED = 2
EMPTY_CLICKED = 3
SHIP_CLICKED = 4


'''
makeModel(data)
Parameters: dict mapping strs to values
Returns: None
'''
def makeModel(data):
    data["row"] = 10
    data["col"] = 10
    data["bsize"] = 500
    data["csize"] = 50
    data["numShips"] = 5
    ub=emptyGrid(data["row"],data["col"])
    data["user"] = ub
    cb = emptyGrid(data["row"], data["col"])
    cb=addShips(cb,data["numShips"])
    data["computer board"]= cb
    data["temp_ship"]= test.testShip()
    return data

'''
makeView(data, userCanvas, compCanvas)
Parameters: dict mapping strs to values ; Tkinter canvas ; Tkinter canvas
Returns: None
'''
def makeView(data, userCanvas, compCanvas):
    grid=data["user"]
    drawGrid(data, userCanvas, grid,showShips=True)
    grid=data["computer board"]
    drawGrid(data, compCanvas, grid,showShips=True)
    drawShip(data,userCanvas,data["temp_ship"])
    return


'''
keyPressed(data, events)
Parameters: dict mapping strs to values ; key event object
Returns: None
'''
def keyPressed(data, event):
    pass


'''
mousePressed(data, event, board)
Parameters: dict mapping strs to values ; mouse event object ; 2D list of ints
Returns: None
'''
def mousePressed(data, event, board):
    pass

#### WEEK 1 ####

'''
emptyGrid(rows, cols)
Parameters: int ; int
Returns: 2D list of ints
'''
def emptyGrid(rows, cols):
    grid=[]
    for i in range(rows):
        b=[]
        for j in range(cols):
            b.append(1)
        grid.append(b)
    return grid


'''
createShip()
Parameters: no parameters
Returns: 2D list of ints
'''
def createShip():
    row=random.randint(1,8)
    col=random.randint(1,8)
    sd=random.randint(0,1)
    if sd ==0: #Vertical
        a=row-1
        b=row
        c=row+1
        d=[[a,col],[b,col],[c,col]]

    elif sd ==1: #Hor
        a=col-1
        b=col
        c=col+1
        d=[[row,a],[row,b],[row,c]]
    
    return d


'''
checkShip(grid, ship)
Parameters: 2D list of ints ; 2D list of ints
Returns: bool
'''
def checkShip(grid, ship):
    p=0
    for i in range(3):
        a1=ship[i]
        if grid[a1[0]][a1[1]]==1:
            p=p+1
    if p==3:
        return True
    else:
        return False


'''
addShips(grid, numShips)
Parameters: 2D list of ints ; int
Returns: 2D list of ints
'''
def addShips(grid, numShips):
    c=0
    while c<numShips:
        ship=createShip()
        g=checkShip(grid,ship)
        if g==True:
            for i in range(3):
                a1=ship[i]
                grid[a1[0]][a1[1]]=2
            c=c+1
    return grid


'''
drawGrid(data, canvas, grid, showShips)
Parameters: dict mapping strs to values ; Tkinter canvas ; 2D list of ints ; bool
Returns: None
'''
def drawGrid(data, canvas, grid, showShips):
    row = data["row"]
    col = data["col"]
    csize = data["csize"]
    size=[0,50,100,150,200,250,300,350,400,450,500]

    for i in range(row):
        for j in range(col):
            if grid[i][j] == 1:
                canvas.create_rectangle(size[j], size[i], size[j + 1], size[i + 1], fill="blue", width=1)
            elif grid[i][j] == 2:
                canvas.create_rectangle(size[j], size[i], size[j + 1], size[i + 1], fill="yellow", width=1)
    
    return

### WEEK 2 ###

'''
isVertical(ship)
Parameters: 2D list of ints
Returns: bool
'''
def isVertical(ship):
    row=[ship[0][0],ship[1][0],ship[2][0]]
    col=[ship[0][1],ship[1][1],ship[2][1]]
    a=col[0]
    b=col[1]
    c=col[2]
    if a == b & b == c:
        d=True
    else:
        d=False
    row.sort()
    p=row[2]-row[1]
    q=row[1]-row[0]

    if p==1 & q==1:
        e=True
    else:
        e=False
    if d==True & e==True:
            return True

    else:
        return False


'''
isHorizontal(ship)
Parameters: 2D list of ints
Returns: bool
'''
def isHorizontal(ship):
    row=[ship[0][0],ship[1][0],ship[2][0]]
    col=[ship[0][1],ship[1][1],ship[2][1]]
    a=row[0]
    b=row[1]
    c=row[2]
    if a == b & b == c:
        d=True
    else:
        d=False
    col.sort()
    p=col[2]-col[1]
    q=col[1]-col[0]

    if p==1 & q==1:
        e=True
    else:
        e=False
    if d==True & e==True:
            return True

    else:
        return False


'''
getClickedCell(data, event)
Parameters: dict mapping strs to values ; mouse event object
Returns: list of ints
'''
def getClickedCell(data, event):
    col=int(event.x/data["csize"])
    row=int(event.y/data["csize"])
    list=[]
    list.append(row)
    list.append(col)
    return list


'''
drawShip(data, canvas, ship)
Parameters: dict mapping strs to values ; Tkinter canvas; 2D list of ints
Returns: None
'''
def drawShip(data, canvas, ship):
    col = data["col"]
    row = data["row"]
    csize = data["csize"]
    for j in ship:
        a = j[1] * csize
        b = j[0] * csize
        canvas.create_rectangle(a, b, a + csize, b + csize, fill="white")
    return


'''
shipIsValid(grid, ship)
Parameters: 2D list of ints ; 2D list of ints
Returns: bool
'''
def shipIsValid(grid, ship):
    return


'''
placeShip(data)
Parameters: dict mapping strs to values
Returns: None
'''
def placeShip(data):
    return


'''
clickUserBoard(data, row, col)
Parameters: dict mapping strs to values ; int ; int
Returns: None
'''
def clickUserBoard(data, row, col):
    return


### WEEK 3 ###

'''
updateBoard(data, board, row, col, player)
Parameters: dict mapping strs to values ; 2D list of ints ; int ; int ; str
Returns: None
'''
def updateBoard(data, board, row, col, player):
    return


'''
runGameTurn(data, row, col)
Parameters: dict mapping strs to values ; int ; int
Returns: None
'''
def runGameTurn(data, row, col):
    return


'''
getComputerGuess(board)
Parameters: 2D list of ints
Returns: list of ints
'''
def getComputerGuess(board):
    return


'''
isGameOver(board)
Parameters: 2D list of ints
Returns: bool
'''
def isGameOver(board):
    return


'''
drawGameOver(data, canvas)
Parameters: dict mapping strs to values ; Tkinter canvas
Returns: None
'''
def drawGameOver(data, canvas):
    return


### SIMULATION FRAMEWORK ###

from tkinter import *

def updateView(data, userCanvas, compCanvas):
    userCanvas.delete(ALL)
    compCanvas.delete(ALL)
    makeView(data, userCanvas, compCanvas)
    userCanvas.update()
    compCanvas.update()

def keyEventHandler(data, userCanvas, compCanvas, event):
    keyPressed(data, event)
    updateView(data, userCanvas, compCanvas)

def mouseEventHandler(data, userCanvas, compCanvas, event, board):
    mousePressed(data, event, board)
    updateView(data, userCanvas, compCanvas)

def runSimulation(w, h):
    data = { }
    makeModel(data)

    root = Tk()
    root.resizable(width=False, height=False) # prevents resizing window

    # We need two canvases - one for the user, one for the computer
    Label(root, text = "USER BOARD - click cells to place ships on your board.").pack()
    userCanvas = Canvas(root, width=w, height=h)
    userCanvas.configure(bd=0, highlightthickness=0)
    userCanvas.pack()

    compWindow = Toplevel(root)
    compWindow.resizable(width=False, height=False) # prevents resizing window
    Label(compWindow, text = "COMPUTER BOARD - click to make guesses. The computer will guess on your board.").pack()
    compCanvas = Canvas(compWindow, width=w, height=h)
    compCanvas.configure(bd=0, highlightthickness=0)
    compCanvas.pack()

    makeView(data, userCanvas, compCanvas)

    root.bind("<Key>", lambda event : keyEventHandler(data, userCanvas, compCanvas, event))
    compWindow.bind("<Key>", lambda event : keyEventHandler(data, userCanvas, compCanvas, event))
    userCanvas.bind("<Button-1>", lambda event : mouseEventHandler(data, userCanvas, compCanvas, event, "user"))
    compCanvas.bind("<Button-1>", lambda event : mouseEventHandler(data, userCanvas, compCanvas, event, "comp"))

    updateView(data, userCanvas, compCanvas)

    root.mainloop()


### RUN CODE ###

# This code runs the test cases to check your work
if __name__ == "__main__":

    ## Finally, run the simulation to test it manually ##
    runSimulation(500, 500)
    test.testGetClickedCell()
