#ID & Name   : 20CE119 DIPKUMAR RUPAPARA
#Aim         : Lapindrome is defined as a string which when split in the middle, 
#              gives two halves having the same characters and same frequency of each character. 
#              If there are odd number of characters in the string, we ignore the middle character 
#              and check for lapindrome. For example gaga is a lapindrome, since the two halves ga 
#              and ga have the same characters with same frequency. Also, abccab, rotor and xyzxy 
#              are a few examples of lapindromes. Note that abbaab is NOT a lapindrome. The two 
#              halves contain the same characters but their frequencies do not match. Your task is 
#              simple. Given a string, you need to tell if it is a lapindrome. 
#link(Github): https://github.com/20CE119/20CE119_CE259_PIP.git

N = int(input()) #take no of input N
for i in range(N):
    S = input() #get input string S
    lenth = len(S) #find lenth of string S
    if lenth % 2 == 0: #separate string into two parts
        x, y = S[:lenth//2], S[lenth//2:]
    else:
        x, y = S[:lenth//2], S[lenth//2+1:]
    if sorted(x) == sorted(y):
        result = "YES" #if both parts are same then result is YES
    else:
        result = "NO" #if both parts are not same then result is NO
    print(result) #print result