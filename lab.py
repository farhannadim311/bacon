"""
6.101 Lab:
Bacon Number
"""

#!/usr/bin/env python3

import pickle
# import typing # optional import
# import pprint # optional import

# NO ADDITIONAL IMPORTS ALLOWED!




def transform_data(raw_data):
    film_graph = {}
    actor_graph = {}
    for a1,a2,f in raw_data:
        if(f in film_graph):
            film_graph[f].add(a1)
            film_graph[f].add(a2)
        else:
            film_graph[f] = set()
            film_graph[f].add(a1)
            film_graph[f].add(a2)
        if(a1 in actor_graph):
            actor_graph[a1].add(a2)
        if(a2 in actor_graph):
            actor_graph[a2].add(a1)
        
        if(a1 not in actor_graph):
            actor_graph[a1] = set()
        if(a2 not in actor_graph):
            actor_graph[a2] = set()
        actor_graph[a1].add(a2)
        actor_graph[a2].add(a1)
    for film, actors in film_graph.items():
        for actor in actors:
            actor_graph[actor].update(actors)
            actor_graph[actor].discard(actor)
    return (film_graph, actor_graph)



def acted_together(transformed_data, actor_id_1, actor_id_2):
    actor_graph = transformed_data[1]
    if(actor_id_1 == actor_id_2):
        return True
    if(actor_id_1 not in actor_graph or actor_id_2 not in actor_graph):
        return False 
    actor_set = actor_graph[actor_id_1]
    if(actor_id_2 in actor_set):
        return True
    return False


def actors_with_bacon_number(transformed_data, num):
    raise NotImplementedError("Implement me!")


def bacon_path(transformed_data, actor_id):
    raise NotImplementedError("Implement me!")


def actor_to_actor_path(transformed_data, actor_id_1, actor_id_2):
    raise NotImplementedError("Implement me!")


def actor_path(transformed_data, actor_id_1, goal_test_function):
    raise NotImplementedError("Implement me!")


def actors_connecting_films(transformed_data, film1, film2):
    raise NotImplementedError("Implement me!")


if __name__ == "__main__":
    with open("resources/tiny.pickle", 'rb') as f:
        tinydb = pickle.load(f)
    transform = transform_data(tinydb)
    actor_graph = transform[1]
    print(actor_graph[4724])
    print(f"{actor_graph[1640] =}")
    print(f"{actor_graph[2876] =}")
    print(f"{actor_graph[1532] =}")
   #with open('resources/small.pickle', 'rb') as f:
    #raw_data = pickle.load(f)

# 2. Load the names to find the IDs
    #with open('resources/names.pickle', 'rb') as f:
        #names = pickle.load(f)

# 3. Transform the data using your new function
    #db = transform_data(raw_data)


    #pierre_id = names['Pierre Johnsson']
    #jim_id = names['Jim Hughes']
    #chris_id = names['Christopher Showerman']
    #matt_id = names['Matt Dillon']


    #print(f"Pierre Johnsson and Jim Hughes: {acted_together(db, pierre_id, jim_id)}")
    #print(f"Christopher Showerman and Matt Dillon: {acted_together(db, chris_id, matt_id)}")
        
    

    # additional code here will be run only when lab.py is invoked directly
    # (not when imported from test.py), so this is a good place to put code
    # used, for example, to generate the results for the online questions.
    
