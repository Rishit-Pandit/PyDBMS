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
			"BOOL" : ['1', '0', 'true', 'false'],
			"INT" : ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'],
			"DATE" : ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '/'],
			"CHAR" : ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],
			"VARCHAR" : ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '!', '@', '#', '$', '%', '^', '&', '*', '-', '+', '=', '_'],
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
def ArrayContains(arr, obj, sel="null"):
	'''
	arr: the array to check
	obj: the object to find
	'''
	contained = False
	for i in  arr:
		if i == obj or i == sel:
			contained = True
			return True
		else:
			pass
	return contained
