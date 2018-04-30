# Config infoFiles - Category names
# Categories - Fill out information
# Translate - Words that translate to information keys
# Keywords - Words that translate to actions
# Actions - Actions and triggerwords
# CRUD - Create, Read, Update, and Delete

import json

#Create and Update data
def addData(file, data):
    end = '.json'
    full = str(file+end)
    with open(full, 'w') as f:
        json.dump(data,f)

#Read data
def loadData(file):
    end = '.json'
    full = str(file+end)
    with open(full, 'r') as f:
        data = json.load(f)
    return data

#Get Specific data e.g. Planets -> Earth
def specificData(data, key1, depth, key2=None , key3=None):
    if depth == 1:
        return data[key1]
    elif depth == 2:
        return data[key][key2]
    elif depth == 3:
        return data[key][key2][Key3]
    return data

#Delete data
def deleteData(data, key1, depth, key2 = None, key3 = None):
    if depth == 1:
        del data[key1]
    elif depth == 2:
        del data[key][key2]
    elif depth == 3:
        del data[key][key2][Key3]
    print(data)
    return data

   

def main():
    '''Function will be run on a loop until user quits, will be used as the
    main point from which training will be conducted'''
    data = {}
    config = None
    keyWords = None
    actions = None
    translate = None
    add = ''
    print("To go back or exit enter end")
    try:
        config = loadData("config")
    except:
        data = {"infoFiles":[]}
        addData("config", data)
        config = loadData("config")
        print(config)
    try:
        keyWords = loadData("keyWords")
    except:
        data = {"keywords":[]}
        addData("keyWords", data)
        keyWords = loadData("keyWords")
        print(keyWords)
    try:
        actions = loadData("actions")
    except:
        data = {"smallest":[], "largest":[]}
        addData("actions", data)
        actions = loadData("actions")
        print(actions)
    try:
        translate = loadData("translate")
    except:
        data = {}
        addData("translate", data)
        translate = loadData("translate")
        print(translate)
    while add != 'end':
        add = input("What do you want to do: ")
        if add.lower() == 'end':
            break
        if add.lower() == 'add new category':
            confirmation = "no"
            while confirmation.lower() != "yes" or confirmation.lower() != "end":
                title = input("Category title: ")
                if title == "end":
                    break
                print("Cateory to add ", title)
                confirmation = input("Is this correct, yes or no: ")
                if confirmation.lower() == 'end':
                    break
                if confirmation.lower() == "yes":
                    confAdd = input("Do you want to add this, yes or no: ")
                    if confAdd == "yes":
                        print(config)
                        config["infoFiles"].append(title)
                        #print(data3)
                        addData("config", config)
                        #data3.append(title)
                        data2 = {}
                        addData(title, data2)
        if add.lower() == 'add new information':
            while True:
                category = input("Category name: ")
                if category == "end":
                    break
                holdInfo = loadData(category)
                depth = int(input("""Information level, maximum of three, e.g. planet->earth->size would be 3: """))
                if depth == "end":
                    break
                if depth == 1:
                    infoName = input("Subcategory name: ")
                    holdInfo[infoName] = {}
                    addData(category, holdInfo)
                elif depth == 2:
                    infoName = input("Subcategory name: ")
                    infoDataKey = input("Data key: ")
                    infoDataValue = input("Data key value: ")
                    if infoDataValue != "[]" and infoDataValue != "{}":
                        holdInfo[infoName][infoDataKey] = infoDataValue
                    elif infoDataValue == "[]":
                        holdInfo[infoName][infoDataKey] = []
                    addData(category, holdInfo)
                elif depth == 3:
                    infoName = input("Subcategory name: ")
                    infoDataKey = input("Data key: ")
                    #infoDataKey2 = input("Data subkey: ")
                    infoDataValue = input("Data key value: ")
                    #holdInfo[infoName][infoDataKey][infoDataKey2] = []
                    holdInfo[infoName][infoDataKey].append(infoDataValue)
                    addData(category, holdInfo)
                
                    
        
if __name__ == "__main__":
    main()
