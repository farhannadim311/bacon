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
    if(len(transformed_data) == 0):
        return set()
    actor_graph = transformed_data[1]
    bacon = [{4724}]
    visited = {4724}
    i = 0
    if(num == 0):
        return bacon[-1]
    else:
        while(bacon):
            actor_set = bacon.pop(0)
            newSet = set()
            if(i == num):
                return actor_set
            for actor1 in actor_set:
                to_explore = actor_graph[actor1]
                for actor2 in to_explore:
                    if(actor2 not in visited):
                        newSet.add(actor2)
                        visited.add(actor2)
            if(len(newSet) == 0):
                return newSet
            bacon.append(newSet)
            i += 1
    return newSet


def bacon_path(transformed_data, actor_id):
    actor_graph = transformed_data[1]
    visited = {4724}
    path = [[4724,]]
    while(path):
        p = path.pop(0)
        if(p[-1] == actor_id):
            return p
        for actor in p:
            to_explore = actor_graph[actor]
            for actor2 in to_explore:
                exploring = []
                if(actor2 not in visited):
                    exploring.append(actor2)
                    visited.add(actor2)
                    new = p + exploring
                    path.append(new)
    return None


    



def actor_to_actor_path(transformed_data, actor_id_1, actor_id_2):
    actor_graph = transformed_data[1]
    visited = {actor_id_1}
    path = [[actor_id_1,]]
    while(path):
        p = path.pop(0)
        if(p[-1] == actor_id_2):
            return p
        for actor in p:
            to_explore = actor_graph[actor]
            for actor2 in to_explore:
                exploring = []
                if(actor2 not in visited):
                    exploring.append(actor2)
                    visited.add(actor2)
                    new = p + exploring
                    path.append(new)
    return None
    


def actor_path(transformed_data, actor_id_1, goal_test_function):
    actor_graph = transformed_data[1]
    visited = {actor_id_1}
    path = [[actor_id_1,]]
    while(path):
        p = path.pop(0)
        if(goal_test_function(p[-1])):
            return p
        for actor in p:
            to_explore = actor_graph[actor]
            for actor2 in to_explore:
                exploring = []
                if(actor2 not in visited):
                    exploring.append(actor2)
                    visited.add(actor2)
                    new = p + exploring
                    path.append(new)
    return None
    


def actors_connecting_films(transformed_data, film1, film2):
    raise NotImplementedError("Implement me!")


if __name__ == "__main__":
    with open("resources/small.pickle", 'rb') as f:
        smalldb = pickle.load(f)
    with open("resources/tiny.pickle", 'rb') as f:
        tinydb = pickle.load(f)
    with open("resources/large.pickle", 'rb') as f:
        largedb = pickle.load(f)
    with open('resources/names.pickle', 'rb') as f:
        names = pickle.load(f)
    t = transform_data(tinydb)
    actor_graph = t[1]
    print(actor_graph)
    #bacon_path(t, 2876669)
    pete_id = names["Pete Ludlow"]
    path = bacon_path(t, pete_id)
    for i in path:
        for key, val in names.items():
            if val == i:
                print(key)
    pass

    
    
    #transformed_data = transform_data(largedb)
    #s = actors_with_bacon_number(transformed_data, 6)
    #print(s)
    #for key,val in names.items():
        #if(val in s):
            #print(key)
    #for actor in actor_graph[4724]:
        #print(f"{actor_graph[actor]=}")
    #bacon = actors_with_bacon_number(transformed_data, 10**20)
    #print(bacon)
        
    #print(actor_graph[4724])
    #print(f"{actor_graph[1640] =}")
    #rint(f"{actor_graph[2876] =}")
    ##print(f"{actor_graph[1532] =}")
    #bacon = actors_with_bacon_number(transform, 2)
    #print(bacon)
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
    
