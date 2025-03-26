# TD TFIDF

Gautier KLEIN

## Instructions

Simplement executer main.py

## Données d'entrainement

Taille des textes d'entrainement

- Religion : 1129
- Sport : 3180
- Economie : 2264
- Politique : 1078

J'ai utilisé un LLM pour enrichir les données d'entrainement.

Le vocabulaire est composé des mots présents au moins 3 fois dans les textes
On supprime aussi la ponctuation, la casse, les nombres et les mots stops

Liste des mots stops :

``` {python}
mots_stop = {
    "alors", "au", "aucun", "aussi", "autre", "avant", "avec", "avoir", "bon", "car", 
    "ce", "cela", "ces", "cet", "cette", "comme", "comment", "dans", "des", "du", 
    "donc", "dont", "elle", "en", "encore", "est", "et", "être", "eux", "fait", "faites", 
    "fois", "hors", "ici", "il", "ils", "je", "juste", "la", "le", "les", "leur", 
    "lui", "mais", "malgré", "me", "même", "mes", "mon", "ne", "nos", "notre", "nous", 
    "ou", "où", "par", "parce", "pas", "peu", "peut", "plupart", "pour", "quand", 
    "que", "quel", "quelle", "quelles", "quels", "qui", "sans", "ses", "si", "son", 
    "sont", "sous", "sur", "ta", "tandis", "tellement", "tels", "tes", "ton", "tous", 
    "tout", "trop", "très", "tu", "voient", "vont", "votre", "vous", "vu", "à", "aux", "de", "l"
}
```

## Résultats

Voici une matrice de confusion obtenue, le résultat est satisfaisant au vue de la diagonale de la matrice qui est plus élevée que le reste.

``` {python}
[0.0006416702728135874, 3.449976488218847e-05, 5.114410736600634e-05, 4.167896340462922e-05]
[2.2662936682312776e-05, 0.0009030285021826957, 1.447573112099333e-05, 2.0202505267855933e-05]
[7.331068482483027e-05, 3.350808353851967e-05, 0.000634355887921586, 4.7237729682354336e-05]
[4.421433526629071e-05, 3.6670609387177526e-05, 1.7366097225042364e-05, 0.0006418469547596783]
```

Remarquez les puissances négative après les résultats, on peut croire à première vue que les valeurs de la diagonale sont plus faibles mais elles ne le sont pas.
