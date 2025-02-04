import pymongo
from db_connection import get_db_connection

# Obtenir la collection
collection = get_db_connection()

# 1. Insertion (Create)
document = {"name": "John Doe", "email": "john.doe@example.com", "age": 30}
result = collection.insert_one(document)
print("Document inséré avec ID:", result.inserted_id)

# 2. Lecture (Read)
query = {"name": "John Doe"}
document = collection.find_one(query)
print("Document trouvé:", document)

# 3. Mise à jour (Update)
update = {"$set": {"age": 31}}
result = collection.update_one(query, update)
print("Documents modifiés:", result.modified_count)

# 4. Suppression (Delete)
result = collection.delete_one(query)
print("Documents supprimés:", result.deleted_count)


# 1. Insertion (Create)
documents = [
    {"name": "John Doe", "email": "john.doe@example.com", "age": 30},
    {"name": "Jane Smith", "email": "jane.smith@example.com", "age": 28},
    {"name": "Sam Brown", "email": "sam.brown@example.com", "age": 35},
    {"name": "Alice Johnson", "email": "alice.johnson@example.com", "age": 22}
]
# Insertion de plusieurs documents
collection.insert_many(documents)

# 5. Exemple de requête avancée avec opérateurs logiques
query = {
    "$and": [
        {"age": {"$gt": 25}},  # L'âge doit être supérieur à 25
        {"email": {"$regex": "@example\.com$"}}  # L'email doit se terminer par "@example.com"
    ]
}
documents = collection.find(query)

print("Documents trouvés avec condition $and:")
for doc in documents:
    print(doc)

# 6. Projection (Limiter les champs retournés)
query = {"age": {"$gt": 25}}
projection = {"_id": 0, "name": 1, "email": 1}  # On ne retourne que 'name' et 'email', pas '_id'
documents = collection.find(query, projection)

print("Documents avec projection:")
for doc in documents:
    print(doc)

# 7. Tri des résultats (Sorting)
query = {"age": {"$gt": 25}}
documents = collection.find(query).sort("name", pymongo.ASCENDING)  # Tri par nom en ordre croissant

print("Documents triés par nom:")
for doc in documents:
    print(doc)
