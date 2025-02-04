# Projet : Gestion de Films avec Neo4j

Ce projet permet de manipuler une base de données Neo4j pour créer des films, des acteurs et des relations entre eux, et inclut une fonctionnalité de recommandation de films.

## Prérequis

1. **Docker** doit être installé sur votre machine.
2. **Python** et **pip** doivent être installés pour gérer les dépendances.
3. **Neo4j** doit être installé dans votre environnement Python. ```pip install neo4j```

## Déploiement de Neo4j

Lancez une instance Neo4j avec Docker :

```
docker run --name my_neo4j -p7474:7474 -p7687:7687 -v ~/neo4j_data:/data -e NEO4J_AUTH=neo4j/password -d neo4j
```

Remarque : Remplacez password par votre mot de passe Neo4j.


