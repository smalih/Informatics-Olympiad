# PALINDROMIC NUMBERS

def palindrome(num):
  num = str(num)
  if num == "9" * len(num):
    return int(num)+2
  elif len(num) % 2 == 0:
    centre1 = num[int(len(num)/2)-1]
    centre2 = num[int(len(num)/2)]

    half = num[:int(len(num)/2)]
    new_num = half + half[::-1]
    while new_num <= num:
      centre1 = int(centre1)
      centre2 = int(centre2)
      centre1+=1
      centre2+=1
      new_num = half[:-1] + str(centre1) + str(centre2) + half[-2::-1]
    return new_num
    print(centre1, centre2)
  else:
    half = num[:int(len(num)/2)+1]
    centre = half[-1]
    new_num = half + half[-2::-1]
    while new_num <= num:
      centre = str(int(centre)+1)
      new_num = half[:-1] + centre + half[-2::-1]
  return new_num
print(palindrome(282))
