import math

def seat_id(line):
    row_label = line[0:7]
    seat_label = line[7:]
    return move_along_rows(row_label, 'B', 127) * 8 + move_along_rows(seat_label, 'R', 7)

def move_along_rows(row, low_letter, max_value):
    current_min = 0
    current_max = max_value
    for letter in row:        
        half = math.floor((current_max-current_min)/2)
        if letter == low_letter:
            current_min = current_max - half
        else:
            current_max = current_min + half        
    row = current_max
    return row

def find_missing(lst): 
    return [x for x in range(lst[0], lst[-1]+1)  
                               if x not in lst] 


# print("test: ", move_along_rows("FBFBBFF", "B", 127))
# print("test: ", move_along_rows("RLR", "R", 7))

text_file = open("boarding.txt", "r")
list = text_file.read().split('\n')
seat_id = [seat_id(line) for line in list]
print(max(seat_id))
seat_id.sort()
my_seat = print(find_missing(seat_id))