import requests

def saveFile(url):
    request = requests.get(url=url).content
    open('shakespeare.txt', 'wb').write(request)

def addToDict(gramDict, key):
    if key in gramDict.keys():
        gramDict[key] += 1
    else:
        gramDict[key] = 1

def topTen(gramDict):
    return sorted(gramDict.items(), key=lambda x:x[1], reverse=True)

def main():
    saveFile('https://www.gutenberg.org/cache/epub/100/pg100.txt')

    with open('shakespeare.txt', 'r') as f:
        text = f.read().split()

    n = len(text)

    twoGram = {}
    threeGram = {}
    fourGram = {}
    fiveGram = {}

    for i in range(0, n):
        twos = ' '.join(text[i:i+2])
        threes = ' '.join(text[i:i+3])
        fours = ' '.join(text[i:i+4])
        fives = ' '.join(text[i:i+5])

        addToDict(twoGram, twos)
        addToDict(threeGram, threes)
        addToDict(fourGram, fours)
        addToDict(fiveGram, fives)

    twoGram = topTen(twoGram)[:10]
    threeGram = topTen(threeGram)[:10]
    fourGram = topTen(fourGram)[:10]
    fiveGram = topTen(fiveGram)[:10]

    allGrams = [twoGram, threeGram, fourGram, fiveGram]

    for num in range(2, 6):
        print("Top 10 n-grams of length {0}:".format(num))

        counter = 1
        for gram in allGrams[num-2]:
            print("{0}. '{1}' : {2}".format(counter, gram[0], gram[1]))
            counter += 1

        print("\n\n\n")

if __name__ == '__main__':
    main()
