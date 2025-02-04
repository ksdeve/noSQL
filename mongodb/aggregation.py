from db_connection import get_db_connection

# Obtenir la collection
collection = get_db_connection()

# Définir le pipeline d'agrégation
pipeline = [
    {"$group": {"_id": "$address.city", "total_balance": {"$sum": "$balance"}}},
    {"$sort": {"total_balance": -1}}  # Trie par total_balance en ordre décroissant
]

# Exécution de l'agrégation
results = collection.aggregate(pipeline)

# Affichage des résultats
for result in results:
    print(f"{result['_id']}: {result['total_balance']}")


pipeline = [
    {"$match": {"age": {"$gt": 25}}},
    {"$group": {"_id": "$age", "count": {"$sum": 1}}}
]

results = collection.aggregate(pipeline)

for result in results:
    print(result)