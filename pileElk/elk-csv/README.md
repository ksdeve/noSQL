# Ingérer des données CSV avec ELK (Elasticsearch, Logstash, Kibana)


## Aperçu de l'architecture
L'architecture du projet pour ingérer des données CSV dans Elasticsearch via Logstash se compose de plusieurs services conteneurisés :

- Elasticsearch : Stocke et indexe les données.
- Logstash : Traite les données CSV et les envoie à Elasticsearch.
- Kibana : Fournit une interface graphique pour visualiser les données.

## Structure


```
├── data
│   ├── data.csv
│   └── data-json.log
├── docker-compose.yml
├── elasticsearch
│   └── elasticsearch.yml
└── logstash
    ├── logstash.conf
    └── logstash.yml
```
