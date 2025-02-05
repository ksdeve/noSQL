import datetime
from connection import create_connection

def insert_documents(es, index_name, docs):
    for doc_id, doc in docs.items():
        try:
            response = es.index(index=index_name, id=doc_id, body=doc)
            print(f"Document {doc_id} inserted successfully into {index_name}")
        except Exception as e:
            print(f"Error inserting document {doc_id}: {e}")