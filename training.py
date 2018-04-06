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
    data = {}
    config = None
    add = ''
    print("To go back or exit enter end")
    try:
        config = loadData("config")
    except:
        data = {"infoFiles":[]}
        addData("config", data)
        config = loadData("config")
        print(config)
    while add != 'end':
        add = input("What do you want to do: ")
        if add == 'end':
            break
        if add.lower() == 'new category':
            confirmation = "no"
            while confirmation.lower() != "yes" or confirmation.lower() != "end":
                title = input("Category title: ")
                if title == "end":
                    break
                print("Cateory to add ", title)
                confirmation = input("Is this correct, yes or no: ")
                if confirmation == 'end':
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
                    
        
if __name__ == "__main__":
    main()
