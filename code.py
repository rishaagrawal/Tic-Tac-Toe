from numpy import random
import os
from termcolor import colored
A=[[1,2,3],[4,5,6],[7,8,9]]
r=[1,2,3,4,5,6,7,8,9]
def printttt():
    os.system('cls' if os.name =='nt' else clear)
    print("<<<<<<<<<<<< "+colored('GAME ON!','red')+" >>>>>>>>>>>>\n")
    for i in range (3):
        for j in range (3):
            print(colored(A[i][j],'grey'), end=" ")
        print()
    print("\n") 
def h():
    for j in range(2):
        for i in range(3):
            if A[i][j]==A[i][j+1]==colored('O','yellow') :
                for k in range(3):
                    if k != j and k != j+1 and (A[i][k]!=colored('X','blue') and A[i][k]!=colored('O','yellow')):
                        A[i][k]=colored('O','yellow')
                        z=(i*3)+k+1
                        l.append(z)
                        return
            if A[i][j]==A[i][j+1]==colored('X','blue') :
                for k in range(3):
                    if k != j and k != j+1 and (A[i][k]!=colored('X','blue') and A[i][k]!=colored('O','yellow')):
                        A[i][k]=colored('O','yellow')
                        z=(i*3)+k+1
                        l.append(z)
                        return
            elif A[i][0]==A[i][2]==colored('O','yellow') and (A[i][1]!=colored('X','blue') and A[i][1]!=colored('O','yellow')):
                A[i][1]=colored('O','yellow')
                z=(i*3)+2
                l.append(z)
                return
            elif A[i][0]==A[i][2]==colored('X','blue') and (A[i][1]!=colored('X','blue') and A[i][1]!=colored('O','yellow')):
                A[i][1]=colored('O','yellow')
                z=(i*3)+2
                l.append(z)
                return
               
    for j in range(3):
        for i in range(2):
            if A[i][j]==A[i+1][j]==colored('O','yellow') :
                for k in range(3):
                    if k != i and k != i+1 and (A[k][j]!=colored('X','blue') and A[k][j]!=colored('O','yellow')):
                        A[k][j]=colored('O','yellow')
                        z=(k*3)+j+1
                        l.append(z)
                        return
            if A[i][j]==A[i+1][j]==colored('X','blue') :
                for k in range(3):
                    if k != i and k != i+1 and (A[k][j]!=colored('X','blue') and A[k][j]!=colored('O','yellow')):
                        A[k][j]=colored('O','yellow')
                        z=(k*3)+j+1
                        l.append(z)
                        return
            elif A[0][j]==A[2][j]==colored('O','yellow') and (A[1][j]!=colored('X','blue') and A[1][j]!=colored('O','yellow')):
                A[1][j]=colored('O','yellow')
                z=4+j
                l.append(z)
                return
            elif A[0][j]==A[2][j]==colored('X','blue') and (A[1][j]!=colored('X','blue') and A[1][j]!=colored('O','yellow')):
                A[1][j]=colored('O','yellow')
                z=4+j
                l.append(z)
                return
    for i in range(2):
        if A[i][i]==A[i+1][i+1]==colored('O','yellow') :
            for k in range(3):
                if k != i and k!=i+1 and (A[k][k]!=colored('X','blue') and A[k][k]!=colored('O','yellow')) :
                    A[k][k]=colored('O','yellow')
                    z=(k*3)+k+1
                    l.append(z)
                    return
        if A[i][i]==A[i+1][i+1]==colored('X','blue') :
            for k in range(3):
                if k != i and k!=i+1 and (A[k][k]!=colored('X','blue') and A[k][k]!=colored('O','yellow')) :
                    A[k][k]=colored('O','yellow')
                    z=(k*3)+k+1
                    l.append(z)
                    return
                                            
    if A[0][0]==A[2][2]==colored('O','yellow') or A[0][2]==A[2][0] and (A[1][1]!=colored('X','blue') and A[1][1]!=colored('O','yellow')):
        A[1][1]=colored('O','yellow')
        z=5
        l.append(z)
        return
    if A[0][0]==A[2][2]==colored('X','blue') or A[0][2]==A[2][0] and (A[1][1]!=colored('X','blue') and A[1][1]!=colored('O','yellow')):
        A[1][1]=colored('O','yellow')
        z=5
        l.append(z)
        return
            
    elif A[1][1]==A[2][0]==colored('O','yellow') and (A[0][2]!=colored('X','blue') and A[0][2]!=colored('O','yellow')):
        A[0][2]=colored('O','yellow')
        z=3
        l.append(z)
        return
    elif A[1][1]==A[2][0]==colored('X','blue') and (A[0][2]!=colored('X','blue') and A[0][2]!=colored('O','yellow')):
        A[0][2]=colored('O','yellow')
        z=3
        l.append(z)
        return
            
    elif A[1][1]==A[0][2]==colored('O','yellow') and (A[2][0]!=colored('X','blue') and A[2][0]!=colored('O','yellow')):
        A[2][0]=colored('O','yellow')
        z=7
        l.append(z)
        return
    elif A[1][1]==A[0][2]==colored('X','blue') and (A[2][0]!=colored('X','blue') and A[2][0]!=colored('O','yellow')):
        A[2][0]=colored('O','yellow')
        z=7
        l.append(z)
        return
