from connection import run_query

delete_nodes_and_relationships = "MATCH (n) DETACH DELETE n"
run_query(delete_nodes_and_relationships)