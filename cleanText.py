import string
import re

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

number_regex = r"^-?\d+(\.\d+)?$"

def prepare_text(plainText : str):
    plainText = plainText.lower()
    plainText = remove_ponctuation(plainText)
    splitText = re.split(r"[ '’]", plainText)
    return remove_stop_words(splitText)

def remove_stop_words(splitText : list[str]):
    return [word for word in splitText if (word not in mots_stop and not re.fullmatch(number_regex, word))]

def remove_ponctuation(plainText : str):
    return plainText.translate(str.maketrans('', '', string.punctuation + "«»--"))
    