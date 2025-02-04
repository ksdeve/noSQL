# Projet MongoDB avec Python et Docker

Ce projet présente la configuration et l'utilisation de **MongoDB** avec **Python** (via **PyMongo**) et **Docker**.

## Description

Le but de ce projet est de configurer un environnement MongoDB via Docker et d'interagir avec la base de données à l'aide de Python.

## Prérequis

1. **Docker** doit être installé sur votre machine.
2. **Python** et **pip** doivent être installés pour gérer les dépendances.
3. **PyMongo** doit être installé dans votre environnement Python.

## Étapes du Projet

### 1. Mise en place de MongoDB avec Docker

#### Télécharger l'image Docker MongoDB

```bash
docker pull mongo
```

Lancer MongoDB dans un conteneur Docker
```bash
docker run --name my-mongo -p 27017:27017 -d mongo
```
Ce conteneur écoute sur le port 27017 et est configuré pour exécuter MongoDB.

1. Connexion à MongoDB avec Python
Installer la bibliothèque PyMongo
```python
pip install pymongo
```
Connexion au serveur MongoDB
```python
from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017/')
```
