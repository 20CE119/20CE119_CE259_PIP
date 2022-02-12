#ID & Name : 20CE119 DIPKUMAR RUPAPARA
#Aim       : Mr. Anant is the manager at the INFINITE hotel. The hotel has an infinite amount of rooms.
#            One fine day, a finite number of tourists come to stay at the hotel.
#            The tourists consist of:
#            → A Captain.
#            → An unknown group of families consisting K of  members per group where  K ≠ 1.
#            The Captain was given a separate room, and the rest were given one room per group. 
#            Mr. Anant has an unordered list of randomly arranged room entries. The list consists 
#            of the room numbers for all of the tourists. The room numbers will appear K times per 
#            group except for the Captain's room. Mr. Anant needs you to help him find the Captain's 
#            room number. The total number of tourists or the total number of groups of families is not 
#            known to you. You only know the value of K and the room number list.

K = int(input())

Room_no = map(int, input().split())
Room_no = sorted(Room_no)

for i in range(len(Room_no)):
    if(i != len(Room_no)-1):
        if(Room_no[i]!=Room_no[i-1] and Room_no[i]!=Room_no[i+1]):
            print(Room_no[i])
            break;
    else:
        print(Room_no[i])