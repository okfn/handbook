---
title: Data Wrangling Walk-through
---

This guide will introduce you to key routines we usually do, before publishing any data package. Nevertheless, these are basic tasks that require data wrangling skills.

# Getting data

There are [many sources of data]({{site.baseurl}}/data/archive/howtogetdata.md). You should always look for the most reliable ones.

For this example, lets say we want to get data about the Historical GDP, like we did, [here](https://github.com/datasets/registry/issues/101).

The source of that indicator is a private spreadsheet and we preferred that because it contains data from the longest time we could find.

# Preparing the Data

The final outcome we want is to have a `.CSV` and `JSON` file. In that case, the first step is to find that data in the pretended `.CSV` file and you can do that by simply building a Python script to remove the many white and blank spaces we do not need. Personally, if you are not too comfortable, it might make sense to simply remove those spaces using Excel/Spreadsheets. However, this dataset in particular is very human readable, but not machine readable. This table is a what we call pivot table. In summary, we need to "unpivot" it.

Assuming you have deleted all the blank spaces manually, and stored all sheets into separate `.CSV` files, using Python's `pandas` package, you can wrangle this table by running the following chunk of code:

 
```python
import pandas as pd

def main():
    df_pop = pd.read_csv('source/population.csv')
    df_gdp = pd.read_csv('source/gdp.csv')
    df_gdp_grow = pd.read_csv('source/gdp-growth.csv')
    df_gdp_pc = pd.read_csv('source/gdp-per-capita.csv')
    df_gdp_pc_growth = pd.read_csv('source/gdp-per-capita-growth.csv')
    df_pop_growth = pd.read_csv('source/population-growth.csv')

    le_pop = pd.melt(df_pop, id_vars=['Country'], var_name="Year", value_name="Value")
    le_popgr = pd.melt(df_pop_growth, id_vars=['Country'], var_name="Year", value_name="Value")
    le_gdp = pd.melt(df_gdp, id_vars=['Country'], var_name="Year", value_name="Value")
    le_gdpgr = pd.melt(df_gdp_grow, id_vars=['Country'], var_name="Year", value_name="Value")
    le_gdppc = pd.melt(df_gdp_pc, id_vars=['Country'], var_name="Year", value_name="Value")
    le_gdppcgr = pd.melt(df_gdp_pc_growth, id_vars=['Country'], var_name="Year", value_name="Value")

    # Sort by country name - convenience only
    le_pop2 = le_pop.sort_values(['Country'])
    le_pop2gr = le_popgr.sort_values(['Country'])
    le_gdp2 = le_gdp.sort_values(['Country'])
    le_gdpgr2 = le_gdpgr.sort_values(['Country'])
    le_gdppc2 = le_gdppc.sort_values(['Country'])
    le_gdppcgr2 = le_gdppcgr.sort_values(['Country'])

    # Write each df to csv
    le_pop2.dropna().to_csv('data/population.csv', sep=',', index=False)
    le_pop2gr.dropna().to_csv('data/population-growth.csv', sep=',', index=False)
    le_gdp2.dropna().to_csv('data/gdp.csv', sep=',', index=False)
    le_gdpgr2.dropna().to_csv('data/gdp-growth.csv', sep=',', index=False)
    le_gdppc2.dropna().to_csv('data/gdp-per-capita.csv', sep=',', index=False)
    le_gdppcgr2.dropna().to_csv('data/gdp-per-capita-growth.csv', sep=',', index=False)

if __name__ == '__main__':
    main()
```

In summary, what this chunk of code does it loading the many `.CSV` files, removes the pivot format by running the `pandas.melt` function, sorts it by country (alphabetically), and then it stores all files as new `.CSV` files, later to be used in the datapackage.



## Setting up a Git Repository

We strongly advise the usage of GitHub as a great way to keep your code open and free of access. Do not worry if you do not know what Git or GitHub is. We have a small guide [here]({{site.baseurl}}/core-datasets/working-with-git.md).

## Directory structure

In order to keep everything organized and as universal as possible, your directory should look similar to:

```
dir
   data
      id-name.csv
   archive
      source.csv
   scripts
      README.md
      py.py
      requirements.txt - optional
   README.md
   datapackage.json
   Makefile
```

In summary, you should fit under `data` the final CSV that you will use for your data package and the source data into the `archive` folder. If you need to perform any script to clean and wrangle any bit of the dataset, you have to post it under `scripts`, preferably with the name `process.py`, but this is not a convention. The `dir/README.md` should contain information about the package, source and licenses (if it applies). On the other hand, `scripts/README.md` should talk about the script and any particular information about it. 

*Note for Python users:* Do not forget to create the `requirements.txt` if you use any special Python package. 

As for the Makefile, which allows us to automate the process of maintaining a data package, it should contain a piece of code similar to:

```
version="0.1.0"

DATADIR=data
SCRIPTDIR=scripts

all: data

data:
      python $(SCRIPTDIR)/process.py

      clean:
            rm -f $(DATADIR)/*

            .PHONY: all data clean
```

This is telling Python where are the base directories to search for the script and to search for the data and it also tells Python to erase the previous outcomes and store new ones with the new data.

## Quality Assurance

At this stage, you should have everything pretty much covered in this simple walk-through, but we advice you to double check your data package by looking for details that make it not machine readable:
 
* The common structure of these packages is `COUNTRY,YEAR,VALUE`. This is not static though. The World Bank of Data usually provides such structure that we generally use `COUNTRY,COUNTRY CODE, YEAR, VALUE`. 
* We prefer using `.` rather than `,` to separate decimal values. We also want to avoid using certain symbols such as `%, &, #, ;, :, ` and a few others that can interfere with the data package.
* If data is not available, you either make that cell as `0` or `NaN`.
* The data package name should be `your-package.csv`. We rather use `-` (underscores) to refer to spaces.

By now you can understand why we use programming skills here, since you can basically automate most of these processes.

# From an API

Another common method to get data is from an API. The process is very similar, although can load the data directly to your Python script. In other words, if you recurr to an API, you can actually fasten this process even more.
 
Lets take another example and assume we want to retrieve data about the GINI Index over time, like we did [here](https://github.com/datasets/registry/issues/179). 

There are two ways you can get data from the World Bank:

1. Downloading the CSV file manually, in the indicator page - in the case of the GINI, that would be http://data.worldbank.org/indicator/SI.POV.GINI. Or

2. Use their API.

The first method requires that you download the `.CSV` as the picture bellow demonstrates and then you have to repeat the process as described above.
![Download as CSV]({{site.baseurl}}/core-datasets/images/export.jpg)

The second method, speeds a lot of this process.

To build an API query, you will have to tell Python the base URL, then the special part of the URL you want and the format. In the case of the World Bank of Data and the GINI Index, you will to have a similar script:

```python
import pandas as pd

apiBase = "http://api.worldbank.org/indicator/"
apiIndicator = "SI.POV.GINI"    # This can be changed to any other indicator
FILE_NAME = 'gini-index.csv'
source = apiBase+apiIndicator+"?format=csv"

def main():
    giniIndex = pd.read_csv(source)
    giniIndex.to_csv('archive/gini-index.csv', sep=",", index_col=0, index=False) 
```  

What this does is fetches the `.CSV` file from the API, the `pandas` package reads it as a dataframe and the script then stores it as a `.CSV` file. However, this is not the end case, as you will need to revise the data and perform the same tasks to ensure quality on these packages.
