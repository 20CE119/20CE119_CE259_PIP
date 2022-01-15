#ID & Name   : 20CE119 DIPKUMAR RUPAPARA
#Aim         : learn Set,Dictionary,Tuple
#link(Github):

#Dictionary

#Que1.Write a python script to check whether a given key is already exists in a dictionary
d1={'20CE119':'DIPKUMAR','20CE120':'Achchyut'}
key=input("Enter key to check it is already exists or not : ")
if key in d1:  #use if else to find key
    print("Key is already exist!")
else:
    print("Key is not present!")

#Que2.Write a python script to merge two dictionaries.
d2_1={'a':'a1','b':'b1'}
d2_2={'c':'c1','d':'d1'}
d2_2.update(d2_1)  #use update() function to merge two dictionaries
print(d2_2)

#Que3.Write a python script to sum all  the item in dictionary
d3={'x':1,'y':2,'z':3}
values=d3.values()  #use sum() to function to sum all element
total=sum(values)
print(total)

#Que4.Write a python program to add key in dictionary
d4={'p':10,'q':20}            
d4.update({'r':30})  #use update() to update both..
print(d4)

#Que5.Write a python program to concatenate following dictionaries to create a new dictionary
#all dictionary are mentioned below
d5_1={1:10,2:20}
d5_2={3:30,4:40}
d5_3={5:50,6:60}
d5_4={}
for i in [d5_1,d5_2,d5_3]:  #use for loop in update() function
    d5_4.update(i)
print(d5_4)