# Changelog
This is the changelog for the PyDBMS Project V2.1 onwards
### V2.4 - 06/12/2024
+ Changed the command ending from a line break (`\n`) to a semicolon (`;`)
+ Introduced strings with `''` now `'first last'` has to be used instead of `first_last`
+ Added conditions to `SHOW` as `WHERE <field> <opperation> <value>`
+ Data Types have been reduced to just `INT` and `STR` and added some basic type handeling
### V2.3 - 02/12/2024
+ Added the `DUPLICATE TABLE ...` command
+ Improved Query Parsing, now `(value1    value2  value3)` can also be used (earlier only `( value1 value2 value3 )` could be used), i.e. spaces between words and parenthesis does not effect the command and spaces between words can be non uniform
+ Changed `INSERT TABLE <TableName> ...` to `INSERT INTO TABLE <TableName> ...`
+ Changed `SELECT TABLE <TableName> ...` to `SHOW TABLE <TableName> ...`
+ `SHOW TABLE <TableName>` now shows all the fields in their default order
### V2.2 - 08/08/2024
+ Field Selective Data Retrieval has been implemented
+ Unit Testing is being introduced (Currently for *Create Table* function only)
+ Fixed some small bugs / errors
### V2.1 - 05/08/2024
+ Added the `ALTER ... CHANGE ...` command
+ Removed some redundant requirements for commands
+ Added Multiple Command Support in single Query (each command as a separate line)
