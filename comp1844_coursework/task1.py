import networkx as nx
import matplotlib.pyplot as plt
import os  # For working with folders

# Initialize the graph for the Piccadilly Line
G = nx.Graph()

# List of real stations on the Piccadilly Line
stations = [
    "Acton Town", "Hammersmith", "Earl's Court",
    "South Kensington", "Green Park", "King's Cross"
]

# Real-world distances between consecutive stations (in km)
# Data referenced from TfL and Google Maps
distances = [3.5, 2.1, 1.1, 2.2, 2.7]

# Predefined node positions for visualization purposes
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

for i in range(len(stations) - 1):
    G.add_edge(stations[i], stations[i + 1], weight=distances[i])

# Get node positions
pos = nx.get_node_attributes(G, 'pos')

# Draw nodes and edges
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=1500, font_size=9)

# Draw edge labels (distance)
nx.draw_networkx_edge_labels(
    G,
    pos,
    edge_labels={(u, v): f"{d} km" for (u, v, d) in G.edges(data='weight')},
    font_size=8
)

# Set chart title
plt.title("Task 1: Piccadilly Line (Real Distances)")

# Save image to folder
os.makedirs("output_images", exist_ok=True)
plt.savefig("output_images/task1_output.png")
plt.show()

# --- Analysis Section ---

# Calculate total, max and min distances
total_distance = sum(distances)
max_distance = max(distances)
min_distance = min(distances)

# Identify which segments are the longest and shortest
longest_segment = stations[distances.index(max_distance)] + " → " + stations[distances.index(max_distance)+1]
shortest_segment = stations[distances.index(min_distance)] + " → " + stations[distances.index(min_distance)+1]

# Display summary statistics
print(f"Total distance of the Piccadilly Line segment: {total_distance:.1f} km")
print(f"Longest segment: {longest_segment} = {max_distance} km")
print(f"Shortest segment: {shortest_segment} = {min_distance} km")
