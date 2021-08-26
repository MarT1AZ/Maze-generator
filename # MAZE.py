# MAZE


# NODE AND PATHFINDING
import sys
import math
import random
from typing import Sized, Union
import pygame
import numpy as NP
from pygame.constants import HAT_RIGHT, KEYDOWN, K_1, K_2, K_RETURN, K_a, K_c, K_d, K_e, K_f, K_k, K_l, K_m, K_r, K_s, K_w, SCALED
from collections import deque
pygame.init()
pygame.display.set_caption("Maze Visualizer")
sys.setrecursionlimit(10**6)

#///COLOR//////////////////////////////////////////////////////////////
#//
Color_white = (255,255,255)
Color_red = (255,0,0)
Color_green = (0,255,0)
Color_blue = (0,0,255)
Color_orange = (255,128,0)
Color_black = (0,0,0)
Color_purple = (127,0,255)
Color_grey = (100,100,100)
Color_yellow = (255,255,0)
Color_brown = (160,82,45)
Color_saddlebrown = (139,69,19)
Color_DarkBlue = (0,51,102)
Color_DarkGreen = (0,102,0)
Color_pink = (255,0,255)
Color_DarkGrey = (48,48,48)
#//
#///COLOR//////////////////////////////////////////////////////////////

font1 = pygame.font.Font('AllTheWayToTheSun-o2O0.ttf',15)
def AddText(name,size,color,x,y):
    font = pygame.font.Font('AllTheWayToTheSun-o2O0.ttf',size)
    text = font.render(name,True,color)
    screen.blit(text,(x,y))


def RedFade(Value):
    if Value > 180:
        Value = Value % 180
    if (Value >= 0 and Value <= 30) or (Value >= 150 and Value <= 180):
        return 255
    elif (Value >= 60 and Value <= 120):
        return 0
    elif (Value >= 30 and Value <= 60):
        return math.floor((-255) * Value/30) + 510
    elif (Value >= 120 and Value <= 150):
        return math.floor((255) * Value/30) - 1020

def GreenFade(Value):
    if Value > 180:
        Value = Value % 180
    if (Value >= 30 and Value <= 90):
        return 255
    elif (Value >= 120 and Value <= 180):
        return 0
    elif (Value >= 90 and Value <= 120):
        return math.floor((-255) * Value/30) + 1020
    elif (Value >= 0 and Value <= 30):
        return math.floor((255) * Value/30)



def BlueFade(Value):
    if Value > 180:
        Value = Value % 180
    if (Value >= 90 and Value <= 150):
        return 255
    elif (Value >= 0 and Value <= 60):
        return 0
    elif (Value >= 150 and Value <= 180):
        return math.floor((-255) * Value/30) + 1530
    elif (Value >= 60 and Value <= 90):
        return math.floor((255) * Value/30) - 510





def ReturnFadeColor(Value):
    if Value < 0:
        if abs(Value) > 180:
            Value = -(abs(Value) % 180)
        Value = 180 + Value
    if Value > 180:
        Value = Value % 180
    return (RedFade(Value),GreenFade(Value),BlueFade(Value))

################################################################## screen setup
#//
ScreenWidth = 1300

ScreenHeight = 1200
screen = pygame.display.set_mode((ScreenWidth,ScreenHeight))




#//
################################################################## screen setup

################################################################## INPUT FUNCTION
#//
def GetPressKey():
    return pygame.key.get_pressed()

def GetMousePosition():
    return pygame.mouse.get_pos()

def GetClickState():
    return pygame.mouse.get_pressed()

#//
################################################################## INPUT FUNCTION

################################################################## ultility function

def MazeGetAvailaiblePath_Backtracker(X_tile,Y_tile):
    k = 2
    Result = []
    if X_tile + k < Int_Tile_count:
        if Matrix_TileState[Y_tile][X_tile + k] == 2:
            Result.append((X_tile + k,Y_tile,"+x"))
    if X_tile - k >= 0:
        if Matrix_TileState[Y_tile][X_tile - k] == 2:
            Result.append((X_tile - k,Y_tile,"-x"))
    if Y_tile + k < Int_Tile_count:
        if Matrix_TileState[Y_tile + k][X_tile] == 2:
            Result.append((X_tile,Y_tile + k,"+y"))
    if Y_tile - k >= 0:
        if Matrix_TileState[Y_tile - k][X_tile] == 2:
            Result.append((X_tile,Y_tile - k,"-y"))
    return Result

def MazeGetAvailaiblePath_Kruskal_Vertical(X_tile,Y_tile):
    k = 1
    Result = []
    if Y_tile + k < Int_Tile_count:
        Result.append((X_tile,Y_tile + k))
    if Y_tile - k >= 0:
        Result.append((X_tile,Y_tile - k))
    return Result

def MazeGetAvailaiblePath_Kruskal_Horizontal(X_tile,Y_tile):
    k = 1
    Result = []
    if X_tile + k < Int_Tile_count:
        Result.append((X_tile + k,Y_tile))
    if X_tile - k >= 0:
        Result.append((X_tile - k,Y_tile))
    return Result

def MazeGetAvailaiblePath_Prim(X_tile,Y_tile):
    k = 2
    Result = []
    if X_tile + k < Int_Tile_count:
        if Matrix_TileState[Y_tile][X_tile + k] == 2:
            Result.append((X_tile + k,Y_tile,"+x"))
    if X_tile - k >= 0:
        if Matrix_TileState[Y_tile][X_tile - k] == 2:
            Result.append((X_tile - k,Y_tile,"-x"))
    if Y_tile + k < Int_Tile_count:
        if Matrix_TileState[Y_tile + k][X_tile] == 2:
            Result.append((X_tile,Y_tile + k,"+y"))
    if Y_tile - k >= 0:
        if Matrix_TileState[Y_tile - k][X_tile] == 2:
            Result.append((X_tile,Y_tile - k,"-y"))
    return Result

def MazeGetAvailaiblePath_BinaryTree(X_tile,Y_tile):
    k = 2
    Result = []
    if X_tile - k >= 0:
        Result.append((X_tile - k,Y_tile,"-x"))
    if Y_tile - k >= 0:
        Result.append((X_tile,Y_tile - k,"-y"))
    return Result

def MazeGetAvailaiblePath_Wilson(X_tile,Y_tile):
    k = 2
    Result = []
    if X_tile + k < Int_Tile_count:
        Result.append((X_tile + k,Y_tile,"+x"))
    if X_tile - k >= 0:
        Result.append((X_tile - k,Y_tile,"-x"))
    if Y_tile + k < Int_Tile_count:
        Result.append((X_tile,Y_tile + k,"+y"))
    if Y_tile - k >= 0:
        Result.append((X_tile,Y_tile - k,"-y"))
    return Result

def MazeGetAvailaiblePath_HuntKill(X_tile,Y_tile):
    k = 2
    Result = []
    if X_tile + k < Int_Tile_count:
        if Matrix_TileState[Y_tile][X_tile + k] == 2:
            Result.append((X_tile + k,Y_tile,"+x"))
    if X_tile - k >= 0:
        if Matrix_TileState[Y_tile][X_tile - k] == 2:
            Result.append((X_tile - k,Y_tile,"-x"))
    if Y_tile + k < Int_Tile_count:
        if Matrix_TileState[Y_tile + k][X_tile] == 2:
            Result.append((X_tile,Y_tile + k,"+y"))
    if Y_tile - k >= 0:
        if Matrix_TileState[Y_tile - k][X_tile] == 2:
            Result.append((X_tile,Y_tile - k,"-y"))
    return Result

def ToBeNode(X_tile,Y_tile):
    
    k = 1
    if ((X_tile + k < Int_Tile_count and Matrix_TileState[Y_tile][X_tile + k] == 1) or (X_tile - k >= 0 and Matrix_TileState[Y_tile][X_tile - k] == 1)) and ((Y_tile + k < Int_Tile_count and Matrix_TileState[Y_tile + k][X_tile] == 1) or (Y_tile - k >= 0 and Matrix_TileState[Y_tile - k][X_tile] == 1)):
        return True
    else:
        return False

def MazeGetAvailaiblePath_BFS(X_tile,Y_tile):
    k = 1
    Result = []
    if X_tile + k < Int_Tile_count:
        if Matrix_TileState[Y_tile][X_tile + k] == 1:
            Result.append(("+x"))
    if X_tile - k >= 0:
        if Matrix_TileState[Y_tile][X_tile - k] == 1:
            Result.append(("-x"))
    if Y_tile + k < Int_Tile_count:
        if Matrix_TileState[Y_tile + k][X_tile] == 1:
            Result.append(("+y"))
    if Y_tile - k >= 0:
        if Matrix_TileState[Y_tile - k][X_tile] == 1:
            Result.append(("-y"))
    return Result



def SetUnion(A,B):
    return (A | B)
        




