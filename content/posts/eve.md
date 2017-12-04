---
Version: 1
Lang: fr
Title: Eve
Tags: python, python3, restful, api, framework, flask, mongodb, elasticsearch, neo4j, sqlalchemy, jwt, oauth2, nosql, product
Summary: Eve permet de générer une API Restful avec MongoDB
Product_version: 0.8-dev
Product_url: https://github.com/pyeve/eve
---

[TOC]

## Commentaires

#### Points Positifs {: .text-success }

* Permet d'obtenir une API Restful très rapidement avec peu de développement
  grâce à son mode déclaratif de schémas.
* La montée en compétence est très rapide
* Permet de profiter des nombreux addons disponibles pour Flask.
* Maintenance et déploiement très simple
* Très peu de dépendences externes
* Testable

#### Points Négatifs {: .text-danger }

* J'aurais préféré une validation json-schema à celle de Cerberus
* Malgré, les autres backend disponible, le produit est surtout conçut pour
  [MongoDB]({filename}mongodb.md).
* La dépendance à Flask ne permet de profiter d'asyncio mais on peut augmenter
  les performances avec [gevent]({filename}gevent.md) ou
  [meinheld](https://github.com/mopemope/meinheld)

## Version testé

* version 0.8-dev du 2017-11-23

## Fonctionnalités principales

* Backend MongoDB
* De nombreaux Hooks pour intervenir à toutes les phases (POST/GET/...)
* Support d'[HATEOAS](https://fr.wikipedia.org/wiki/HATEOAS) optionnel
* Format JSON ou XML
* Schémas et validation avec [Cerberus](http://docs.python-cerberus.org)
* Authentification Basic, HMAC, Token, facilement extensible
* Permissions par rôle

> En options, par l'ajout d'extension:

* Backend ElasticSearch, Neo4j, SQLAlchemy
* Authentification OAuth2, JWT
* Documentation Swagger

## QuickStart

* Installez Eve et un client http (plus pratique que curl):

```bash
$ pip install eve httpie
```

```bash
$ pip install eve httpie
```

* Fichier de configuration:

```python
# settings.py
# resource_methods: pour les opérations sur la collection people
# item_methods: pour les opérations sur un élément de la collection people
DOMAIN = {
    'people': {
        'resource_title': 'People',
        'resource_methods': ['GET', 'POST'],
        'item_methods': ['GET', 'PATCH', 'DELETE'],
        'allow_unknown': False,
        'schema': {
            'email': {
                'type': 'string',
                'required': True,
                'unique': True,
            },
            'city': {
                'type': 'string',
                'maxlength': 255,
            }
        }
    }
}
```

* Application minimum pour Eve:

```python
# app.py
from eve import Eve
app = Eve()
app.run()
```

* Démarrez le serveur MongoDB:

```bash
$ mongod --noauth --nojournal --smallfiles --directoryperdb --wiredTigerCacheSizeGB 1
```

* Démarrez Eve:

```shell
$ python app.py
```

* Et dans un autre shell:

```
# POST
$ http --json --print b POST http://127.0.0.1:5000/people email=user@example.net city=Paris
{
    "_created": "Sat, 02 Dec 2017 21:54:13 GMT",
    "_etag": "bbcf449f45b1cd74d0924b6a4fa5e56283514d94",
    "_id": "5a232105a78e50876ca83395",
    "_links": {
        "self": {
            "href": "people/5a232105a78e50876ca83395",
            "title": "People"
        }
    },
    "_status": "OK",
    "_updated": "Sat, 02 Dec 2017 21:54:13 GMT"
}

# GET
$ http --json --print b http://127.0.0.1:5000/people
{
    "_items": [
        {
            "_created": "Sat, 02 Dec 2017 20:56:21 GMT",
            "_etag": "6b1c9ed06dabeaa39c780e113594daeed5abd4d1",
            "_id": "5a231375a78e50876ca83393",
            "_links": {
                "self": {
                    "href": "people/5a231375a78e50876ca83393",
                    "title": "People"
                }
            },
            "_updated": "Sat, 02 Dec 2017 20:56:21 GMT",
            "city": "Paris",
            "email": "user@example.net"
        }
    ],
    "_links": {
        "parent": {
            "href": "/",
            "title": "home"
        },
        "self": {
            "href": "people",
            "title": "People"
        }
    },
    "_meta": {
        "max_results": 25,
        "page": 1,
        "total": 1
    }
}

# PATCH (update partiel)
# L'id après people est celui du document créé précédement (champs _id)
# La valeur de If-Match vient du champs _etag
$ http --json --print b PATCH http://127.0.0.1:5000/people/5a231375a78e50876ca83393  city=Marseille If-Match:6b1c9ed06dabeaa39c780e113594daeed5abd4d1
{
    "_created": "Sat, 02 Dec 2017 20:56:21 GMT",
    "_etag": "4a47482b09d7ea2accaaa249abbe3faca4dbac44",
    "_id": "5a231375a78e50876ca83393",
    "_links": {
        "self": {
            "href": "people/5a231375a78e50876ca83393",
            "title": "People"
        }
    },
    "_status": "OK",
    "_updated": "Sun, 03 Dec 2017 00:22:00 GMT"
}

# DELETE (pas de réponse)
$ http --json --print b DELETE http://127.0.0.1:5000/people/5a231375a78e50876ca83393 If-Match:4a47482b09d7ea2accaaa249abbe3faca4dbac44
```

* Si vous n'utilisez pas [HATEOAS](https://fr.wikipedia.org/wiki/HATEOAS),
  désactivez-le:

```python
# settings.py
HATEOAS = False
```

## Liens

* Source : [https://github.com/pyeve/eve](https://github.com/pyeve/eve)
* Docs: [http://python-eve.org/](http://python-eve.org/)
* Démo :
  [https://eve-demo.herokuapp.com/people](https://eve-demo.herokuapp.com/people)

## Extensions

> Attention, la plupart des extensions sont assez anciennes et ne semblent pas
> maintenus

* [Swagger](https://github.com/pyeve/eve-swagger)
* [Backend sqlalchemy](https://github.com/pyeve/eve-sqlalchemy)
* [Backend ElasticSearch](https://github.com/petrjasek/eve-elastic)
* [Backend Neo4j](https://github.com/Abraxas-Biosystems/eve-neo4j)
* [Auth JWT](https://github.com/rs/eve-auth-jwt)
* [Auth OAuth2](https://github.com/pyeve/eve-oauth2)
