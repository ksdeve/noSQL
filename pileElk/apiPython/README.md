# Api Python

Ce projet utilise Elasticsearch pour indexer des documents et effectuer diverses analyses sur des textes, y compris la reconnaissance de smileys.

## Prérequis
- Python 3.x / PIP
- Elasticsearch installé et en cours d'exécution
- Librairie elasticsearch-py pour interagir avec Elasticsearch
```
pip3 install elasticsearch==7.13.4
```
- Installer le plugin qui contient ```icu_tokenizer``` :

```
sudo docker exec -it {id_container} bin/elasticsearch-plugin install analysis-icu
```

## Tests effectués
- Recherche de films avec conditions booléennes.
- Agrégations sur les ratings des films.
- Recherche de villes avec préfixes et expressions régulières.
- Analyse de texte avec un analyseur personnalisé pour reconnaître des smileys.

## Structure des Fichiers
- main.py : Le script principal qui exécute toutes les opérations (création d'index, insertion, requêtes, etc.).
- connection.py : Contient la fonction create_connection pour établir la connexion avec Elasticsearch.
- insert_documents.py : Contient les fonctions pour insérer des documents dans les indices.
- query.py : Contient des fonctions de recherche et d'extraction d'informations des résultats des requêtes.
- index_operations.py : Gère la création et la vérification des indices.

## Test

![Test1](pileElk/apiPython/Capture d'écran 2025-02-07 141130.png)
