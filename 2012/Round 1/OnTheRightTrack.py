# 64 min 35s remaining

ffps = input()
direction = input()
start, next = direction[0], direction[1]
minPassed = int(input())
passed = 0
# > 20, -child
#< 12, +child
# ord A = 65
# so - 64
# dict1 = {1:[4,5,3], 2:[5, 6], 3:[6, 7], 4:[7,8], 5:[8, 9], 6:[8, 9], 7:[8, 9], 8:[8, 9], 9:[8, 9], 10:[8, 9], 11:[8, 9], 12:[8, 1], 21:[8, 7, 1], 22:[1, 7,6], 23:[6,5,1], 24:[1, 5, 4]}
lor = {}
dict1 = {"A": "EF", "B": "GH", "C": "IJ", "D": "KL", "E":"MN", "F":"NO", "G":"OP", "H":"PQ", "I":"QR", "J":"RS", "K":"ST", "L":"TM", "M":"LE", "N":"EF", "O":"FG", "P":"GH", "Q":"HI", "R":"IJ", "S":"JK", "T":"KL", "U":"MN", "V":"OP", "W":"QR", "X":"ST"}
for key in dict1.keys():
  lor[key] = "L"
# Whenever a ffp is passed: l-r or r-l


while passed < minPassed:
  start = next
  # if start in ffps:

  if start not in ffps:
    next = dict1[start][0 if lor[start] == "L" else 1]
    print(next)
    lor[next] = "L" if dict1[start].index(next) == 0 else "R"
  passed+=1

print(start, next)
