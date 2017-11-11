#!/bin/python3

import sys

if __name__ == "__main__":
    n = int(input().strip())
    d = input().strip()
    board_game=[];
    for i in range(n):
        board_game.append([])
        for k in range(n):
            board_game[i].append(0)
    new_board_game =[];
    for i in range(n):
        new_board_game.append([]);
    
    x, y = input().strip().split(' ')
    x, y = [int(x), int(y)]
    startpoint=0;
    # Write Your Code Here
    count = 1;
    board_game[x][y]=count;
    while count < n*n:
        count+=1;
        if d=='n':
            if ( x-1 >=0 and board_game[x-1][y]==0):  #North
                board_game[x-1][y]=count;
                x=x-1;
            elif(y-1 >=0 and board_game[x][y-1]==0): #West
                board_game[x][y-1]=count;
                y=y-1;
            elif (y+1 < n and board_game[x][y+1]==0):   #East
                board_game[x][y+1]=count;
                y=y+1;
            elif(x+1<n and board_game[x+1][y]==0):   #South
                board_game[x+1][y]=count;
                x=x+1;
                
        if d=='s':
            if(x+1<n and board_game[x+1][y]==0):
                board_game[x+1][y]=count;
                x=x+1;
            elif(y-1 >=0 and board_game[x][y-1]==0):
                board_game[x][y-1]=count;
                y=y-1;
            elif (y+1 < n and board_game[x][y+1]==0):
                board_game[x][y+1]=count;
                y=y+1;
            elif ( x-1 >=0 and board_game[x-1][y]==0):
                board_game[x-1][y]=count;
                x=x-1;
                
        if d=='w':
            if(y-1 >=0 and board_game[x][y-1]==0): #West
                board_game[x][y-1]=count;
                y=y-1;
            elif ( x-1 >=0 and board_game[x-1][y]==0):  #North
                board_game[x-1][y]=count;
                x=x-1;
            elif(x+1<n and board_game[x+1][y]==0):   #South
                board_game[x+1][y]=count;
                x=x+1;
            elif (y+1 < n and board_game[x][y+1]==0):   #East
                board_game[x][y+1]=count;
                y=y+1;
         
        if d=='e':
            if (y+1 < n and board_game[x][y+1]==0):   #East
                board_game[x][y+1]=count;
                y=y+1;
            elif ( x-1 >=0 and board_game[x-1][y]==0):  #North
                board_game[x-1][y]=count;
                x=x-1;
            elif(x+1<n and board_game[x+1][y]==0):   #South
                board_game[x+1][y]=count;
                x=x+1;
            elif(y-1 >=0 and board_game[x][y-1]==0): #West
                board_game[x][y-1]=count;
                y=y-1;
            
    for i in range(n):
        for j in range(n):
            print(board_game[i][j], end =" ");
        print()
