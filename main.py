'''
   Made by RKAISSI Youssef
   Version : 1.0
   3/7/2019

'''

########################## Compare titles #################################

'''
   I made this code for comparing titles, wich is very useful in eCommerce, with this tool you can find the perfect keywords in a sepecific niche.
'''


import re
import string

def extract_words(s):
    return [re.sub('^[{0}]+|[{0}]+$'.format(string.punctuation), '', w) for w in s.split()]



print("How many titles you need to compare ?\n ")
nb=int(input())
L=[]
i=0
while(i<nb):
    str=input("Entre the title :\n")
    L.append(str)
    str=None
    i+=1
print(L)  
title=[]
for i in range(len(L)-1):
    compareThis=extract_words(L[i].lower())


    for j in range(i+1,len(L)):
        withThis=extract_words(L[j].lower())
        for m in range(len(compareThis)):
            for n in range(len(withThis)):
                if compareThis[m]==withThis[n]:
                    title.append(compareThis[m])

        withThis=[]


    compareThis=[]    

if title ==[]:
    print("Titles dont match")

else:
    print("The commun words are :\n")   
    print(title)                 





