inner = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
outer = []


# Change to user input
n = 5

# ord Z is 90
# ord A is 65

# you start counting from letter you're on so
# we start from -1 and count, then remove current letter and count again so

'''
start -1
count to 4
return 4
count to 9
return 9
count to 14
return 14
count to 19
return 19
count to 24
return 24

now, if we count to 29, it's greater than list range so we do n-difference

eg (ord x =88, ord z = 90, we do 90 - 8 == 2)
then do n-2
start counting from -1, add n-2

problem is everytime we return a value, we then need to remove it but count from the value after that if you know what I mean?

Lets say we have A B C D E F G H I

n = 3
we count to C
return to C
pop C
so A B D E F G H I
and we're starting on D
distance has decreased by 1 so we add n-1 rather than n
land on F
count to I so counter has gone back to 3

what has happened here is that the absolute index of F has changed but the index of F relative to D has not

so we can do if ord(next item) > ord (current), we do add n-1, else we add n
then we reset n = n-1 and we risne and repeat

count F
return F
count to I
return I

'''

current = -1

for i in range(25):

    if (ord('Z') - (current+65)) < n:
        n -= (ord('Z') - (current+65))
        current = -1
        current+=n

        while inner[current] == False:
            current+=1

    n = 5
    elif inner[current] == False:
        while inner[current] == False:

            current+=1
            n-= 1
        current+=n

    print(inner[current])
    inner[current] = False
