import cleanText, cosdist, split, tfidf

# lire les fichiers
with open("eco.txt", "r", encoding="utf-8") as fichier:
    ecoText = fichier.read()

with open("sport.txt", "r", encoding="utf-8") as fichier:
    sportText = fichier.read()

with open("reli.txt", "r", encoding="utf-8") as fichier:
    reliText = fichier.read()

with open("poli.txt", "r", encoding="utf-8") as fichier:
    poliText = fichier.read()

#préparation des données
ecoTextSplit = cleanText.prepare_text(ecoText)
eco80, eco20 = split.split_text(ecoTextSplit)

sportTextSplit = cleanText.prepare_text(sportText)
sport80, sport20 = split.split_text(sportTextSplit)

reliTextSplit = cleanText.prepare_text(reliText)
reli80, reli20 = split.split_text(reliTextSplit)

poliTextSplit = cleanText.prepare_text(poliText)
poli80, poli20 = split.split_text(poliTextSplit)

allSplitText = [eco80, sport80, reli80, poli80]

#créer le vocabulaire
vocabulaire = tfidf.create_word_table(allSplitText)
print(vocabulaire)

#vectorisation texte 80
ecoVectorized = tfidf.vectorize_text_tfidf(allSplitText, eco80, vocabulaire)
reliVectorized = tfidf.vectorize_text_tfidf(allSplitText, reli80, vocabulaire)
sportVectorized = tfidf.vectorize_text_tfidf(allSplitText, sport80, vocabulaire)
poliVectorized = tfidf.vectorize_text_tfidf(allSplitText, poli80, vocabulaire)

#vectorisation texte 20 avec voc des texte 80
ecoVectorizedTest = tfidf.vectorize_text_tfidf(allSplitText, eco20, vocabulaire)
reliVectorizedTest = tfidf.vectorize_text_tfidf(allSplitText, reli20, vocabulaire)
sportVectorizedTest = tfidf.vectorize_text_tfidf(allSplitText, sport20, vocabulaire)
poliVectorizedTest = tfidf.vectorize_text_tfidf(allSplitText, poli20, vocabulaire)

trainVects = [ecoVectorized, reliVectorized, sportVectorized, poliVectorized]
testVect = [ecoVectorizedTest, reliVectorizedTest, sportVectorizedTest, poliVectorizedTest]

# calcul de la matrice de confusion
confmatrix = []
for i in range(0, len(allSplitText)):
    line = []
    for j in range(0, len(allSplitText)):
        line.append(cosdist.distance_cosinus(trainVects[i], testVect[j]))
    confmatrix.append(line)

print("Taille eco : ", len(eco80))
print("Taille sport : ", len(sport80))
print("Taille reli : ", len(reli80))
print("Treli poli : ", len(poli80))

print("Matrice de confusion : ")
print("Eco, sport, reli, poli")

for line in confmatrix:
    print(line)










