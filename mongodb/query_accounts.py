from db_connection import get_db_connection

# Obtenir la collection
collection = get_db_connection()

# Rechercher tous les comptes d'une ville spécifique
city = "San Jose"
results = collection.find({"address.city": city})

print(f"Comptes situés à {city}:")
for result in results:
    print(result)

# Rechercher tous les comptes avec un solde supérieur à une valeur spécifique
min_balance = 30000
results = collection.find({"balance": {"$gt": min_balance}})

print(f"\nComptes avec un solde supérieur à {min_balance}:")
for result in results:
    print(result)
