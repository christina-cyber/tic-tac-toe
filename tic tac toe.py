from unittest.util import three_way_cmp
import os
def sum(a,b,c):
    return a+b+c


def printBoard(xstate, zstate):
    one ='X' if xstate[1] else ('O' if zstate[1] else 1)
    zero='X' if xstate[0] else ('O' if zstate[0] else 0)
    two='X' if xstate[2] else ('O' if zstate[2] else 2)
    three='X' if xstate[3] else ('O' if zstate[3] else 3)
    four ='X' if xstate[4] else ('O' if zstate[4] else 4)
    five ='X' if xstate[5] else ('O' if zstate[5] else 5)
    six  ='X' if xstate[6] else ('O' if zstate[6] else 6)
    seven  ='X' if xstate[7] else ('O' if zstate[7] else 7)
    eight ='X' if xstate[8] else ('O' if zstate[8] else 8)
  
   
    print(f"| {zero} | {one} | {two} |")
    print(f"|---|---|---|")
    print(f"| {three} | {four} | {five} |")
    print(f"|---|---|---|")
    print(f"| {six} | {seven} | {eight} |")

def checkwin (xstate, zstate):
    wins=[[0,1,2], [3,4,5],[6,7,8],[0,4,8],[2,4,6],[0,3,6],[1,4,7],[2,5,8]]
    for win in wins:
        if (sum(xstate[win[0]], xstate[win[1]],xstate[win[2]])==3):
            print(sum(xstate[win[0]], xstate[win[1]],xstate[win[2]]))
            print("x won the match")
            return 1
        if (sum(zstate[win[0]], zstate[win[1]],zstate[win[2]])==3):
            print(sum(zstate[win[0]], zstate[win[1]],zstate[win[2]]))
            print("O won the match")
            return 0
    return -1

   


if __name__ == "__main__" :
    xstate =[0,0,0,0,0,0,0,0,0]
    zstate =[0,0,0,0,0,0,0,0,0]
    turn=1
    gameover = False
    print("welcome to tic tac toe")
    while(not gameover):
        os.system("clear")
        printBoard(xstate, zstate)
        if(turn==1):
            print("X's chance")
            value=int(input("please enter a value: "))
            xstate[value] = 1
        else:
            print("O's chance")
            value=int(input("please enter a value: "))
            zstate[value] = 1
        cwin = checkwin(xstate, zstate)
        if(cwin != -1):
            print("match over")
            gameover = True
            printBoard(xstate, zstate)
        turn= 1-turn
    