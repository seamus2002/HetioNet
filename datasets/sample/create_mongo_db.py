from pymongo import MongoClient
import csv

client = MongoClient("mongodb://localhost:27017/")

db = client["hetiosample"]

nodes = db["nodes"]
edges = db["edges"]

with open('sample_nodes.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        kind = row['kind']
        # Remove the prefix and store the ID
        id = row['id'].replace(f'{kind}::', '')
        document = {"id": id, "name": row['name'], "kind": kind}
        nodes.insert_one(document)
        print(document)

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
        document = {"source": source_id,
                    "metaedge": row['metaedge'], "target": target_id}
        edges.insert_one(document)
        print(document)

print("All done! No errors detected.")
