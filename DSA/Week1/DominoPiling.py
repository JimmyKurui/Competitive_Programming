## @author: JimmyKurui
## date: 27/10/2022
##
## CodeForces: Domino Piling

import numpy as np

def DominoFiller(M,N):
#    1. Create board of zero fills
    board = np.zeros((M,N))
##    2. Create cache for dominoes placed
    filled=0;
##    3. Domino to fill board
    domino = np.reshape([1,1], (2,1))
##     4. Place domino and save to filled
##    5. Check for empty strip for each placing
    i=j=0; m=0; 
    while m < M:
        n=j=0;
        if M-m == 1:
            #Horizontal placing for single row
            while n < N:
                domino = np.reshape([3,3],(1,2))
                board[m:m+1,j:j+2] = domino
                filled= filled+1
                print(board)
                j=j+2; n=n+2;
                if N-n == 1:
                    # Ignoring single cell
                    break
            break
        while n < N:
            board[i:i+2,j:j+1] = domino
            filled= filled+1
            print(board)
            j=j+1; n=n+1;
        i=i+2; m=m+2;
        print(m)
    print('Maximum: %d' % filled)
    

# Test Cases         
DominoFiller(3,3)
DominoFiller(2,4)
DominoFiller(5,4)

