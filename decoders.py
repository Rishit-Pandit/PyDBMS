from utils import Table
from utils import TABLES, REPORTS, FORMS

def DecodeCreateCommand(commandArr):
	# CREATE TABLE <TableName> ( <field1> <field2> ... )
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


def DecodeSaveCommand(commandArr):
	# SAVE TABLE <tableName> FILE <fileName>
	saveType = commandArr[1]
	name = str(commandArr[2]).upper()
	filename = str(commandArr[4])
	OUTPUT = []

	if saveType == "TABLE":
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

	return saveType, name, filename


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


def DecodeInsertCommand(commandArr):
	# INSERT TABLE <tableName> ( <> ____ ____ ) ( ____ ____ ____ )
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
