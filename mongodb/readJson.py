import json

from db_connection import get_db_connection

# Obtenir la collection
collection = get_db_connection()


# Charger les données JSON à partir du fichier
with open("assets/accounts.json", "r") as file:
    data = json.load(file)

# Insérer les données dans MongoDB
result = collection.insert_many(data)

# Afficher les IDs des documents insérés
print("Données insérées avec les IDs suivants:", result.inserted_ids)

# Créer un index sur 'address.city' pour améliorer les performances de recherche
index_name = "city_index"
collection.create_index([("address.city", 1)], name=index_name)
print(f"Index créé avec le nom: {index_name}")

# Récupérer tous les documents de la collection
documents = collection.find()

# Afficher les documents
for doc in documents:
    print(doc)
