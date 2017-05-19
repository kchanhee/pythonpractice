test = "<thing>bob</thing><bob><yolo>lol</yolo><zxc>stuff</zxc></bob>"
 
# read the left bracket and get the key inside
def parse_begin_bracket(text, index):
    if text[index] == "<":
        key = ""
        index += 1
        while text[index] != ">":
            key = key + text[index]
            index += 1
        return key
    # program should never reach this return statement
    return None
 
# read the right bracket and check inside. return None if this index isn't part of
# the closing bracket
def attempt_to_parse_closing_bracket(text, index):
    if index < len(text) - 1 and text[index] == "<" and text[index + 1] == "/":
        key = ""
        index += 2
        while text[index] != ">":
            key = key + text[index]
            index += 1
        return key
    return None
 
# recursive solution: treat the nested string between the begin and end brackets
# of a key as a sub problem. The key's value in a dictionary should be the solution
# to this sub problem
def parse_xml(text):
    if len(text) == 0:
        return ""
    elif text[0] == "<":
        key_dict = {}
        index = 0
        while index < len(text):
            # get the key of the first bracket
            key = parse_begin_bracket(text, index)
            index = index + len(key) + 2
            nest = ""
            # keep adding text to the nested string until you read the end bracket of this key
            while attempt_to_parse_closing_bracket(text, index) != key:
                nest = nest + text[index]
                index += 1
            index = index + len(key) + 3
            # solve the sub problem and put it in the dictionary
            key_dict[key] = parse_xml(nest)
        return key_dict
    else:
        # if it's just text, return that text
        return text
 
print(parse_xml(test))


# global NUM_LESS
# global NUM_GREATER
# global CLASS
# global IS_KEY
# global IS_VALUE


# def xmlParser(inputStr):
# 	NUM_LESS = 0
# 	NUM_GREATER = 0
# 	CLASS = 0
# 	IS_KEY = False
# 	IS_VALUE = True
# 	key_stack = []
# 	value_stack = []
# 	outDict = {}
# 	key = ""
# 	value = ""
# 	for i in range(0,len(inputStr)):
# 		char = inputStr[i]
		
# 		if inputStr[i] == "<":
# 			NUM_LESS += 1
# 			CLASS += 1
# 			if len(key) > 0:
# 				key_stack.append(key)
# 			if len(value) > 0:
# 				value_stack.append(value)
# 			print("key_stack ",key_stack)
# 			print("current Key:", key) 
# 			print("value_stack",value_stack)
# 			print("current_value:", value)
# 			key = ""
# 			value = ""	
# 			IS_KEY = True
# 			IS_VALUE = False
# 			continue
# 		if inputStr[i] == "/": # closing of the class
# 			NUM_LESS -= 2
# 			CLASS -= 1
# 			continue
# 		if inputStr[i] == ">":
# 			NUM_GREATER += 1
# 			IS_KEY = False
# 			IS_VALUE = True
# 			if len(key_stack) == 1:
# 				outDict[key_stack[0]] = value_stack[0]
# 			elif len(key_stack) >= 1:
# 				temp = {key_stack.pop():0}
# 				for i in range(len(value_stack)):
# 					temp[temp.keys()[0]] = value_stack.pop()
				
# 			continue


# 		if IS_KEY:
# 			key += char
# 		if IS_VALUE:
# 			value += char
# 	return outDict

# test = "<thing>bob</thing><bob><yolo>lol</yolo><zxc>stuff</zxc></bob>"
# print(xmlParser(test))

