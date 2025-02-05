# Travailler avec l'interface Kibana
Dans cette section, nous allons travailler avec l'interface utilisateur graphique (GUI) des outils de développement Kibana. Nous utiliserons un cluster élastique à nœud unique avec l'interface graphique Kibana, le tout en utilisant Docker Compose.

## Prérequis
Avant de commencer, assurez-vous d'avoir installé : 
- Docker et Docker Compose sur votre machine.
- OpenJDK 8 avec la commande suivante :
```
sudo apt install openjdk-8-jdk

// pour vérifier la version
java -version
```
- Ubuntu avec minimum 8Go de ram

## Setup

Docker Compose Setup
Vous pouvez exécuter un cluster Elasticsearch et l'interface graphique Kibana avec le fichier docker-compose.yml suivant :

```
version: '2.2'
services:
  elasticsearch:
    image: docker.elastic.co/elasticsearch/elasticsearch:7.11.1
    container_name: elasticsearch
    restart: always
    environment:
      - xpack.security.enabled=false
      - discovery.type=single-node
    ulimits:
      memlock:
        soft: -1
        hard: -1
      nofile:
        soft: 65536
        hard: 65536
    cap_add:
      - IPC_LOCK
    volumes:
      - ./elas1:/usr/share/elasticsearch/data
    ports:
      - 9200:9200
      - 9300:9300
    networks:
      - esnet

  kibana:
    container_name: kibana
    image: docker.elastic.co/kibana/kibana:7.11.1
    restart: always
    ports:
      - 5601:5601
    depends_on:
      - elasticsearch
    networks:
      - esnet

networks:
  esnet:
    driver: bridge
```

Explication du fichier docker-compose.yml :
1. Elasticsearch : Ce service utilise l'image Docker officielle d'Elasticsearch (version 7.11.1). Il définit le nom du conteneur comme elasticsearch et le redémarre toujours en cas de panne. La sécurité X-Pack est désactivée et il est configuré pour fonctionner comme un cluster à nœud unique. Les ports 9200 et 9300 sont exposés pour l'accès externe.

2. Kibana : Ce service utilise l'image Docker officielle de Kibana (version 7.11.1). Le conteneur est nommé kibana et redémarre toujours en cas de panne. Il expose le port 5601 pour permettre l'accès à l'interface graphique de Kibana. Kibana dépend du service Elasticsearch et ne démarrera que lorsque ce dernier sera prêt.

## Démarrage de l'application

Pour démarrer l'application, exécutez les commandes suivantes :
```
docker-compose up -d
// -d (mode détaché)
```

En cas d'erreur, vérifier bien que le dossier ``elas1`` à les droits, sinon éxecuter cette commande :
```
sudo chmod 777 elas1
```

Cela démarrera les services Elasticsearch et Kibana en arrière-plan. Après quelques secondes, vous pourrez accéder à Kibana via votre navigateur à l'adresse suivante :

http://localhost:5601/app/dev_tools#/console

Vous serez redirigé vers la console de développement de Kibana où vous pourrez interagir avec Elasticsearch.

## Vérification des indices
Pour vérifier les indices dans votre cluster Elasticsearch, exécutez la commande suivante dans la console de développement de Kibana :

```
GET /_cat/indices?v
```
Cette commande retournera la liste des indices disponibles dans Elasticsearch.


⚠️ Remarque importante : Pour obtenir le mappage de votre index, comme par exemple receipe, vous pouvez exécuter la commande suivante dans la console Kibana :

```
GET /receipe/_mapping
```
Cette commande retournera le mappage de l'index receipe, vous permettant de visualiser sa structure.

> Cependant, si vous souhaitez créer des index, par exemple à partir d'un fichier JSON, veuillez consulter le fichier [README.md](../elasticSearch/README.md) de ElasticSearch pour obtenir des instructions détaillées sur la procédure à suivre.


