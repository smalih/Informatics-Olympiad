num = int(input())

oddNums = []
primes = [2]
pf = []
def isPrime(oddNum):
  for i in range(3, int(oddNum/2),2):
    if oddNum % i == 0:
      return False
  return True


for i in range(3, int(num/2)+1, 2):
  if isPrime(i):
    primes.append(i)

for prime in primes:
  if num % prime == 0:
    pf.append(prime)

answer = 1

for num in pf:
  answer *= num
if answer == 1:
  print(num)
else:
  print(answer)


''' 1b

10, 20, 40, 50, 80, 100, 200, 400, 500, 800

1c 2 (19 times)
