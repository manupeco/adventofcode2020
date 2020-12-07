import itertools
import functools

def intersection(lst1, lst2): 
    return list(set(lst1) & set(lst2)) 

def count_answers_for_group(group_answers):
    persons_answers = [group_answer.split('\n') for group_answer in group_answers ]        
    responses = [list(set(itertools.chain(*row))) for row in persons_answers]
    splitted_answers = [functools.reduce(lambda a,b: set(a).intersection(b), group_answer) for group_answer in persons_answers]
    print(splitted_answers)
    # responses_intersections = [set.intersection(row) for row in persons_answers]
    
    response_counters = [len(answers) for answers in responses]
    splitted_response_counters = [len(answers) for answers in splitted_answers]
    return sum(response_counters), sum(splitted_response_counters)


text_file = open("answers.txt", "r")
groups = text_file.read().split('\n\n')
print(count_answers_for_group(groups))