while (1):   
    print(colored("\n========== TIC TAC TOE ==========\n1)PLAYER vs COMPUTER.\n2)PLAYER vs PLAYER.\n3)QUIT GAME.\n=================================",'light_magenta'))
    ch=int(input("\nEnter choice : "))
    print(colored("---------------------------------\n",'light_magenta'))
    if ch==3:
        break 
    if ch==1:
        print(colored("PLAYER: X  ::  COMPUTER: O\n",'light_cyan'))
        ch3=int(input(colored("1)EASY\n2)MODERATE\n\nSelect diffulty level:: ",'light_cyan')))
    l=[]
    printttt()
    for f in range(9):
        ch1=int (input("PLAYER X::"))
        for k in range (len(l)):
            for i in range (len(l)):
                if l[i]==ch1:
                    print(colored("Place already taken.\n",'red'))
                    ch1=int (input("PLAYER X::"))
        A[int((ch1-1)/3)][(ch1-1)%3]=colored('X','blue')
        l.append(ch1)
        printttt()
        if A[0][0]==A[0][1]==A[0][2] or A[1][0]==A[1][1]==A[1][2] or A[2][0]==A[2][1]==A[2][2] or A[0][0]==A[1][0]==A[2][0] or A[0][1]==A[1][1]==A[2][1] or A[0][2]==A[1][2]==A[2][2] or A[0][0]==A[1][1]==A[2][2] or A[2][0]==A[1][1]==A[0][2]:
            print(colored('X WON !\n','green'))
            break 
        
        if f==4:
            print(colored("IT'S A TIE !\n",'red')) 
            break
    
        if ch==1:
            print("COMPUTER O::")
            if ch3==1:
                res = [i for i in r if i not in l]
                x = random.choice(res)
                l.append(x)
                A[int((x-1)/3)][(x-1)%3]=colored('O','yellow')
            if ch3==2:
                h()
                if (A[0].count(colored('X','blue'))+A[1].count(colored('X','blue'))+A[2].count(colored('X','blue'))-A[0].count(colored('O','yellow'))-A[1].count(colored('O','yellow'))-A[2].count(colored('O','yellow')))==1 :
                    res = [i for i in r if i not in l]
                    z = random.choice(res)
                    l.append(z)
                    A[int((z-1)/3)][(z-1)%3]=colored('O','yellow')
            printttt()

        if ch==2:
            ch2=int (input("PLAYER O::"))
            for k in range (len(l)):
                for i in range (len(l)):
                    if l[i]==ch2:
                        print(colored("Place already taken.\n",'red'))
                        ch2=int (input("PLAYER O::"))
            A[int((ch2-1)/3)][(ch2-1)%3]=colored('O','yellow')
            l.append(ch2)
            printttt()
        
        if A[0][0]==A[0][1]==A[0][2] or A[1][0]==A[1][1]==A[1][2] or A[2][0]==A[2][1]==A[2][2] or A[0][0]==A[1][0]==A[2][0] or A[0][1]==A[1][1]==A[2][1] or A[0][2]==A[1][2]==A[2][2] or A[0][0]==A[1][1]==A[2][2] or A[2][0]==A[1][1]==A[0][2]:
            print(colored('O WON !\n','green'))
            break
    A=[[1,2,3],[4,5,6],[7,8,9]]
