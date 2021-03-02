#This file will deal with importing triples from graph databases - Neo4J, GraphDB(Ontotext), BlazeGraph, DataStax and many more.. (You mention and it will be here)

"""Handling Neo4J:
A post request to run cypher query which in turn exports triples in RDF/XML format, readily imported into KGLAB.
Would require IP-Port and authentication data. (localhost by default)
Currently all graph triples from Neo4J will be imported. Subgraphs will be accessible in near future using cyper."""

"""Handling GraphDB (Ontotext):
A get request to pass SPARQL query to GraphDB server(RDF4J) running at localhost. The generated data will be preprocessed and could then be imported by KGLAB framework.
"""

"""Handling Blazegraph:
A get request to pass SPARQL query to BlazeGraph server running. The generated data could then be imported by KGLAB framework.
"""
