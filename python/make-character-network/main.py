
import csv
from collections import Counter
from re import search
import pandas as pd
from itertools import tee


def pairwise(iterable):
    '''Create pairwise tupples from input list
    s -> (s0,s1), (s1,s2), (s2, s3), ...'''
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


# Create empty list for characters
character_interactions = []

# Fill the character_interactions list with character names from scripts
with open('futurama_scripts.txt') as data:
    reader = csv.reader(data)
    for row in reader:
        if search(':', row[0]):
            character_interactions.append(row[0].split(':')[0])

# Change the list into a dictionary and count the occurrences
d = dict(Counter(character_interactions))
# 1x only characters
OneX_Dict = {key: val for key, val in d.items() if val == 1}
# Extra characters, for example 'Robot Guard # 2'
Extras_Dict = {key: val for key, val in d.items()
               if search("#", str(key))}

# Change the dictionaries back to lists to facilitate item removal
OneX_List = list(OneX_Dict.keys())
Extras_List = list(Extras_Dict.keys())

# Use the pairwise function to create tupples of characters
# Changes:
#   character_interaction = ['Fry','Leela','Bender',...]
#   into...
#   character_interaction_list = [('Fry','Leela'),('Leela','Bender'),('Bender',...)]
#
character_interaction_list = [i for i in pairwise(character_interactions)]

# Change list of tupples into dataframe to facilitate cleanup
df = pd.DataFrame.from_records(
    character_interaction_list, columns=['from', 'to'])

# Remove records from the dataframe that have 1x or Extra characters
df = df[~df['from'].isin(OneX_List)]
df = df[~df['to'].isin(OneX_List)]
df = df[~df['from'].isin(Extras_List)]
df = df[~df['to'].isin(Extras_List)]
