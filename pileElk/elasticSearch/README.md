# Installation d'Elasticsearch avec Docker

Ce guide vous montre comment installer et configurer Elasticsearch en utilisant Docker. Vous n'avez pas besoin d'installer Elasticsearch manuellement sur votre machine ; Docker s'occupe de tout pour vous.

## Prérequis
- Docker doit être installé sur votre machine. Si vous ne l'avez pas encore installé, consultez la documentation officielle de Docker.
- jq (outil de ligne de commande pour traiter les données JSON) est nécessaire pour formater la sortie des commandes. Si vous ne l'avez pas encore installé, vous pouvez l'installer avec la commande suivante :
```
sudo apt-get install jq
```
## Installation d'Elasticsearch
1. Télécharger et exécuter l'image Docker Elasticsearch
Ouvrez une invite de commande et exécutez la commande suivante pour télécharger et démarrer Elasticsearch dans un conteneur Docker :
```
sudo docker run -p 9200:9200 -p 9300:9300 -d -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:7.14.0
```
Cette commande exécute un conteneur à partir de l'image Elasticsearch, avec les paramètres suivants :

- -p 9200:9200 : Expose le port 9200 de votre machine hôte vers le conteneur (pour accéder à Elasticsearch via HTTP).
- -p 9300:9300 : Expose le port 9300 de votre machine hôte vers le conteneur (pour permettre aux nœuds du cluster de communiquer).
- -d : Exécute le conteneur en mode détaché (en arrière-plan).
- -e "discovery.type=single-node" : Lance Elasticsearch en mode cluster à un seul nœud pour les tests.
docker.elastic.co/elasticsearch/elasticsearch:7.14.0 : Spécifie l'image et la version d'Elasticsearch.

2. Vérification de l'installation
Pour tester si Elasticsearch est correctement installé et en fonctionnement, vous pouvez vérifier l'état du cluster avec la commande suivante :
```
sudo curl 0.0.0.0:9200/_cluster/health | jq
```
Cette commande renvoie des informations sur l'état du cluster, comme le nombre de nœuds et l'état général du cluster, formatées par jq.

Pour obtenir plus d'informations sur les nœuds du cluster, utilisez :

```
sudo curl -X GET "http://0.0.0.0:9200/_cat/nodes?v"
```

3. Configuration d'un cluster multi-nœuds
Si vous souhaitez configurer un cluster Elasticsearch avec plusieurs nœuds, vous pouvez utiliser Docker Compose avec le fichier suivant docker-compose.yml :

```
version: '3'
services:
  es01:
    image: docker.elastic.co/elasticsearch/elasticsearch:7.15.0
    container_name: es01
    environment:
      - node.name=es01
      - node.roles=master
      - cluster.name=es-docker-cluster
      - bootstrap.memory_lock=true
      - "ES_JAVA_OPTS=-Xms512m -Xmx512m"
      - "discovery.seed_hosts=es02,es03"
      - "cluster.initial_master_nodes=es01,es02,es03"
    ulimits:
      memlock:
        soft: -1
        hard: -1
    volumes:
      - data01:/usr/share/elasticsearch/data
    ports:
      - 9200:9200
    networks:
      - elastic

  es02:
    image: docker.elastic.co/elasticsearch/elasticsearch:7.15.0
    container_name: es02
    environment:
      - node.name=es02
      - node.roles=data
      - cluster.name=es-docker-cluster
      - bootstrap.memory_lock=true
      - "ES_JAVA_OPTS=-Xms512m -Xmx512m"
      - "discovery.seed_hosts=es01,es03"
      - "cluster.initial_master_nodes=es01,es02,es03"
    ulimits:
      memlock:
        soft: -1
        hard: -1
    volumes:
      - data02:/usr/share/elasticsearch/data
    networks:
      - elastic

  es03:
    image: docker.elastic.co/elasticsearch/elasticsearch:7.15.0
    container_name: es03
    environment:
      - node.name=es03
      - node.roles=ingest
      - cluster.name=es-docker-cluster
      - bootstrap.memory_lock=true
      - "ES_JAVA_OPTS=-Xms512m -Xmx512m"
      - "discovery.seed_hosts=es01,es02"
      - "cluster.initial_master_nodes=es01,es02,es03"
    ulimits:
      memlock:
        soft: -1
        hard: -1
    volumes:
      - data03:/usr/share/elasticsearch/data
    networks:
      - elastic

volumes:
  data01:
    driver: local
  data02:
    driver: local
  data03:
    driver: local

networks:
  elastic:
    driver: bridge
```

4. Démarrer le cluster multi-nœuds
Dans le répertoire où se trouve votre fichier docker-compose.yml, exécutez la commande suivante pour démarrer le cluster Elasticsearch avec plusieurs nœuds :

```
sudo docker-compose up -d
```
Cela va démarrer les trois nœuds dans un cluster Elasticsearch.

## Modélisation des données dans Elasticsearch

1. Créer un Index avec des Paramètres
Nous allons créer un index appelé cities, avec des paramètres spécifiques pour définir 2 fragments (shards) et 

2. répliques (replicas) pour chaque fragment.

Exécutez la commande suivante pour créer l'index cities :

```
sudo curl -XPUT 'http://localhost:9200/cities' -H 'Content-Type: application/json' -d '
{
  "settings": {
    "number_of_shards": 2,
    "number_of_replicas": 2
  }
}'
```
- number_of_shards : Spécifie le nombre de fragments pour l'index. Chaque fragment est une portion des données distribuées sur différents nœuds.
- number_of_replicas : Définit le nombre de répliques (copies) pour chaque fragment pour assurer la tolérance aux pannes.


3. Vérifier les Paramètres de l'Index
Pour vérifier les paramètres de l'index cities que nous venons de créer, exécutez la commande suivante :

```
sudo curl -XGET 'http://localhost:9200/cities/_settings' | jq
```
Cette commande récupère les paramètres de l'index et utilise jq pour formater la sortie JSON de manière lisible.

4. Insérer un Document dans l'Index
Nous allons maintenant insérer un document dans l'index cities. Ce document contiendra des informations sur une ville (London) et son pays (England).

Exécutez la commande suivante pour ajouter le document :

```
sudo curl -XPOST 'http://localhost:9200/cities/_doc' -H 'Content-Type: application/json' -d '
{
  "city": "London",
  "country": "England"
}'
```
Cette commande insère un document avec deux champs : city et country.


5. Vérifier le Document Inséré
6. 
Une fois le document inséré, vous pouvez le vérifier en utilisant son identifiant unique (_id). Remplacez {1Xxx1ZQBeurP9PmK1nYl} par l'ID réel du document retourné lors de l'insertion.

Exécutez la commande suivante pour vérifier le contenu du document inséré :
```
sudo curl -XGET 'http://localhost:9200/cities/_doc/{1Xxx1ZQBeurP9PmK1nYl}'
```
Cette commande permet de récupérer le document à l'aide de son identifiant unique et affiche son contenu JSON.

### Exemple de Réponse
Après l'insertion et la récupération du document, vous devriez obtenir une réponse similaire à celle-ci :

```json
{
  "_index": "cities",
  "_type": "_doc",
  "_id": "1Xxx1ZQBeurP9PmK1nYl",
  "_version": 1,
  "_seq_no": 1,
  "_primary_term": 1,
  "found": true,
  "_source": {
    "city": "London",
    "country": "England"
  }
}
```
_source : Ce champ contient les données du document, ici "city": "London" et "country": "England".
found: true : Indique que le document a bien été trouvé dans l'index.