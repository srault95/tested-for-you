---
Version: 1
Lang: fr
Title: MongoDB Server
Tags: mongodb, nosql, db, backend, server, big-data, product, iot, storage
Summary: Serveur NoSQL pour le Big Data
Product_version: 3.5
Product_url: https://www.mongodb.com
---

[TOC]

## Mes Commentaires

#### Points Positifs {: .text-success }

* Installation facile grâces aux binaires déjà compilés pour plusieurs
  plateformes, dont Windows.
* Monté en compétence rapide (une fois passé l'apprentissage des concepts NoSQL)
* Clients/Librairies dans plusieurs languages (Python, Java, Javascript, C++,
  Ruby, ...)
* Un language de Query puissant
* La sécurité, sous plusieurs formes: Authentification, Keyfile, SSL,
  Branchement externe
* Stockage au format BSON (Json Binaire)
* 5ème au classement [db-engine](https://db-engines.com/en/ranking) et 1er dans
  le classement des
  [document store](https://db-engines.com/en/ranking/document+store)

#### Points Négatifs {: .text-danger }

* La difficulté à optimiser ce qui doit être chargé en RAM.
* La ré-indexation qui demande autant de place libre que la taille actuelle de
  l'index.
* Les limitations dans la taille d'un document.
* Le clustering car j'ai une préférence pour le modèle multi-maîtres comme
  Cassandra.

## Fonctionnalités principales

* Base NoSQL orienté documents (possibilité de Graph)
* Haute disponibilité avec le clustering
* Montée en charge avec le Sharding
* Aggrégations de données
* Map / Reduce
* Création automatique des Bases et collections (équivalent d'une table SQL)
* Schema-less (schéma optionnel)

### Remarque sur le schema-less

Le modèle sans obligation de schéma, vous permet de stocker dans la même
collection (table au sens SQL), des données dont la structure peut varier.

Dans le SQL, vous devez déclarer chaque champs et préciser ses contraintes
(type, unique, non null, ...)

**Dans la pratique**, ne pas déclarer de schéma est **une très mauvaise idée**
car les performances et la maintenance peuvent devenir désastreuses.

Avant la version 3.2 de MongoDB, la validation coté serveur était réalisé à
l'aide des indexes avec très peu de possibilités

Depuis la 3.2, vous pouvez utiliser un **validator** pendant la création de la
collection. Je n'ai pas encore testé cette fonctionnalité car elle est peu
documenté et ne semble pas prise en comptes par les drivers clients comme
pymongo.

Le seul usage que je connais, où vous pouvez ne pas gérer de schémas, c'est le
stockage de données brut qui ne seront pas analysés, agrégés, interrogés dans
MongoDB mais extrait et transmit à d'autres applicatifs comme Spark. Dans ce
cas, MongoDB ne sert que de store (comme un filesystem), avec le clustering en
plus.

### Remarque sur les ODM

Le terme ODM (Object Document Manager) fait référence à son pendant SQL, l'ORM
(Object Relational Manager)

C'est une utilisation un peu trompeuse car avec un ORM, en SQL, vous pouvez
utiliser la même librairie, par exemple Peewee ou SQLAlchemy, pour plusieurs
bases de données (MySQL, PostgreSQL, Oracle, ..) sans changer, ou très peu, le
code.

Je ne connais aucun ODM, aujourd'hui, qui permette d'utiliser autre choses que
MongoDB pour le NoSQL, avec un même code.

Seuls exceptions, en Javascript, le framework Loopback qui utilise
[juggler](https://github.com/strongloop/loopback-datasource-juggler) pour
communiquer avec des bases SQL, autant que des bases NoSQL. Toujours en
Javascript avec [waterline](https://github.com/balderdashy/waterline) utilisé
surtout par Sails.js. En PHP, avec [Doctrine](https://github.com/doctrine),
l'ORM/ODM de Symfony.

## Cas d'utilisation

* Tous les cas qui ne nécessite pas du transactionnel coté serveur ou trop de
  relations entre collections (tables), en prevoyant une restructuration
  (dénormalisation) du modèle de données.
* Logs
* Statistiques.
* Fichiers binaires ou textuels.
* Données des objets connectés (IOT).

## Liens

* [Sources](https://github.com/mongodb)
* [Documentation](https://docs.mongodb.com/manual/)

## Librairies / ODM

### Python

* [native](http://api.mongodb.com/python/current/)
* [mongoengine](http://mongoengine.org/)
* [motor](https://github.com/mongodb/motor)
* [umongo](https://github.com/Scille/umongo)

### Javascript

* [native](https://mongodb.github.io/node-mongodb-native/)
* [mongoose.js](http://mongoosejs.com)
* [waterline](https://github.com/balderdashy/waterline)

## Services SASS / Hosting

* [Cloud](https://cloud.mongodb.com/)
* [Compose.io](https://www.compose.com/databases/mongodb)
* [Mlab](https://mlab.com/)
* [Heroku](http://heroku.com) (par Mlab ou Compose)
