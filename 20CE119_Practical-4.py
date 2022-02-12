#ID & Name : 20CE119 DIPKUMAR RUPAPARA
#Aim       : Given the participants' score sheet for your University Sports Day, 
#            you are required to find the runner-up score. You are given n scores.
#            Store them in a list and find the score of the runner-up.

if __name__ == '__main__':
    n = int(input())
    A = map(int, input().split())
    A = sorted(A,reverse=True)
    for i in range(len(A)):
        if A[i] == A[0]:
            continue
        else:
            print(A[i])  
            break