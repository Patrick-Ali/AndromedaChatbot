import json
from nltk import word_tokenize as wt

#data = {}

def addData(file, data):
    end = '.json'
    full = str(file+end)
    with open(full, 'w') as f:
        json.dump(data,f)

def getData(file, key, value = None): #, value
    end = '.json'
    full = str(file+end)
    with open(full, 'r') as f:
        data = json.load(f)
    if value == None:
        return data[key]#[value]
    else:
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

def generalInfo(inputText, file):
    #hold = brokenWords(inputText)
    hold = loadData(file)
    for i in hold:
        if inputText == i:
            return hold[i]
    return specificInfo(inputText)

def categorySearch(category, text):
    config = getData('config', 'infoFiles')
    data = loadData(config[category])
    print("It works")
    pot = []
    for element in data:
        pot.append({element:data[element]})
    print("Data \n", pot)
    print(text)
    return compareData(text, pot)

def specificInfoP1(inputText):
    config = getData('config', 'infoFiles')
    print(config)
    count = 0
    hold = brokenWords(inputText)
    text = translate(hold)
    print("Text is ", text)
    potential = []
    unique = 0
    previousHit = ''
    while count < len(config): 
        data = loadData(config[count])
        print(config[count])
        count += 1
        for element in data:
            print("Element ", element)
            for word in text:
                print('Start ', count)
                print('Word ', word)
                if word == config[count-1]:
                    print("Category Found")
                    print(config[count])
                    #categorySearch(count-1, hold)
                    return categorySearch(count-1, hold)
                if element == word or element.lower() == word or element == (word+"'s") or element.lower() == (word+"'s"):
                    if element != previousHit:
                        unique += 1
                    previousHit = element
                    potential.append({element:data[element]})
    if unique < 2:
        return specificInfoP2(hold, potential)
    elif unique > 2 and ('to' in hold or 'from' in hold):
        return distanceToObject(hold, potential)
    else:
        return compareData(hold, potential)

#def checkKey(key, word)
def distanceToObject(inputText, info):
    hold = specificInfoP2(inputText, info)
    print("Holdaro ", hold)
    first = hold[0]
    against = 0
    tempHold = []
    test = ''
    print("First Len ", len(first))
    if len(first) > 0:
        check = first[-1]
        print('Checked ', check)
        for key in check:
            against = check[key]
            print(against)
        i = 0
        while i < (len(first)-1):
            temp = first[i]
            for key in temp:
                print("Kiloro ", key)
                tempAgainst = temp[key]
                print(tempAgainst)
                tempSet = against-tempAgainst
                print(tempSet)
                tempHold.append({key:tempSet})
            i += 1
        print('TH ', tempHold)
        if 'to' in inputText:
            test = compareSmallest(tempHold)
        elif 'from' in inputText:
            test = compareLargest(tempHold)
        print('Testaro ', test)
            #specificInfoP1('closest to earth venus mercury')
    return test

def specificInfoP2(inputText, info):
    potentialInfo = []
    print("Hello 1 ", inputText)
    print(info)
    lastWord = ''
    tempInfo = []
    count = 0
    counting = 0
    keys = []
    usedKey = []
    held = []
    for element in info:
        #tempInfo.append(info[counting])
        #counting += 1
        for key in element:
            keys.append(key)
            print('Key2 ', key)
            print('Info2 ', info[counting][key])
            tempInfo.append(info[counting][key])
            counting += 1
    print("Temp info2 ", tempInfo)    
    for element in tempInfo:
        print("Element2 ", element)
        print("Corosponding key2 ", keys[count])
        for key in element:
            
            for word in inputText:
                print('Word ', word)
                print("Key ", key)
                print("Potential Word ", lastWord+' '+word)
                tempHold = word.split(" ")
                if len(tempHold) > 1:
                    print("tempHold ", tempHold)
                    counting = 0
                    for entry in tempHold:
                        print("Entry ", entry)
                        print("Key ", key)
                        extraHelp = translate(entry)
                        print("Extra Help ", extraHelp)
                        move = counting
                        if counting + 1 < len(tempHold):
                            move = counting + 1
                        print('Move ', (lastWord+' '+entry+' '+tempHold[move]))
                        print('Move2', (entry+' '+tempHold[move]))
                        if key == entry or key == (lastWord+' '+entry) or key == extraHelp or key == (lastWord+' '+entry+' '+tempHold[move]) or key == (entry+' '+tempHold[move]):
                            print('Key found')
                            addInfo = True
                            print('Keys Count ', keys[count])
                            print('pInfo1 ', potentialInfo)
                            for i in potentialInfo:
                                if keys[count] in i:
                                    print("I is ", i)
                                    print('Keys Count ', keys[count])
                                    print('Check ', element[key])
                                    #print('pInfo ', potentialInfo[keys[count]])
                                    print('eKey ', element[key])
                                    if element[key] == i[keys[count]]:  #potentialInfo[keys[count]] == element[key]:
                                        addInfo = False
                            hopeing = True
                            if hopeing == True: #addInfo == True: keys[count] not in potentialInfo or
                                print('pInfo3 ', potentialInfo)
                                print({keys[count]:element[key]})
                                if addInfo == True:
                                    potentialInfo.append({keys[count]:element[key]})
                                print('key used ', key)
                                if (counting + 1) < len(tempHold):
                                    print('TH ', tempHold[counting + 1])
                                    print('LW ', lastWord)
                                    usedKey.append(lastWord + ' ' + tempHold[counting + 1])
                                    usedKey.append(tempHold[counting + 1] + ' ' + lastWord)
                                    usedKey.append(key + ' ' + tempHold[counting + 1])
                                    usedKey.append(tempHold[counting + 1] + ' ' + key)
                                    usedKey.append(lastWord+' '+key)
                                    usedKey.append(key+' '+lastWord)
                                    usedKey.append(lastWord+' '+entry+' '+tempHold[counting+1])
                                else:
                                    print('TH2 ', tempHold[counting])
                                    print('LW2 ', lastWord)
                                    usedKey.append(lastWord + ' ' + tempHold[counting])
                                    usedKey.append(tempHold[counting] + ' ' + lastWord)
                                    usedKey.append(key + ' ' + tempHold[counting])
                                    usedKey.append(tempHold[counting] + ' ' + key)
                                    usedKey.append(lastWord+' '+key)
                                    usedKey.append(key+' '+lastWord)
                                    usedKey.append(lastWord+' '+entry+' '+tempHold[counting])
                                    print(key + ' ' + tempHold[counting])
                                    #specificInfoP1('most moons earth mars')
                        lastWord = entry
                        counting += 1
                if key == word or key == (lastWord+' '+word):
                    if keys[count] in potentialInfo:
                        if potentialInfo[keys[count]] != element[key]:
                            potentialInfo.append({keys[count]:element[key]})
                    usedKey.append(key)
                    lastWord = word
        count += 1
    print("Kilo ", usedKey)
    print("Pot ", potentialInfo)
    held.append(potentialInfo)
    held.append(usedKey)
    return held #potentialInfo

