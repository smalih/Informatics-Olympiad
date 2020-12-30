# BLOCK PALINDROMES

'''
Start from both ends
If first last letter are same, that's one combo
if first two and last are same, another combo
if first three and last 3 are same, another combo
etc..., the remianing letters are just grouped

eg lets say first three and last three are not same,
then we know that we know that secondandthird and thridtolastandsecondtolast are not the same

'''

def checkIndividual(word, i, num_ways):
    if i < int(len(word)/2):
        if word[i] == word[-i-1]:
            num_ways+=1
            i+=1
            num_ways = checkIndividual(word, i, num_ways)

    return num_ways

def checkMultiple(word, i, num_ways):
    if i <= int(len(word)/2):
        if i == 0:
            pass
        elif word[:i] == word[-i:]:
            num_ways+=1
            num_ways = checkIndividual(word, i, num_ways)
            i+=1
            num_ways = checkMultiple(word, i, num_ways)
    return num_ways

word = input()

num_ways = 0

# If first and last are same, we can check if first two and last are same, and if second andsecond to last are same
i = 0
num_ways = 0

num_ways = checkIndividual(word, i, num_ways)
i = 2
num_ways = checkMultiple(word, i, num_ways)


print(num_ways)

print("\n\nSolomon Malih - Colchester Royal Grammar School")

'''
Answer to 1b)

(A)(ABCBA)(A)
(A)(A)(BCB)(A)(A)
(A)(A)(B)(C)(B)(A)(A)
(AA)(BCB)(AA)
(AA)(B)(C)(B)(AA)
'''