def IsInRect(X1,Y1,W,H,OX,OY):
    return X1 <= OX and OX <= X1 + W and Y1 <= OY and OY <= Y1 + H

def LessEven(Num):
    if Num % 2 == 0:
        return Num
    else:
        return Num - 1

def LargerEven(Num):
    if Num % 2 == 1:
        return Num + 1
    else:
        return Num

def Int_Bool_Switch(Num):
    if Num == 1:
        return 0
    else:
        return 1






################################################################## ultility function

################################################################ DRAW FUNCTION
#//
def UpdateScreen():
    pygame.display.update() ### important

def UpdateScreen():
    pygame.display.update()

def ClearScreen(color):
    DrawRect(color,0,0,ScreenWidth,ScreenHeight) ### important

def DrawRect(COLOR,X,Y,W,H):
    pygame.draw.rect(screen,COLOR,[X,Y,W,H])

def DrawLine(COLOR,X1,Y1,X2,Y2,Thickness):
    pygame.draw.line(screen,COLOR,(X1,Y1),(X2,Y2),Thickness)

def DrawUIbox(X,Y,W,H,Thickness,ShadowOffset):
    DrawRect(Color_black,X + ShadowOffset,Y + ShadowOffset,W,H)
    DrawRect(Color_purple,X,Y,W,H)
    DrawRect(Color_DarkGrey,X + Thickness,Y + Thickness,W - 2* Thickness,H - 2 * Thickness)

def DrawUIboxGreen(X,Y,W,H,Thickness):
    DrawRect(Color_green,X - 3,Y - 3,W + 6,H + 6)
    DrawRect(Color_DarkGrey,X + Thickness,Y + Thickness,W - 2* Thickness,H - 2 * Thickness)
#//
################################################################ DRAW FUNCTION

################################################################ Tile Variable
#//

Bool_GridUpdateSize = False
Bool_SmallerWall = False
Int_Tile_count = 51
Int_TileWidth = int(1000/Int_Tile_count) # float
Int_TileHeight = int(1000/Int_Tile_count) # float
Queue_BackTrackTile = deque()
X_HL = -1
Y_HL = -1
X_now = -1
Y_now = -1
X_consider = -1
Y_consider = -1
X_RemoveNext = -1
Y_RemoveNext = -1
# TEST


# TEST
################### ARRAY and set
#//
Matrix_NodeVisit = NP.empty([Int_Tile_count,Int_Tile_count])
Matrix_TileState = NP.empty([Int_Tile_count,Int_Tile_count])
Matrix_TileSetIndex = NP.empty([Int_Tile_count,Int_Tile_count])
Matrix_SelectAsNode = NP.empty([Int_Tile_count,Int_Tile_count]) # FINDPATH ARRAY
Matrix_SelectAsPath = NP.empty([Int_Tile_count,Int_Tile_count]) # FINDPATH ARRAY
Matrix_NodeWeight = NP.empty([Int_Tile_count,Int_Tile_count]) # FINDPATH ARRAY
Matrix_NodeConsider = NP.empty([Int_Tile_count,Int_Tile_count]) # FINDPATH ARRAY
Matrix_Occupied = NP.empty([Int_Tile_count,Int_Tile_count])
List_TileDirection = [[(-1,-1,"Notset") for x in range(Int_Tile_count)] for y in range(Int_Tile_count)]
List_PathSet = [[{} for x in range(Int_Tile_count)] for y in range(Int_Tile_count)]

DivisionWallToAdd = "Vertical"
Set_MazePath = set()
Set_randomPath = set()
Set_PathToRemove = set()
Set_Node = set()
Set_NodeToRemove = set()

for Y in range(0,Int_Tile_count):
    if Y % 2 != 0:
        continue    
    for X in range(0,Int_Tile_count):
        if X % 2 == 0:
            List_PathSet[Y][X] = {}

for Y in range(0,Int_Tile_count):
    for X in range(0,Int_Tile_count):
        Matrix_NodeVisit[Y][X] = 0
        Matrix_NodeConsider[Y][X] = 0
        Matrix_SelectAsNode[Y][X] = 0
        Matrix_SelectAsPath[Y][X] = 0
        Matrix_NodeWeight[Y][X] = -1
        Matrix_TileState[Y][X] = 2
        Matrix_TileSetIndex[Y][X] = 0
        Matrix_Occupied[Y][X] = 0
#//
################### ARRAY and set

#//
################################################################ Tile Variable

################################################################ Maze Variable
#//
Bool_SetNode = False
Bool_FindPath = False
Bool_Warning = False
Bool_InstantMaze = False
Bool_GenerateMaze = False
Maze_Algorithm = "BackTracking"
Int_AnimationDelay = 1
Bool_PuaseAnimation = False
#//
################################################################ Maze Variable

# program variable
Bool_EnableGreenHighlight = True
Bool_UpgradeGrid = False
Reset_Wall = False
Bool_ShowGrid = False
Int_Time = 0
ClickCoolDown = 10
ClickAllow = 3
# program variable





















