def compareData(inputText, info):
    hold = specificInfoP2(inputText, info)
    values = hold[0]
    print(values)
    keyWords = loadData("keyWords")
    key = ''
    print('Testel ', hold[1])
    for i in hold[1]:
        print("val1 ", i)
        if i in keyWords["keywords"]:
            #key += i + ' '
            key = i
    print("KeyLime ", key)
    
    actions = loadData("actions")
    for action in actions:
        print("Actions ", action)
        for actionKey in actions[action]:
            print("Action ", actionKey)
            if actionKey == key:
                key = action
    
##    if key == "Diameter":
##        key = "largest"
##    if key == "Diameter smallest":
##        key = "smallest"
    print("Yolo Key is ", key)
    if key == "largest":
        return compareLargest(values)
    elif key == "smallest":
        return compareSmallest(values)
    else:
        return values
##    count = 0
##    rawVals = []
##    for i in values:
##        print(i)
##        for j in i:
##            print(values[count][j])
##            print(type(values[count][j]))
##            rawVals.append(values[count][j])
##        count += 1
##    count = 0
##    highest = rawVals[0]
##    for val in rawVals:
##        if val > highest:
##            highest = val
##    print(highest)
##    lp = ''
##    for i in values:
##        print(i)
##        for j in i:
##            if values[count][j] == highest:
##                print(j)
##                lp = j
##            #print(values[count][j])
##            #print(type(values[count][j]))
##            #rawVals.append(values[count][j])
##        count += 1
##    
##    return lp

def getRawValue(values):
    count = 0
    rawVals = []
    for i in values:
        print(i)
        for j in i:
            print(values[count][j])
            print(type(values[count][j]))
            rawVals.append(values[count][j])
        count += 1
    return rawVals

def compareSmallest(values):
    rawValues = getRawValue(values)
    smallest = rawValues[0]
    for val in rawValues:
        if type(val) == int or type(val) == float:
            if val < smallest:
                smallest = val
    print(smallest)
    smallestEntry = ''
    count = 0
    for entry in values:
        print(entry)
        for key in entry:
            if values[count][key] == smallest:
                print(key)
                smallestEntry = key
            #print(values[count][j])
            #print(type(values[count][j]))
            #rawVals.append(values[count][j])
        count += 1
    
    return smallestEntry

def compareLargest(values):
    rawValues = getRawValue(values)
    largest = rawValues[0]
    for val in rawValues:
        if type(val) == int or type(val) == float:
            if val > largest:
                largest = val
    print(largest)
    largestEntry = ''
    count = 0
    for entry in values:
        print(entry)
        for key in entry:
            if values[count][key] == largest:
                print(key)
                largestEntry = key
            #print(values[count][j])
            #print(type(values[count][j]))
            #rawVals.append(values[count][j])
        count += 1
    
    return largestEntry

def translate(inputText):
    data = loadData("translate")
    text = inputText
    print(text)
    print("Text length ", len(text))
    lastWord = ''
    #count = 0
    for entry in data:
        print(entry)
        #print(count)
        #count = 0
        for words in data[entry]:
            print(words)
            count = 0
            if type(text) == list:
                for word in text:
                    print("Happy ", word)
                    print("Testaro ", lastWord+' '+word)
                    move = count
                    if count + 1 < len(text):
                        move = count+1
                    if words == word or words.lower() == word or words == lastWord+' '+word or words == lastWord+' '+word+' '+text[move]:
                        print("Word found ", word)
                        print(text)
                        print(count)
                        text[count] = entry
                    lastWord = word
                    count += 1
            else:
                if words == text or words.lower() == text:
                        print("Word found ", text)
                        print(text)
                        #print(count)
                        text = entry
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
