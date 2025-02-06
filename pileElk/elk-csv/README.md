# Ingérer des données CSV avec ELK (Elasticsearch, Logstash, Kibana)

## Comandes utiles :

Installer logstash

```
wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo gpg --dearmor -o /usr/share/keyrings/elastic-keyring.gpg

echo "deb [signed-by=/usr/share/keyrings/elastic-keyring.gpg] https://artifacts.elastic.co/packages/8.x/apt stable main" | sudo tee /etc/apt/sources.list.d/elastic-8.x.list

sudo apt-get update
sudo apt-get install logstash
sudo systemctl start logstash
sudo systemctl enable logstash
```



```
sudo docker compose exec logstash /bin/bash/logstash --config.test_and_exit -f /usr/share/logstash/pipeline/logstash.conf 
```


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
