import json
from nltk import word_tokenize as wt

#data = {}

def addData(file, data):
    end = '.json'
    full = str(file+end)
    with open(full, 'w') as f:
        json.dump(data,f)

def getData(file, key, value):
    end = '.json'
    full = str(file+end)
    with open(full, 'r') as f:
        data = json.load(f)
    return data[key][value]

def loadData(file):
    end = '.json'
    full = str(file+end)
    with open(full, 'r') as f:
        data = json.load(f)
    return data

def brokenWords(inputText):
    hold = wt(inputText)
    return hold

# File - Which category you want to update, e.g., planets
# Info - what information you want to add
# Categories -  the level you wish yo go, e.g. Mars - Moons - Phobes - Rotation
def addInfo(file, info, categories):
    data = loadData(file)
    tokens = wt(categories)
    words = [w for w in tokens]
    print(words)
    #print(data)
    if len(words) == 1:
        data[words[0]] = info
    elif len(words) == 2:
        data[words[0]][words[1]] = info
    elif len(words) == 3:
        data[words[0]][words[1]][words[2]] = info
    elif len(words) == 1:
        data[words[0]][words[1]][words[2]][words[3]] = info
    elif len(words) > 4 or len(words) == 0:
        msg = "Categories aren't right"
        return msg
    print(data[words[0]][words[1]])

if __name__ == "__main__":
    test = getData('planet', 'Earth', 'info')
    print(test)
