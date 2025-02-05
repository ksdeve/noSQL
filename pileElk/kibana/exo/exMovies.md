# Exercice (Movies)

## 1. Récupérez tous les films intitulés « Star Wars » réalisés par « George Lucas » en utilisant une requête booléenne.

```json
GET movies/_search
{
  "query": {
    "bool": {
      "must": [
        {
          "match": {
            "fields.title": "Star Wars"
          }
        },
        {
          "match": {
            "fields.director": "George Lucas"
          }
        }
      ]
    }
  }
}
```

## 2. Récupérer tous les films dans lesquels "Harrison Ford" a joué.

```json
GET movies/_search
{
  "query": {
    "match": {
      "fields.actors": "Harrison Ford"
    }
  }
}
```

## 3. Récupérez tous les films dans lesquels "Harrison Ford" a joué et l'intrigue contient "Jones".

```json
GET movies/_search
{
  "query": {
    "bool": {
      "must": [
        {
          "match": {
            "fields.actors": "Harrison Ford"
          }
        },
        {
          "match": {
            "fields.plot": "Jones"
          }
        }
      ]
    }
  }
}
```

## 4. Récupérez tous les films dans lesquels "Harrison Ford" a joué, l'intrigue contient "Jones", mais pas le mot "Nazis".


```json
GET movies/_search
{
  "query": {
    "bool": {
      "must": [
        {
          "match": {
            "fields.actors": "Harrison Ford"
          }
        },
        {
          "match": {
            "fields.plot": "Jones"
          }
        }
      ],
      "must_not": [
        {
          "match": {
            "fields.plot": "Nazis"
          }
        }
      ]
    }
  }
}
```

## 5. Récupérez tous les films réalisés par « James Cameron » avec un rang inférieur à 1000 en utilisant une requête booléenne et de plage.

```json

GET movies/_search
{
  "query": {
    "bool": {
      "must": [
        {
          "match": {
            "fields.director": "James Cameron"
          }
        }
      ],
      "filter": [
        {
          "range": {
            "fields.rank": {
              "lt": 1000
            }
          }
        }
      ]
    }
  }
}
```


## 6. Récupérer tous les films réalisés par « James Cameron » avec un rang inférieur à 400. (Réponse exacte : 2)