from nltk.corpus import wordnet as wn, words as dictionary

def testForWord(words, tested):
    word = words.lower()
    wordLen = len(word)
    count = 0
    wordList = []
    testWord = ''
    sendWord = ''
    wordsTested = tested

    if word in dictionary.words():
        return [words, wordsTested]

    while wordLen > count:
        testWord += word[count]
        count += 1
        testing = testWord in dictionary.words()
        tested = testWord in wordList
        print("Current Word ", testWord)
        if tested == False:
            alreadyTested = testWord in wordsTested
            print("Word to be tested ", testWord)
            print("Previous test words", wordsTested)
            if testing == True and alreadyTested == False:
                wordList.append(testWord)
                print("Updated word list ", wordList)
                test4 = testWord in wordsTested
                if test4 == False:
                    wordsTested.append(testWord)
                testWord = ''
                #print(testWord+"2")
                if count < wordLen:
                    count2 = count
                    while count2 < wordLen:
                        sendWord += word[count2]
                        count2 += 1
                    print("Send Word is ", sendWord)
                    test4 = testWord in wordsTested
                    if test4 == False:
                        wordsTested.append(testWord)
                    extraList = testForWord(sendWord, wordsTested)
                    print("Extra List ", extraList)
                    sendWord = ''
                    if len(extraList[0]) > 0:
                        
                        if extraList[0] in dictionary.words() and (extraList[0] in wordList) == False:
                            wordList.append(extraList[0])
                            
                        for element in extraList[0]:
                           tested2 = element in wordList
                           if tested2 == False:
                               wordList.append(element)
                    if len(extraList[1]) > 0:
                        for element in extraList[1]:
                            tested2 = element in wordsTested
                            if tested2 == False:
                                wordsTested.append(element)
                        #wordList.append(extraList)
                    print(wordList)
                    count = 0
            test4 = testWord in wordsTested
            if test4 == False:
                wordsTested.append(testWord)

            
        
                
    return [wordList, wordsTested]
        #for i in word:

def getWordDef(word):
     hold = wn.synsets('car')
     print(hold)
     if len(hold) > 1:
         for element in hold:
             holding = element.definition()
             print(holding)
         correct = int(input('\n which is the correct deffenition?: '))
         print(correct)
     
if __name__ == "__main__":
    hold = testForWord("AppleIs", [])
    print(hold)
