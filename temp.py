import matplotlib.pyplot as plt
import networkx as nx

# Create the network graph
G = nx.DiGraph()

# Wellington Site
G.add_node("Wellington Site", pos=(0, 3), node_type='site')
G.add_node("WLG Switch", pos=(-1, 2), node_type='device')
G.add_node("WLG PCs", pos=(-2, 1), node_type='pc')
G.add_node("WLG Printer", pos=(0, 1), node_type='printer')
G.add_node("WLG Server", pos=(1, 1), node_type='server')
G.add_node("WLG Router", pos=(0, 2), node_type='router')

# Auckland Site
G.add_node("Auckland Site", pos=(6, 3), node_type='site')
G.add_node("AKL Switch", pos=(5, 2), node_type='device')
G.add_node("AKL PCs", pos=(4, 1), node_type='pc')
G.add_node("AKL Printer", pos=(6, 1), node_type='printer')
G.add_node("AKL Server", pos=(7, 1), node_type='server')
G.add_node("AKL Router", pos=(6, 2), node_type='router')

# Internet / VPN Connection
G.add_node("Internet / VPN Tunnel", pos=(3, 2.5), node_type='vpn')

# Add edges (connections)
edges = [
    # Wellington
    ("Wellington Site", "WLG Router"),
    ("WLG Router", "WLG Switch"),
    ("WLG Switch", "WLG PCs"),
    ("WLG Switch", "WLG Printer"),
    ("WLG Switch", "WLG Server"),
    ("WLG Router", "Internet / VPN Tunnel"),

    # Auckland
    ("Auckland Site", "AKL Router"),
    ("AKL Router", "AKL Switch"),
    ("AKL Switch", "AKL PCs"),
    ("AKL Switch", "AKL Printer"),
    ("AKL Switch", "AKL Server"),
    ("AKL Router", "Internet / VPN Tunnel"),
]

G.add_edges_from(edges)

# Draw the network
pos = nx.get_node_attributes(G, 'pos')
node_colors = {
    'site': '#FFD700',
    'router': '#FF7F50',
    'device': '#87CEEB',
    'pc': '#90EE90',
    'printer': '#DDA0DD',
    'server': '#FFA07A',
    'vpn': '#D3D3D3'
}
node_types = nx.get_node_attributes(G, 'node_type')
colors = [node_colors.get(node_types[node], '#FFFFFF') for node in G.nodes()]

plt.figure(figsize=(12, 7))
nx.draw(G, pos, with_labels=True, node_color=colors, node_size=2000, font_size=9, font_weight='bold', arrows=True)
plt.title("Spring Computers - Network Extension Plan: Wellington ↔ Auckland", fontsize=14)
plt.axis('off')
plt.tight_layout()
plt.show()
