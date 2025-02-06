# Traitement des journaux du serveur Apache avec la Stack Elastic

Ce projet a pour but de configurer un pipeline d'ingestion de données afin de traiter les journaux (logs) d'un serveur web Apache à l'aide de Logstash, tout en visualisant les résultats dans Kibana. Ce mini-projet vous permettra d'acquérir une expérience pratique avec la Stack Elastic en travaillant sur des données issues de cas réels.

## Aperçu de l'architecture du projet

```
.
├── data
│   └── apache_logs.txt
├── docker-compose.yml
├── logstash
│   └── logstash.conf
```

### 1. Téléchargement des journaux du serveur web
Téléchargez un fichier d'exemple de journaux de serveur web à partir du lien fourni.

Enregistrez ce fichier sous le nom `apache_logs.txt` dans un répertoire dédié à ce projet.

---

### 2. Configuration de Logstash

Modifiez le fichier `logstash.conf` pour ajouter une configuration permettant de lire et traiter les logs :

- **Entrée** : Spécifie le fichier contenant les journaux Apache.
- **Filtrage** : Utilisation de `grok` pour analyser les journaux Apache standard.
- **Date** : Transformation du champ `timestamp` en horodatage Elasticsearch.
- **GeoIP** : Enrichissement des données avec les informations géographiques.
- **Sortie** : Envoi des journaux traités à Elasticsearch.

Assurez-vous que le chemin d'accès au fichier de journaux correspond à votre architecture.

---

### 3. Mise à jour de la configuration Docker Compose

Modifiez le fichier `docker-compose.yml` pour inclure le fichier de configuration Logstash :

- Montez le fichier `logstash-apache.conf` comme pipeline.
- Montez le fichier de journaux `apache_logs.txt`.

Vérifiez que les chemins d’accès sont corrects.

---

### 4. Redémarrage du conteneur Logstash
Pour appliquer la nouvelle configuration :

1. Arrêtez les conteneurs Docker en cours.
2. Relancez les conteneurs avec la commande Docker appropriée.

---

### 5. Visualisation des journaux dans Kibana

1. Ouvrez Kibana dans votre navigateur (à l’adresse [http://localhost:5601](http://localhost:5601)).
2. Créez un nouveau motif d’index (“index pattern”) nommé `web_server_logs`.
3. Naviguez vers l'onglet “Discover” pour explorer les données indexées.

---

### 6. Création de visualisations
Pour créer des visualisations personnalisées :

1. Accédez à l’onglet “Visualize”.
2. Cliquez sur “Create visualization”.
3. Sélectionnez un type de visualisation (par exemple, “Pie” ou “Vertical bar”).
4. Choisissez `web_server_logs` comme source de données.

#### Exemples de visualisations possibles :
- **Codes de réponse HTTP** : utilisez le champ `response`.
- **Adresses IP clientes les plus fréquentes** : utilisez le champ `clientip`.
- **Ressources les plus demandées** : utilisez le champ `request`.
- **Nombre de requêtes au fil du temps** : utilisez le champ `@timestamp`.
- **Répartition géographique des adresses IP clientes** : utilisez le champ `geoip.location`.

