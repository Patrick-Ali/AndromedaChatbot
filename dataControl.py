import json
from nltk import word_tokenize as wt

#data = {}

def addData(file, data):
    '''Add data to a specific file'''
    end = '.json'
    full = str(file+end)
    with open(full, 'w') as f:
        json.dump(data,f)

def getData(file, key, value = None): #, value
    '''Open a file and get the specific data from it'''
    end = '.json'
    full = str(file+end)
    with open(full, 'r') as f:
        data = json.load(f)
    if value == None:
        return data[key]#[value]
    else:
        return data[key][value]

def loadData(file):
    '''Open a file and get all the data from it'''
    end = '.json'
    full = str(file+end)
    with open(full, 'r') as f:
        data = json.load(f)
    return data

def brokenWords(inputText):
    '''Break a sentence into the words (tokens) that make it up'''
    hold = wt(inputText)
    return hold

def generalInfo(inputText, file):
    #hold = brokenWords(inputText)
    hold = loadData(file)
    for i in hold:
        if inputText == i:
            return hold[i]
    return specificInfo(inputText)

def remember(text):
    '''Add information to remember'''
    addData("remember", text)

def getMemory():
    '''Load the chatbots memory'''
    data = loadData("remember")
    print("Data ", data)
    return data


def cleaningData(text, data):
    '''Determin if the user wants anything extra, e.g. compare all planets and dwarf planets'''
    count = 0
    extra = []
    while count < len(text):
        if text[count] == 'exclude':
            counting = count
            while counting < len(text):
                counting += 1
                for elment in data:
                    if text[counting] == element:
                        extra.append(element)
                    elif text[counting] == 'and' or text[counting] == 'also':
                        continue
                    else:
                        break
        count += 1
    return extra

def categorySearch(category, text, trans):
    '''Gather all the information from a category'''
    config = getData('config', 'infoFiles')
    print("It works")
    pot = []
    try:
        holder = temp3(text, trans)
    except:
        holder = []
    print("Temp3 ", holder)
    for i in category:
        count = 0
        while count < len(config):
            if i == config[count]:
                data = loadData(config[count])
                testingData = cleaningData(text, data)
                print('TD ', testingData)
                for element in data:
                    if element not in text and element.lower() not in text:
                        pot.append({element:data[element]})
            count += 1
    print("Data \n", pot)
    print(text)
    if len(holder) == 0:
        return compareData(text, pot)
    else:
        return distanceToObject(text, pot, holder)

def trueStatement(inputText):
    '''Determine if the user input is a true or
    false question and then determine the validity of the statement'''
    #Is Neptune bigger than Earth
    lastWord = ''
    lookFor1 = ''
    lookFor2 = ''
    lookFor3 = ''
    count = 0
    prohibit = ['Which', "which", "what", "What", "how", "How"]
    trueState = False
    holder = brokenWords(inputText)
    text = translate(holder)
    potWords = []
    for element in text:
        print("Working 1")
        if lastWord in prohibit:
            print("Pro")
            trueState = False
            break
        if lastWord.lower() == 'is':
            print("Found is")
            trueState = True
            potWords.append(text[-1])
            if count < len(text):
                #lookFor1 = element
                potWords.append(element)
            if (count + 1) < len(text):
                #lookFor2 = text[count+1]
                potWords.append(text[count+1])
            if (count + 2) < len(text):
                #lookFor3 = text[count+2]
                potWords.append(text[count+2])
            break
        
        count += 1
        lastWord = element
    
    if trueState == False:
        return specificInfoP1(inputText)
    elif trueState == True:
        hold = specificInfoP1(inputText)
        #for word in hold:
        for entry in potWords:
            print("Ent", entry)
            print(type(entry))
            print("Hol", hold)
            print(type(hold))
            if hold == entry:
                return "True"
            elif type(hold) == str:
                if hold.lower() == entry:
                    return "True"
            try:
                tempInt = int(entry)
                if tempInt == hold:
                    return "True"
            except:
                continue
                    
        return 'False'


