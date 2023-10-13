from py2neo import Graph
from pymongo import MongoClient

# Neo4j Configuration
graph = Graph("bolt://localhost:7687", user="neo4j", password="fall2023")

# MongoDB Configuration
client = MongoClient("mongodb://localhost:27017/")

db = client["hetionet"]

nodes = db["nodes"]
edges = db["edges"]


# Get disease info
def get_disease_info(disease_id):
    result = nodes.find_one({"id": disease_id})
    if not result:
        return None

    disease_name = result["name"]

    drug_ids = [edge["source"] for edge in edges.find(
        {"metaedge": "CtD", "target": disease_id})]
    drugs = []
    for id in drug_ids:
        drugs.append(nodes.find_one({"id": id})["name"])

    gene_ids = [edge["target"] for edge in edges.find(
        {"source": disease_id, "metaedge": {"$in": ["DdG", "DuG"]}})]
    genes = []
    for id in gene_ids:
        genes.append(nodes.find_one({"id": id})["name"])

    location_ids = [edge["target"] for edge in edges.find(
        {"source": disease_id, "metaedge": "DlA"})]
    locations = []
    for id in location_ids:
        locations.append(nodes.find_one({"id": id})["name"])

    return {
        "disease_name": disease_name,
        "drugs": drugs,
        "genes": genes,
        "locations": locations,
    }


# Find compounds to treat new disease
def find_compounds_to_treat_new_disease(new_disease_id):
    unknown_cures = graph.run(
        '''MATCH (d:Disease{{id:'{}'}})-[:DlA]->(a:Anatomy)-[:AuG|:AdG]->(g:Gene)<-[:CdG|:CuG]-(dc:Compound)-[:CrC*0..1]-(c:Compound)
            WHERE NOT (c)-->(d) AND ( (a)-[:AdG]->(g)<-[:CuG]-(dc) OR (a)-[:AuG]->(g)<-[:CdG]-(dc))
            RETURN collect(Distinct c.name)'''.format(new_disease_id))

    return unknown_cures


def main():
    while True:
        print("Choose an action:")
        print("1. Get Disease Information")
        print("2. Find Compounds to Treat New Disease")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            disease_id = input("Enter Disease ID: ")
            result = get_disease_info(disease_id)
            if result:
                print(f"\nDisease Name: {result['disease_name']} \n")
                print(f"Drugs that can cure/palliate: {result['drugs']} \n")
                print(f"Genes that cause this disease: {result['genes']} \n")
                print(f"Disease Locations: {result['locations']} \n")
            else:
                print("Disease not found.")

        elif choice == "2":
            new_disease_id = input("Enter Disease ID: ")
            compounds = find_compounds_to_treat_new_disease(new_disease_id)
            if compounds:
                print("Potential compounds to treat the disease: ")
                for compound in compounds:
                    print(compound)
            else:
                print("No compounds found for the new disease.")
            print("\n")

        elif choice == "3":
            break

        else:
            print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main()
