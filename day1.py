import itertools

text_file = open("numbers.txt", "r")
list = text_file.read().split('\n')
ylist = [int(i) for i in list]

print(ylist)
target = 2020 
for i in range(len(ylist)):
    sno = target-ylist[i]
    for j in range(i+1, len(ylist)):
        if ylist[j] == sno:
            print (ylist[i], ylist[j])
            print(ylist[i] * ylist[j])



def find3Numbers(A, arr_size, sum): 
    for i in range(0, arr_size-1): 
        # Find pair in subarray A[i + 1..n-1]  
        # with sum equal to sum - A[i] 
        s = set() 
        curr_sum = sum - A[i] 
        for j in range(i + 1, arr_size): 
            if (curr_sum - A[j]) in s: 
                print("Triplet is", A[i],  
                        ", ", A[j], ", ", curr_sum-A[j])                 
                return True
            s.add(A[j]) 
      
    return False
  
# Driver program to test above function  
A = ylist
sum = 2020
arr_size = len(A)  
find3Numbers(A, arr_size, sum)  