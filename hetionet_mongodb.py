from pymongo import MongoClient

# MongoDB Configuration
client = MongoClient("mongodb://localhost:27017/")

db = client["hetionet"]

nodes = db["nodes"]
edges = db["edges"]


# Get disease info
def get_disease_info(disease_id):
    return {
        "disease_name": "Not finished.",
        "drugs": "Not finished.",
        "genes": "Not finished.",
        "locations": "Not finished.",
    }

# Find compounds to treat new disease


def find_compounds_to_treat_new_disease(new_disease_id):
    return "Not finished."


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
            new_disease_id = input("Enter New Disease ID: ")
            compounds = find_compounds_to_treat_new_disease(new_disease_id)
            if compounds:
                print("Compounds to treat the new disease: ")
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
