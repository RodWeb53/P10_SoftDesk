![Réalisé avec Python + Django + Django rest framwork](/src/softdesk/images/made-with-python-+-django-+-django-rest-framework.svg)
![API request avec Postman](/src/softdesk/images/api-request-tool-postman.svg)
![Documentation avec Postman](/src/softdesk/images/documentation-postman.svg)
![Validation PEP8 avec FLAKE8](/src/softdesk/images/pep-8-validation-flake-8.svg)

![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg) (https://forthebadge.com)

## Mise en place du programme

`Pré-requis : python 3 doit être installé sur votre machine`

- Télécharger ce code dans ''code'' > ''Download ZIP''
- Décompresser le dossier

### 1. Création de l'environnement virtuel

Ouvrez le terminal, allez dans le dossier que vous avez téléchargé

Tapez la commande suivante pour créer l'environnement virtuel

    python -m venv env

### 2. Lancement de l'environnement virtuel

Sous Windows tapez la commande suivante :

    env\Scripts\activate.bat

Sous MAC ou Linux tapez la commande suivante :

    source env/bin/activate

### 3. Intallation des dépendance

Tapez la commande suivante :

    pip install -r requirements.txt

### 4. Lancement du serveur

Aller dans un terminal et tapez les commandes suivantes :

    cd src

Ensuite 

    python manage.py runserver

### 5. Adresse de l'API

L'adresse de l'API est : 
    http://127.0.0.1:8000/api/


### 6. Endpoints

  ------------------------------------------------------------------------------------------------------------------------------------------------------
| Description                                                                                 | Méthode | Endpoint                                       |
| ------------------------------------------------------------------------------------------- | ------- | ---------------------------------------------- |
| Inscription de l'utilisateur                                                                | POST    | `/api/signup/`                                 |
| Connexion de l'utilisateur                                                                  | POST    | `/api/login/`                                  |
| Récupérer la liste de tous les projets (projects) rattachés à l'utilisateur (user) connecté | GET     | `/api/projects/`                               |
| Créer un projet                                                                             | POST    | `/api/projects/`                               |
| Récupérer les détails d'un projet (project) via son id                                      | GET     | `/api/projects/{id}/`                          |
| Mettre à jour un projet                                                                     | PUT     | `/api/projects/{id}/`                          |
| Supprimer un projet et ses problèmes                                                        | DELETE  | `/api/projects/{id}/`                          |
| Ajouter un utilisateur (collaborateur) à un projet                                          | POST    | `/api/projects/{id}/users/`                    |
| Récupérer la liste de tous les utilisateurs (users) attachés à un projet (project)          | GET     | `/api/projects/{id}/users/`                    |
| Supprimer un utilisateur d'un projet                                                        | DELETE  | `/api/projects/{id}/users/{id}`                |
| Récupérer la liste des problèmes (issues) liés à un projet (project)                        | GET     | `/api/projects/{id}/issues/`                   |
| Créer un problème dans un projet                                                            | POST    | `/api/projects/{id}/issues/`                   |
| Mettre à jour un problème dans un projet                                                    | PUT     | `/api/projects/{id}/issues/{id}`               |
| Supprimer un problème d'un projet                                                           | DELETE  | `/api/projects/{id}/issues/{id}`               |
| Créer des commentaires sur un problème                                                      | POST    | `/api/projects/{id}/issues/{id}/comments/`     |
| Récupérer la liste de tous les commentaires liés à un problème (issue)                      | GET     | `/api/projects/{id}/issues/{id}/comments/`     |
| Modifier un commentaire                                                                     | PUT     | `/api/projects/{id}/issues/{id}/comments/{id}` |
| Supprimer un commentaire                                                                    | DELETE  | `/api/projects/{id}/issues/{id}/comments/{id}` |
| Récupérer un commentaire (comment) via son id                                               | GET     | `/api/projects/{id}/issues/{id}/comments/{id}` |
  ------------------------------------------------------------------------------------------------------------------------------------------------------


## Listes des utilisateurs dans la base de données
     
 ----------------------------------------------
| *Identifiant*            |   *Mot de passe*  |
|--------------------------|-------------------|
| CreateurProjet@mail.com  |     Test2023*     |
| Contributeur@mail.com    |     Test2023*     |
| Contributeur2@mail.com   |     Test2023*     |
| visiteur@mail.com        |     Test2023*     |
 ----------------------------------------------


## Documentation Postman

Lien pour la documentaion publiée :

    https://documenter.getpostman.com/view/26418588/2s946feCoq



## Générer un rapport avec flake8-html

Le rapport flake8 créer un rapport montrant que le code ne contient pas d'érreur de peluchage

Le rapport sera créer à l'aide du fichier setup.cfg
le fichier de configuration permet de ne pas prendre en analyse l'environnement virtuel
Limite la longueur des lignes à 119
Et paramètre le répertoire de sortie

Taper la commande "flake8" a la racine du projet
