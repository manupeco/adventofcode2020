test = '''light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.'''

def contant_of_bag(line):    
    bag_index = line.index('bag')
    name = line[0:bag_index]
    contain_index = line.index('contain')
    content = line[contain_index+8:]
    content = content.replace('bags', '')
    content = content.replace('bag', '')
    content = content.replace('.', '').strip()
    content = content.split(' , ')

    return name.strip(), content

def bag_containing_shiny(list_of_bag_to_found, luggages):    
    shiny_bag_found = 0
    for key,value in list(luggages.items()):
        content_joins = ' '.join(luggages[key]["content"])
        if any(shiny_bag in content_joins for shiny_bag in containing_shiny_gold):
            containing_shiny_gold.append(key)
            del luggages[key]
            shiny_bag_found += 1
    return shiny_bag_found, list_of_bag_to_found, luggages

def find_no_other_bags():    
    for key,value in list(luggages.items()):
        content_joins = ''.join(luggages[key]["content"])        
        if content_joins == "no other":
            count_bag[key] = {"quantity": 1}                


lines = test.split('\n')
#text_file = open("bags.txt", "r")
#lines = text_file.read().split('\n')
content_of_bags = []
luggages = {}
for line in lines:
    name, content = contant_of_bag(line)    
    luggages[name] = {"content": content}

containing_shiny_gold = ['shiny gold']
shiny_bag_found = -1
while shiny_bag_found != 0:
    shiny_bag_found, containing_shiny_gold, luggages = bag_containing_shiny(containing_shiny_gold, luggages)

print('result: ', len(containing_shiny_gold)-1) # -1 because the first cell allows to start looking for shiny gold
print(luggages)

#get the shiny bag
shiny_bag = luggages['shiny gold']
content = shiny_bag['content']

count_bag = {}
find_no_other = find_no_other_bags()
print('count_bag: ', count_bag)