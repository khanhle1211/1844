import networkx as nx
import numpy as np


G = nx.Graph()

lines = {
    'Piccadilly Line': (
        ["Acton Town", "Hammersmith", "Earl's Court", "South Kensington", "Green Park", "King's Cross"],
        [1.5, 1.3, 1.7, 1.8, 2.1]
    ),
    'Northern Line': (
        ["Paddington", "Baker Street", "Euston", "King's Cross", "Angel", "Old Street"],
        [1.1, 2.0, 1.9, 1.5, 2.3]
    ),
    'District Line': (
        ["Whitechapel", "Aldgate East", "South Kensington", "Sloane Square", "Victoria", "Vauxhall"],
        [1.4, 1.2, 1.7, 2.0, 1.6]
    ),
    'Victoria Line': (
        ["Notting Hill", "High Street Kensington", "Green Park", "Vauxhall", "Stockwell", "Brixton"],
        [1.6, 1.5, 1.9, 2.1, 2.2]
    )
}

# Add edge with weight (weight is distance)
for line_name, (stations, distances) in lines.items():
    for i in range(len(stations) - 1):
        G.add_edge(stations[i], stations[i + 1], weight=distances[i])

# Analyze data from the edge
distances = [d['weight'] for u, v, d in G.edges(data=True)]
total = sum(distances)
avg = np.mean(distances)
std = np.std(distances)

# Print the results
print(f"Total network length: {total:.2f} km")
print(f"Average distance: {avg:.2f} km")
print(f"Standard deviation: {std:.2f} km")
