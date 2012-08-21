
===============================================
Liberating Data from Microsoft Access Databases
===============================================
.. sectionauthor:: Rufus Pollock (rufuspollock on Twitter)

Use the `mdbtools library`_. On Ubuntu / Debian you can install this via::

   apt-get install mdbtools

.. _mdbtools library: http://mdbtools.sourceforge.net/

Key functions::

  # Get an SQL schema
  mdb-schema {database-name}

  # Get a list of the table names
  mdb-tables {database-name}

  # Export a table as a CSV file
  mdb-export {databbase-name} {table-name}

Here's an example script to extract all of the data from the Access database
into CSV files::

  import os, sys, subprocess

  # Get database name from arguments passed to the script
  # Alternative you could set explicitly e.g. DATABASe = 'my-access-db.mdb'
  DATABASE = sys.argv[1]

  # Get table names using mdb-tables
  table_names = subprocess.Popen(['mdb-tables', '-1', DATABASE],
                                 stdout=subprocess.PIPE).communicate()[0]
  tables = table_names.split('\n')

  # Walk through each table and dump as CSV file using 'mdb-export'
  # Replace ' ' in table names with '_' when generating CSV filename
  for table in tables:
      if table != '':
          filename = table.replace(' ','_') + '.csv'
          file = open(filename, 'w')
          print('Exporting ' + table)
          contents = subprocess.Popen(['mdb-export', DATABASE, table],
                                      stdout=subprocess.PIPE).communicate()[0]
          file.write(contents)
          file.close()

If you save this script as script.py you can use it as follows::

  python script.py {path-to-access-database}

CSV files will be written to the current directory.

