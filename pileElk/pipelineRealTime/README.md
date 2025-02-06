# Visualisation de données en temps réel avec Kibana


## Commandes utiles

```
sudo docker compose up
sudo docker compose-up
```


Pour vérifier les indices :
```
curl http://0.0.0.0:9200/_cat/indices?v
```


Rentrer dans le conteneur :
```
docker run -it ---- /bin/bash
```

## Remarques

Ne pas oublier d'attribuer les droits de ``filebeat`` :
```
chmod go-w filebeat.yml
```

## Création d'un modèle d'index
1. Ouvrez Kibana dans votre navigateur web.
2. Accédez à la section **Stack Management** dans la barre latérale gauche, puis cliquez sur **Index Patterns**.
3. Cliquez sur le bouton **Create index pattern**.
4. Entrez le nom du modèle d'index (dans notre cas, "python-logs*") puis cliquez sur **Next**.
5. Sélectionnez le champ **@timestamp** comme champ de filtre temporel, puis cliquez sur **Create index pattern**.

## Créer un tableau de bord avec les données indexées
Maintenant que notre index est reconnu par Kibana, créons des graphiques pour visualiser les données.

1. Dans le menu de Kibana, accédez à la section **Discover** pour explorer les données indexées. Vous pouvez ajuster l'intervalle de temps avec le bouton calendrier situé en haut à droite. Cette section fournit une visualisation générale des données et permet de les actualiser pour voir les mises à jour en temps réel.
2. Pour créer des visualisations et des tableaux de bord, accédez à la section **Dashboard**, puis cliquez sur le bouton **+ Create panel**.
3. Choisissez l'option **Aggregation based**, puis **Metrics**, sélectionnez l'index "python-logs" et renseignez les options nécessaires.
4. Sauvegardez le graphique et retrouvez-le dans la section **Visualize**.

## Création de différents types de graphiques
1. **Graphique en camembert (Pie chart)** :
   - Allez dans **Aggregation based > Pie**, choisissez l'index "python-logs" et renseignez les options souhaitées.

2. **Graphique de série temporelle (Time series)** :
   - Accédez à **TSVB** pour visualiser automatiquement le nombre de documents par intervalle de 30 secondes.

3. **Filtrer le graphique de série temporelle** :
   - Créez un autre panneau en utilisant les paramètres requis pour afficher les données filtrées.
