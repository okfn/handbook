CSV: Lingua Data
================

People love CSV (Comma-Separated Values) for its simplicity: it stores tables in plain text files, one row per line with the first row defining column names. In many ways this is the lingua franca of data. Things become a bit messy, however, when you realize that very little of the above description  is ever true in practice: rows can extend across several lines, file headers are often missing or preceded by some random headings and the flexible format even invites producers to vary the number of cells per row.

Things that are not true about CSV:

 * Every row is one line, every line is a row.
 * The first column contains column headings.
 * All rows have the same number of columns.

Before you process CSV files
----------------------------

It is advisable to deal with CSV encoding and quoting issues early  in your workflow.

If there's a chance that your CSV file contains non-English words, or English proper names such as surnames or placenames, then you should verify that the data is in the character set encoding that you expect, e.g., `UTF-8` or `ISO-8859-1`. Otherwise, convert it to the encoding you work in, using iconv.
GNU iconv is limited to converting files which will fit in the RAM available on your machine and which contain data in a single character set encoding.

There are multiple methods for quoting the markers which delimit fields and lines in CSV files. The tool which generated your CSV files may have done so such that they are unreadable by other computer programmes.
In particular, a naive CSV implementation may have left backslashes or double quotes near the edges of fields in way that Excel will ignore but which are unacceptable to stricter systems such as databases. Try to identify these issues early; they may be trivially fixable with basic
UNIX tools such as `tr` and `sed`.

CSV options
-----------

The markers for lines and fields differ between CSV files. There are four of them: line terminators, field separators, field quotes, and escape markers.

CSV files comprise a set of lines. Each line is followed by a termination marker, including the final line. Within each line there are fields.

*  field separator
*  field quoting (delimiter and policy)
*  line separator (at end of every line)


Exporting from a relational database to CSV
-------------------------------------------
* MySQL (server-side):
```SQL
SELECT INTO OUTFILE
```
* postgres:
```SQL
COPY 'table_name' TO STDOUT WITH ...
```
* sqlite:
```SQL
.dump
```
* DB2:
```SQL
EXPORT COLSEP=0x09 SELECT * FROM schema.table;
```
* SQL Server:
```SQL
bcp
```

Import CSV to a relational database
-----------------------------------

* MySQL:
```SQL
LOAD DATA LOCAL INFILE '/path/to/file.csv' INTO TABLE 'table_name' FIELDS SEPARATED BY '\t' OPTIONALLY ENCLOSED BY '"' LINES TERMINATED BY '\n' IGNORE 1 LINES; SHOW WARNINGS;
```
* postgres:
```SQL
COPY 'table_name' FROM '/path/to/file.csv' WITH ...
```
* sqlite3:
```SQL
.mode ; .import
```
* python:
```SQL
.executemany()
```

Exporting CSV from spreadsheets
-------------------------------
* Excel gotchas
* Refine gotchas
* Gnumeric gotchas


programming
-----------
* python csv module
* awk


Folding nested values into CSV
------------------------------

About halfway through producing a CSV export, you usually realize that the data does not neatly lend itself to be serialized into a single table: a cell value can really only be expressed as a mapping or it can have several values at once. At this stage you have several options:

 * Quote CSV in CSV. Yo dawg, don't do that, please.
 * Generate a proper relational database dump or SQLite image. Not bad, but not a well-defined and generally compatible data exchange format either.
 * Export multiple CSV sheets that combine to a relational model. This is probably the cleanest solution but requires that you also specify how the sheets relate to each other, e.g. by releasing an SQL schema (or at least a list of foreign keys).
 * Generate the export in a more expressive format, such as JSON. This is not such a bad idea, as it will leave rows as list items while giving you the ability to have lists and mappings as values.
 * Have magic column names that allow folding and unfolding of nested structures. One nice example of this is formencode's [`NestedVariables`](http://formencode.org/Validator.html#http-html-form-input) which can also be used without the remainder of the library.

