from utils import Table, ArrayContains
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


def DecodeInsertCommand(commandArr):
	# INSERT INTO TABLE <tableName> ( <val1> <val2> <val3>... )
	insertType = commandArr[2]
	name = str(commandArr[3]).upper()
	
	if insertType == "TABLE":
		table = TABLES[name]
		fillRow = []
		for i in range(
				commandArr.index("(") + 1,
				commandArr.index(")")
				):
			fillRow.append(commandArr[i])
		
		print(fillRow)
		for i in range(len(table.columns.keys())):
			print(list(table.columns.keys()))
			table.columns[list(table.columns.keys())[i]]["Values"].append(fillRow[i])

		TABLES[name] = table

	print(TABLES[name].columns)
	return insertType, name


def DecodeShowCommand(commandArr):
	# SHOW TABLE <tableName> ( <field1> <field2> ... )
	showType = commandArr[1]
	name = str(commandArr[2]).upper()
	OUTPUT = []

	if showType == "TABLE":
		table = TABLES[name]		
		keys = []
		if not ArrayContains(commandArr, '('):
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
				x.append(table.columns[key]['Values'][i])
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

