---
Version: 1
Lang: fr
Title: Algolia Search
Tags: algolia, search, service, elasticsearch
Summary: Algolia est un moteur d'indexation extrèment rapide et facile à mettre en oeuvre
Product_version: 0
Product_url:
---

[TOC]

## Mes Commentaires

**Remarques sur le fonctionnement d'Algolia:**

Les performances sont excellentes, à condition de brancher directement
l'utilisateur avec le moteur de recherche, sans passer par votre backend.

Les communications entre votre backend (python/js/go/php/..) serviront
uniquement à la création et la maintenance de vos indexes.

**Un des points les plus important sur la sécurité** est que Algolia fournit
deux clés d'api pour communiquer avec leur services. L'une d'elle, sert aux
recherches (en lecture seule) et peut être exposé dans votre client Web mais
l'autre, la clé Admin ne doit être utilisé que dans votre backend ou dans des
scripts qui ne sont jamais exposés.

#### Points Positifs {: .text-success }

* Des temps de réponses exceptionnels.
* Un dashboard très fonctionnel.
* Des librairies et clients pour plusieurs languages.
* Une très bonne documentation et de nombreux exemples.
* [Intégration](https://www.algolia.com/integrations) à plusieurs CMS et
  solutions d'Ecommerce (Magento, Wordpress, Shopify, ...).
* Des prix raisonnables et gratuit des petits besoins.

#### Points Négatifs {: .text-danger }

* Le manque de personnalisation qui est volontaire pour garantir les
  performances
* Cet
  [article](https://jolicode.com/blog/retour-sur-algolia-solution-de-recherche-en-saas)
  résume bien les différences avec ElasticSearch.

## Cas d'utilisations

* Fonction de recherche pour votre site internet
* Recherche et filtrage à facets dans votre application d'e-commerce
* Tout autres besoins de recherche full-text pour lesquels, vous alimentez vous
  même vos indexes.

## Quickstart

**[sources]()**

### Introduction

L'exemple suivant est volontairement allégé pour simplifier la prise en main de
l'outil mais il existe de nombreux paramètres de configuration que vous
trouverez dans la documentation officielle du produit.

**Données à indexer** qui peuvent provenir de votre base de données ou tout
autres sources:

```json
// datas.json
[
  {
    "slug": "algolia-intro",
    "title": "Algolia est un excellent moteur d'indexation",
    "tags": ["search", "saas"],
    "url": "http://example.net/articles/algolia.html",
    "content": "Lorem Ipsum..."
  },
  {
    "slug": "algolia-tuto-1",
    "title": "Mise en oeuvre d'Algolia Search dans votre site",
    "tags": ["search", "python", "algolia", "tutorial"],
    "url": "http://example.net/articles/algolia-mise-en-oeuvre.html",
    "content": "Lorem Ipsum..."
  }
]
```

### Backend Python

```python
# pip install algoliasearch

import hashlib
import json
from algoliasearch import algoliasearch

APP_ID = "[REMPLACER PAR VOTRE APP ID]"
APP_ADMIN_KEY = "[REMPLACER PAR VOTRE ADMIN KEY]"
APP_INDEX = "demo"
sc = algoliasearch.Client(APP_ID, APP_ADMIN_KEY)

index = sc.init_index(APP_INDEX)

index.set_settings({
  # Par défaut, tous les champs de type texte
  'searchableAttributes': [
    'title',
    'content',
  ],
  # Le nombre d'entrée affiché dans le filtrage par facets
  'maxFacetHits': 20,
  'attributesForFaceting': [
    'tags'
  ]
})

with open('datas.json') as fp:
  datas = json.load(fp)
  for data in datas:
    objectId = hashlib.sha256(str(data['slug']).encode('utf-8')).hexdigest()
    response = index.add_object(data, objectId)
```

**Sur votre dashboard Algolia (onglet Indices), vous devriez trouvez ceci:**

![Algolia Dashboard Demo](/theme/thumbnail/algolia-dashboard-demo_middle.png)
[Big picture](/theme/thumbnail/algolia-dashboard-demo_full.png){:target="_blank"}

### frontend Javascript/Vue.js

```

```

## Liens

* [Site](https://www.algolia.com)
* [Documentation](https://www.algolia.com/doc)

```

```
