from pymongo import MongoClient
import csv

client = MongoClient("mongodb://localhost:27017/")

db = client["hetionet"]

nodes = db["nodes"]
edges = db["edges"]


print("no errors")
