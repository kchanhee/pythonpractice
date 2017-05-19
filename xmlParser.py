# global NUM_LESS
# global NUM_GREATER
# global CLASS
# global IS_KEY
# global IS_VALUE


def xmlParser(inputStr):
	NUM_LESS = 0
	NUM_GREATER = 0
	CLASS = 0
	IS_KEY = False
	IS_VALUE = True
	key_stack = []
	value_stack = []
	outDict = {}
	key = ""
	value = ""
	for i in range(0,len(inputStr)):
		char = inputStr[i]
		
		if inputStr[i] == "<":
			NUM_LESS += 1
			CLASS += 1
			if len(key) > 0:
				key_stack.append(key)
			if len(value) > 0:
				value_stack.append(value)
			print("key_stack ",key_stack)
			print("current Key:", key) 
			print("value_stack",value_stack)
			print("current_value:", value)
			key = ""
			value = ""	
			IS_KEY = True
			IS_VALUE = False
			continue
		if inputStr[i] == "/": # closing of the class
			NUM_LESS -= 2
			CLASS -= 1
			continue
		if inputStr[i] == ">":
			NUM_GREATER += 1
			IS_KEY = False
			IS_VALUE = True
			if len(key_stack) == 1:
				outDict[key_stack[0]] = value_stack[0]
			elif len(key_stack) >= 1:
				temp = {key_stack.pop():0}
				for i in range(len(value_stack)):
					temp[temp.keys()[0]] = value_stack.pop()
				
			continue


		if IS_KEY:
			key += char
		if IS_VALUE:
			value += char
	return outDict


test = "<thing>bob</thing><bob><yolo>lol</yolo><zxc>stuff</zxc></bob>"
print(xmlParser(test))