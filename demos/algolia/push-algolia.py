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
