
# Get deck
deck=[]
suits = ["C", "H", "S", "D"]
values = ["A", "2", "3", "4", "5", "6", "7","8","9","T","J","Q","K"]
piles = []
for i in range(4):
  for j in range(13):
    deck.append(f"{values[j]}{suits[i]}")
def shuffleDeck(a, b, c, d, e, f):
  shuffNums = [a, b, c, d, e, f]
  while True:
    try:
      for num in shuffNums:
        if num == 1:
          piles.append(deck.pop(0))
        else:
          for i in range(num-1):
            deck.append(deck.pop(0))
          piles.append(deck.pop(0))
    except IndexError:
      return piles
shuffleDeck(1, 3, 5, 7, 2, 4)

def match(card1, card2):
  for char in card1:
    if char in card2:
      return True
  return False

def strat1():
  if len(piles) == 1:
    return 1
  try:
    for i in range(-1, -len(piles), -1):
      if match(piles[i][-2:], piles[i-1][-2:]):
        piles[i-1] = f"{piles[i-1]}{piles.pop(i)}"
        return 0
      elif match(piles[i][-2:], piles[i-3][-2:]):
        piles[i-3] = f"{piles[i-3]}{piles.pop(i)}"
        return 0

  except IndexError:
    return 1
  return 1

x = 0
while x!=1:
  x = strat1()

print(piles)
