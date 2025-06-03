# bacon
This project explores the famous "Bacon Number" problem, identifying the degrees of separation between actors through shared movie appearances. Built using pure Python and a simple WSGI server, it also includes a frontend to visualize and interact with the actor/movie network.

## 🧠 Features

- Compute the **Bacon Number** for any actor using Kevin Bacon as the root.
- Return the **shortest actor-to-actor path** based on movie co-appearances.
- Return the **list of movies** that connect two actors.
- Discover **which actors connect two films**.
- Frontend interface (HTML/JS in `ui/`) for user interaction.

---

## ✅ Functions Implemented

- **`transform_data(raw_data)`**
  - Builds a bidirectional graph connecting actors and movies.
  
- **`movie_helper(raw_data)`**
  - Creates a helper dictionary mapping actors to the set of movies they appeared in.

- **`actors(transformed_data, actor)`**
  - Returns a list of actor IDs who have directly worked with the given actor.

- **`movies(transformed_data, actor)`**
  - Returns a list of movies the given actor appeared in.

- **`actors_in_movies(transformed_data, actor)`**
  - Returns the movie IDs (as integers) associated with an actor.

- **`acted_together(transformed_data, actor_id_1, actor_id_2)`**
  - Returns `True` if two actors have acted together, else `False`.

- **`actors_with_bacon_number(transformed_data, n)`**
  - Finds all actors with a Bacon number `n`.

- **`bacon_path(transformed_data, actor_id)`**
  - Returns the shortest actor path from Kevin Bacon to the given actor.

- **`actor_to_actor_path(transformed_data, actor_id_1, actor_id_2)`**
  - Finds the shortest path between two given actors.

- **`actor_path(transformed_data, actor_id_1, goal_test_function)`**
  - Generic BFS search utility to find a path between actors using a goal condition.

- **`movie_path(transformed_data, actor_id_1, actor_id_2, movie_data)`**
  - Given two actors and a movie helper dictionary, returns the movies that connect the actor path.

- **`actors_connecting_films(transformed_data, film1, film2)`**
  - Finds a path of actors connecting two movies, using actors as links between the films.

---

## 📘 Learning Outcomes

- 🧠 **Graph Data Structures**:
  - Modeled real-world actor-movie relationships as a graph.

- 🔄 **Bidirectional Search**:
  - Implemented BFS to efficiently find shortest paths between nodes (actors/movies).

- 🔍 **Custom Traversal Logic**:
  - Designed functions to explore data under constraints (e.g., `actors_connecting_films`).

- 🧪 **Testing & Debugging**:
  - Validated correctness using both provided and custom test cases.

- 🌐 **Full Stack Integration**:
  - Served backend logic using a WSGI server (`server.py`) and connected it to a frontend.

---
## Deployed on https://bacon-tdwt.onrender.com/
