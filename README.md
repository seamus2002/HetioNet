# 📖 HetioNet

## 📐 MongoDB Design Diagram

![MondoDB Diagram](images/MondoDB_Diagram.jpg)

## 📐 Neo4j Design Diagram

![Neo4j Diagram](images/Neo4j_Diagram.jpg)

## 🖥️ All Queries

### 📚 Query 1 (MongoDB)

- `disease_name = result["name"]` (Line 20)
- `edges.find({"metaedge": "CtD", "target": disease_id})` (Line 22)
- `nodes.find_one({"id": id})["name"]` (Line 26)
- `edges.find({"source": disease_id, "metaedge": {"$in": ["DdG", "DuG"]}})` (Line 28)
- `nodes.find_one({"id": id})["name"]` (Line 32)
- `edges.find({"source": disease_id, "metaedge": "DlA"})` (Line 34)
- `nodes.find_one({"id": id})["name"]` (Line 38)

### 🌐 Query 2 (Neo4j)

- `graph.run('''MATCH (d:Disease{{id:'{}'}})-[:DlA]->(a:Anatomy)-[:AuG|:AdG]->(g:Gene)<-[:CdG|:CuG]-(dc:Compound)-[:CrC*0..1]-(c:Compound)WHERE NOT (c)-->(d) AND ( (a)-[:AdG]->(g)<-[:CuG]-(dc) OR (a)-[:AuG]->(g)<-[:CdG]-(dc))RETURN collect(Distinct c.name)'''.format(new_disease_id))` (Line 50)

## 🚀 Potential Improvements

### 🌐 Query 1 (MongoDB)

- To have a collection for each kind of node. This would shorten the time it takes to search for all the compounds, genes, and anatomies that are related to the disease.

- Deploying the database on the cloud would allow for faster queries due to possiblity of sharding.

### 📚 Query 2 (Neo4j)

- To use "Read Replicas" to optimize for read-heavy workloads. However, since we deployed the database locally we were unable to utilize this feature.