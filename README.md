# 📖 Project Document

## 📐 Design Diagram

![Design Diagram](<images/Screenshot 2023-10-11 at 5.16.24 PM.png>)

## 🖥️ All Queries

### 🌐 Neo4j

- `MATCH (c:Compound)-[:CtD]->(d:Disease) WHERE d.id = $disease_id RETURN c.name` (Line 14)
- `MATCH (d:Disease)-[:DdG]->(g:Gene) WHERE d.id = $disease_id RETURN g.name` (Line 19)
- `MATCH (d:Disease)-[:DlA]->(a:Anatomy) WHERE d.id = $disease_id RETURN a.name` (Line 24)

### 📚 Hetionet

- `db.edges.find({"metaedge": "CtD", "target": disease_id})` (Line 18)
- `drugs.append(db.nodes.find_one({"id": id})["name"])` (Line 22)
- `db.edges.find({"source": disease_id, "metaedge": "DdG"})` (Line 24)
- `genes.append(db.nodes.find_one({"id": id})["name"])` (Line 28)
- `db.edges.find({"source": disease_id, "metaedge": "DlA"})` (Line 30)
- `locations.append(db.nodes.find_one({"id": id})["name"])` (Line 34)

## 🚀 Potential Improvements

### 🌐 Improvements for Neo4j

- Due to the way the data is organized there are a few potential improvements that could be made. The most obvious one is to add a relationship between the disease and the gene. This would allow us to find all the compounds that can treat a disease in a single query. This would also allow us to find all the genes that cause a disease in a single query.

- Another improvement would be to add a relationship between the disease and the anatomy. This would allow us to find all the compounds that can treat a disease in a single query. This would also allow us to find all the anatomies that cause a disease in a single query.

### 📚 Improvements for MongoDB

- One potential improvement would be to add a relationship between the disease and the gene. This would allow us to find all the compounds that can treat a disease in a single query. This would also allow us to find all the genes that cause a disease in a single query.

# Project Instructions

Build a database system to model HetioNet.

## Instructions

The database should at least answer the following questions in the quickest response time:

1. Given a disease id, what is its name, what are drug names that can treat or palliate this disease, what are gene names that cause this disease, and where does this disease occur? Obtain and output this information in a single query.

2. We assume that a compound can treat a disease if the compound up-regulates/down-regulates a gene, but the location down-regulates/up-regulates the gene in an opposite direction where the disease occurs. Find all compounds that can treat a new disease (i.e. this missing edges between compound and disease excluding existing drugs). Obtain and output all drugs in a single query.

## Requirements

- A Python command-line client interface for database creation and query

- Use at least two types of NoSQL stores

  - Document (MongoDB/PyMongo)
  - Graph (Neo4j/Py2neo)
  - Key-value
  - Column Family (Cassandra/DataStax Python Driver)

- Document

  - Design diagram
  - All queries
  - Potential improvements (i.e. how to speed up the query)

- All source code (sent by email)

- Two-person team

## Rubric

- Database design: 30%

  - Rationale: 15%
  - Implementation: 15%

- Query Functionality: 40%

  - Each query: 20%

- Client interface: 20%

  - GUI: 10 points

- Presentation: 10%

## Due Dates

Project: Thursday, October 12 at 11:59pm

Project Demo: Friday, October 13 at 10:00am - 11:30am

## Sample CSV Files for Testing

nodes.csv
id,name,kind
Anatomy::UBERON:0000002,uterine cervix,Anatomy
Disease::DOID:0050156,idiopathic pulmonary fibrosis,Disease
Gene::1,A1BG,Gene
Compound::DB00014,Goserelin,Compound
Compound::DB00035,Desmopressin,Compound

edges.csv
source,metaedge,target
Disease::DOID:0050156,DdG,Gene::1
Compound::DB00035,CuG,Gene::1
Compound::DB00035,CrC,Compound::DB00014
Compound::DB00014,CtD,Disease::DOID:0050156
Compound::DB00014,CuG,Gene::1
Disease::DOID:0050156,DlA,Anatomy::UBERON:0000002
Anatomy::UBERON:0000002,AdG,Gene::1

# Neo4j Queries for Testing

To delete all nodes and relationships:
MATCH (n)
DETACH DELETE n

To show all nodes and relationships:
MATCH (n)
RETURN n
