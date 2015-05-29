Outputting CSV from Postgres
============================

```
 \f ','
    \a
    \t
    \o /path/to/my.csv
    SELECT field1,field2 FROM some_table;
    \o

```
