# Redis Example with Docker and Python


## Lien de mes notes de cours : 
https://docs.google.com/document/d/1qaOQejrpY60PV4uGTpxFEucIaD8HRcpF4wXGcN3kItA/edit?usp=drive_link

## Introduction
Ce projet montre comment configurer et utiliser Redis avec Python en utilisant Docker. Redis est un magasin de données en mémoire populaire qui prend en charge des structures de données comme les chaînes, les hachages, les listes, et plus encore. Nous allons apprendre à installer Redis avec Docker, à le connecter à un script Python, et à effectuer des opérations de base avec Redis.

### Prérequis
Avant de commencer, assurez-vous d'avoir installé les éléments suivants sur votre machine :

- Docker : [Installer Docker](https://www.docker.com/get-started/)
- Python : [Télécharger Python](https://www.python.org/downloads/)
- pip : Le gestionnaire de paquets pour Python. Il devrait être installé avec Python.
- Ubuntu : [Ubuntu 22.04 LTS](https://releases.ubuntu.com/jammy/)

### Installation
1. Installer Redis avec Docker
Nous allons utiliser Docker pour installer et exécuter Redis. 
Suivez ces étapes :

Téléchargez l'image Redis depuis Docker Hub :

```
docker pull redis
```


2. Démarrez un conteneur Redis :

```
docker run --name my-redis -d redis
```

Vérifiez que Redis fonctionne en consultant les conteneurs en cours d'exécution :
```
docker ps
```

Connectez-vous à Redis avec la CLI :


```
docker exec -it my-redis redis-cli
```

À ce stade, Redis est installé et opérationnel. Vous pouvez exécuter des commandes Redis dans cette session CLI pour tester.

3. Installer les dépendances Python
Pour interagir avec Redis depuis Python, vous devez installer la bibliothèque redis-py :

```
pip install redis
```

4. Cloner ce dépôt
Clonez ce dépôt sur votre machine locale pour accéder au code Python et à d'autres fichiers associés :

```
git clone https://github.com/ksdeve/noSQL.git
cd redis
```

## Utilisation du Code Python
- Script Python redis_example.py
Le fichier redis_example.py contient des exemples de commandes Redis en Python. Vous y trouverez des opérations comme la création, la lecture et la suppression de clés.

Exemple de code :

```python
import redis

# Connexion à Redis
r = redis.Redis(host='localhost', port=6379, db=0)

# Créer une clé et une valeur
r.set('user:1:name', 'John Doe')

# Lire la valeur d'une clé
user_name = r.get('user:1:name').decode('utf-8')
print(user_name)  # Affiche : John Doe
```

2. Exemple de commande Redis
Voici quelques commandes Redis de base que vous pouvez exécuter dans la CLI de Redis :

```
SET user:1:name "John Doe"
GET user:1:name
```
