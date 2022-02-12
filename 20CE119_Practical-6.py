#ID & Name   : 20CE119 DIPKUMAR RUPAPARA
#Aim         : You are given n words. Some words may repeat. For each word,
#              output its number of occurrences. The output order should 
#              correspond with the input order of appearance of the word.
#              See the sample input/output for clarification. 
#link(Github): https://github.com/20CE119/20CE119_CE259_PIP.git

import collections;

n = int(input()) #take no of input n
Dictionary = collections.OrderedDict() #make Dictionary which will help to track of count of no. for keys

for i in range(n):
    word = input() #take word as input
    if word in Dictionary:
        Dictionary[word] +=1 #if word is present in dictionary so incrementing count
    else:
        Dictionary[word] = 1 #if word isn't present in dictionary so taking it in

print(len(Dictionary)); #print no. of items in a dictionary
for k,v in Dictionary.items():
    print(v,end = " ");