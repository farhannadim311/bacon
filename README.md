# Bacon Number Lab

This project implements a "Bacon Number" style graph traversal and pathfinding system for actors and movies.

## Features

- **Data Transformation**: Efficiently transforms raw actor-movie data into searchable graph structures.
- **Shortest Path**: Finds the shortest path between any two actors using Breadth-First Search (BFS).
- **Actors with Bacon Number**: Identifies all actors who are exactly $N$ steps away from Kevin Bacon (or any other actor).
- **Movie Path**: Reconstructs the specific movies that connect a sequence of actors in a shortest path.

## How to Run

### Prerequisite: Python 3
Ensure you have Python 3 installed on your system.

### Running Tests
To verify the implementation against the provided test suite, run:
```bash
python3 test.py
```
Or use `pytest`:
```bash
pytest test.py
```

## Structure
- `lab.py`: Core logic for graph transformations and pathfinding.
- `test.py`: Comprehensive test suite.
- `resources/`: Directory containing movie database files (`.pickle`).
