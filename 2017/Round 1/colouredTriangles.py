# Coloured Triangles
# CODE
def colouredTriangles(firstRow):
  colours = ["R", "G", "B"]
  finalRow = []
  while len(firstRow)!= 1:
    finalRow = []
    for i in range(len(firstRow)-1):
      pair = [firstRow[i], firstRow[i+1]]
      if firstRow[i] == firstRow[i+1]:
        finalRow.append(firstRow[i])
      else:
        for colour in colours:
          if colour not in pair:
            finalRow.append(colour)
    firstRow = finalRow
  return firstRow[0]
startingRow = input()
print(colouredTriangles(startingRow))

# WRITTEN ANSWERS
'''
1b)

3 Rows:
RRRBBGGRG
GBGGRRBBB
BGBRGBRGR

1c) 1 Way because all different arrangements that lead to the same colour do not have the same
colour in the same position. eg for 1b) For the different arrangements, there is no same colour
in the first position, similarly in the second position and the third etc. Knowing just one colour in
each row means that for that specific position, any different arrangement will have a different colour
in that position therefore the answer is 1.

1d) Row size 6
'''
