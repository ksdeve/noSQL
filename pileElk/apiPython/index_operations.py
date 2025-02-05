# index_operations.py
from connection import create_connection

def create_index(es):
    # Create an index
    es.indices.create(index="first_index", ignore=400)

def verify_index(es):
    # Verify if the index exists
    return es.indices.exists(index="first_index")

def get_mapping(es):
    # Retrieve the mapping of the "cities" index
    return es.indices.get_mapping(index='cities')