def temp3(text, trans):
    '''Determine the key components of a senetence'''
    config = getData('config', 'infoFiles')
    print(config)
    count = 0
    print("Text is ", text)
    print("Trans is ", trans)
    potential = []
    unique = 0
    previousHit = ''
    catSearch = []
    while count < len(config): 
        data = loadData(config[count])
        print(config[count])
        count += 1
        for element in data:
            print("Element ", element)
            for word in text:
                print('Start ', count)
                print('Word ', word)
                counter = 0
                if element == word or element.lower() == word or element == (word+"'s") or element.lower() == (word+"'s"):
                    if element != previousHit:
                        unique += 1
                    previousHit = element
                    potential.append({element:data[element]})

    
    tempInfo = specificInfoP2(trans, potential)
    holder = tempInfo[0][0]
    print("Ho ", holder)
    return holder

def specificInfoP1(inputText):
    '''starting point for determining the key components of a senetence'''
    config = getData('config', 'infoFiles')
    print(config)
    count = 0
    hold = inputText
    if type(inputText) == str:
        hold = brokenWords(inputText)
    text = translate(hold)
    print("Text is ", text)
    potential = []
    unique = 0
    previousHit = ''
    catSearch = []
    memoryHolder = []
    while count < len(config): 
        data = loadData(config[count])
        print(config[count])
        count += 1
        for element in data:
            print("Element ", element)
            for word in text:
                print('Start ', count)
                print('Word ', word)
                counter = 0
                while counter < len(config):
                    prevEnt = ''
                    for entry in text:
                        if entry == config[counter]:
                            if prevEnt != 'the':
                                catSearch.append(entry)
                                print("Category Found")
                                print(config[counter])
                        prevEnt = entry
                    counter += 1
                    #categorySearch(count-1, hold)
                if len(catSearch) > 0:
                    return categorySearch(catSearch, hold, text)
                if element == word or element.lower() == word or element == (word+"'s") or element.lower() == (word+"'s"):
                    if element != previousHit:
                        unique += 1
                    previousHit = element
                    #remember(element)
                    memoryHolder.append(element)
                    potential.append({element:data[element]})
    if len(memoryHolder) > 0:
        remember(memoryHolder)
    
    if unique < 2 and unique > 0:
        tempInfo = specificInfoP2(hold, potential)
        holder = tempInfo[0][0]
        if len(holder) == 0:
            return holder
        for element in holder:
            return holder[element]
    elif unique > 2 and ('to' in hold or 'from' in hold):
        return distanceToObject(hold, potential, [])
    elif len(potential) == 0:
        memory = getMemory()
        print(memory)
        if type(memory) == list:
            for element in memory:
                text.append(element)
        else:
            text.append(memory)
        print("Text ", text)
        return specificInfoP1(text)
    else:
        return compareData(hold, potential)

#def checkKey(key, word)
def distanceToObject(inputText, info, special):
    '''Determine the distance between objects'''
    hold = specificInfoP2(inputText, info)
    print("Holdaro ", hold)
    first = hold[0]
    against = 0
    tempHold = []
    test = ''
    print("First Len ", len(first))
    if len(first) > 0:
        if special == []:
            check = first[-1]
        else:
            check = special
        print('Checked ', check)
        for key in check:
            against = check[key]
            print(against)
        i = 0
        while i < len(first):
            temp = first[i]
            for key in temp:
                print("Kiloro ", key)
                tempAgainst = temp[key]
                print(tempAgainst)
                tempSet = abs(against-tempAgainst)
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
    '''Pick out the information that is needed to supply the user with output'''
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
                    print("KWF")
                    print(keys)
                    print(keys[count])
                    print(potentialInfo)
                    if {keys[count]:element[key]} in potentialInfo:
                        print("Hello extra")
                    else:
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
    '''Determine what action needs to be done to produce output'''
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

    print("Yolo Key is ", key)
    if key == "largest":
        return compareLargest(values)
    elif key == "smallest":
        return compareSmallest(values)
    else:
        return values


def getRawValue(values):
    '''Get values for comparisons'''
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
    '''Determine what the smallest value is'''
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
        count += 1
    
    return smallestEntry

def compareLargest(values):
    '''Determine what the largest value is'''
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
        count += 1
    
    return largestEntry

def translate(inputText):
    '''Translate the user input into something the chatbot can understand'''
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
    '''NOT IN USE'''
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
