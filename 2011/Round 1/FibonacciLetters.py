con = input()

first, second, n = con.split(" ")
n = int(n)

sequence = [first, second]

def getNext(previous, current):
  s1, s2 = ord(previous)-64, ord(current)-64
  sum = s1+s2
  if sum > 26:
    sum -=26
    return chr(sum+64)
  return chr(sum+64)

if n == 1:
  print(first)
elif n == 2:
  print(second)
else:
  previous, current = first, second
  while len(sequence) < n:
    next = getNext(previous, current)
    sequence.append(next)
    previous = current
    current = next
  print(next)



'''
1B) Letter 'R'


'''
