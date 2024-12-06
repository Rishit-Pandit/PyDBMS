import numpy as np
import pandas as pd


# Main Variables
commands = [
	"CREATE", 
	"ALTER", 
	"DROP", 
	"TRUNCATE", 
	"RENAME", 
	"SELECT", 
	"INSERT", 
	"UPDATE", 
	"DELETE", 
	"SAVE", 
	"GRANT", 
	"REVOKE", 
	"COMMIT", 
	"ROLLBACK", 
	"SAVEPOINT", 
	"SET_TRANSACTION", 
	"QUIT"
	"*"
]

TABLES = {}
REPORTS = {}
FORMS = {}

class Params():
	def __init__(self):
		self.KEY = "KEY"
		self.PRIMARY = "PRIMARY"
		self.FORGEIN = "FORGEIN"
		self.NOTNULL = "NOTNULL"
		self.NULL = "NULL"

class Type():
	def __init__(self, charLimit):
		self.valTypes = {
			"INT" : ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'],
			"STR" : ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '!', '@', '#', '$', '%', '^', '&', '*', '-', '+', '=', '_'],
			}


# Main Classes
class Table():
	"""docstring for Table"""
	def __init__(self, name):
		super(Table, self).__init__()
		self.name = name
		self.columns = {}

	def __str__(self):
		return self.name

	def addColumn(self, colName, valType, params=[]):
		self.columns[colName] = {"Values": [], "Type": valType, "Params": params}

	def addValues(self, values):
		if values.length == self.columns.keys.length:
			for i, key in enumerate(self.columns.keys):
				if self.check(self.columns[keys]["Type"], values[i]):
					self.columns[key]["Values"] = values[i]
				else:
					RaiseValueError("Incorrect DataType used in Values!")

	def check(self, valType, val):
		for i in val:
			print(i)
			if ArrayContains(Type.valTypes[valType], i) == False:
				return False
		return True

	def dropColumn(self, colName):
		del self.columns[colName]


	def hasColumn(self, colName):
		return ArrayContains(list(self.columns.keys()), colName)


# Helper Functions
def ArrayContains(arr, obj):
	'''
	arr: the array to check
	obj: the object to find
	'''
	contained = False
	for i in  arr:
		if i == obj:
			contained = True
			return True
		else:
			pass
	return contained


def processCommandStr(x):
	'''
	x: command string to process
	'''
	if x == None:
		return ''
	if len(x) <= 0:
		return ''
	x = x.split(" ")
	if ArrayContains(x, ''):
		x = preProcessStr(x)
	for i, o in enumerate(x):
		if o[0] == '(' and o != "(":
			x[i] = o[1:]
			x.insert(i, "(")
		elif o[-1] == ')' and o != ")":
			x[i] = o[:-1]
			x.insert(i+1, ")")
		elif o[0] == "'" and o != "'":
			x[i] = o[1:]
			x.insert(i, "'")
		elif o[-1] == "'" and o != "'":
			x[i] = o[:-1]
			x.insert(i+1, "'")
		elif o[0] == "\n":
			x[i] = o[1:]
		elif o[-1] == "\n":
			x[i] = o[:-1]
	return x


def preProcessStr(x):
	for i in range(len(x)):
		if ArrayContains(x, ''):
			x.remove('')
	return x

def processDataArr(data, tags):
	arr = []
	data2 = data
	for i in tags:
		if i[1] == "STR":
			arr.append(" ".join(data2[data2.index("'")+1 : data2.index("'", 1)]))
			data2 = data2[data2.index("'", 1)+1 :]
			print(data2)
		elif i[1] == "INT":
			try:
				int(data2[0])
			except Exception as e:
				raise RaiseValueError('value not int')
			arr.append(data2[0])
			data2 = data2[1:]
			print(data2)
		else:
			arr.append(data2[0])
			data2 = data2[1:]
			print(data2)
	return arr

def condMet(x, cond):
	opp, val = cond
	if opp == "=":
		return x == val
	elif opp == "!=":
		return x != val
	elif opp == ">":
		print(type(val))
		return x > val
	elif opp == "<":
		return x < val
	elif opp == ">=":
		return x >= val
	elif opp == "<=":
		return x <= val