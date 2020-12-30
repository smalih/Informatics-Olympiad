
def calculateRomanNumeral(i, outputString=''):

    # Account for special cases
    if i == 0:
        print(outputString)
        return outputString
    if i == 1:
        outputString+='I'

        print (outputString)
        return outputString

    if i == 4:
        outputString+='IV'
        print (outputString)
        return outputString
    elif i == 9:
        outputString+='IX'
        print (outputString)
        return outputString
    elif i == 40:
        outputString+='XL'
        print (outputString)
        return outputString
    elif i == 90:
        outputString+='XC'
        print (outputString)
        return outputString
    elif i == 400:
        outputString+='CD'
        print (outputString)
        return outputString
    elif i == 900:
        outputString+='CM'
        print (outputString)
        return outputString

# Main part of function

    if i >= 1000:
        outputString+=("M")
        i -= 1000
        calculateRomanNumeral(i, outputString)

    elif i>= 500:
        outputString+=('D')
        i -= 500
        calculateRomanNumeral(i, outputString)

    elif i>= 100:
        outputString+=('C')
        i -= 100
        calculateRomanNumeral(i, outputString)

    elif i>= 50:
        outputString+=('L')
        i -= 50
        calculateRomanNumeral(i, outputString)

    elif i>= 10:
        outputString+=('X')
        i -= 10
        calculateRomanNumeral(i, outputString)

    elif i>= 5:
        outputString+=('V')
        i -= 5
        calculateRomanNumeral(i, outputString)

    elif i> 1:
        outputString+=('I')
        i -= 1
        calculateRomanNumeral(i, outputString)




def main(romanNumeralString, numberOfApplications):
    FinalString = romanNumeralString
    for i in range(numberOfApplications):
        for i in range(len(FinalString)):
            tempNumI = 0
            tempNumV = 0
            tempNumX = 0
            tempNumL = 0
            tempNumD = 0
            tempNumM = 0
            if romanNumeral[i] == 'I':
                tempNumI +=1
                continue
            else:
                returnString = (calculateRomanNumeral(tempNumI))
                FinalString+=returnString

            if romanNumeral[i] == 'I':
                tempNumI +=1
                continue
            else:
                returnString = (calculateRomanNumeral(tempNumI))
                FinalString+=returnString

            if romanNumeral[i] == 'V':
                tempNumV +=1
                continue
            else:
                returnString = (calculateRomanNumeral(tempNumV))
                FinalString+=returnString


            if romanNumeral[i] == 'X':
                tempNumI +=1
                continue
            else:
                returnString = (calculateRomanNumeral(tempNumX))
                FinalString+=returnString


            if romanNumeral[i] == 'L':
                tempNumL +=1
                continue
            else:
                returnString = (calculateRomanNumeral(tempNumL))
                FinalString+=returnString


            if romanNumeral[i] == 'C':
                tempNumC +=1
                continue
            else:
                returnString = (calculateRomanNumeral(tempNumC))
                FinalString+=returnString

            if romanNumeral[i] == 'D':
                tempNumD +=1
                continue
            else:
                returnString = (calculateRomanNumeral(tempNumD))
                FinalString+=returnString

            if romanNumeral[i] == 'M':
                tempNumM +=1
                continue
            else:
                returnString = (calculateRomanNumeral(tempNumM))
                FinalString+=returnString
        return FinalString







main(INSERT_STRING, NUMBER_OF_APPLICATIONS)
