# -*- coding: utf-8 -*-
"""
Spyder Editor

Filename: createEgonetsGraphs.py
Author: K Perez-Lopez
Date:   89/8/2014
Description: For Kaggle competition, Learning Social Circles in Networks
101 egonet datasets downloaded into one dedicated directory from
    http://www.kaggle.com/c/learning-social-circles/data
The filenames are <ego id>.egonet.
Each file is an egonet for one person: it lists the person's freinds (one per 
Line) and their friends (following on the line), thereby describing an 
undirected social network.

This program populates a separate graph (a social network) for each file.
It reads each file, extracts the ego id from the filename, creates a node
for ego, iterates through the lines of the file, creating nodes for ego's
friends and their friends, and creating edges between them.

The Python module, Netowrkx, is used to create the graphs and to write them
to individual graphML files. Graph visualization capability is pretty limited
in Networkx. I tried to use python-igraph, but it is not straightforward for 
Windows, so I am using NodeXL to visualize the networks unitl I install ubuntu.
NodeXL has a graphML converter which converted these files automatically from 
the directory, after which they were easily ingested into NodeXL. 

In progress: to capture the data as a pandas dataframe; which will be better
for further processing of the data.  
"""
import glob
import networkx as nx
import string
#import matplotlib.pyplot as plt #may be needed for nx.draw, or python-igraph
#import pandas as pd
#import numpy as np
 
path = \
  "C:\Users\kperez-lopez\Documents\GA_dataScience\ClassProject\KaggleSocialCircles\egonets"

# glob picks up the filenames in lexicographic order.
egonet_filenames = glob.glob(path + "\*")  

egos = []
#Split the full path name by the folder breaks, then take the last item (-1)
# and split that by the dot before the file extension, and take the first item
egos = [efn.split("\\")[-1].split(".")[0] for efn in egonet_filenames]
#Check: 
#print egos

for filename, ego in zip(egonet_filenames, egos):
    #print filename
    #print ego
    G_ego=nx.Graph()
    G_ego.add_node(ego, color = 'black', label = ego, shape = 'square')
    with open(filename, 'rU') as f:
        #print filename
        egos_friends_and_fofs = f.read()
        f_and_fofs_list = egos_friends_and_fofs.split("\n")   
        for entry in f_and_fofs_list:
            # last entry seems to be a blank; tried to use entry.find(":"), 
            # didn't work.  Try it again at some point
            if entry.count(":") > 0:
                friend_node = entry.split(":")[0]
                G_ego.add_node(friend_node, color = 'green', label = friend_node)
                G_ego.add_edge(ego, friend_node, color = 'gray')
                fofs = entry.split(":")[1]
                fofs = string.lstrip(fofs)
                fofs = fofs.split(" ")
                for fof in fofs:
                    if fof <> "":
                        G_ego.add_node(fof)
                        G_ego.add_edge(friend_node, fof)
                        
    outfilename = "all_fofs_ego_"+ ego + ".graphml"
    nx.write_graphml(G_ego, outfilename)                      
#    nx.draw(G_ego)
    G_ego.clear()  