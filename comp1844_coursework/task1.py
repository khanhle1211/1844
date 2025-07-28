import networkx as nx
import matplotlib.pyplot as plt
import os  # 👈 Libraries for working with directories
# Create a graph for the Piccadilly line with 6 stations
G = nx.Graph()

stations = ["Acton Town", "Hammersmith", "Earl's Court", "South Kensington", "Green Park", "King's Cross"]

distances = [1.5, 1.3, 1.7, 1.8, 2.1]  # đơn vị km

positions = {
    "Acton Town": (0, 0),
    "Hammersmith": (1, 1),
    "Earl's Court": (2, 2),
    "South Kensington": (3, 3),
    "Green Park": (4, 4),
    "King's Cross": (5, 5)
}

# Add nodes and edges to the graph
for station in stations:
    G.add_node(station, pos=positions[station])

for i in range(len(stations)-1):
    G.add_edge(stations[i], stations[i+1], weight=distances[i])

# Get node location
pos = nx.get_node_attributes(G, 'pos')

# Drawing nodes and edges
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=1500, font_size=9)
nx.draw_networkx_edge_labels(
    G,
    pos,
    edge_labels={(u, v): f"{d} km" for (u, v, d) in G.edges(data='weight')}
)

plt.title("Task 1: Piccadilly Line")

# 👇 Save image to folder
os.makedirs("output_images", exist_ok=True)
plt.savefig("output_images/task1_output.png")
plt.show()
