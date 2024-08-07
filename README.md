# PyDBMS

PyDBMS is an initiative to make a Database Management Software in Python to aid in autonomous operations that are carried out on databases by using the same language in both the Platform.  
This is a GUI Client that take SQL like single lined text based commands to Create, Update and Retrive Data to and from the Databases.  
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
  Field1: {
    DataType: dType, 
    Values: [Val1, Val2, Val3], 
    Params: params
    },
  Field2: {
    DataType: dType, 
    Values: [Val4, Val5, Val6], 
    Params: params
    },
  }
```

#### Data Types

There are 5 Data Types:  
* **BOOL** - 1,0, true,false
* **INT** - 0-9
* **DATE** - 0-9,/
* **CHAR** - a-z
* **VARCHAR** - a-z, 0-9, !, @, #, $, %, ^, &, *, -, +, =, _  


### Commands

#### CREATE

This command is used to Create a Table with a certain Name and Fields with specified DataTypes.  
The CREATE command is used as such:  
```
CREATE TABLE <TableName> ( <field1> <dType1> <field2> <dType2> <field3> <dType3>... )
```
*NOTE: Commas have not been yet implemented so it just uses spaces as delimitters*

#### INSERT

This command is used to Insert Values into the respective Fields in a prexistant table.  
The INSERT command is used as such:  
```
INSERT TABLE <TableName> ( <val1> <val2> <val3>... )
```

#### SELECT

This command is used to show the table with its Fields and Records in a Separate Window in chronological order.  
The SELECT command is used as such:  
```
SELECT * FROM TABLE <TableName>
```
*NOTE: Field Selective Data Retreival has not yet been implemented so only the full table can be shown at once*

#### SAVE

This command saves a Table in the Specified file in `.CSV` format.  
The SAVE command is used as such:  
```
SAVE TABLE <TableName> FILE <FileName>
```
*NOTE: This command can only save one table per file.*

#### LOAD

This command loads a Table from the Specified file in `.CSV` format.  
The LOAD command is used as such:  
```
LOAD TABLE <TableName> FILE <FileName>
```

#### ALTER

This command can add, change or drop (delete) a field from the table as specified.  
The ALTER command is used as such: 
```
ALTER TABLE <TableName> ADD <fieldName> <dType> <defaultVal>
ALTER TABLE <TableName> DROP <fieldName>
ALTER TABLE <TableName> CHANGE <fieldName> <newFieldName> <dType>
```


### Changelog
#### V2 - 05/08/2024
+ Added the `ALTER ... CHANGE ...` command
+ Removed some redundant requirements for commands
+ Added Multi-Line Command / Multi-Command Support
