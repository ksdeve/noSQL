# connection.py
import warnings
from elasticsearch import Elasticsearch

# Suppress warnings
warnings.filterwarnings('ignore')

# Connect to Elasticsearch
def create_connection():
    es = Elasticsearch('http://localhost:9200')
    return es
