def magicSquareFunc(n):
    #making the magic sqaure
    magicSquare = [[0 for x in range(n) ] for y in range(n)]
    for i in magicSquare:
        for j in i:
            print(j, end=" ")
        print()
    #setting the position for the first number n/2 will be pos 1.5 and 2,
    r = n / 2
    c = n - 1
    print(r)
    print (c)
    num = 1
    #repeat until magic square is filled with values 
    while num <= (n * n):
        #if row is negative and column =3 reset position to column 1 and row to 0, allows to move downwards and is in top right corner, resets column to middle
        if r == -1 and c == n:
            c = n - 2
            r = 0
        else:
        #wraps matric if numbers goes of the right side of 3x3 matrix
            if c == n:
                c = 0
        #wrap matrix  out of upper side
            if r < 0:
                r = n - 1
        #if there is a number there already, sets position back to column -2 and row + 1, resets column to middle
        if magicSquare[int(r)][int(c)]:
            c = c - 2
            r = r + 1
            continue
        else:
        #set [r][c] to num
            magicSquare[int(r)][int(c)] = num
            num = num + 1
        #allows to move up and right after placing num
        c = c + 1
        r = r - 1
    print("magic sqauure for n = " , n)
    
    for i in range(0, n):
        for j in range (0, n):
            print('%2d' % (magicSquare[i][j]), end=' ')
            if j == n - 1:
                print()
        

n = int(input("Enter odd int postive: "))

while(n % 2 == 0):
    n = int(input("Please enter the correct int, positive odd number: "))
print (n)
magicSquareFunc(n)