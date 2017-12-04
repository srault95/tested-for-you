# Démonstration Algolia Search

* Voir l'article correspondant sur le site
  [tested-for-you](https://tested-for-you.s2ltic.fr/algolia.html)

**Fichiers:**

```
datas.json: jeux de données
push-algolia.py: Script pour alimenter votre index
index.html: Web App vue.js
```

**Installation:**

> requis: python 3.5+

```
# pip install -r requirements.txt
# Ou
# pipenv --three && pipenv shell && pipenv install
```

**Avant l'execution du script**, pensez à mettre à jour les informations (app_id
et app_keys).

```bash
python push-algolia.py

python -m http.server 8080
```

**Ouvrez votre navigateur sur http://localhost:8080**
