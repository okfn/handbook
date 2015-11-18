---
title: Liberating Data from Microsoft Access Databases
---

Use the [`mdbtools library`](http://mdbtools.sourceforge.net/). On
Ubuntu / Debian you can install this via:

```bash
$ apt-get install mdbtools
```

It is also available via [Homebrew](http://brew.sh/) on the Mac:

```bash
$ brew install mdbtools
```

Key functions:

+ Get an SQL schema

```bash
$ mdb-schema {database-name}
```

+ Get a list of the table names

```bash
$ mdb-tables {database-name}
```

+ Export a table as a CSV file

```bash
$ mdb-export {databbase-name} {table-name}
```

Here's an example script to extract all of the data from the Access
database into CSV files:

```python
#!/usr/bin/env python
import os, sys, subprocess

# Get database name from arguments passed to the script
# Alternative you could set explicitly e.g. `DATABASE = 'my-access-db.mdb'`

DATABASE = sys.argv[1]

# Get table names using mdb-tables
table_names = subprocess.Popen(['mdb-tables', '-1', DATABASE], stdout=subprocess.PIPE).communicate()[0]
tables = table_names.split('\n')

# Walk through each table and dump as CSV file using 'mdb-export'
# Replace ' ' in table names with '_' when generating CSV filename
for table in tables:
    if table != '':
        filename = table.replace(' ','_') + '.csv'
        print('Exporting ' + table)
        with open(filename, 'wb') as f:
            subprocess.check_call(['mdb-export', DATABASE, table], stdout=f)
```

If you save this script as `script.py`, you can use it as follows::

```bash
$ python script.py {path-to-access-database}
```

CSV files will be written to the current directory.
