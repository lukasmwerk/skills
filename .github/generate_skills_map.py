import os
from graphviz import Digraph

def add_nodes_edges(dot, parent_name, path):
    for entry in os.listdir(path):
        entry_path = os.path.join(path, entry)
        if os.path.isdir(entry_path):
            dot.node(entry_path, entry)  # Create a node for the directory
            dot.edge(parent_name, entry_path)  # Create an edge from parent to child
            add_nodes_edges(dot, entry_path, entry_path)  # Recursively add child nodes

def generate_skills_map(repo_path):
    dot = Digraph(comment='Skills Map')

    for entry in os.listdir(repo_path):
        entry_path = os.path.join(repo_path, entry)
        if os.path.isdir(entry_path):
            dot.node(entry_path, entry)
            add_nodes_edges(dot, entry_path, entry_path)

    dot.render('skills_map', format='png', cleanup=True)
    print("Skills map saved as 'skills_map.png'.")

if __name__ == "__main__":
    repo_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    generate_skills_map(repo_path)
