---
Version: 1
Lang: fr
Title: gevent
Tags: coroutine, async, python, python3, lib
Summary: Librairie Python pour la programmation asynchrone avec les co-routines
Product_version: 1.2.2
Product_url: https://github.com/gevent/gevent
---

[TOC]

## Mes Commentaires

#### Points Positifs {: .text-success }

* Peu intrusif pour améliorer un code existant, grâce au monkey patch
* Une syntaxe clair et facile à prendre en main (que je regrette de ne pas avoir
  trouvé dans asyncio)
* Utilisé par de nombreuses
  [librairies et frameworks](https://github.com/gevent/gevent/wiki/Projects)

#### Points Négatifs {: .text-danger }

* Les performances sont maintenant dépassés pour certains besoins, par des
  frameworks comme [Sanic](https://github.com/channelcat/sanic) qui s'appuie sur
  [uvloop](https://github.com/MagicStack/uvloop) au lieu de
  [libev](http://libev.schmorp.de/) pour Gevent

## Fonctionnalités principales

* Boucle d'évènements [libev](http://libev.schmorp.de/)
* S'appuie sur [greenlet](http://pypi.python.org/pypi/greenlet)
* Socket amélioré
* Patchs pour les librairies Python standard (os, select, signal, ssl,
  subprocess, sys, thread, time, socket)
* Création de serveur WSGI asynchrone
* Création de serveur TCP/UDP
* Librairie DNS client basé sur [c-ares](http://c-ares.haxx.se/)

## Liens

* [Sources](https://github.com/gevent/gevent)
* [Documentation](http://www.gevent.org/)
* [Tutorial](http://sdiehl.github.io/gevent-tutorial/)
