numbers = '''35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576'''

def is_sum_of_two_numbers(numberToFind, startIndex, endIndex):
    index = startIndex
    while index < endIndex:
        result = numberToFind - numbers[index]        
        if result in numbers[startIndex:endIndex+1]:            
            return True
        else:
            index += 1
    return False

def subArraySum(arr, n, sum): 
      
    # Pick a starting  
    # point 
    for i in range(n): 
        curr_sum = arr[i] 
      
        # try all subarrays 
        # starting with 'i' 
        j = i + 1
        while j <= n: 
          
            if curr_sum == sum: 
                print ("Sum found between") 
                print("indexes % d and % d"%( i, j-1)) 
                  
                return i, j-1
                  
            if curr_sum > sum or j == n: 
                break
              
            curr_sum = curr_sum + arr[j] 
            j += 1
  
    print ("No subarray found") 
    return 0

#lines = numbers.split('\n')
text_file = open("xmas.txt", "r")
lines = text_file.read().split('\n')
numbers = [int(number) for number in lines]
low_limit = 0
high_limit = 24
number_index = 25
while number_index < len(numbers):
    if is_sum_of_two_numbers(numbers[number_index], low_limit, high_limit):
        low_limit +=1
        high_limit +=1
        number_index += 1                
    else:        
        break
if number_index < len(numbers):
    print('part one result: ', numbers[number_index])

n = len(numbers)
sum = numbers[number_index]

arrayLow, arrayHigh = subArraySum(numbers, n, sum) 
found_array = numbers[arrayLow:arrayHigh+1]
min = min(found_array)
max = max(found_array)
print ('part two result: ', (min+max))