Bool_running = True
while Bool_running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Bool_running = False
    ClearScreen(Color_DarkGrey)

    ############################ get input
    keys = GetPressKey()
    mx ,my = GetMousePosition()
    Coordinate_mouse = NP.array([mx,my])
    click = GetClickState()
    ############################ get input

    ########################################################### setup UI
    if Bool_GenerateMaze:
        DrawUIboxGreen(50,1040,110,40,3)
    else:
        DrawUIbox(50,1040,110,40,3,3)
    AddText("Generate !",20,Color_white,60,1050)
    if IsInRect(50,1040,110,40,mx,my) and ClickCoolDown >= ClickAllow and click[0] == 1:
        ClickCoolDown = 0
        Bool_SetNode = False
        Bool_FindPath = False
        Reset_Wall = True
        Set_MazePath = set()
        Set_randomPath = set()
        Set_PathToRemove = set()
        List_TileDirection = [[(-1,-1,"Notset") for x in range(Int_Tile_count)] for y in range(Int_Tile_count)]
        if Maze_Algorithm == "BackTracking":
            (X_now,Y_now) = (LessEven(random.randint(0,Int_Tile_count - 1)),LessEven(random.randint(0,Int_Tile_count - 1)))
            Queue_BackTrackTile.append((X_now,Y_now))
        else:
            (X_now,Y_now) = (-1,-1)
        Bool_GenerateMaze = True

    DrawUIbox(170,1040,60,40,3,3)
    AddText("Stop",20,Color_white,180,1050)
    if IsInRect(170,1040,60,40,mx,my) and ClickCoolDown >= ClickAllow and click[0] == 1:
        ClickCoolDown = 0
        Bool_GenerateMaze = False
        Reset_Wall = True
        (X_now,Y_now) = (-1,-1)
        (X_HL,Y_HL) = (-1,-1)

    DrawUIbox(50,1090,100,40,3,3)
    AddText("Delay : " + str(Int_AnimationDelay),20,Color_white,60,1100)

    DrawUIbox(160,1090,40,40,3,3)
    AddText("+",20,Color_white,180,1100)
    if IsInRect(160,1090,40,40,mx,my) and ClickCoolDown >= ClickAllow and click[0] == 1:
        ClickCoolDown = 0
        Int_AnimationDelay += 1

    DrawUIbox(210,1090,40,40,3,3)
    AddText("-",20,Color_white,230,1100)
    if IsInRect(210,1090,40,40,mx,my) and ClickCoolDown >= ClickAllow and click[0] == 1:
        ClickCoolDown = 0
        Int_AnimationDelay -= 1
        if Int_AnimationDelay < 1:
            Int_AnimationDelay = 1

    if Bool_PuaseAnimation:
        DrawUIboxGreen(50,1140,80,40,3)
    else:
        DrawUIbox(50,1140,80,40,3,3)
    AddText("Puase",20,Color_white,60,1150)
    if IsInRect(50,1140,80,40,mx,my) and ClickCoolDown >= ClickAllow and click[0] == 1:
        ClickCoolDown = 0
        Bool_PuaseAnimation = not Bool_PuaseAnimation

    if Bool_InstantMaze:
        DrawUIboxGreen(140,1140,125,40,3)
    else:
        DrawUIbox(140,1140,125,40,3,3)
    AddText("Instant maze",20,Color_white,150,1150)
    if IsInRect(140,1140,125,40,mx,my) and ClickCoolDown >= ClickAllow and click[0] == 1:
        ClickCoolDown = 0
        Reset_Wall = True
        Bool_InstantMaze = not Bool_InstantMaze


    DrawLine(Color_white,280,900,280,ScreenHeight,5)

    AddText("Maze Size",30,Color_white,300,1040)
    #Bool_UpgradeGrid = True
    DrawUIbox(300,1090,150,40,3,3)
    AddText("Size :" + str(Int_Tile_count),20,Color_white,310,1100)
    DrawUIbox(460,1090,40,40,3,3)
    AddText("+",20,Color_white,470,1100)
    DrawUIbox(510,1090,40,40,3,3)
    AddText("-",20,Color_white,520,1100)

    DrawUIbox(300,1140,70,40,3,3)
    AddText("Small",20,Color_white,310,1150)
    DrawUIbox(385,1140,80,40,3,3)
    AddText("Medium",20,Color_white,400,1150)
    DrawUIbox(480,1140,70,40,3,3)
    AddText("Large",20,Color_white,490,1150)


    if ClickCoolDown >= ClickAllow and click[0] == 1:
        if IsInRect(460,1090,40,40,mx,my):
            ClickCoolDown = 0
            Bool_GridUpdateSize = True
            Int_Tile_count += 2
            if Int_Tile_count > 101:
                Int_Tile_count = 101
        elif IsInRect(510,1090,40,40,mx,my):
            ClickCoolDown = 0
            Bool_GridUpdateSize = True
            Int_Tile_count -= 2
            if Int_Tile_count < 11:
                Int_Tile_count = 11
        elif IsInRect(300,1140,70,40,mx,my):
            ClickCoolDown = 0
            Bool_GridUpdateSize = True
            Int_Tile_count = 11
        elif IsInRect(385,1140,70,40,mx,my):
            ClickCoolDown = 0
            Bool_GridUpdateSize = True
            Int_Tile_count = 51
        elif IsInRect(480,1140,70,40,mx,my):
            ClickCoolDown = 0
            Bool_GridUpdateSize = True
            Int_Tile_count = 101
    
    

    

    DrawLine(Color_white,570,900,570,ScreenHeight,5)
    
    AddText("Maze Algorithm",30,Color_white,590,1040)


    if Maze_Algorithm == "BackTracking":
        DrawUIboxGreen(590,1090,140,40,3)
    else:
        DrawUIbox(590,1090,140,40,3,3)
    AddText("BackTracker",20,Color_white,600,1100)
    if IsInRect(590,1090,140,40,mx,my) and ClickCoolDown >= ClickAllow and click[0] == 1:
        Bool_GenerateMaze = False
        ClickCoolDown = 0
        Maze_Algorithm = "BackTracking"

    if Maze_Algorithm == "Randomized Kruskal":
        DrawUIboxGreen(590,1140,140,40,3)
    else:
        DrawUIbox(590,1140,140,40,3,3)
    AddText("Kruskal",20,Color_white,600,1150)
    if IsInRect(590,1140,140,40,mx,my) and ClickCoolDown >= ClickAllow and click[0] == 1:
        Bool_GenerateMaze = False
        ClickCoolDown = 0
        Maze_Algorithm = "Randomized Kruskal"

    if Maze_Algorithm == "Prim":
        DrawUIboxGreen(750,1090,140,40,3)
    else:
        DrawUIbox(750,1090,140,40,3,3)
    AddText("Prim",20,Color_white,760,1100)
    if IsInRect(750,1090,140,40,mx,my) and ClickCoolDown >= ClickAllow and click[0] == 1:
        Bool_GenerateMaze = False
        ClickCoolDown = 0
        Maze_Algorithm = "Prim"

    if Maze_Algorithm == "BinaryTree":
        DrawUIboxGreen(750,1140,140,40,3)
    else:
        DrawUIbox(750,1140,140,40,3,3)
    AddText("Binary Tree",20,Color_white,760,1150)
    if IsInRect(750,1140,140,40,mx,my) and ClickCoolDown >= ClickAllow and click[0] == 1:
        Bool_GenerateMaze = False
        ClickCoolDown = 0
        Maze_Algorithm = "BinaryTree"

    if Maze_Algorithm == "Wilson":
        DrawUIboxGreen(910,1090,140,40,3)
    else:
        DrawUIbox(910,1090,140,40,3,3)
    AddText("Wilson",20,Color_white,920,1100)
    if IsInRect(910,1090,140,40,mx,my) and ClickCoolDown >= ClickAllow and click[0] == 1:
        Bool_GenerateMaze = False
        ClickCoolDown = 0
        Maze_Algorithm = "Wilson"

    if Maze_Algorithm == "HuntAndKill":
        DrawUIboxGreen(910,1140,140,40,3)
    else:
        DrawUIbox(910,1140,140,40,3,3)
    AddText("Hunt And Kill",20,Color_white,920,1150)
    if IsInRect(910,1140,140,40,mx,my) and ClickCoolDown >= ClickAllow and click[0] == 1:
        Bool_GenerateMaze = False
        ClickCoolDown = 0
        Maze_Algorithm = "HuntAndKill"

    if Maze_Algorithm == "Division":
        DrawUIboxGreen(1070,1090,140,40,3)
    else:
        DrawUIbox(1070,1090,140,40,3,3)
    AddText("Division",20,Color_white,1080,1100)
    if IsInRect(1070,1090,140,40,mx,my) and ClickCoolDown >= ClickAllow and click[0] == 1:
        Bool_GenerateMaze = False
        ClickCoolDown = 0
        Maze_Algorithm = "Division"








    #########################




    AddText("Animation Setting",30,Color_white,1050,50)
    
    if Bool_SmallerWall:
        DrawUIboxGreen(1050,120,140,40,3)
    else:
        DrawUIbox(1050,120,140,40,3,3)
    AddText("Smaller wall",20,Color_white,1060,130)
    if IsInRect(1050,120,140,40,mx,my) and ClickCoolDown >= ClickAllow and click[0] == 1:
        ClickCoolDown = 0
        Bool_SmallerWall = not Bool_SmallerWall

  
    if Bool_ShowGrid:
        DrawUIboxGreen(1050,200,110,40,3)
    else:
        DrawUIbox(1050,200,110,40,3,3)
    AddText("Show Grid",20,Color_white,1060,210)
    if IsInRect(1050,200,110,40,mx,my) and ClickCoolDown >= ClickAllow and click[0] == 1:
        ClickCoolDown = 0
        Bool_ShowGrid = not Bool_ShowGrid
    if Bool_SmallerWall:
        AddText("Disable in smaller wall mode",15,Color_yellow,1050,180)
        Bool_ShowGrid = False

    if Bool_EnableGreenHighlight:
        DrawUIboxGreen(1050,260,150,40,3)
    else:
        DrawUIbox(1050,260,150,40,3,3)
    AddText("Green Highlight",20,Color_green,1060,270)
    if IsInRect(1050,260,150,40,mx,my) and ClickCoolDown >= ClickAllow and click[0] == 1:
        ClickCoolDown = 0
        Bool_EnableGreenHighlight = not Bool_EnableGreenHighlight
    
    DrawLine(Color_white,1000,350,1400,350,5) ######################


    AddText("Solve Maze",30,Color_white,1050,400)

    if Bool_Warning:
        AddText("Maze not generate or not fully finish",15,Color_red,1050,500)
    if Bool_FindPath:
        DrawUIboxGreen(1050,450,120,40,3)
    else:
        DrawUIbox(1050,450,120,40,3,3)
    AddText("Solve Maze",20,Color_white,1060,460)
    if IsInRect(1050,450,120,40,mx,my) and ClickCoolDown >= ClickAllow and click[0] == 1:
        Bool_EnableGreenHighlight = True
        Bool_SetNode = False
        ClickCoolDown = 0
        Bool_FindPath = True
        Bool_Warning = False
        Set_NodeToRemove = set()
        Set_Node = set()
        Matrix_SelectAsNode[0][0] = 1
        Matrix_SelectAsNode[Int_Tile_count - 1][Int_Tile_count - 1] = 1
        Matrix_NodeWeight[0][0] = 0
        Matrix_NodeConsider[0][0] = 1
        Matrix_SelectAsPath[Int_Tile_count - 1][Int_Tile_count - 1] = 1
        Set_Node.add((0,0))
        Set_Node.add((Int_Tile_count - 1,Int_Tile_count - 1))
        for Y in range(0,Int_Tile_count):
            if Y % 2 != 0:
                continue
            for X in range(0,Int_Tile_count):
                if X % 2 != 0:
                    continue
                else:
                    if Matrix_TileState[Y][X] == 2 or Bool_GenerateMaze:
                        Bool_FindPath = False
                        Bool_Warning = True
                        break
            if not Bool_FindPath:
                break
    
    DrawRect(Color_green,1050,550,20,20)
    AddText("Solution path",20,Color_white,1100,550)

    DrawRect(Color_blue,1050,600,20,20)
    AddText("visit path",20,Color_white,1100,600)

    DrawRect(Color_orange,1050,650,20,20)
    AddText("unvisit path",20,Color_white,1100,650)

    DrawRect(Color_white,1050,700,20,20)
    AddText("walk path",20,Color_white,1100,700)

    DrawRect(Color_black,1050,750,20,20)
    AddText("wall path",20,Color_white,1100,750)

    DrawRect(Color_red,1050,800,20,20)
    AddText("high light",20,Color_white,1100,800)
                
















    if Bool_SmallerWall:
        Int_TileWidth = int(1000/(LargerEven(Int_Tile_count)/2))
        Int_TileHeight = int(1000/(LargerEven(Int_Tile_count)/2))
    else:
        Int_TileWidth = int(1000/Int_Tile_count)
        Int_TileHeight = int(1000/Int_Tile_count)

    if Bool_GridUpdateSize:
        Bool_FindPath = False
        Bool_SetNode = False
        Bool_PuaseAnimation = False
        Queue_BackTrackTile = deque()
        Bool_GenerateMaze = False
        Bool_GridUpdateSize = False
        Matrix_NodeVisit = NP.empty([Int_Tile_count,Int_Tile_count])
        Matrix_TileState = NP.empty([Int_Tile_count,Int_Tile_count])
        Matrix_TileSetIndex = NP.empty([Int_Tile_count,Int_Tile_count])
        Matrix_SelectAsNode = NP.empty([Int_Tile_count,Int_Tile_count]) # FINDPATH ARRAY
        Matrix_SelectAsPath = NP.empty([Int_Tile_count,Int_Tile_count]) # FINDPATH ARRAY
        Matrix_NodeWeight = NP.empty([Int_Tile_count,Int_Tile_count]) # FINDPATH ARRAY
        Matrix_NodeConsider = NP.empty([Int_Tile_count,Int_Tile_count]) # FINDPATH ARRAY
        Matrix_Occupied = NP.empty([Int_Tile_count,Int_Tile_count])
        List_PathSet = [[{} for x in range(Int_Tile_count)] for y in range(Int_Tile_count)]
        for Y in range(0,Int_Tile_count):
            for X in range(0,Int_Tile_count):
                Matrix_NodeVisit[Y][X] = 0
                Matrix_NodeConsider[Y][X] = 0
                Matrix_SelectAsNode[Y][X] = 0
                Matrix_SelectAsPath[Y][X] = 0
                Matrix_NodeWeight[Y][X] = -1
                Matrix_TileState[Y][X] = 2
                Matrix_TileSetIndex[Y][X] = 0
                Matrix_Occupied[Y][X] = 0

        for Y in range(0,Int_Tile_count):
            if Y % 2 != 0:
                continue    
            for X in range(0,Int_Tile_count):
                if X % 2 == 0:
                    List_PathSet[Y][X] = {}

    AddText(str(Bool_GenerateMaze),30,Color_white,1900,1100)## remove later
    DrawRect(Color_purple,0,0,1020,1020) # maze draw area
    if Bool_SmallerWall:
        DrawRect(Color_white,10,10,Int_Tile_count * Int_TileWidth/2 + Int_TileWidth/2,Int_Tile_count * Int_TileWidth/2 + Int_TileWidth/2)
    ########################################################### setup UI

    ########################################################### Solve MAZE
    if Bool_FindPath and Int_Time % Int_AnimationDelay == 0 and not Bool_PuaseAnimation:
        if not Bool_SetNode:
            Bool_SetNode = True
            for Y in range(0,Int_Tile_count): # SET NODE LOOP
                if Y % 2 != 0:
                    continue
                for X in range(0,Int_Tile_count): # SET NODE LOOP
                    if X % 2 != 0:
                        continue
                    else:
                        NBget = MazeGetAvailaiblePath_BFS(X,Y) # SET NODE LOOP
                        if ToBeNode(X,Y): # 0 1 2 3 4
                            Matrix_SelectAsNode[Y][X] = 1 # SET NODE LOOP
                            Set_Node.add((X,Y))
                            #print(len(Set_Node))

        if Matrix_NodeWeight[Int_Tile_count - 1][Int_Tile_count - 1] == -1:
            for Node in Set_Node:#pass
                (X,Y) = Node
                if Matrix_NodeConsider[Y][X] == 1 and Matrix_NodeVisit[Y][X] == 0:#pass
                    Matrix_NodeVisit[Y][X] = 1
                    for direction in MazeGetAvailaiblePath_BFS(X,Y):#pass
                        if direction == "+x":
                            for X2 in range(X + 1,Int_Tile_count):
                                if Matrix_SelectAsNode[Y][X2] == 1 and Matrix_NodeVisit[Y][X2] == 0:
                                    Matrix_NodeWeight[Y][X2] = Matrix_NodeWeight[Y][X] + 1
                                    Matrix_NodeConsider[Y][X2] = 1
                                    break
                                if Matrix_TileState[Y][X2] == 2:#pass
                                    break
                        elif direction == "-x":
                            for X2 in range(X - 1,-1,-1):
                                if Matrix_SelectAsNode[Y][X2] == 1 and Matrix_NodeVisit[Y][X2] == 0:
                                    Matrix_NodeWeight[Y][X2] = Matrix_NodeWeight[Y][X] + 1
                                    Matrix_NodeConsider[Y][X2] = 1
                                    break
                                if Matrix_TileState[Y][X2] == 2:#pass
                                    break
                        elif direction == "+y":
                            for Y2 in range(Y + 1,Int_Tile_count):
                                if Matrix_SelectAsNode[Y2][X] == 1 and Matrix_NodeVisit[Y2][X] == 0:
                                    Matrix_NodeWeight[Y2][X] = Matrix_NodeWeight[Y][X] + 1
                                    Matrix_NodeConsider[Y2][X] = 1
                                    break
                                if Matrix_TileState[Y2][X] == 2:#pass
                                    break

                        elif direction == "-y":
                            for Y2 in range(Y - 1,-1,-1):
                                if Matrix_SelectAsNode[Y2][X] == 1 and Matrix_NodeVisit[Y2][X] == 0:
                                    Matrix_NodeWeight[Y2][X] = Matrix_NodeWeight[Y][X] + 1
                                    Matrix_NodeConsider[Y2][X] = 1
                                    break
                                if Matrix_TileState[Y2][X] == 2:#pass
                                    break
        else:
            Matrix_SelectAsPath[Int_Tile_count - 1][Int_Tile_count - 1] = 1
            
            for Node in Set_Node:
                (X,Y) = Node
                if Matrix_SelectAsPath[Y][X] == 1:
                    for direction in MazeGetAvailaiblePath_BFS(X,Y):
                        if direction == "+x":
                            for X2 in range(X + 1,Int_Tile_count):
                                if Matrix_TileState[Y][X2] == 2:
                                    break
                                if Matrix_SelectAsNode[Y][X2] == 1 and Matrix_NodeWeight[Y][X2] == Matrix_NodeWeight[Y][X] - 1:
                                    for X3 in range(X + 1,Int_Tile_count):
                                        Matrix_SelectAsPath[Y][X3] = 1
                                        if Matrix_SelectAsNode[Y][X3] == 1:
                                            break
                                    break

                        elif direction == "-x":
                            for X2 in range(X - 1,-1,-1):
                                if Matrix_TileState[Y][X2] == 2:
                                    break
                                if Matrix_SelectAsNode[Y][X2] == 1 and Matrix_NodeWeight[Y][X2] == Matrix_NodeWeight[Y][X] - 1:
                                    for X3 in range(X - 1,-1,-1):
                                        Matrix_SelectAsPath[Y][X3] = 1
                                        if Matrix_SelectAsNode[Y][X3] == 1:
                                            break
                                    break

                        elif direction == "+y":
                            for Y2 in range(Y + 1,Int_Tile_count):
                                if Matrix_TileState[Y2][X] == 2:
                                    break
                                if Matrix_SelectAsNode[Y2][X] == 1 and Matrix_NodeWeight[Y2][X] == Matrix_NodeWeight[Y][X] - 1:
                                    for Y3 in range(Y + 1,Int_Tile_count):
                                        Matrix_SelectAsPath[Y3][X] = 1
                                        if Matrix_SelectAsNode[Y3][X] == 1:
                                            break
                                    break
                        elif direction == "-y":
                            for Y2 in range(Y - 1,-1,-1):
                                if Matrix_TileState[Y2][X] == 2:
                                    break
                                if Matrix_SelectAsNode[Y2][X] == 1 and Matrix_NodeWeight[Y2][X] == Matrix_NodeWeight[Y][X] - 1:
                                    for Y3 in range(Y - 1,-1,-1):
                                        Matrix_SelectAsPath[Y3][X] = 1
                                        if Matrix_SelectAsNode[Y3][X] == 1:
                                            break
                                    break
            if Matrix_SelectAsPath[0][0] == 1:
                Bool_FindPath = False














    ########################################################### Solve MAZE

    if True:
        for Y in range(0,Int_Tile_count):
            for X in range(0,Int_Tile_count):

                if Reset_Wall:
                    Matrix_NodeVisit[Y][X] = 0
                    Matrix_NodeConsider[Y][X] = 0
                    Matrix_SelectAsNode[Y][X] = 0
                    Matrix_SelectAsPath[Y][X] = 0
                    Matrix_NodeWeight[Y][X] = -1
                    Matrix_TileSetIndex[Y][X] = 0
                    Matrix_Occupied[Y][X] = 0
                    if Maze_Algorithm == "Division":
                        Matrix_TileState[Y][X] = 1
                    else:
                        Matrix_TileState[Y][X] = 2
                    if Maze_Algorithm == "Randomized Kruskal":
                        if X % 2 == 0 and Y % 2 == 0: ############################### only Path Tile
                            List_PathSet[Y][X] = {(X,Y)}
                        elif (X % 2 == 0 and Y % 2 == 1) or (X % 2 == 1 and Y % 2 == 0): ################# get WALl
                            Set_MazePath.add((X,Y))

                if not Bool_SmallerWall:
                    if Matrix_TileState[Y][X] == 1: ########### WALK TILE
                        if (X,Y) == (X_HL,Y_HL):
                            DrawRect(Color_red,10 + X * Int_TileWidth,Y * Int_TileHeight + 10,Int_TileWidth,Int_TileHeight)
                        elif Matrix_SelectAsPath[Y][X] == 1 and Bool_EnableGreenHighlight:
                            DrawRect(Color_green,10 + X * Int_TileWidth,Y * Int_TileHeight + 10,Int_TileWidth,Int_TileHeight)
                        elif Matrix_NodeVisit[Y][X] == 1 and Bool_FindPath:
                            DrawRect(Color_blue,10 + X * Int_TileWidth,Y * Int_TileHeight + 10,Int_TileWidth,Int_TileHeight)
                        elif Matrix_SelectAsNode[Y][X] == 1 and Bool_FindPath:
                            DrawRect(Color_orange,10 + X * Int_TileWidth,Y * Int_TileHeight + 10,Int_TileWidth,Int_TileHeight)
                        elif Matrix_Occupied[Y][X] == 1 and Bool_GenerateMaze and Maze_Algorithm == "Division" and Bool_EnableGreenHighlight:
                            if Bool_ShowGrid:
                                DrawRect(Color_green,11 + X * Int_TileWidth,Y * Int_TileHeight + 11,Int_TileWidth - 2,Int_TileHeight - 2)
                            else:
                                DrawRect(Color_green,10 + X * Int_TileWidth,Y * Int_TileHeight + 10,Int_TileWidth,Int_TileHeight)
                        elif Bool_ShowGrid:
                            DrawRect(Color_white,10 + X * Int_TileWidth + 1,1 + Y * Int_TileHeight + 10,Int_TileWidth - 2,Int_TileHeight - 2)
                        else:
                            DrawRect(Color_white,10 + X * Int_TileWidth,Y * Int_TileHeight + 10,Int_TileWidth,Int_TileHeight)
                    elif Matrix_TileState[Y][X] == 2: ########### WALL TILE
                        if (X,Y) in Set_randomPath:
                            DrawRect(Color_red,10 + X * Int_TileWidth,Y * Int_TileHeight + 10,Int_TileWidth,Int_TileHeight)
                        elif Bool_ShowGrid:
                            DrawRect(Color_black,10 + X * Int_TileWidth + 1,1 + Y * Int_TileHeight + 10,Int_TileWidth - 2,Int_TileHeight - 2)
                        else:
                            DrawRect(Color_black,10 + X * Int_TileWidth,Y * Int_TileHeight + 10,Int_TileWidth,Int_TileHeight)

                elif not (X % 2 == 1 and Y % 2 == 1):

                    if Matrix_TileState[Y][X] == 1 and (X % 2 == 0 and Y % 2 == 0): ########### WALK TILE
                        if (X,Y) == (X_HL,Y_HL):
                            DrawRect(Color_red,10 + X/2 * Int_TileWidth,Y/2 * Int_TileHeight + 10,Int_TileWidth,Int_TileHeight)
                        elif Matrix_SelectAsPath[Y][X] == 1 and Bool_EnableGreenHighlight:
                            DrawRect(Color_green,10 + X/2 * Int_TileWidth,Y/2 * Int_TileHeight + 10,Int_TileWidth,Int_TileHeight)
                        elif Matrix_NodeVisit[Y][X] == 1 and Bool_FindPath:
                            DrawRect(Color_blue,10 + X/2 * Int_TileWidth,Y/2 * Int_TileHeight + 10,Int_TileWidth,Int_TileHeight)
                        elif Matrix_SelectAsNode[Y][X] == 1 and Bool_FindPath:
                            DrawRect(Color_orange,10 + X/2 * Int_TileWidth,Y/2 * Int_TileHeight + 10,Int_TileWidth,Int_TileHeight)
                        elif Matrix_Occupied[Y][X] == 1 and Bool_GenerateMaze and Maze_Algorithm == "Division" and Bool_EnableGreenHighlight:
                            DrawRect(Color_green,10 + X/2 * Int_TileWidth,Y/2 * Int_TileHeight + 10,Int_TileWidth,Int_TileHeight)
                    if Matrix_TileState[Y][X] == 2: ########### WALL TILE # LessEven(Y) LessEven(X) LargerEven(Y) LargerEven(X)
                        wall_thicc_ness = 10
                        if (X % 2 == 0 and Y % 2 == 1): # horizontal wall
                            if not (X,Y) in Set_randomPath:
                                DrawLine(Color_black,10 + X/2 * Int_TileWidth,LargerEven(Y)/2 * Int_TileHeight + 10,10 + X/2 * Int_TileWidth + Int_TileWidth,LargerEven(Y)/2 * Int_TileHeight + 10,wall_thicc_ness)
                        elif (X % 2 == 1 and Y % 2 == 0): # # vertical wall
                            if not (X,Y) in Set_randomPath:
                                DrawLine(Color_black,10 +  LargerEven(X)/2 * Int_TileWidth,Y/2 * Int_TileHeight + 10,10 +  LargerEven(X)/2 * Int_TileWidth,Y/2 * Int_TileHeight + 10 + Int_TileHeight,wall_thicc_ness)
                        elif (X % 2 == 0 and Y % 2 == 0): # full wall
                            if (X,Y) in Set_randomPath:
                                DrawRect(Color_red,10 + X/2 * Int_TileWidth,Y/2 * Int_TileHeight + 10,Int_TileWidth,Int_TileHeight)
                            else:
                                DrawRect(Color_black,10 + X/2 * Int_TileWidth,Y/2 * Int_TileHeight + 10,Int_TileWidth,Int_TileHeight)
                        


                
                if Bool_GenerateMaze and Bool_InstantMaze and not Reset_Wall:
                    if Queue_BackTrackTile and Maze_Algorithm == "BackTracking":
                        X_now,Y_now = Queue_BackTrackTile.pop()
                        X_HL,Y_HL = X_now,Y_now
                        NB = MazeGetAvailaiblePath_Backtracker(X_now,Y_now)
                        if len(NB) >= 1:
                            Queue_BackTrackTile.append((X_now,Y_now))
                        if len(NB) != 0:
                            Xnext,Ynext,NBdirection = NB[random.randint(0,len(NB) - 1)]
                            X_HL,Y_HL = Xnext,Ynext
                            Queue_BackTrackTile.append((Xnext,Ynext))
                            if NBdirection == "+x":
                                Matrix_TileState[Y_now][X_now + 1] = 1
                                Matrix_TileState[Y_now][X_now + 2] = 1
                            elif NBdirection == "-x":
                                Matrix_TileState[Y_now][X_now - 1] = 1
                                Matrix_TileState[Y_now][X_now - 2] = 1
                            elif NBdirection == "+y":
                                Matrix_TileState[Y_now + 1][X_now] = 1
                                Matrix_TileState[Y_now + 2][X_now] = 1
                            elif NBdirection == "-y":
                                Matrix_TileState[Y_now - 1][X_now] = 1
                                Matrix_TileState[Y_now - 2][X_now] = 1
                    
                    elif Maze_Algorithm == "Randomized Kruskal" and len(Set_MazePath) != 0:
                        if len(Set_MazePath) != 0:
                            RandomTileindex = random.randint(0,len(Set_MazePath) - 1)
                        index = 0
                        for Element in Set_MazePath:
                            if index == RandomTileindex:
                                (X_now,Y_now) = Element
                                (X_HL,Y_HL) = (X_now,Y_now)
                                break
                            index += 1
                        Set_MazePath.remove((X_now,Y_now))
                        if (X_now % 2 == 1 and Y_now % 2 == 0): ##################### Horizontal NB
                            NB = MazeGetAvailaiblePath_Kruskal_Horizontal(X_now,Y_now)
                        elif (X_now % 2 == 0 and Y_now % 2 == 1): ##################### vertical NB
                            NB = MazeGetAvailaiblePath_Kruskal_Vertical(X_now,Y_now)
                        if len(NB) == 2:
                            (X_test1,Y_test1) = NB[0]
                            (X_test2,Y_test2) = NB[1]
                            if not (X_test2,Y_test2) in List_PathSet[Y_test1][X_test1]:
                                Matrix_TileState[Y_test1][X_test1] = 1
                                Matrix_TileState[Y_test2][X_test2] = 1
                                Matrix_TileState[Y_now][X_now] = 1
                                UnionResult = SetUnion(List_PathSet[Y_test2][X_test2],List_PathSet[Y_test1][X_test1])
                                for i in UnionResult:
                                    (X_get,Y_get) = i
                                    List_PathSet[Y_get][X_get] = UnionResult

                    elif Maze_Algorithm == "Prim" and len(Set_MazePath) != 0:
                        RandomTileindex = random.randint(0,len(Set_MazePath) - 1)
                        index = 0
                        for Element in Set_MazePath:
                            if index == RandomTileindex:
                                (X_now,Y_now) = Element
                            index += 1
                        X_HL,Y_HL = X_now,Y_now
                        NB = MazeGetAvailaiblePath_Prim(X_now,Y_now)
                        if len(NB) != 0:
                            Xnext,Ynext,NBdirection = NB[random.randint(0,len(NB) - 1)]
                            Set_MazePath.add((Xnext,Ynext)) 
                            if NBdirection == "+x":
                                Matrix_TileState[Y_now][X_now + 1] = 1
                                Matrix_TileState[Y_now][X_now + 2] = 1
                            elif NBdirection == "-x":
                                Matrix_TileState[Y_now][X_now - 1] = 1
                                Matrix_TileState[Y_now][X_now - 2] = 1
                            elif NBdirection == "+y":
                                Matrix_TileState[Y_now + 1][X_now] = 1
                                Matrix_TileState[Y_now + 2][X_now] = 1
                            elif NBdirection == "-y":
                                Matrix_TileState[Y_now - 1][X_now] = 1
                                Matrix_TileState[Y_now - 2][X_now] = 1
                        else:
                            Set_MazePath.remove((X_now,Y_now))
                    
                    elif Maze_Algorithm == "BinaryTree":
                        NB = MazeGetAvailaiblePath_BinaryTree(X_now,Y_now)
                        Matrix_TileState[Y_now][X_now] = 1
                        Xnext,Ynext,NBdirection = NB[random.randint(0,len(NB) - 1)]
                        if NBdirection == "-x":
                            Matrix_TileState[Y_now][X_now - 1] = 1
                        elif NBdirection == "-y":
                            Matrix_TileState[Y_now - 1][X_now] = 1
                        X_now += 2
                        if X_now > LessEven(Int_Tile_count - 1):
                            X_now = 0
                            Y_now += 2
                        if Y_now > LessEven(Int_Tile_count - 1):
                            Bool_GenerateMaze = False

                    elif Maze_Algorithm == "Wilson":
                        NB = MazeGetAvailaiblePath_Wilson(X_consider,Y_consider)
                        Xnext,Ynext,NBdirection = NB[random.randint(0,len(NB) - 1)]
                        List_TileDirection[Y_consider][X_consider] = (Xnext,Ynext,NBdirection) #############zzz
                        (X_consider,Y_consider) = (Xnext,Ynext)
                        if not (X_consider,Y_consider) in Set_randomPath:
                            if NBdirection == "+x":
                                Set_randomPath.add((Xnext - 1,Ynext))
                                Set_randomPath.add((Xnext - 2,Ynext))
                            elif NBdirection == "-x":
                                Set_randomPath.add((Xnext + 1,Ynext))
                                Set_randomPath.add((Xnext + 2,Ynext))
                            elif NBdirection == "+y":
                                Set_randomPath.add((Xnext,Ynext - 1))
                                Set_randomPath.add((Xnext,Ynext - 2))
                            elif NBdirection == "-y":
                                Set_randomPath.add((Xnext,Ynext + 1))
                                Set_randomPath.add((Xnext,Ynext + 2))

                        if (X_consider,Y_consider) in Set_randomPath: ############# check for cycle and remove them
                            X_RemoveNext,Y_RemoveNext,NBdirection = List_TileDirection[Y_consider][X_consider] #############zzz
                            for i in Set_randomPath:
                                if (X_RemoveNext,Y_RemoveNext) == (X_consider,Y_consider):
                                    break
                                if NBdirection == "+x":
                                    Set_PathToRemove.add((X_RemoveNext - 1,Y_RemoveNext))
                                elif NBdirection == "-x":
                                    Set_PathToRemove.add((X_RemoveNext + 1,Y_RemoveNext))
                                elif NBdirection == "+y":
                                    Set_PathToRemove.add((X_RemoveNext,Y_RemoveNext - 1))
                                elif NBdirection == "-y":
                                    Set_PathToRemove.add((X_RemoveNext,Y_RemoveNext + 1))
                                Set_PathToRemove.add((X_RemoveNext,Y_RemoveNext)) #############zzz
                                
                                (X_RemoveNext,Y_RemoveNext,NBdirection) = List_TileDirection[Y_RemoveNext][X_RemoveNext]
                                
                            Set_randomPath = Set_randomPath - Set_PathToRemove
                            Set_PathToRemove = set()

                        if len(Set_randomPath) >= 500:
                            Set_randomPath = set()
                            (X_consider,Y_consider) = (X_now,Y_now)

                        if (X_consider,Y_consider) in Set_MazePath: ############# merge path set
                            for i in Set_randomPath:
                                (X2,Y2) = i
                                Matrix_TileState[Y2][X2] = 1
                                if X2 % 2 == 0 and Y2 % 2 == 0:
                                    Set_MazePath.add((X2,Y2))
                            Set_randomPath = set()
                            while (X_now,Y_now) in Set_MazePath:
                                X_now += 2
                                if X_now > LessEven(Int_Tile_count - 1):
                                    X_now = 0
                                    Y_now += 2
                                if Y_now > LessEven(Int_Tile_count - 1):
                                    Bool_GenerateMaze = False
                            (X_consider,Y_consider) = (X_now,Y_now)
                    
                    elif Maze_Algorithm == "HuntAndKill":
                        (X_HL,Y_HL) = (X_now,Y_now)
                        NB = MazeGetAvailaiblePath_HuntKill(X_now,Y_now)
                        if len(NB) != 0:
                            Xnext,Ynext,NBdirection = NB[random.randint(0,len(NB) - 1)]
                            if NBdirection == "+x":
                                Matrix_TileState[Y_now][X_now + 1] = 1
                                Matrix_TileState[Y_now][X_now + 2] = 1
                            elif NBdirection == "-x":
                                Matrix_TileState[Y_now][X_now - 1] = 1
                                Matrix_TileState[Y_now][X_now - 2] = 1
                            elif NBdirection == "+y":
                                Matrix_TileState[Y_now + 1][X_now] = 1
                                Matrix_TileState[Y_now + 2][X_now] = 1
                            elif NBdirection == "-y":
                                Matrix_TileState[Y_now - 1][X_now] = 1
                                Matrix_TileState[Y_now - 2][X_now] = 1
                            (X_now,Y_now) = (Xnext,Ynext)   
                        else:
                            (X_now,Y_now) = (0,0)
                            NB = MazeGetAvailaiblePath_HuntKill(X_now,Y_now)
                            while len(NB) == 0 or Matrix_TileState[Y_now][X_now] == 2:
                                X_now += 2
                                if X_now > LessEven(Int_Tile_count - 1):
                                    X_now = 0
                                    Y_now += 2
                                if Y_now > LessEven(Int_Tile_count - 1):
                                    Bool_GenerateMaze = False
                                    break
                                NB = MazeGetAvailaiblePath_HuntKill(X_now,Y_now)
                    
                    elif Maze_Algorithm == "Division":

                        (X_start,Y_start) = (-1,-1)
                        Y_vertical_end = -1
                        X_horizontal_end = -1
                        
                        for Y2 in range(0,Int_Tile_count):
                            for X2 in range(0,Int_Tile_count): # FIND START
                                if Matrix_Occupied[Y2][X2] == 0:
                                    (X_start,Y_start) = (X2,Y2)
                                    break
                            if (X_start,Y_start) != (-1,-1):
                                break
                            
                        
                        if (X_start,Y_start) != (-1,-1):

                            for X2 in range(X_start,Int_Tile_count): # Horizontal loop use y = Y_start
                                if X2 < Int_Tile_count - 1:
                                    if Matrix_Occupied[Y_start][X2 + 1] == 1:
                                        X_horizontal_end = X2
                                        break
                                X_horizontal_end = X2
                                    

                            for Y2 in range(Y_start,Int_Tile_count): # vertical loop use x = X_start
                                if Y2 < Int_Tile_count - 1:
                                    if Matrix_Occupied[Y2 + 1][X_start] == 1:
                                        Y_vertical_end = Y2
                                        break
                                Y_vertical_end = Y2
                                    

                            if X_start == X_horizontal_end or Y_start == Y_vertical_end:
                                for Y2 in range(Y_start,Y_vertical_end + 1):
                                    for X2 in range(X_start,X_horizontal_end + 1):
                                        Matrix_Occupied[Y2][X2] = 1

                            else:
                                if DivisionWallToAdd == "Vertical":
                                    X_walltoadd = LessEven(random.randint(X_start,X_horizontal_end)) + 1 # odd
                                    if X_walltoadd > X_horizontal_end:
                                        X_walltoadd -= 2
                                    for Y2 in range(Y_start,Y_vertical_end + 1):
                                        Matrix_TileState[Y2][X_walltoadd] = 2
                                        Matrix_Occupied[Y2][X_walltoadd] = 1
                                    Y_passage = LessEven(random.randint(Y_start,Y_vertical_end)) # Even
                                    if Y_passage < Y_start:
                                        Y_passage += 2
                                    Matrix_TileState[Y_passage][X_walltoadd] = 1 # add path
                                    DivisionWallToAdd = "Horizontal"
                                elif DivisionWallToAdd == "Horizontal":
                                    Y_walltoadd = LessEven(random.randint(Y_start,Y_vertical_end)) + 1 # odd
                                    if Y_walltoadd > Y_vertical_end:
                                        Y_walltoadd -= 2
                                    for X2 in range(X_start,X_horizontal_end + 1):
                                        Matrix_TileState[Y_walltoadd][X2] = 2
                                        Matrix_Occupied[Y_walltoadd][X2] = 1
                                    X_passage = LessEven(random.randint(X_start,X_horizontal_end)) # Even
                                    if X_passage < X_start:
                                        X_passage += 2
                                    Matrix_TileState[Y_walltoadd][X_passage] = 1 # add path
                                    DivisionWallToAdd = "Vertical"
                        else:
                            Bool_GenerateMaze = False

                        ############## ADD WALL
                
                





    if Reset_Wall:
        if Maze_Algorithm == "Prim" and Bool_GenerateMaze:
            (X_now,Y_now) = (LessEven(random.randint(0,Int_Tile_count - 1)),LessEven(random.randint(0,Int_Tile_count - 1)))
            Matrix_TileState[Y_now][X_now] = 1
            Set_MazePath.add((X_now,Y_now))
        elif Maze_Algorithm == "BinaryTree" and Bool_GenerateMaze:
            Matrix_TileState[0][0] = 1
            (X_now,Y_now) = (2,0)
        elif Maze_Algorithm == "Wilson" and Bool_GenerateMaze:
            Matrix_TileState[0][0] = 1
            # Matrix_TileState[1][0] = 1
            # Matrix_TileState[2][0] = 1
            # Matrix_TileState[2][1] = 1
            # Matrix_TileState[0][2] = 1
            # Matrix_TileState[1][2] = 1
            # Matrix_TileState[2][2] = 1
            Set_MazePath.add((0,0))
            # Set_MazePath.add((2,0))
            # Set_MazePath.add((0,2))
            # Set_MazePath.add((2,2))

            (X_now,Y_now) = (2,0)
            (X_consider,Y_consider) = (2,0)
            Set_randomPath.add((X_consider,Y_consider))
        elif Maze_Algorithm == "BackTracking" and Bool_GenerateMaze:
            Matrix_TileState[Y_now][X_now] = 1
        elif Maze_Algorithm == "HuntAndKill"  and Bool_GenerateMaze:
            (X_now,Y_now) = (LessEven(random.randint(0,Int_Tile_count - 1)),LessEven(random.randint(0,Int_Tile_count - 1)))
            Matrix_TileState[Y_now][X_now] = 1
    Reset_Wall = False  





    if Bool_GenerateMaze:
        if Maze_Algorithm == "BackTracking" and Int_Time % Int_AnimationDelay == 0 and not Bool_PuaseAnimation and not Reset_Wall and not Bool_InstantMaze:
            X_now,Y_now = Queue_BackTrackTile.pop()
            X_HL,Y_HL = X_now,Y_now
            NB = MazeGetAvailaiblePath_Backtracker(X_now,Y_now)
            if len(NB) >= 1:
                Queue_BackTrackTile.append((X_now,Y_now))
            if len(NB) != 0:
                Xnext,Ynext,NBdirection = NB[random.randint(0,len(NB) - 1)]
                X_HL,Y_HL = Xnext,Ynext
                Queue_BackTrackTile.append((Xnext,Ynext))
                if NBdirection == "+x":
                    Matrix_TileState[Y_now][X_now + 1] = 1
                    Matrix_TileState[Y_now][X_now + 2] = 1
                elif NBdirection == "-x":
                    Matrix_TileState[Y_now][X_now - 1] = 1
                    Matrix_TileState[Y_now][X_now - 2] = 1
                elif NBdirection == "+y":
                    Matrix_TileState[Y_now + 1][X_now] = 1
                    Matrix_TileState[Y_now + 2][X_now] = 1
                elif NBdirection == "-y":
                    Matrix_TileState[Y_now - 1][X_now] = 1
                    Matrix_TileState[Y_now - 2][X_now] = 1    

        elif Maze_Algorithm == "Randomized Kruskal" and Int_Time % Int_AnimationDelay == 0 and not Bool_PuaseAnimation and not Bool_InstantMaze:
            if len(Set_MazePath) != 0:
                RandomTileindex = random.randint(0,len(Set_MazePath) - 1)
            index = 0
            for Element in Set_MazePath:
                if index == RandomTileindex:
                    (X_now,Y_now) = Element
                    (X_HL,Y_HL) = (X_now,Y_now)
                    break
                index += 1
            Set_MazePath.remove((X_now,Y_now))
            if (X_now % 2 == 1 and Y_now % 2 == 0): ##################### Horizontal NB
                NB = MazeGetAvailaiblePath_Kruskal_Horizontal(X_now,Y_now)
            elif (X_now % 2 == 0 and Y_now % 2 == 1): ##################### vertical NB
                NB = MazeGetAvailaiblePath_Kruskal_Vertical(X_now,Y_now)
            if len(NB) == 2:
                (X_test1,Y_test1) = NB[0]
                (X_test2,Y_test2) = NB[1]
                if not (X_test2,Y_test2) in List_PathSet[Y_test1][X_test1]:
                    Matrix_TileState[Y_test1][X_test1] = 1
                    Matrix_TileState[Y_test2][X_test2] = 1
                    Matrix_TileState[Y_now][X_now] = 1
                    UnionResult = SetUnion(List_PathSet[Y_test2][X_test2],List_PathSet[Y_test1][X_test1])
                    for i in UnionResult:
                        (X_get,Y_get) = i
                        List_PathSet[Y_get][X_get] = UnionResult
            
        elif Maze_Algorithm == "Prim" and Int_Time % Int_AnimationDelay == 0 and not Bool_PuaseAnimation and not Bool_InstantMaze:
            RandomTileindex = random.randint(0,len(Set_MazePath) - 1)
            index = 0
            for Element in Set_MazePath:
                if index == RandomTileindex:
                    (X_now,Y_now) = Element
                index += 1
            X_HL,Y_HL = X_now,Y_now
            NB = MazeGetAvailaiblePath_Prim(X_now,Y_now)
            if len(NB) != 0:
                Xnext,Ynext,NBdirection = NB[random.randint(0,len(NB) - 1)]
                Set_MazePath.add((Xnext,Ynext)) 
                if NBdirection == "+x":
                    Matrix_TileState[Y_now][X_now + 1] = 1
                    Matrix_TileState[Y_now][X_now + 2] = 1
                elif NBdirection == "-x":
                    Matrix_TileState[Y_now][X_now - 1] = 1
                    Matrix_TileState[Y_now][X_now - 2] = 1
                elif NBdirection == "+y":
                    Matrix_TileState[Y_now + 1][X_now] = 1
                    Matrix_TileState[Y_now + 2][X_now] = 1
                elif NBdirection == "-y":
                    Matrix_TileState[Y_now - 1][X_now] = 1
                    Matrix_TileState[Y_now - 2][X_now] = 1
            else:
                Set_MazePath.remove((X_now,Y_now))

        elif Maze_Algorithm == "BinaryTree" and Int_Time % Int_AnimationDelay == 0 and not Bool_PuaseAnimation and not Bool_InstantMaze:
            NB = MazeGetAvailaiblePath_BinaryTree(X_now,Y_now)
            X_HL,Y_HL = X_now,Y_now
            Matrix_TileState[Y_now][X_now] = 1
            Xnext,Ynext,NBdirection = NB[random.randint(0,len(NB) - 1)]
            if NBdirection == "-x":
                Matrix_TileState[Y_now][X_now - 1] = 1
            elif NBdirection == "-y":
                Matrix_TileState[Y_now - 1][X_now] = 1
            X_now += 2
            if X_now > LessEven(Int_Tile_count - 1):
                X_now = 0
                Y_now += 2
            if Y_now > LessEven(Int_Tile_count - 1):
                Bool_GenerateMaze = False

        elif Maze_Algorithm == "Wilson" and Int_Time % Int_AnimationDelay == 0 and not Bool_PuaseAnimation and not Bool_InstantMaze:
            NB = MazeGetAvailaiblePath_Wilson(X_consider,Y_consider)
            Xnext,Ynext,NBdirection = NB[random.randint(0,len(NB) - 1)]
            List_TileDirection[Y_consider][X_consider] = (Xnext,Ynext,NBdirection) #############zzz
            (X_consider,Y_consider) = (Xnext,Ynext)
            if not (X_consider,Y_consider) in Set_randomPath:
                if NBdirection == "+x":
                    Set_randomPath.add((Xnext - 1,Ynext))
                    Set_randomPath.add((Xnext - 2,Ynext))
                elif NBdirection == "-x":
                    Set_randomPath.add((Xnext + 1,Ynext))
                    Set_randomPath.add((Xnext + 2,Ynext))
                elif NBdirection == "+y":
                    Set_randomPath.add((Xnext,Ynext - 1))
                    Set_randomPath.add((Xnext,Ynext - 2))
                elif NBdirection == "-y":
                    Set_randomPath.add((Xnext,Ynext + 1))
                    Set_randomPath.add((Xnext,Ynext + 2))

            if (X_consider,Y_consider) in Set_randomPath: ############# check for cycle and remove them
                X_RemoveNext,Y_RemoveNext,NBdirection = List_TileDirection[Y_consider][X_consider] #############zzz
                for i in Set_randomPath:
                    if (X_RemoveNext,Y_RemoveNext) == (X_consider,Y_consider):
                        break
                    if NBdirection == "+x":
                        Set_PathToRemove.add((X_RemoveNext - 1,Y_RemoveNext))
                    elif NBdirection == "-x":
                        Set_PathToRemove.add((X_RemoveNext + 1,Y_RemoveNext))
                    elif NBdirection == "+y":
                        Set_PathToRemove.add((X_RemoveNext,Y_RemoveNext - 1))
                    elif NBdirection == "-y":
                        Set_PathToRemove.add((X_RemoveNext,Y_RemoveNext + 1))
                    Set_PathToRemove.add((X_RemoveNext,Y_RemoveNext)) #############zzz
                    
                    (X_RemoveNext,Y_RemoveNext,NBdirection) = List_TileDirection[Y_RemoveNext][X_RemoveNext]
                    
                Set_randomPath = Set_randomPath - Set_PathToRemove
                Set_PathToRemove = set()

            if len(Set_randomPath) >= 500:
                Set_randomPath = set()
                (X_consider,Y_consider) = (X_now,Y_now)

            if (X_consider,Y_consider) in Set_MazePath: ############# merge path set
                for i in Set_randomPath:
                    (X2,Y2) = i
                    Matrix_TileState[Y2][X2] = 1
                    if X2 % 2 == 0 and Y2 % 2 == 0:
                        Set_MazePath.add((X2,Y2))
                Set_randomPath = set()
                while (X_now,Y_now) in Set_MazePath:
                    X_now += 2
                    if X_now > LessEven(Int_Tile_count - 1):
                        X_now = 0
                        Y_now += 2
                    if Y_now > LessEven(Int_Tile_count - 1):
                        Bool_GenerateMaze = False
                (X_consider,Y_consider) = (X_now,Y_now)

        elif Maze_Algorithm == "HuntAndKill" and Int_Time % Int_AnimationDelay == 0 and not Bool_PuaseAnimation and not Bool_InstantMaze:
            (X_HL,Y_HL) = (X_now,Y_now)
            NB = MazeGetAvailaiblePath_HuntKill(X_now,Y_now)
            if len(NB) != 0:
                Xnext,Ynext,NBdirection = NB[random.randint(0,len(NB) - 1)]
                if NBdirection == "+x":
                    Matrix_TileState[Y_now][X_now + 1] = 1
                    Matrix_TileState[Y_now][X_now + 2] = 1
                elif NBdirection == "-x":
                    Matrix_TileState[Y_now][X_now - 1] = 1
                    Matrix_TileState[Y_now][X_now - 2] = 1
                elif NBdirection == "+y":
                    Matrix_TileState[Y_now + 1][X_now] = 1
                    Matrix_TileState[Y_now + 2][X_now] = 1
                elif NBdirection == "-y":
                    Matrix_TileState[Y_now - 1][X_now] = 1
                    Matrix_TileState[Y_now - 2][X_now] = 1
                (X_now,Y_now) = (Xnext,Ynext)   
            else:
                (X_now,Y_now) = (0,0)
                NB = MazeGetAvailaiblePath_HuntKill(X_now,Y_now)
                while len(NB) == 0 or Matrix_TileState[Y_now][X_now] == 2:
                    X_now += 2
                    if X_now > LessEven(Int_Tile_count - 1):
                        X_now = 0
                        Y_now += 2
                    if Y_now > LessEven(Int_Tile_count - 1):
                        Bool_GenerateMaze = False
                        break
                    NB = MazeGetAvailaiblePath_HuntKill(X_now,Y_now)

        elif Maze_Algorithm == "Division" and Int_Time % Int_AnimationDelay == 0 and not Bool_PuaseAnimation and not Bool_InstantMaze:

            (X_start,Y_start) = (-1,-1)
            Y_vertical_end = -1
            X_horizontal_end = -1
            
            for Y2 in range(0,Int_Tile_count):
                for X2 in range(0,Int_Tile_count): # FIND START
                    if Matrix_Occupied[Y2][X2] == 0:
                        (X_start,Y_start) = (X2,Y2)
                        break
                if (X_start,Y_start) != (-1,-1):
                    break
                
            
            if (X_start,Y_start) != (-1,-1):

                for X2 in range(X_start,Int_Tile_count): # Horizontal loop use y = Y_start
                    if X2 < Int_Tile_count - 1:
                        if Matrix_Occupied[Y_start][X2 + 1] == 1:
                            X_horizontal_end = X2
                            break
                    X_horizontal_end = X2
                        

                for Y2 in range(Y_start,Int_Tile_count): # vertical loop use x = X_start
                    if Y2 < Int_Tile_count - 1:
                        if Matrix_Occupied[Y2 + 1][X_start] == 1:
                            Y_vertical_end = Y2
                            break
                    Y_vertical_end = Y2
                        

                if X_start == X_horizontal_end or Y_start == Y_vertical_end:
                    for Y2 in range(Y_start,Y_vertical_end + 1):
                        for X2 in range(X_start,X_horizontal_end + 1):
                            Matrix_Occupied[Y2][X2] = 1

                else:
                    if DivisionWallToAdd == "Vertical":
                        X_walltoadd = LessEven(random.randint(X_start,X_horizontal_end)) + 1 # odd
                        if X_walltoadd > X_horizontal_end:
                            X_walltoadd -= 2
                        for Y2 in range(Y_start,Y_vertical_end + 1):
                            Matrix_TileState[Y2][X_walltoadd] = 2
                            Matrix_Occupied[Y2][X_walltoadd] = 1
                        Y_passage = LessEven(random.randint(Y_start,Y_vertical_end)) # Even
                        if Y_passage < Y_start:
                            Y_passage += 2
                        Matrix_TileState[Y_passage][X_walltoadd] = 1 # add path
                        DivisionWallToAdd = "Horizontal"
                    elif DivisionWallToAdd == "Horizontal":
                        Y_walltoadd = LessEven(random.randint(Y_start,Y_vertical_end)) + 1 # odd
                        if Y_walltoadd > Y_vertical_end:
                            Y_walltoadd -= 2
                        for X2 in range(X_start,X_horizontal_end + 1):
                            Matrix_TileState[Y_walltoadd][X2] = 2
                            Matrix_Occupied[Y_walltoadd][X2] = 1
                        X_passage = LessEven(random.randint(X_start,X_horizontal_end)) # Even
                        if X_passage < X_start:
                            X_passage += 2
                        Matrix_TileState[Y_walltoadd][X_passage] = 1 # add path
                        DivisionWallToAdd = "Vertical"
            else:
                Bool_GenerateMaze = False

            ############## ADD WALL
            




            









    if Maze_Algorithm == "BackTracking" and not Queue_BackTrackTile:
        Bool_GenerateMaze = False
    elif Maze_Algorithm == "Prim" and len(Set_MazePath) == 0:
        Bool_GenerateMaze = False
    elif Maze_Algorithm == "Randomized Kruskal" and len(Set_MazePath) == 0:
        Bool_GenerateMaze = False
    ClickCoolDown += 1
    Int_Time += 1
    if not Bool_GenerateMaze:
        (X_HL,Y_HL) = (-1,-1)
    UpdateScreen()



