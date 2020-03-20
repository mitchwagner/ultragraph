# UltraGraph 

UltraGraph is a Python 3 library motivated by the principle of designing
an algorithm and data structure suite for graphs that adheres closely to
the mathematical treatment of these objects. 

## FAQ

### Why don't I just use NetworkX?
You absolutely should not rule out using NetworkX! NetworkX is an amazing
library- I've never encountered another that seems like such a natural
extension of a language. It makes by far the best use of light-weight
class-based design I've ever encountered. It's a well-developed,
thoroughly-tested, and mature library crafted by some fantastic folks. What
more could you want?

Well, that's the question this library is designed to answer. I really enjoy
graph theory, and I wanted to create a personal suite of my own. Yet, if I'm
going to spend that kind of time, I don't want to clone NetworkX- my library
should be differentiated somehow. In this case, that differentiation comes from
a special focus on avoiding class-based design in favor of a more functional
style that matches natural mathematical definitions and specifications of
graphs and the algorithms that operate over them.

Consider, for example, Dijsktra's algorithm:

```python
import networkx as nx

a = nx.Graph()
# ... populate the graph ...
a.shortest_path(source, target, weight_attr)
```

This is a perfectly fine, useful syntax for operating on graphs, but it
gets somewhat away from the more natural, mathematical definition:

```python
'''
Given the arguments
    
V: a set of nodes,
E: a set of edges,
c: a function mapping each edge in G to a non-negative real value,
s: a node in V,

this function performs Dijkstra's shortest-path algorithm over the
graph G = (V, E), starting from s. It returns a mapping
(dictionary) that relates each node v in V to the length of the
shortest path from s to v in G.
'''

def dijkstra(V, E, c, s):
    ...
```

This library is designed to provide precisely that alternative
conceptualization. Python is a natural langauge for this, as first-class
functions allow us to pass, for example, the function *c* as an argument into
the interface defined by this more formal specification.

In summary, UltraGraph is not so much an exercise in avoiding class-based
design, nor recreating the wheel for the sake of it, as in promoting a
mathematical mindset with respect to programming itself.
