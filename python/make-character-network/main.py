import csv
from collections import Counter
from re import search

character_interactions = []

with open('futurama_scripts.txt') as data:
    reader = csv.reader(data)
    for row in reader:
        if search(':', row[0]):
            character_interactions.append(row[0].split(':')[0])

d = dict(Counter(character_interactions))
temp_dict = {key: val for key, val in d.items() if val != 1}
character_dictionary = {key: val for key,
                        val in temp_dict.items() if not search("#", str(key))}


# print(len(character_interactions))
