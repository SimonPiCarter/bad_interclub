### Installation

## pré requis

Le script a été codé et testé en utilisant python3.

Il est conseillé de travailler dans un environnement virtual pour installer les composants requis pour le fonctionnement de ce module.

https://docs.python.org/fr/3/library/venv.html

Toutes les commandes suivantes sont à exécuter dans le répertoire principal du projet.

## installation des modules externes

Le fichier requirements.txt liste les dépendances externes requises.

Installer les dépendances externes : `pip install -r requirements.txt`

## script d'installation

Les modules internes sont la principale raison qui justifie un environnement virtuel (ces modules s'installent dans l'environnement python et sont nécessaires au fonctionnement interne du script, il n'est donc d'aucun intérêt de les installer de manière globale).

Installer les dépendances internes : `./setup.sh`

Si le message `Failed building wheel for opt` s'affiche vous pouvez l'ignorer.

## Tester

Une fois toutes les dépendances installées vous pouvez tester le script : `python3 ./src/test.py --input data/data.json`

Le résultat attendu est :

```
SH1 : 3
SH2 : 3
SH3 : 1
SH4 : 1
DH1 : 2
DH2 : 0
isMatchRankOk_Real_DH2_0 : 1
isMatchOrderOK_Real_DH1_Before_SH1 : 1
```

Un fichier `out.json` devrait avoir été généré.
