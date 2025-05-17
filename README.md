# PyDBMS

PyDBMS is a Database Management Software in Python which stores data at runtime using Dictionaries and for long-term storage in a `.csv` file format. The program includes a GUI Client that takes SQL like multi-lined text commands to Create, Update, Alter, Delete and Retrive Data from the Database and save or load data from a local file.  

The GUI Client appears as such with an Input Text Area and an Output Text Area:  

![The GUI Client](/GUIClient.jpg "GUI Client")

## Basic Fuctionalities

### Structures and Classes

#### Table

The table is the fundamental class of the Database which is a Dictionary that stores `Fields` as Keys. The Value of the Keys is another Dictionary that
holds 3 things - The Data Type, The Values or `Records` and the Extra Parameters.  
For example:
``` python
Table = {
  'Field1': {
    'Type': 'dType', 
    'Values': [Val1, Val2, Val3], 
    'Params': [params]
    },
  'Field2': {
    'Type': 'dType', 
    'Values': [Val4, Val5, Val6], 
    'Params': [params]
    },
  }
```

#### Data Types

There are 5 Data Types:  
* **INT** - 0-9
* **STR** - a-z, 0-9, !, @, #, $, %, ^, &, *, -, +, =, _  


### Commands

#### CREATE

This command is used to Create a Table with a certain Name and Fields with specified DataTypes.  
The CREATE command is used as such:  
```
CREATE TABLE <TableName> ( <field1> <dType1> <field2> <dType2> <field3> <dType3>... );
```
*NOTE: Commas have not been yet implemented so it just uses spaces as delimitters*

#### INSERT

This command is used to Insert Values into the respective Fields in an existing table.  
The INSERT command is used as such:  
```
INSERT INTO TABLE <tableName> FIELDS ( <field1> <field2> <field3>... ) VALUES ( <val1> <val2> <val3>... );
INSERT INTO TABLE <tableName> VALUES ( <val1> <val2> <val3>... );
```

#### SHOW

This command is used to show the table with its Fields and Records in a Separate Window in chronological order.  
The SHOW command is used as such:  
```
SHOW TABLE <TableName> ( <field1> <field2> <field3>... );
SHOW TABLE <TableName>; # for all the fields and in default order
SHOW TABLE <TableName> ( <field1> <field2> <field3>... ) WHERE <field> <opperation> <value>;
```

#### SAVE

This command saves a Table in the Specified file in `.csv` format.  
The SAVE command is used as such:  
```
SAVE TABLE <TableName> FILE <FileName>;
```
*NOTE: This command can only save one table per file.*

#### LOAD

This command loads a Table from the Specified file in `.csv` format.  
The LOAD command is used as such:  
```
LOAD TABLE <TableName> FILE <FileName>;
```

#### ALTER

This command can add, change or drop (delete) a field from the table as specified.  
The ALTER command is used as such: 
```
ALTER TABLE <TableName> ADD <fieldName> <dType> <defaultVal>;
ALTER TABLE <TableName> DROP <fieldName>;
ALTER TABLE <TableName> CHANGE <fieldName> <newFieldName> <dType>;
```

#### DUPLICATE

This command is used to Duplicate an existing table, with the FILL tag the table is cloned and with the EMPTY tag only the table structure is cloned.  
The INSERT command is used as such:  
```
DUPLICATE TABLE <TableName> FROM <TableName> <EMPTY/FILL>;
```
