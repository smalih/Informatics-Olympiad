# DECODER RING - INCOMPLETE



# A = 65
# Z = 90


# So while n >ord(Z) - ord(current), we do n - ord(Z) - ord(current)
# then we do ord(current) plus (n)

# A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
# E J O T Y D K Q W




n = 5
inner = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
outer = []
current = -1

# while n > ord('Z') - ord(inner[current]):
#     n-= (ord('Z') - ord(inner[current]))
# current+=n-1
# print(inner[current])

counter = 0

# while n > ord('Z') - ord(inner[current]):
#     n-= (ord('Z') - ord(inner[current]))

for i in range(18):
    if (90-counter) - ord(inner[current]) < n:
        n -= (ord('Z') - ord(inner[current]))
        current = -1





    current+=n
    n = 5-counter

    print(inner[current])
    inner.pop(current)
    counter+=1


print(90 - ord(inner[0]))
