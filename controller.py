import dataControl as data
import wordAnlysis as word

class AnalyseInput:   
    def __init__(self):
        print("Class initalized")

    def analyseWord(self, words):
        element = word.testForWord(words,[])
        print("Element is ", element)
        words = []
        if ',' in element[0]:
            print(element[0])
            print(len(element))
            for item in element[0]:
                words.append(item)
        else:
            words.append(element[0])
        return words

    def readInput(self, inputText):
        
        hold = inputText.split(" ")
        print("Hold is ", hold)
        temp = []
        for i in hold:

            if i == "Mercury":
                hold = data.getData('planet', 'Mercury', 'info')
                return hold
                #return(self.pDictionary["Mercury"])
            elif i == "Venus":
                hold = data.getData('planet', 'Venus', 'info')
                return hold
                #return(self.pDictionary["Venus"])
            elif i == "Earth":
                hold = data.getData('planet', 'Earth', 'info')
                return hold
            elif i == "Mars":
                hold = data.getData('planet', 'Mars', 'info')
                return hold
            elif i == "Jupiter":
                hold = data.getData('planet', 'Jupiter', 'info')
                return hold
            elif i == "Saturn":
                hold = data.getData('planet', 'Saturn', 'info')
                return hold
            elif i == "Uranus":
                hold = data.getData('planet', 'Uranus', 'info')
                return hold
            elif i == "Neptune":
                hold = data.getData('planet', 'Neptune', 'info')
                return hold
            else:
                test = self.analyseWord(i)
                for wordFound in test:
                    temp.append(wordFound)

        return temp
                
        #return("Nothing Found")

    def giveResponse(self, text):
        return 0


if __name__ == "__main__":
    test = AnalyseInput()
    print(test.readInput("Mercury"))
    print("\n")
    print(test.readInput("Venus"))
    print("\n")
    print(test.readInput("Hello Test"))
    #print(test.readInput("AppleIs"))
