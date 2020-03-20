# UltraGraph 

UltraGraph is a Python 3 library motivated by the principle of designing
an algorithm and data structure suite for graphs that adheres closely to
the mathematical treatment of these objects. 

UltraGraph has no external dependencies!

## Structure

This project is broken up into two components: algorithms and data structures.
Put briefly, it takes the conventional view of data structures a static
collections of data associated with a common set of operations. However, the
scope of that set of operations is severely circumscribed here. For example, in
the case of a standard, undirected graph, we specify a graph *G*=(*V*, *E*),
where *V* is a set of nodes, and *E* is a set of edges, each edge *e*=(*u*,
*v*) consisting of a pair of nodes in *V*. This leaves us very little
interface, if any, to implement.

There exist, of course, numerous representations of a graph, with various
time/space tradeoffs. Conversion between these, and the implementation of the
most basic functions, are provided in the data structures folder. Yet, our goal
really should be to move away from the consideration of such low-level details
as representation in the first place. These are implementation concerns, and
best abstracted away as much as possible. The *end-user* should be thinking of
graphs in terms of mathematical definition like the one given above, not in
terms of its representation in memory.

In contrast, the bulk of this project will be implemented under the
'algorithms'. This is where one will find all of the interesting functions
defined over graphs.

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
