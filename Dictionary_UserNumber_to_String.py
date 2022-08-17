phonedict = {
    "1":"one",
    "2":"two",
    "3":"three",
    "4":"four",
    "5":"five",
    "6":"six",
    "7":"seven",
    "8":"eight",
    "9":"nine",
    "0":"zero"
}
Userinput = input("Enter some numbers: \n")
for character in Userinput:
    if character in phonedict:
        #slight redundancy to avoid printing white space like alteranate method
        print(phonedict.get(character))
"""       
Alternate method

phonedict = {
    "1":"one",
    "2":"two",
    "3":"three",
    "4":"four",
    "5":"five",
    "6":"six",
    "7":"seven",
    "8":"eight",
    "9":"nine",
    "0":"zero"
}
Userinput = input("Enter some numbers: \n")
for character in Userinput:
    print(phonedict.get(character,""),end=" ")
    """
  