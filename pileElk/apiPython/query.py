# query.py
from connection import create_connection

def get_document(es, doc_id):
    # Retrieve a document by its ID
    try:
        res = es.get(index="cities", doc_type="places", id=doc_id)
        if res['found']:
            city_info = res['_source']  # Extract only the city and country
            return city_info
        else:
            return {"error": "Document not found"}
    except Exception as e:
        return {"error": str(e)}


def search_all_cities(es):
    # Use the search API with a match_all query to retrieve all documents in the "cities" index
    res = es.search(index="cities", body={"query": {"match_all": {}}})
    return res


def extract_city_info_from_search_results(res):
    # Extracting the necessary information from the search results
    cities_info = []
    for hit in res['hits']['hits']:
        city_data = {
            '_id': hit['_id'],
            '_index': hit['_index'],
            '_score': hit['_score'],
            '_source': hit['_source']  # Extract only the '_source' which contains 'city' and 'country'
        }
        cities_info.append(city_data)
    return cities_info


def search_movies(es):
    # Performing a search query with _source filtering
    res = es.search(index="movies", body={
        "_source": {
            "includes": [
                "*.title",  # Include all title fields
                "*.directors"  # Include all directors fields
            ],
            "excludes": [
                "*.actors*",  # Exclude all actors fields
                "*.genres"  # Exclude all genres fields
            ]
        },
        "query": {
            "match": {
                "fields.directors": "George"  # Searching for movies where directors contain "George"
            }
        }
    })
    return res

def extract_movie_info_from_search_results(res):
    # Extracting the movie titles and directors
    movies_info = []
    for hit in res['hits']['hits']:
        movie_data = {
            '_id': hit['_id'],
            '_index': hit['_index'],
            '_score': hit['_score'],
            '_source': hit['_source']  # Only including title and directors (due to _source filtering)
        }
        movies_info.append(movie_data)
    return movies_info


def search_movies_with_boolean_logic(es):
    # Search using boolean logic (must with two match conditions)
    res = es.search(index="movies", body={
        "query": {
            "bool": {
                "must": [
                    {
                        "match": {
                            "fields.directors": "George"
                        }
                    },
                    {
                        "match": {
                            "fields.title": "Star Wars"
                        }
                    }
                ]
            }
        }
    })
    return res
    
    
def extract_movie_info_from_boolean_search(res):
    # Extracting the necessary information from the search results
    movie_info = []
    for hit in res['hits']['hits']:
        movie_data = {
            '_id': hit['_id'],
            '_index': hit['_index'],
            '_score': hit['_score'],
            '_source': hit['_source']  # Extracting only the '_source' which contains 'title' and 'directors'
        }
        movie_info.append(movie_data)
    return movie_info

def search_movies_with_must_should_and_must_not(es):
    res = es.search(index="movies", body={
        "query": {
            "bool": {
                "must": [
                    { "match": { "fields.title": "Star Wars" }}
                ],
                "must_not": [
                    { "match": { "fields.directors": "George Miller" }}
                ],
                "should": [
                    { "match": { "fields.title": "Star" }},
                    { "match": { "fields.directors": "George Lucas" }}
                ]
            }
        }
    })
    return res
    
def extract_movie_info_from_must_should_and_must_not(res):
    movie_info = []
    for hit in res['hits']['hits']:
        movie_data = {
            '_id': hit['_id'],
            '_index': hit['_index'],
            '_score': hit['_score'],
            '_source': hit['_source']
        }
        movie_info.append(movie_data)
    return movie_info



def search_recipe_with_ingredients_and_time_filter(es):
    res = es.search(index="receipe", body={
        "query": {
            "bool": {
                "must": [
                    {
                        "match": {
                            "ingredients.name": "parmesan"
                        }
                    }
                ],
                "must_not": [
                    {
                        "match": {
                            "ingredients.name": "tuna"
                        }
                    }
                ],
                "filter": [
                    {
                        "range": {
                            "preparation_time_minutes": {
                                "lte": 15
                            }
                        }
                    }
                ]
            }
        }
    })
    return res
    
def extract_recipe_info(res):
    recipe_info = []
    for hit in res['hits']['hits']:
        recipe_data = {
            '_id': hit['_id'],
            '_index': hit['_index'],
            '_score': hit['_score'],
            '_source': hit['_source']
        }
        recipe_info.append(recipe_data)
    return recipe_info


