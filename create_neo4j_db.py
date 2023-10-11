from py2neo import Graph, Node, Relationship
import csv

# Connect to Neo4j
graph = Graph("bolt://localhost:7687", user="neo4j", password="fall2023")

# Create nodes and relationships
with open('sample_nodes.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        kind = row['kind']
        # Remove the prefix and store the ID
        id = row['id'].replace(f'{kind}::', '')
        node = Node(kind, id=id, name=row['name'])
        graph.create(node)
        print(node)

with open('sample_edges.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        source_kind, target_kind = row['source'].split(
            '::')[0], row['target'].split('::')[0]
        # Remove the prefixes and store the IDs
        source_id = row['source'].replace(
            f'{source_kind}::', '')
        target_id = row['target'].replace(
            f'{target_kind}::', '')
        source_node = graph.nodes.match(id=source_id).first()
        target_node = graph.nodes.match(id=target_id).first()
        relationship = Relationship(source_node, row['metaedge'], target_node)
        graph.create(relationship)
        print(relationship)

print("All done! No errors detected.")
