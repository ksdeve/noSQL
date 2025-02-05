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

