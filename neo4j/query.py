from connection import run_query


query_all_persons = "MATCH (p:Person) RETURN p.name, p.age"

results = run_query(query_all_persons)

for record in results:
    print(f"Name: {record['p.name']}, Age: {record['p.age']}")


# Find specific friend

def get_friends(name):
    query = f"MATCH (p:Person {{name: '{name}'}})-[:FRIEND]->(friend) RETURN friend.name, friend.age"
    results = run_query(query)
    return results

name = "Alice"
friends = get_friends(name)

print(f"Friends of {name}:")
for record in friends:
    print(f"Name: {record['friend.name']}, Age: {record['friend.age']}")