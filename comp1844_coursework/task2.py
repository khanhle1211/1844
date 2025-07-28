import networkx as nx
import matplotlib.pyplot as plt
import os
import matplotlib.patches as mpatches

G = nx.Graph()

# Define the lines with stations, distances, and colors
lines = {
    'Piccadilly Line': (
        ["Acton Town", "Hammersmith", "Earl's Court", "South Kensington", "Green Park", "King's Cross"],
        [1.5, 1.3, 1.7, 1.8, 2.1],
        'red'
    ),
    'Northern Line': (
        ["Paddington", "Baker Street", "Euston", "King's Cross", "Angel", "Old Street"],
        [1.1, 2.0, 1.9, 1.5, 2.3],
        'blue'
    ),
    'District Line': (
        ["Whitechapel", "Aldgate East", "South Kensington", "Sloane Square", "Victoria", "Vauxhall"],
        [1.4, 1.2, 1.7, 2.0, 1.6],
        'green'
    ),
    'Victoria Line': (
        ["Notting Hill", "High Street Kensington", "Green Park", "Vauxhall", "Stockwell", "Brixton"],
        [1.6, 1.5, 1.9, 2.1, 2.2],
        'purple'
    )
}

# ✅ Create locations and graphs
pos = {}
for idx, (line, (stations, distances, color)) in enumerate(lines.items()):
    for i, station in enumerate(stations):
        if station not in pos:
            pos[station] = (i, idx)
        G.add_node(station)
    for i in range(len(stations) - 1):
        G.add_edge(stations[i], stations[i + 1], weight=distances[i], color=color)

# ✅ Graphing
edges = G.edges()
colors = [G[u][v]['color'] for u, v in edges]
weights = nx.get_edge_attributes(G, 'weight')

# Draw node + edge
nx.draw_networkx_nodes(G, pos, node_color='lightyellow', node_size=1200)
nx.draw_networkx_edges(G, pos, edge_color=colors)

# Label edge
nx.draw_networkx_edge_labels(
    G, pos,
    edge_labels={(u, v): f"{d}km" for (u, v, d) in G.edges(data='weight')},
    font_size=7
)

# Label station 
adjusted_labels_pos = {k: (v[0], v[1] + 0.25) for k, v in pos.items()}
nx.draw_networkx_labels(G, adjusted_labels_pos, font_size=8)

# Create legend for lines
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

# ✅ Save and show the plot
os.makedirs("output_images", exist_ok=True)
plt.title("Task 2: Multi-Line London Transport Map")
plt.tight_layout()  # 👈 Để tránh bị cắt legend
plt.savefig("output_images/task2_output.png", bbox_inches='tight')
plt.show()
