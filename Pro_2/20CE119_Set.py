#ID & Name   : 20CE119 DIPKUMAR RUPAPARA
#Aim         : learn Set,Dictionary,Tuple
#link(Github):

#Set

#Que1:Write a python program to add members in a set and clear a set
s_1={'DIP','MAYANK','SHUBHAM'}
s_1.add('DHRUV')  #use add() function to add element
print(s_1)
s_1.clear()  #after use clear() function set is empty
print(s_1)

#Que2:Write a python program to remove item from a set if it's present in set
s_2={0,23,45,3,6}
s_2.remove(45)  #use remove() function to remove those element
print(s_2)  #after use print 0,3,6,23

#Que3:Write a python program to an intersection,Union,difference of set
s_3_1={0,1,2,4,5,6,8}          
s_3_2={1,2,3,5,7,9}  #(| for union.)(& for intersection.)(– for difference)
print("Union       : ",s_3_1|s_3_2)
print("Intersection: ",s_3_1&s_3_2)
print("Difference  : ",s_3_1-s_3_2)

#Que4:Write a python program to fine maximun and minimum vaiue in set
s_4={2,4,46,78}
print(max(s_4))  #use max() function to find maximum number
print(min(s_4))  #use min() function to find minimum number

#Que5:Write a python program to find the most common elements their counts from list,tuple,dictionary
def most_frequent(List):
    return max(set(List), key = List.count)
List = [2, 1, 2, 2, 1, 3]
print(most_frequent(List))