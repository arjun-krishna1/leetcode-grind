My notes from [LeetCode Graph Series](https://leetcode.com/explore/learn/card/graph/?ref=landing)
# Introduction
- nodes connected by edges
- represent many real relationships

# Types of "graphs"
## Undirected Graphs
- The edges between any two vertices in an undirected graph don't have any direction
- This is a two-way relationship
- A two-way road, COVID-19 contact

## Directed Graphs
- Edges are directional
- This person liked your image (relationship is directional)

## Weighted graphs
- Each edge has an associated weights
- City map, each edge's weight is its distance; Nodes are objects, cost is transforming the object

# Information
- Vertex: nodes are also called vertices
- Edge: the connection between two vertices
- Path: the sequence of vertices to go through from one vertex to another
- Path Length: the number of edges in a path
- Cycle: a path where the starting point and endpoint are the same vertex
- Negative Weight Cycle: if the sum of the weights of all edges of a cycle is a negative value
- Connectivity: if there exists at least one path between two vertices, these two vertices are connected
- Degree of a vertex: applies to unweighted graphs. The number of edges connecting the vertex/
- In-Degree: the number of directional edges incident to the vertex. The number of directed edges pointing to a node.
- Out-degree: The number of directed edges pointing away from the node.

# Disjoint Set
- Given the vertices and edges between them
- How could we quickly check whether two vertices are connected
- We can use the Disjoint Set to quickly check if two nodes are connected
- This is also known as the union-find data structure
- The use of disjoint sets is to address the connectivity between the components of a network
- The network could be a computer network, a social network or etc
- e.g. we can use a disjoint set to determine if two people share a common ancestor
- parent node: the direct parent node of a vertex
- root node: a node without a parent node
