import json
from nltk import word_tokenize as wt

#data = {}

def addData(file, data):
    end = '.json'
    full = str(file+end)
    with open(full, 'w') as f:
        json.dump(data,f)

def getData(file, key): #, value
    end = '.json'
    full = str(file+end)
    with open(full, 'r') as f:
        data = json.load(f)
    return data[key]#[value]

def loadData(file):
    end = '.json'
    full = str(file+end)
    with open(full, 'r') as f:
        data = json.load(f)
    return data

def brokenWords(inputText):
    hold = wt(inputText)
    return hold

def generalInfo(inputText, file):
    #hold = brokenWords(inputText)
    hold = loadData(file)
    for i in hold:
        if inputText == i:
            return hold[i]
    return specificInfo(inputText)

def specificInfoP1(inputText):
    config = getData('config', 'infoFiles')
    print(config)
    count = 0
    hold = brokenWords(inputText)
    text = translate(hold)
    potential = []
    unique = 0
    previousHit = ''
    while count < len(config): 
        data = loadData(config[count])
        #print(data)
        count += 1
        for element in data:
            print(element)
            for word in text:
                if element == word or element.lower() == word:
                    if element != previousHit:
                        unique += 1
                    previousHit = element
                    potential.append({element:data[element]})
    if unique < 2:
        return specificInfoP2(hold, potential)
    else:
        return compareData(hold, potential)

#def checkKey(key, word)


def specificInfoP2(inputText, info):
    potentialInfo = []
    print(inputText)
    print(info)
    lastWord = ''
    tempInfo = []
    count = 0
    counting = 0
    keys = []
    for element in info:
        #tempInfo.append(info[counting])
        #counting += 1
        for key in element:
            keys.append(key)
            print('Key ', key)
            print('Info ', info[counting][key])
            tempInfo.append(info[counting][key])
            counting += 1
    print("Temp info ", tempInfo)    
    for element in tempInfo:
        print("Element ", element)
        print("Corosponding key ", keys[count])
        for key in element:
            
            for word in inputText:
                print(word)
                print(key)
                print(lastWord+' '+word)
                if key == word or key == (lastWord+' '+word):
                    potentialInfo.append({keys[count]:element[key]})
                lastWord = word
        count += 1
    return potentialInfo

def compareData(inputText, info):
    values = specificInfoP2(inputText, info)
    print(values)
    count = 0
    rawVals = []
    for i in values:
        print(i)
        for j in i:
            print(values[count][j])
            print(type(values[count][j]))
            rawVals.append(values[count][j])
        count += 1
    count = 0
    highest = rawVals[0]
    for val in rawVals:
        if val > highest:
            highest = val
    print(highest)
    lp = ''
    for i in values:
        print(i)
        for j in i:
            if values[count][j] == highest:
                print(j)
                lp = j
            #print(values[count][j])
            #print(type(values[count][j]))
            #rawVals.append(values[count][j])
        count += 1
    
    return lp

def translate(inputText):
    data = loadData("translate")
    text = inputText
    print(text)
    for entry in data:
        print(entry)
        count = 0
        for words in data[entry]:
            print(words)
            for word in text:
                print(word)
                if words == word or words.lower() == word:
                    print("Word found ", word)
                    text[count] = entry
                count += 1
    print(text)
    return text

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
    test = getData('planet', 'Earth') #, 'info'
    print(test)
