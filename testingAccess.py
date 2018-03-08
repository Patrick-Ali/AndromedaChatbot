Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> test = {"testing":"Print"}
>>> def printTest(word):
	print(word)

	
>>> testaro = "I am testing this"
>>> for key in test:
	if key in testaro:
		if test[key] == "Print":
			printTest(testaro)

			
I am testing this
>>> for i in testing:
	print(i)

	
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    for i in testing:
NameError: name 'testing' is not defined
>>> for i in test:
	print(i)

	
testing
>>> helping = []
>>> helping.append(test['testing'])
>>> print(helping)
['Print']
>>> test["trial"] = {"testaro":"testing", "testra":"Hope"}
>>> helping.append(test["trial"])
>>> print(helping)
['Print', {'testaro': 'testing', 'testra': 'Hope'}]
>>> def specificInfo(inputText):
    config = getData('config', info)
    count = 0
    hold = brokenWords(inputText)
    potential = []
    while count < len(config): 
        data = loadData(config[count])
        count += 1
        for element in data:
            for word in hold:
                if element == word:
                    potential.append(data[element])
    return potential

>>> 
