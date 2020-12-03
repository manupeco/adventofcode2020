def get_line_array(line):
    return list(line)

def number_of_tree(horizontal_steps, vertical_steps):
    horizontal_index = horizontal_steps
    line_index = vertical_steps
    count = 0    
    while line_index < len(map_matrix):
        map_line = map_matrix[line_index]    
        if map_line[horizontal_index] == '#':
            count += 1
        line_index += vertical_steps
        horizontal_index += horizontal_steps
        if horizontal_index > len(map_line) - 1:
            horizontal_index = horizontal_index - len(map_line)
    return count

text_file = open("trees.txt", "r")
map_lines = text_file.read().split('\n')
map_matrix = list(map(get_line_array, map_lines))
# print(map_matrix)

result = number_of_tree(1, 1) * number_of_tree(3, 1) * number_of_tree(5, 1) * number_of_tree(7, 1) * number_of_tree(1, 2)

print('result: ', result)


    
    


