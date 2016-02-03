#!/bin/python3

def get_knowledge_of_the_pair(person_1, person_2):
    knowledge = 0
    for ii in range(len(person_1)):
        knowledge += person_1[ii] | person_2[ii]
    return knowledge

N,M = [int(x) for x in input().strip().split(" ")]
persons = []
for ii in range(N):
    topic_t = [int(x) for x in list(input().strip())]
    persons.append(topic_t)

"""
To keep track of the maximum knowledge that can be stacked up
"""
max_knowledge = 0
"""
To keep track of how many pairs share that "knowledgability"
"""
num_pairs = 0
for ii in range(N):
    person_1 = persons[ii]
    for jj in range(ii, N):
        person_2 = persons[jj]
        next_knowledge = get_knowledge_of_the_pair(person_1, person_2)
        if next_knowledge > max_knowledge:
            max_knowledge = next_knowledge
            num_pairs = 1
        elif next_knowledge == max_knowledge:
            num_pairs += 1

print(max_knowledge)
print(num_pairs)
