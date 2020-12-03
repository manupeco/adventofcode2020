text_file = open("pwd.txt", "r")
list = text_file.read().split('\n')
valid = 0
valid2 = 0
for line in list:
    lineparts = line.split(':')
    specs = lineparts[0]
    pwd = lineparts[1].strip()
    specparts = specs.split(' ')
    letter = specparts[1]
    minandmax = specparts[0].split("-")
    min = int(minandmax[0])
    max = int(minandmax[1])    
    occurrences = pwd.count(letter)

    if min <= occurrences and occurrences <= max:
        valid += 1        

    if (pwd[min-1] == letter) ^ (pwd[max-1] == letter):
        valid2 += 1

print('valid-1: ', valid)
print('valid-2: ', valid2)
