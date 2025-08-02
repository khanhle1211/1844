import networkx as nx
import matplotlib.pyplot as plt
import os
import matplotlib.patches as mpatches

# Graph Initialization
G = nx.Graph()

# Train route data (stations, distances, colors)
lines = {
    'Piccadilly Line': (
        ["Acton Town", "Hammersmith", "Earl's Court", "South Kensington", "Green Park", "King's Cross"],
        [3.5, 2.1, 1.1, 2.2, 2.7],
        'red'
    ),
    'Northern Line': (
        ["Paddington", "Baker Street", "Euston", "King's Cross", "Angel", "Old Street"],
        [2.4, 2.1, 1.5, 1.2, 1.8],
        'blue'
    ),
    'District Line': (
        ["Whitechapel", "Aldgate East", "South Kensington", "Sloane Square", "Victoria", "Vauxhall"],
        [1.1, 5.1, 1.1, 1.3, 1.6],
        'green'
    ),
    'Victoria Line': (
        ["Notting Hill", "High Street Kensington", "Green Park", "Vauxhall", "Stockwell", "Brixton"],
        [2.0, 3.2, 2.1, 1.4, 1.3],
        'purple'
    )
}

# Dictionary to store the position and color of buttons
pos = {}
node_colors = {}

# Add buttons and edges
for idx, (line, (stations, distances, color)) in enumerate(lines.items()):
    for i, station in enumerate(stations):
        if station not in pos:
            pos[station] = (i, -idx)  # Gán vị trí duy nhất cho mỗi trạm
            node_colors[station] = color
        G.add_node(station)
    for i in range(len(stations) - 1):
        G.add_edge(stations[i], stations[i + 1], weight=distances[i], color=color)

# Check the connection of the graph
print("Graph is connected:", nx.is_connected(G))

# Draw edges with color
edges = G.edges()
edge_colors = [G[u][v]['color'] for u, v in edges]
nx.draw_networkx_edges(G, pos, edge_color=edge_colors)

# Draw buttons with color
node_color_list = [node_colors[node] for node in G.nodes()]
nx.draw_networkx_nodes(G, pos, node_color=node_color_list, node_size=1200)

# Draw distance labels on the edges
nx.draw_networkx_edge_labels(
    G, pos,
    edge_labels={(u, v): f"{d} km" for (u, v, d) in G.edges(data='weight')},
    font_size=7
)

# Draw station name
label_pos = {k: (v[0], v[1] + 0.25) for k, v in pos.items()}
nx.draw_networkx_labels(G, label_pos, font_size=8)

# Legend
legend_handles = [
    mpatches.Patch(color=color, label=line)
    for line, (_, _, color) in lines.items()
]
plt.legend(
    handles=legend_handles,
    title="Tube Lines",
    loc="center left",
    bbox_to_anchor=(1, 0.5),
    fontsize=8,
    title_fontsize=9
)

# Title and save image
plt.title("Task 2: Multi-Line London Transport Map (Real Distances)")
os.makedirs("output_images", exist_ok=True)
plt.tight_layout()
plt.savefig("output_images/task2_output.png", bbox_inches='tight')
plt.show()