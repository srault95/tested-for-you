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

**Un des points les plus important sur la sécurité** est qu'Algolia fournit deux
clés d'api pour communiquer avec leur services. L'une d'elles, sert aux
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

## Quickstart Démo

**[sources](https://github.com/srault95/tested-for-you/tree/master/demos/algolia)**

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

**index.html:**

```html
<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="utf-8">
  <meta http-equiv="x-ua-compatible" content="ie=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
  <title>Démonstration Algolia / Vue.js</title>
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" />
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css" />
  <style>
    .badge {
        float: right;
    }
  </style>
</head>
<body>
  <div id="app" class="container" style="margin-top: 20px;">
    <ais-index app-id="CXRBLEEQRP" api-key="111fde9bb941f02276e76a9c732651b6" index-name="demo">
        <div class="row">
            <div class="col-md-2">
                <h3>Search Démo</h3>
            </div>
            <div class="col-md-10" style="margin-top: 20px;">
                <ais-search-box placeholder="Recherchez un article..."></ais-search-box>
            </div>
        </div>
        <div class="row">
            <div class="col-md-2">
                <ais-tree-menu
                    :attributes="['tags']"
                    :sort-by="['count:desc']"
                    :class-names="{
                        'ais-tree-menu__list': 'list-unstyled',
                        'ais-tree-menu__count': 'badge badge-secondary'
                    }">
                    <h4 slot="header">Tags</h4>
                </ais-tree-menu>
            </div>
            <div class="col-md-10" id="content">
                <ais-results>
                    <template scope="{ result }">
                    <div class="search-result">
                        <div class="result__info">
                            <h4 class="result__name">
                                <i class="fa fa-bars"></i>
                                <a :href="result.url">
                                    <ais-highlight :result="result" attribute-name="title"/>
                                </a>
                            </h4>
                        </div>
                    </div>
                    </template>
                </ais-results>
            </div>
        </div>
    </ais-index>
  </div>
  <script src="https://unpkg.com/vue/dist/vue.js"></script>
  <script src="https://unpkg.com/vue-instantsearch@1.3.2/dist/vue-instantsearch.js"></script>
  <script>
    new Vue({
      el: '#app',
      data: {}
    })
  </script>
</body>
</html>
```

## Liens

* [Site](https://www.algolia.com)
* [Documentation](https://www.algolia.com/doc)
