import json
import difflib
from difflib import get_close_matches
data = json.load(open("data.json"))
def dict(q):
    m = get_close_matches(q,data.keys())[0]
    if q in data:
        print("The meaning of the word is:\n ")
        for item in data[q]:
            print(item)
    elif q.title() in data:
        print("The meaning of the word is:\n ")
        for item in data[q]:
            print(item)
    elif q.upper() in data:
        print("The meaning of the word is:\n ")
        for item in data[q.upper()]:
            print(item)
    elif m in data:
        answ =input("do you want to search this?y/n "+ m +" \n")
        if answ=="y":
            print("The meaning of the word is: \n")
            for item in data[m]:
                print(item)
        elif answ=="n":
            print("Sorry,The word doesn't exist in our dictionary.\n")
        else:
            print("Invalid response\n")
    else:
         print("The word doesn't exist.Please double check it\n")
while(1):
    ans = input("\nYou want to search something in dictionary?y/n \n")
    if ans=="y":
        query = input("give the word: \n")
        dict(query.lower())
    elif ans=="n":
        print("Thank you for using\n")
        break
    else:
        print("you gave invalid response\n")        

      
    



