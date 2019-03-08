import random

d = {}
remGuess=6
inp=''
position=[]
picks=''

def replacer(s, newstring, index, nofail=False):
    if not nofail and index not in range(len(s)):
        raise ValueError("index outside given string")
    if index < 0: 
        return newstring + s
    if index > len(s):      
        return s + newstring
    return s[:index] + newstring + s[index + 1:]

with open("D:\\hangman.dat") as f:
    for line in f:
       (key, val) = line.split(':')
       val=val.replace("\n", "")
       d[key] = val

word,category=random.choice(list(d.items()))
print("Welcome to PYTHON Hangman...\ncategory:",category)

count=0
strn='_'*len(word)
while(remGuess!=0):
    
    if count==0:
       print("word:",'_'*len(word),"picks:","remaining:",remGuess)
       
    if(remGuess>0):
        inp = input("enter letter: ")
        if (inp in word and inp not in picks):
            picks+=inp
            position = [pos for pos, char in enumerate(word) if char == inp]
            for i in range(len(position)):
                strn=replacer(strn,inp,position[i])

            if (strn==word):
                print("YOU WIN!!")
                break
            print("word:",strn,"picks:",picks,"remaining:",remGuess)
            count=count+1
        else:
            remGuess-=1
            picks+=inp
            print("word:",strn,"picks:",picks,"remaining:",remGuess)
            count=count+1
