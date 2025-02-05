# main.py
import datetime

from connection import create_connection
from index_operations import create_index, verify_index, get_mapping
from insert_documents import insert_documents

from query import search_recipe_with_ingredients_and_time_filter, extract_recipe_info, search_movies_with_must_should_and_must_not, extract_movie_info_from_must_should_and_must_not, search_all_cities, get_document, extract_city_info_from_search_results, search_movies, extract_movie_info_from_search_results, search_movies_with_boolean_logic, extract_movie_info_from_boolean_search

# Create the Elasticsearch connection
es = create_connection()


# Supprimer l'index existant, s'il y en a un
if es.indices.exists(index="travel"):
    es.indices.delete(index="travel", ignore=[400,404])

# Définir les paramètres et le mapping pour l'index "travel"
settings = {
    "settings": {
        "number_of_shards": 2,
        "number_of_replicas": 1
    },
    "mappings": {
        "properties": {
            "city": {
                "type": "text",
                "fields": {
                    "keyword": {
                        "type": "keyword",
                        "ignore_above": 256
                    }
                }
            },
            "country": {
                "type": "text",
                "fields": {
                    "keyword": {
                        "type": "keyword",
                        "ignore_above": 256
                    }
                }
            },
            "datetime": {
                "type": "date",
            }
        }
    }
}

# Créer l'index "travel"
es.indices.create(index="travel", ignore=400, body=settings)

# Step 1: Create the index and verify if it exists
create_index(es)
if verify_index(es):
    print("Index created and verified successfully.")
else:
    print("Index creation failed.")

# Step 2: Insert documents into the "cities" index
# Documents for the "cities" index
cities_docs = {
    1: {"city": "New Delhi", "country": "India"},
    2: {"city": "London", "country": "England"},
    3: {"city": "Los Angeles", "country": "USA"}
}

# Documents for the "travel" index (with datetime)
travel_docs = {
    1: {"city": "Bangalore", "country": "India", "datetime": datetime.datetime(2018, 1, 1, 10, 20, 0)},
    2: {"city": "London", "country": "England", "datetime": datetime.datetime(2018, 1, 2, 22, 30, 0)},
    3: {"city": "Los Angeles", "country": "USA", "datetime": datetime.datetime(2018, 4, 19, 18, 20, 0)}
}

# Insert documents into Elasticsearch
insert_documents(es, "cities", cities_docs)
insert_documents(es, "travel", travel_docs)



# Step 3: Query a document by ID (for example, ID 2)
result = get_document(es, 2)
if "error" in result:
    print("Error:", result["error"])
else:
    print("Document found:", result)

# Step 4: Get and display the mapping of the "cities" index
mapping = get_mapping(es)
print("\nMapping of the 'cities' index:")
print(mapping)

# Step 5: Search all cities (match_all query)
search_result = search_all_cities(es)
print(search_result)

# STEP 6 :


# Step 1: Search for cities
search_result_cities = es.search(index="cities", body={"query": {"match_all": {}}})
city_info = extract_city_info_from_search_results(search_result_cities)
print("City Info:", city_info)

# Step 2: Search for movies (directors matching "George")
search_result_movies = search_movies(es)
movie_info = extract_movie_info_from_search_results(search_result_movies)
print("Movie Info:", movie_info)



## STEP 7 :

search_result_movies = search_movies_with_boolean_logic(es)
movie_info = extract_movie_info_from_boolean_search(search_result_movies)

# Display the filtered results
print("Filtered Movie Info:", movie_info)


## STEP 8 :

# Step 1: Search for movies with must, must_not, and should conditions
search_result_movies = search_movies_with_must_should_and_must_not(es)

# Step 2: Extract and display relevant information
movie_info = extract_movie_info_from_must_should_and_must_not(search_result_movies)

# Display the extracted movie information
print("Filtered Movie Info:", movie_info)


## STEP 9 :

# Step 1: Search for recipes with parmesan, no tuna, and preparation time <= 15 minutes
search_result_recipes = search_recipe_with_ingredients_and_time_filter(es)

# Step 2: Extract and display relevant information
recipe_info = extract_recipe_info(search_result_recipes)

# Display the extracted recipe information
print("Filtered Recipe Info:", recipe_info)
    

## STEP 10 :

# Recherche avec préfixe :
es.search(index="cities", body={"query": {"prefix": { "city": "l" }}})

# Recherche avec expression régulière pour toutes les villes :
es.search(index="cities", body={"query": {"regexp": { "city": ".*" }}})

# Recherche avec expression régulière pour les villes commençant par "L" :
es.search(index="cities", body={"query": {"regexp": { "city": "l.*" }}})

# Recherche avec expression régulière pour les villes commençant par "L" et se terminant par "n" :
es.search(index="cities", body={"query": {"regexp": { "city": "l.*n" }}})



## STEP 11 :

# Agrégation simple par année (terms aggregation) :
res = es.search(index="movies", body={
    "aggs": {
        "nb_par_annee": {
            "terms": {
                "field": "fields.year"
            }
        }
    }
})

# Agrégation des moyennes des ratings :
res = es.search(index="movies", body={
    "aggs": {
        "note_moyenne": {
            "avg": {
                "field": "fields.rating"
            }
        }
    }
})

# Agrégation des ratings par année avec des statistiques (moyenne, min, max) :
res = es.search(index="movies", body={
    "aggs": {
        "group_year": {
            "terms": {
                "field": "fields.year"
            },
            "aggs": {
                "note_moyenne": {
                    "avg": {
                        "field": "fields.rating"
                    }
                },
                "note_min": {
                    "min": {
                        "field": "fields.rating"
                    }
                },
                "note_max": {
                    "max": {
                        "field": "fields.rating"
                    }
                }
            }
        }
    }
})





# Doc 4
doc4 = {4: {"city":"Sydney", "country":"Australia","datetime":datetime.datetime(2019,4,19,18,20,0)}}


insert_documents(es, "travel", doc4)


# Supprimer l'index s'il existe
if es.indices.exists(index="french"):
    es.indices.delete(index="french", ignore=[400, 404])

# Définir le mapping et les settings pour l'index avec un analyzer personnalisé
settings = {
    "settings": {
        "analysis": {
            "tokenizer": {
                "smiley_tokenizer": {
                    "type": "pattern",
                    "pattern": "(:\\)|:\\()"
                }
            },
            "filter": {
                "smiley_filter": {
                    "type": "pattern_replace",
                    "pattern": ":\\)",
                    "replacement": "_content_"
                },
                "triste_filter": {
                    "type": "pattern_replace",
                    "pattern": ":\\(",
                    "replacement": "_triste_"
                }
            },
            "analyzer": {
                "smiley_analyzer": {
                    "tokenizer": "smiley_tokenizer",
                    "filter": ["lowercase", "smiley_filter", "triste_filter"]
                }
            }
        }
    },
    "mappings": {
        "properties": {
            "text": {
                "type": "text",
                "analyzer": "smiley_analyzer"
            }
        }
    }
}

# Créer l'index avec ce mapping
es.indices.create(index="french", body=settings)

# Document avec des smileys
doc1 = {"text": "Je dois bosser pour mon QCM sinon je vais avoir une sale note :( ..."}
es.index(index="french", id=1, body=doc1)


# Requête pour analyser le texte dans le document inséré
response = es.search(index="french", body={
    "query": {
        "match": {
            "text": "Je dois bosser pour mon QCM sinon je vais avoir une sale note :( ..."
        }
    }
})

# Affichage de la réponse
print(response)
