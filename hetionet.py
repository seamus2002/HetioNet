from py2neo import Graph, Node, Relationship

# Neo4j Configuration
graph = Graph("bolt://localhost:7687", user="neo4j", password="fall2023")


# Get disease info
def get_disease_info(disease_id):
    disease = graph.nodes.match("Disease", id=disease_id).first()
    if not disease:
        return None

    drugs = graph.run(
        "MATCH (c:Compound)-[:CtD]->(d:Disease) WHERE d.id = $disease_id RETURN c.name",
        disease_id=disease_id
    ).data()

    genes = graph.run(
        "MATCH (d:Disease)-[:DdG]->(g:Gene) WHERE d.id = $disease_id RETURN g.name",
        disease_id=disease_id
    ).data()

    locations = graph.run(
        "MATCH (d:Disease)-[:DlA]->(a:Anatomy) WHERE d.id = $disease_id RETURN a.name",
        disease_id=disease_id
    ).data()

    return {
        "disease_name": disease["name"],
        "drugs": [record["c.name"] for record in drugs],
        "genes": [record["g.name"] for record in genes],
        "locations": [record["a.name"] for record in locations],
    }


# Find compounds to treat new disease
def find_compounds_to_treat_new_disease(new_disease_id):
    print("Under Development")


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
                print(result)
            else:
                print("Disease not found.")

        elif choice == "2":
            new_disease_id = input("Enter New Disease ID: ")
            compounds = find_compounds_to_treat_new_disease(new_disease_id)
            if compounds:
                print("Compounds to treat the new disease:")
                for compound in compounds:
                    print(compound)
            else:
                print("No compounds found for the new disease.")

        elif choice == "3":
            break

        else:
            print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main()
