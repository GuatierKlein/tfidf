import random

def split_text(splitText : list[str]):
    text80 = []
    text20 = []

    size = len(splitText)

    for i in range(0, int(0.2 * size)):
        randomIndex = random.randint(0, size - i -1)
        text20.append(splitText[randomIndex])
        del splitText[randomIndex]

    text80 = splitText
    return text80, text20
