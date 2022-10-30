from utils import Table
from utils import TABLES, REPORTS, FORMS


def DecodeCreateCommand(commandArr):
	# CREATE TABLE <TableName> ( <field1> <dType1> <field2> <dType2>... )
	createType = commandArr[1]
	name = str(commandArr[2]).upper()

	print(commandArr)

	if createType == "TABLE":
		table = Table(name)
		for i in range(
				commandArr.index("(") + 1,
				commandArr.index(")"), 2
				):
			table.addColumn(commandArr[i], commandArr[i+1])
		TABLES[name] = table


	print(TABLES[name].columns)
	return createType, name


def DecodeInsertCommand(commandArr):
	# INSERT TABLE <tableName> ( <field1> <field2> <field3>... ) ( <val1> <val2> <val3>... )
	insertType = commandArr[1]
	name = str(commandArr[2]).upper()
	
	if insertType == "TABLE":
		table = TABLES[name]
		fillCol = []
		fillRow = []
		for i in range(
				commandArr.index("(") + 1,
				commandArr.index(")")
				):
			fillCol.append(commandArr[i])
		for i in range(
				commandArr.index("(", commandArr.index(")") + 1) + 1,
				commandArr.index(")", commandArr.index(")") + 1)
				):
			fillRow.append(commandArr[i])
		
		print(fillCol + fillRow)
		for i in range(len(fillCol)):
			table.columns[fillCol[i]]['Values'].append(fillRow[i])

		TABLES[name] = table

	print(TABLES[name].columns)
	return insertType, name


def DecodeSelectCommand(commandArr):
	# SELECT <fields> FROM TABLE <tableName>
	selectType = commandArr[commandArr.index("FROM") + 1]
	name = str(commandArr[commandArr.index("FROM") + 2]).upper()
	OUTPUT = []

	if selectType == "TABLE":
		table = TABLES[name]
		keys = list(table.columns.keys())
		OUTPUT.append(keys)
		for i in range(len(table.columns[keys[0]]['Values'])):
			x = []
			for key in keys:
				x.append(table.columns[key]['Values'][i])
			OUTPUT.append(x)


	return selectType, name, OUTPUT


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
			OUTPUT.append(keys)
			for i in range(len(table.columns[keys[0]]['Values'])):
				x = []
				for key in keys:
					x.append(table.columns[key]['Values'][i])
				OUTPUT.append(x)
			for cols in OUTPUT:
				for row in cols:
					file.write(row + ", ")
				file.write("\n")

	return Type, name, filename


def DecodeAlterCommand(commandArr):
	# ALTER TABLE <TableName> <AlterType> ( <fieldName> <dType> <defaultVal>... )
	Type = commandArr[1]
	name = str(commandArr[2]).upper()
	AlterType = str(commandArr[3])

	print(commandArr)

	if Type == "TABLE":
		table = TABLES[name]
		if AlterType == "ADD":
			for i in range(
					commandArr.index("(") + 1,
					commandArr.index(")"), 3
					):
				table.addColumn(commandArr[i], commandArr[i+1])
				for n in table.columns[list(table.columns.keys())[0]]["Values"]:
					table.columns[commandArr[i]]["Values"].append(commandArr[i+2])

		elif AlterType == "DROP":
			for i in range(
					commandArr.index("(") + 1,
					commandArr.index(")"), 1
					):
				table.dropColumn(commandArr[i])


	return Type, name, AlterType

