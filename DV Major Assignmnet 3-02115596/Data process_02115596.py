
                                                                                        #Kamalika Dasgupta - 02115596
import pandas as pd
import networkx as nx
import json
import matplotlib.pyplot as plt
import seaborn as sns


dd = pd.read_csv("https://raw.githubusercontent.com/umassdgithub/Fall-2023-DataViz/main/Week-8-ForceSimulator/data/data_scopus.csv")


dd = dd.dropna(subset=['Authors with affiliations'])


def get_first_author_country(author_affiliations):
    return author_affiliations.split(";")[0].split(",")[-1].strip()

dd['First_author_Country'] = dd['Authors with affiliations'].apply(get_first_author_country)


dd = dd.dropna(subset=['Author(s) ID'])

GR = nx.Graph()


def add_author_nodes(row):
    authors = row['Authors'].split(', ')
    author_ids = row['Author(s) ID'].split(';')
    affiliation_country = row['First_author_Country']

    for author_id, author_name in zip(author_ids, authors):
        GR.add_node(author_id, id=author_id, name=author_name, country=affiliation_country)

def add_coauthor_edges(row):
    author_ids = row['Author(s) ID'].split(";")
    for i, author_id in enumerate(author_ids):
        for coauthor_id in author_ids[i+1:]:
            GR.add_edge(author_id, coauthor_id)


dd.apply(add_author_nodes, axis=1)
dd.apply(add_coauthor_edges, axis=1)


nx.readwrite.json_graph.node_link_data(GR, open("author_network.json", 'w'))
nx.write_gml(GR, "network-part1.gml")








#Kamalika Dasgupta - 02115596