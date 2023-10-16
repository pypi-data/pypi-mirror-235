from QtGraphVisuals import quick_view
import networkx as nx

G1 = nx.DiGraph([(1,2), (2,3), (3,4)])
G2 = nx.DiGraph([(1,2), (2,3), (3,4), (2,4)])

quick_view({'G1': G1, 'G2': G2})
