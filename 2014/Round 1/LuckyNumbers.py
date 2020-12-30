# LUCKY NUMBERS - FULL MARKS 100%

target = int(input())

def luckyNumbers():
  # Works
  luckyNum_array = [i for i in range(1, 10004, 2)]
  counter = 1
  while True:

    try:
      increment = luckyNum_array[counter]
      while True:
        try:

          luckyNum_array[increment-1] = False
          increment+= luckyNum_array[counter]
        except IndexError:
          luckyNum_array = [item for item in luckyNum_array if item!= False]
          counter+=1
          break
    except IndexError:
      break

  return luckyNum_array



def largestSmallest(target, luckyNum_array):
  target_largest = target_smallest = target
  while True:
    target_largest+=1
    if target_largest in luckyNum_array:
      break
  while True:
    target_smallest-=1
    if target_smallest in luckyNum_array:
      break
  return target_smallest, target_largest


luckyNum_array = luckyNumbers()
target_smallest, target_largest = largestSmallest(target, luckyNum_array)
print(target_smallest, target_largest)


print("\nSolomon Malih - Colchester Royal Grammar School")



'''
Q 1b

ANSWER: 23

CODE:
def luckyNumbers():
  # Works
  luckyNum_array = [i for i in range(1, 101, 2)]
  counter = 1
  while True:

    try:
      increment = luckyNum_array[counter]
      while True:
        try:

          luckyNum_array[increment-1] = False
          increment+= luckyNum_array[counter]
        except IndexError:
          luckyNum_array = [item for item in luckyNum_array if item!= False]
          counter+=1
          break
    except IndexError:
      break
  return luckyNum_array


luckyNum_array = luckyNumbers()
print(len(luckyNum_array))


'''


'''
Q 1c
print(2 * (1,000,000,000 - 1))
ANSWER: 1,999,999,998
'''
