'''
THIS APPLICATION RETURNS DEFINITIO OF WORDS
'''

import json
from difflib import get_close_matches
data = json.load(open("076 data.json"))




#METHOD ONE USING IF ELSE
'''
def search(x):
    try :
        y=data[x]
        return y
    except KeyError :
        return 1
    
while(1):
    x=input("entert the word you want to search ?\n")
    z= search(x)
    if(z==1):
        a=search(x[1:]) #remove fisrt alphabet
        if(a==1):
            b=search(x[:-1])  #remove last alphabet
            if(b==1):
                print("sorry please double check the keyword")
            else:
                c=input("did u mean " + x[:-1]+"? Y/N\n")
                if(c=="y"):
                    print(b)
                else:
                    print("sorry please double check the keyword")
        else:
            c = input("did u mean " + x[1:] + "? Y/N\n")
            if(c=="y"):
                print(a)
            else:
                print("sorry please double check the keyword")

    else:
        print(z)
'''

# METHOD 2 USING DIFFLIB

def translate(w):
    if w in data:    #if key is in dictionary data
        return data[w]  #then return the corresponding value of the key
    #elif w.lower() in data:  #if lower case of the entered key is in dictionary
      #  return data[w.lower()] # this wont work because try entering paris, it will not display Paris but will find prism.hence go for title.

    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data :
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys())[0]) > 0 :#get the most matched key from data
        c = input("did u mean " + get_close_matches(w, data.keys())[0]  + "? Y/N\n")
        if(c=="y"):
            return data[get_close_matches(w, data.keys())[0]]
        else:
            return "the word is not found"
    else:
        return "the word is not found"

while(1):
    x=input("entert the word you want to search ?\n")
    z= translate(x)
    if z is list:
        for i in z :
            print(i +"\n")  # str + var possible , but list +var not possible
    else:
        print(z)