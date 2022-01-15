#ID & Name   : 20CE119 DIPKUMAR RUPAPARA
#Aim         : learn Set,Dictionary,Tuple
#link(Github):

#Tuple

#Que1:Write a python program to create tuple with diffrent data types
fruit_t=('mango','apple','chikoo',10,True)
print(fruit_t)  #print tuple as it's

#Que2:Write a python program to create tuple with numbers and print one item
num_t=(12,24,45,590)
print(num_t[2])  #print item at index 2

#Que3:Write a python program to add item in tupple
t=('A','B','C','D')
t=t+('E',)  #add item in below tuple and print final tuple
print(t)

#Que4:Write a python program to convert tuple to string
con_t=('D','I','P','K','U','M','A','R')         
N1="".join(con_t)  #use join() function to convert tuple to string
print(N1)

#Que5:Write a python program to find length of tuple
tuple=('2','0','C','E','1','1','9')
print(len(tuple))  #use len function to find length of tuple