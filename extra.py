def compareSmallest(values):
    rawValues = getRawValue(values)
    smallest = rawValues[0]
    for val in rawValues:
        if val < smallest:
            largest = val
    print(largest)
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

    "Orbit Distance":["further", "more distant", "more remote", "remoter", "furthest"]
    "Number Moons": ["Moons"]