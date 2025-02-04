from neo4j import GraphDatabase

uri = "bolt://localhost:7687"

user = "neo4j"
password = "password" # Penser à changer le mot de passe

driver = GraphDatabase.driver(uri, auth=(user, password))

def run_query(query):
    with driver.session() as session:
        result = session.run(query)
        return result.data()
