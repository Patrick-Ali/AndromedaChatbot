import dataControl as data

#global op
#global numbers

def multi(num1, num2):
    num = num1*num2
    return num

def add(num1, num2):
    num = num1 + num2
    return num

def minus(num1, num2):
    num = num1-num2
    return num

def div(num1, num2):
    num = num1/num2
    return num

def getNum(num):
    nums = data.loadData("numbers")
    print(num.lower())
    for element in nums:
        print(element)
        print(element == num)
        if nums[element] == num.lower() or element == num:
            print("Working")
            print(nums[element])
            numb = int(element)
            print(numb)
            return numb
        
    return "Unkown Number"

def getOp(text):
    testing = data.loadData("math")
    for i in testing:
        if i == text:
            return i
        else:
            for j in testing[i]:
                if j == text:
                    return i
    return "Unkown Operator"

def translate(inputNum):
    op = []
    numbers = []
    if type(inputNum) != str:
        return "Can't work with that input"
    text = data.brokenWords(inputNum)
    print(text)
    for i in text:
        print(i)
        temp = getOp(i)
        if temp != "Unkown Operator":
            op.append(temp)
            print(op)
            continue
        else:
            tempNum = getNum(i)
            if tempNum != "Unkown Number":
                print("wORKING ")
                numbers.append(tempNum)
                print(numbers)
                continue
            
    if len(op) != 0 and  len(numbers) > 1:
        if op[0] == 'multi':
            ans = multi(numbers[0], numbers[1])
            print(ans)
            del op[0]
            del numbers[0]
            del numbers[0]
            return ans
        elif op[0] == 'div':
            ans = div(numbers[0], numbers[1])
            del op[0]
            del numbers[0]
            del numbers[0]
            return ans
        elif op[0] == 'add':
            ans = add(numbers[0], numbers[1])
            del op[0]
            del numbers[0]
            del numbers[0]
            return ans
        elif op[0] == 'minus':
            ans = minus(numbers[0], numbers[1])
            del op[0]
            del numbers[0]
            del numbers[0]
            return ans
    
    return "Can't work with that input"


if __name__ == "__main__":
    test = input("Enter a test calc:")
    translate(test)
    #print(op)
    #print(numbers)
