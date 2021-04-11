
import csv
from collections import Counter
from re import search
import pandas as pd
from itertools import tee
import networkx as nx
from networkx.algorithms import community
from operator import itemgetter


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

# Remove the records where the from and to are the same
df.drop(df[df['from'] == df['to']].index, inplace=True)

G = nx.from_pandas_edgelist(df, "from", "to")

print(nx.info(G))

degree_dict = dict(G.degree(G.nodes()))
nx.set_node_attributes(G, degree_dict, 'degree')

sorted_degree = sorted(degree_dict.items(), key=itemgetter(1), reverse=True)

print("Top 20 nodes by degree:")
for d in sorted_degree[:20]:
    print(d)

betweenness_dict = nx.betweenness_centrality(G)  # Run betweenness centrality
eigenvector_dict = nx.eigenvector_centrality(G)  # Run eigenvector centrality

# Assign each to an attribute in your network
nx.set_node_attributes(G, betweenness_dict, 'betweenness')
nx.set_node_attributes(G, eigenvector_dict, 'eigenvector')

sorted_betweenness = sorted(
    betweenness_dict.items(), key=itemgetter(1), reverse=True)

print("Top 20 nodes by betweenness centrality:")
for b in sorted_betweenness[:20]:
    print(b)

# First get the top 20 nodes by betweenness as a list
top_betweenness = sorted_betweenness[:20]

# Then find and print their degree
for tb in top_betweenness:  # Loop through top_betweenness
    # Use degree_dict to access a node's degree, see footnote 2
    degree = degree_dict[tb[0]]
    print("Name:", tb[0], "| Betweenness Centrality:",
          tb[1], "| Degree:", degree)

components = nx.connected_components(G)
largest_component = max(components, key=len)

subgraph = G.subgraph(largest_component)
diameter = nx.diameter(subgraph)
print("Network diameter of largest component:", diameter)

communities = community.greedy_modularity_communities(G)

modularity_dict = {}  # Create a blank dictionary
# Loop through the list of communities, keeping track of the number for the community
for i, c in enumerate(communities):
    for name in c:  # Loop through each person in a community
        # Create an entry in the dictionary for the person, where the value is which group they belong to.
        modularity_dict[name] = i

# Now you can add modularity information like we did the other metrics
nx.set_node_attributes(G, modularity_dict, 'modularity')

# First get a list of just the nodes in that class
class0 = [n for n in G.nodes() if G.nodes[n]['modularity'] == 0]

# Then create a dictionary of the eigenvector centralities of those nodes
class0_eigenvector = {n: G.nodes[n]['eigenvector'] for n in class0}

# Then sort that dictionary and print the first 5 results
class0_sorted_by_eigenvector = sorted(
    class0_eigenvector.items(), key=itemgetter(1), reverse=True)

print("Modularity Class 0 Sorted by Eigenvector Centrality:")
for node in class0_sorted_by_eigenvector[:5]:
    print("Name:", node[0], "| Eigenvector Centrality:", node[1])

for i, c in enumerate(communities):  # Loop through the list of communities
    if len(c) > 2:  # Filter out modularity classes with 2 or fewer nodes
        # Print out the classes and their members
        print('Class '+str(i)+':', list(c))
