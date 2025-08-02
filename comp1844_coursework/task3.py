import networkx as nx
import numpy as np

G = nx.Graph()

# Same data as Task 2 (real distances)
lines = {
    'Piccadilly Line': (
        ["Acton Town", "Hammersmith", "Earl's Court", "South Kensington", "Green Park", "King's Cross"],
        [3.5, 2.1, 1.1, 2.2, 2.7]
    ),
    'Northern Line': (
        ["Paddington", "Baker Street", "Euston", "King's Cross", "Angel", "Old Street"],
        [2.4, 2.1, 1.5, 1.2, 1.8]
    ),
    'District Line': (
        ["Whitechapel", "Aldgate East", "South Kensington", "Sloane Square", "Victoria", "Vauxhall"],
        [1.1, 5.1, 1.1, 1.3, 1.6]
    ),
    'Victoria Line': (
        ["Notting Hill", "High Street Kensington", "Green Park", "Vauxhall", "Stockwell", "Brixton"],
        [2.0, 3.2, 2.1, 1.4, 1.3]
    )
}

# Add all edges to the graph
for stations, distances in lines.values():
    for i in range(len(stations) - 1):
        G.add_edge(stations[i], stations[i + 1], weight=distances[i])

# Extract distances
distances = [d['weight'] for _, _, d in G.edges(data=True)]

# Stats
total = sum(distances)
avg = np.mean(distances)
std = np.std(distances)

# Output
print("📊 Task 3: Network Analysis")
print(f"Total network length: {total:.2f} km")
print(f"Average segment length: {avg:.2f} km")
print(f"Standard deviation: {std:.2f} km")
