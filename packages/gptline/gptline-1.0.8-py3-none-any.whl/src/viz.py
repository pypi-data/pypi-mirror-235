#!/usr/bin/env python3
import sqlite3

def generate_dot_file():
    # Connect to the SQLite database
    conn = sqlite3.connect('/tmp/experiment')
    cursor = conn.cursor()

    # Retrieve all nodes from the 'nodes' table
    cursor.execute('SELECT id, name FROM nodes')
    nodes = cursor.fetchall()

    # Retrieve all edges from the 'edges' table
    cursor.execute('SELECT source_node_id, target_node_id, relationship FROM edges')
    edges = cursor.fetchall()

    # Generate the .dot file content
    dot_content = 'digraph G {\n'

    # Add nodes to the .dot file
    for node in nodes:
        dot_content += f'    {node[0]} [label="{node[1]}"];\n'

    # Add edges to the .dot file
    for edge in edges:
        dot_content += f'    {edge[0]} -> {edge[1]} [label="{edge[2]}"];\n'

    dot_content += '}'

    # Write the .dot file
    with open('graph.dot', 'w') as dot_file:
        dot_file.write(dot_content)

    print('graph.dot file generated successfully.')

    # Close the database connection
    conn.close()

# Call the function to generate the .dot file
generate_dot_file()

