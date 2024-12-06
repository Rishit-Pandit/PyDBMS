from utils import Table, ArrayContains, processDataArr, condMet
from utils import TABLES, REPORTS, FORMS


def createTable(name, fieldsArr):
	table = Table(name)
	for i in range(
			fieldsArr.index("(") + 1,
			fieldsArr.index(")"), 2
			):
		table.addColumn(fieldsArr[i], fieldsArr[i+1])
	return table


def DecodeCreateCommand(commandArr):
	# CREATE TABLE <TableName> ( <field1> <dType1> <field2> <dType2>... )
	createType = commandArr[1]
	name = str(commandArr[2]).upper()

	print(commandArr)

	if createType == "TABLE":
		table = createTable(name, commandArr[3:])
		TABLES[name] = table


	print(TABLES[name].columns)
	return createType, name


def DecodeDuplicateCommand(commandArr):
	# DUPLICATE TABLE <TableName> FROM <TableName> <EMPTY/FILL>
	dupType = commandArr[1]
	name = str(commandArr[2]).upper()
	oldName = str(commandArr[4]).upper()
	fill = str(commandArr[5]).upper()

	print(commandArr)

	if dupType == "TABLE":
		if fill == "FILL":
			table = TABLES[oldName]
			TABLES[name] = table
		elif fill == "EMPTY":
			table = TABLES[oldName]
			for key in table.columns.keys():
				table.columns[key]["Values"] = []
			TABLES[name] = table


	print(TABLES[name].columns)
	return dupType, name


def DecodeInsertCommand(arr):
	# INSERT INTO TABLE <tableName> FIELDS ( <field1> <field2> <field3>... ) VALUES ( <val1> <val2> <val3>... )
	insertType = arr[2]
	name = str(arr[3])

	print(arr)

	if insertType == "TABLE":
		table = TABLES[name]
		fillRow = []
		fillCol = []
		if arr[4] == "FIELDS":
			for i in range(
					arr.index("(") + 1,
					arr.index(")")
					):
				fillCol.append([arr[i], table.columns[arr[i]]["Type"]])
			for i in range(
					arr.index("(", arr.index("VALUES")) + 1,
					arr.index(")", arr.index("VALUES"))
					):
				fillRow.append(arr[i])
			
		elif arr[4] == "VALUES":
			for key in list(table.columns.keys()):
				fillCol.append([key, table.columns[key]["Type"]])
			for i in range(
					arr.index("(") + 1,
					arr.index(")")
					):
				fillRow.append(arr[i])
		
		print(fillRow)
		
		try:
			fillRow = processDataArr(fillRow, fillCol)
		except Exception as e:
			raise e

		for i, data in enumerate(fillCol):
			table.columns[data[0]]["Values"].append(fillRow[i])

		TABLES[name] = table

	print(TABLES[name].columns)
	return insertType, name


def DecodeShowCommand(commandArr):
	# SHOW TABLE <tableName> ( <field1> <field2> ... ) WHERE <field> <cond> <value>
	showType = commandArr[1]
	name = str(commandArr[2]).upper()
	OUTPUT = []
	cond = ArrayContains(commandArr, "WHERE")
	condition, whereLoc = [], 0
	if cond:
		whereLoc = commandArr.index("WHERE")
		condition = [commandArr[whereLoc+1], commandArr[whereLoc+2], int(commandArr[whereLoc+3])]
	if showType == "TABLE":
		table = TABLES[name]		
		keys = []
		if commandArr[3] != "(":
			keys = list(table.columns.keys())
		else:
			for i in range(
					commandArr.index("(") + 1,
					commandArr.index(")")
					):
				keys.append(commandArr[i])
		OUTPUT.append(keys)
		for i in range(len(table.columns[keys[0]]['Values'])):
			x = []
			for key in keys:
				if cond:
					if condMet(int(table.columns[condition[0]]['Values'][i]), condition[1:]):
						x.append(table.columns[key]['Values'][i])
				else:
					x.append(table.columns[key]['Values'][i])
			if len(x)>0:
				OUTPUT.append(x)


	return showType, name, OUTPUT


def DecodeSaveCommand(commandArr):
	# SAVE TABLE <TableName> FILE <fileName>
	Type = commandArr[1]
	name = str(commandArr[2]).upper()
	filename = str(commandArr[4])
	OUTPUT = []

	if Type == "TABLE":
		table = TABLES[name]
		with open(f'{filename}.csv', 'w') as file:
			keys = list(table.columns.keys())
			x = []
			for key in keys:
				x.append(key)
				x.append(table.columns[key]["Params"])
				x.append(table.columns[key]["Type"])
				x.append(table.columns[key]["Values"])
				for i in x:
					file.write(str(i)+";")
				file.write('\n')
				x = []

	return Type, name, filename


def DecodeLoadCommand(commandArr):
	# LOAD TABLE <TableName> FILE <fileName>
	Type = commandArr[1]
	name = str(commandArr[2]).upper()
	filename = str(commandArr[4])
	OUTPUT = []

	if Type == "TABLE":
		table = Table(name)
		with open(f'{filename}.csv', newline='') as csvfile:
			data = csv.reader(csvfile, delimiter=';', quotechar='\'')
			arr = []
			for row in data:
				row.pop(-1)
				arr = row
				
				field = arr[0]
				params = arr[1]
				valType = arr[2]
				values = arr[3]

				table.addColumn(field, valType, params)
				values = values[1:-2]
				values = stringToList(values)

				table.columns[field]['Values'] = values

		TABLES[name] = table
		print(table.columns)
				
	return Type, name, filename


def DecodeAlterCommand(commandArr):
	# ALTER TABLE <TableName> ADD <fieldName> <dType> <defaultVal>
	# ALTER TABLE <TableName> DROP <fieldName>
	# ALTER TABLE <TableName> CHANGE <fieldName> <newFieldName> <dType>
	Type = commandArr[1]
	name = str(commandArr[2]).upper()
	AlterType = str(commandArr[3])

	print(commandArr)

	if Type == "TABLE":
		table = TABLES[name]
		if AlterType == "ADD":
			table.addColumn(commandArr[4], commandArr[5])
			for n in table.columns[list(table.columns.keys())[0]]["Values"]:
				table.columns[commandArr[4]]["Values"].append(commandArr[6])

		elif AlterType == "DROP":
			table.dropColumn(commandArr[4])

		elif AlterType == "CHANGE":
			if table.hasColumn(commandArr[4]) == False:
				return Type, name, AlterType
			table.addColumn(commandArr[5], commandArr[6])
			table.columns[commandArr[5]]["Values"] = table.columns[commandArr[4]]["Values"]
			table.dropColumn(commandArr[4])

	return Type, name, AlterType

