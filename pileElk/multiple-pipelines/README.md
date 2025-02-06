# Configuration de pipelines multiples avec Logstash et Elasticsearch

Dans cette partie, nous allons voir comment ingérer plusieurs sources de données à l'aide de Logstash et Elasticsearch. Pour cela, nous allons fusionner trois pipelines précédemment établis : le pipeline pour les fichiers CSV, le pipeline utilisant Grok et le pipeline avec Filebeat.

## Aperçu de l'architecture

La structure du projet est la suivante :

```
.
├── data
│   ├── apache_logs.txt
│   ├── data.csv
│   └── data-json.log
├── docker-compose.yml
├── filebeat
│   └── filebeat.yml
├── logs
│   └── python_logs.log
├── logstash
│   ├── config
│   │   ├── logstash.yml
│   │   └── pipelines.yml
│   └── pipeline
│       ├── logstash-apache.conf
│       ├── logstash-python-log.conf
│       └── logstash-csv.conf
├── README.md
└── send_logs.py
```

## Configuration des fichiers Logstash

Nous allons utiliser trois fichiers de configuration Logstash :

- `logstash-apache.conf` pour le traitement des logs Apache.
- `logstash-csv.conf` pour le traitement des fichiers CSV.
- `logstash-python-log.conf` pour les logs Python en temps réel.

Ces fichiers doivent être placés dans le répertoire `pipeline`.

Ensuite, créez le fichier `pipelines.yml` dans le répertoire `config` pour configurer les pipelines Logstash :

**Contenu du fichier pipelines.yml :**

- Déclaration des pipelines avec leurs chemins de configuration.
- Assurez-vous que chaque pipeline dispose d'un `pipeline.id` unique.

Enfin, ajoutez un fichier `logstash.yml` pour indiquer à Logstash où trouver la configuration des pipelines.

**Contenu du fichier logstash.yml :**

- Spécification du chemin vers `pipelines.yml`.
- Par défaut, Logstash cherche ce fichier dans le même répertoire que `logstash.yml`.

## Mise à jour du fichier docker-compose.yml

Pour monter les fichiers dans le conteneur Logstash et spécifier la configuration, modifiez le fichier `docker-compose.yml` :

- Ajoutez une variable d'environnement pour indiquer le chemin des configurations.
- Montez les volumes suivants :
  - Le répertoire `pipeline`.
  - Le fichier `pipelines.yml`.
  - Le répertoire contenant les données externes.

## Exécution du projet

Lancez la commande suivante pour démarrer les services :
```bash
docker-compose up -d
```

Ensuite, vérifiez si les index sont créés en interrogeant Elasticsearch :
```bash
curl http://0.0.0.0:9200/_cat/indices?v
```

Si tout fonctionne correctement, vous devriez voir une sortie indiquant la présence des index pour les différentes sources de données :

```
health status index                           uuid                   pri rep docs.count docs.deleted store.size pri.store.size
green  open   .apm-custom-link                Eww7EOhAS6aSKENm14yv4g   1   0          0            0       208b           208b
yellow open   csv-data                        1PDAef-cS82F8NP6F72Hpg   1   1       4174            0      1.4mb          1.4mb
green  open   .kibana_task_manager_1          wpmgiisqQCGuIHxhlzB6Vw   1   0          8           24     62.7kb         62.7kb
green  open   .kibana-event-log-7.11.1-000001 xk67yAl1RyuVED8h1FKuYg   1   0          1            0      5.5kb          5.5kb
green  open   .apm-agent-configuration        HS51EL_6ScO4PCwfQgD5hA   1   0          0            0       208b           208b
yellow open   web_server_logs                 tUiVljDOQICNnv_af_ystg   1   1      10000            0      6.6mb          6.6mb
green  open   .kibana_1                       ltbQgXoVTrehRy79x5yWzw   1   0          8            0      2.1mb          2.1mb
yellow open   python-logs-2023.04.07          QBqBOF88TSGNspubKMaUPg   1   1       4089            0    438.2kb        438.2kb
```