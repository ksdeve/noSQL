# Mon Repo de Projets Docker et Python

Ce dépôt contient des exemples d'utilisation de plusieurs technologies populaires (Redis, MongoDB, Neo4j) avec Docker et Python. Chaque projet est bien distinct mais ils partagent un but commun : montrer comment utiliser ces bases de données avec Python en environnement Docker.

- **Lien vers les notes de cours** : [Google Docs](https://docs.google.com/document/d/1qaOQejrpY60PV4uGTpxFEucIaD8HRcpF4wXGcN3kItA/edit?usp=drive_link)

## Projets disponibles

### 1. [Redis avec Docker et Python](redis/README.md)
Ce projet montre comment configurer et utiliser **Redis** avec Python en utilisant Docker. Redis est un système de gestion de base de données en mémoire clé-valeur.

- **Technologies utilisées** : Redis, Python, Docker
- [Consulter le README spécifique à Redis](redis/README.md)

### 2. [MongoDB avec Docker et Python](mongodb/README.md)
Ce projet montre comment configurer et utiliser **MongoDB** avec Python en utilisant Docker. MongoDB est une base de données NoSQL orientée document.

- **Technologies utilisées** : MongoDB, Python, Docker
- [Consulter le README spécifique à MongoDB](mongodb/README.md)

<!-- ### 3. [Neo4j avec Docker et Python](neo4j/README.md)
Ce projet montre comment configurer et utiliser **Neo4j**, une base de données orientée graphes, avec Python en utilisant Docker.

- **Technologies utilisées** : Neo4j, Python, Docker
- [Consulter le README spécifique à Neo4j](neo4j/README.md) -->

---

## Prérequis communs
Avant de commencer, assurez-vous d'avoir installé les éléments suivants sur votre machine :

- Docker : [Installer Docker](https://www.docker.com/get-started/)
- Python : [Télécharger Python](https://www.python.org/downloads/)
- pip : Le gestionnaire de paquets pour Python. Il devrait être installé avec Python.
- Ubuntu : [Ubuntu 22.04 LTS](https://releases.ubuntu.com/jammy/)
---

## Installation et Exécution des Projets
Voici les étapes de base pour exécuter chacun des projets localement.

1. **Cloner le dépôt** :

```bash
git clone https://github.com/ksdeve/noSQL.git
cd noSQL
