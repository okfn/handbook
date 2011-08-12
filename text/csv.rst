CSV: Lingua Data
================

People love CSV (Comma-Separated Values) for its simplicity: it stores tables
in plain text files, one row per line with the first row defining column
names. In many ways this is the lingua franca of data. Things become a bit
messy, however, when you realize that very little of the above description 
is ever true in practice: rows can extend across several lines, file headers
are often missing or preceded by some random headings and the flexible format
even invites producers to vary the number of cells per row.


Things that are not true about CSV: 

 * Every row is one line, every line is a row. 
 * The first column contains column headings.
 * All rows have the same number of columns.

## Folding nested values into CSV
---------------------------------

About halfway through producing a CSV export, you usually realize that the 
data does not neatly lend itself to be serialized into a single table: a 
cell value can really only be expressed as a mapping or it can have several
values at once. At this stage you have several options:

 * Quote CSV in CSV. Yo dawg, don't do that, please.
 * Generate a proper relational database dump or SQLite image. Not bad, 
   but not a well-defined and generally compatible data exchange format 
   either.
 * Export multiple CSV sheets that combine to a relational model. This is
   probably the cleanest solution but requires that you also specify how
   the sheets relate to each other, e.g. by releasing an SQL schema
   (or at least a list of foreign keys).
 * Generate the export in a more expressive format, such as JSON. This is 
   not such a bad idea, as it will leave rows as list items while giving 
   you the ability to have lists and mappings as values.
 * Have magic column names that allow folding and unfolding of nested
   structures. One nice example of this is formencode's `NestedVariables`_ 
   which can also be used without the remainder of the library.

.. _`NestedVariables`: http://formencode.org/Validator.html#http-html-form-input




