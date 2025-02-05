# Principes des Requêtes Booléennes

Les requêtes booléennes permettent de combiner plusieurs conditions :

- must : Toutes les conditions doivent être satisfaites.

- filter : Conditions obligatoires mais non notées pour la pertinence (meilleure performance).


> Différences entre must et filter

>> - must : Toutes les conditions dans must doivent être satisfaites.
Les documents correspondants sont notés (scorés) en fonction de leur pertinence.


>> - filter : Les conditions doivent être satisfaites, mais sans scoring.



- should : Au moins une condition doit être satisfaite.

- must_not : Exclut certains documents.

Exemple avancé avec exclusion et filtres :

```
GET my-movie-index/_search
{
  "query": {
    "bool": {
      "must": [
        { "match": { "title": "Star Wars" }},
        { "match": { "director": "George Lucas" }}
      ]
    }
  }
}
```

# Opérations CRUD dans Elasticsearch

1. Créer un document (POST)
```
POST my-index/_doc
{
  "title": "Star Wars",
  "director": "George Lucas",
  "release_year": 1977
}
```

2. Lire un document (GET)
```
GET my-index/_doc/1
```

3. Mettre à jour un document (POST ou PUT)

```
POST my-index/_update/1
{
  "doc": {
    "title": "Star Wars: A New Hope"
  }
}
```

4. Supprimer un document (DELETE)
```
DELETE my-index/_doc/1
```


## Voici une liste de mots-clés fréquemment utilisés :

- match (textuel) : Recherche une correspondance partielle.

- term : Recherche une correspondance exacte.

- range (numérique) : Recherche des documents dans une plage de valeurs. (plage)

- exists : Vérifie si un champ existe.

- prefix : Recherche les termes commençant par une chaîne donnée.

- wildcard (%%) : Recherche avec des caractères génériques (*, ?).

- fuzzy : Recherche en tolérant des fautes de frappe.