---
title: Contributing to the Core Datasets 
---

## Quick Links

- [Discussion forum](http://discuss.okfn.org/category/open-knowledge-labs/core-datasets) - discussion takes place here by default 
  - This is the place to ask questions, get help etc. - just open a new topic 
- [Introduction to Core Datasets Project](http://data.okfn.org/roadmap/core-datasets) 
  - [Join the Team Post](http://okfnlabs.org/blog/2015/01/03/data-curators-wanted-for-core-datasets.html) 
- [Packaging Queue (GitHub Issues Tracker)](https://github.com/datasets/registry/issues) 
- [Publish Data Packages Documentation on Frictionless Data Site](http://data.okfn.org/doc/publish) 
- [What is a Data Package](http://frictionlessdata.io/guides/data-package/)

## Quick Start

1. Please take 2m to introduce yourself in the [discussion forum](http://discuss.okfn.org/t/core-data-curators-introductions/145) so that other team members can get to know you
2. Read the contributing guide below so you:
  * understand the details of the curator workflow
  * can work out where you'd like to contribute
3.  **Stop: have you read the contributing guide? The next items only make sense if you have!**
4.  Now you can dive in with one or both of:

  - Researching: start reviewing the [current queue](https://github.com/datasets/registry/issues) - add new items, comment on existing ones etc. 
  - Packaging:  check out the [“Ready to Package”](https://github.com/datasets/registry/labels/Status%3A%20Ready%20to%20Package) section of the queue and assign yourself (drop a comment in the issue claiming it) 

## Contributor Guide

<img src="https://docs.google.com/drawings/d/1Emi_N9GTv95Z_STW7XO2PVo0ykZgbgKvT30b1tpuXqI/pub?w=1136&h=318" alt="" style="min-width: 950px; margin-left: -200px;" />

*Fig 1: Overview of the Curation Workflow [[Source Drawing - Full Size](https://docs.google.com/a/okfn.org/drawings/d/1Emi_N9GTv95Z_STW7XO2PVo0ykZgbgKvT30b1tpuXqI/edit)]*

There are 2 areas of activity:

1. Preparing datasets as Core Data Packages - finding them, cleaning them, data-packaging them 
2. Maintaining Core Data Packages - keeping them up to date with the source dataset, handling changes, responding to user queries 

Each of these have sub-steps which we detail below and you can contribute in any and all of these. [In fact given how many of us there are you will almost end up doing several of these at once!]

### Preparing Datasets as Core Data Packages ###

There are different areas where people can contribute:

1. Research
2. Packaging up data
3. Quality assurance
4. Final Publication into the official core datasets list

Often you will contribute in all 4 by taking a dataset all the way from a suggestion to a fully packaged data package published online.

#### 1. Research

This involves researching and selecting datasets as core datasets and adding them to the queue for packaging - no coding or data wrangling skill is needed for this 

* To propose a dataset for addition you [open an issue in the Registry](https://github.com/datasets/registry/issues/new) with the details of the proposed dataset. 
* Identify relevant source or sources for the dataset 
  * To propose a dataset you do not have to know where to get the data from (e.g. you could suggest “US GDP” as a core dataset without yet knowing where to get the data from) 
* Discuss with Queue Manager(s) (they will spot your submission and start commenting in the GitHub issue)
* If good =&gt; Shortlist for Packaging - add [Label “Status: Ready to Package”](https://github.com/datasets/registry/labels/Status%3A%20Ready%20to%20Package) 

##### 1.1 Retrieving Data From the World Bank's API

Since the World Bank is one of the most reliable sources of information, knowing how to get data from their databases is a useful skill. Having a script that fetches data automatically also helps automating the process of maintaining a data package.
The following paragraphs describe how you can write a small Python script to automatically get data about an indicator.

Using the `csv, numpy` and `pandas` packages, you can easily retrieve data from the API.

```python 
apiBase = "http://api.worldbank.org/indicator/";
apiIndicator = "SI.POV.GINI";    # This can be changed to any other indicator
FILE_NAME = 'gini-index.csv';
source = apiBase+apiIndicator+"?format=csv";
```

The first line represents the base link of the API, while you should place the indicator you want in the second variable. Third, name your file. 


##### 1.2 With the source .CSV

Additionally, you can retrieve data from the World Bank manually, by downloading the `.CSV` version.

![Download GINI in CSV]({{site.baseurl}}/core-datasets/images/export.jpg)

In any case, now you need to tell Python to read the data. Here is an example using the previous API query:

```python
giniIndex = pd.read_csv(source)
giniIndex.to_csv('archive/gini-index.csv', sep=",", index_col=0, index=False) 
print("Saved archive CSV file.")
```

#### 2. Packaging up data

Assuming you already have the `.CSV` file with the data you fetched from the source and that it is ready to be packaged, the next step is to structure the entire project in the standardized method we use at the Core Datasets.

You should be looking to have something similar to this:

```
dir-name/
   	data
      		datapackage-id-name.csv
   	archive - optional directory and files
      		source.csv - optional
   	scripts
      		README.md
      		process.py
     	requirements.txt - optional
   	README.md
   	datapackage.json
   	Makefile
```

In summary, you should fit under `data` the final CSV that you will use for your data package and the source data into the `archive` folder. If you need to perform any script to clean and wrangle any bit of the dataset, you have to post it under `scripts`, preferably with the name `process.py`, but this is not a convention. The `dir/README.md` should contain information about the package, source and licenses (if it applies). On the other hand, `scripts/README.md` should talk about the script and any particular information about it. 

*Note for Python users:* Do not forget to create the `requirements.txt` if you use any special Python package. 

As for the Makefile, which allows us to automate the process of curating a package, you should create a small script similar to:

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

This script will tell Python where the directories are and will automatically remove all the previously stored files, replacing them with more recent ones.

#### 3. Quality Assurance

This next part involves validating and ensuring all packages are machine readable. 

Here is a list of things we commonly have to look for before submitting for final appreciation:

* The common structure of these packages is `COUNTRY,YEAR,VALUE`. This is not static though. The World Bank of Data usually provides such structure that we generally use `COUNTRY,COUNTRY CODE, YEAR, VALUE`. For country codes, we use the ones promoted by [SMDG](https://github.com/datasets/country-codes)
* We prefer using `.` rather than `,` to separate decimal values. We also want to avoid using certain symbols such as `%, &, #, ;, :, ` and a few others that can interfere with the data package.
* If data is not available, you either make that cell as `0` or `NaN`.
* The data package name should be `your-package.csv`. We rather use `-` (underscores) to refer to spaces.

##### 3.1 Working with Pivot Tables with Python

One common problem is that you find pivot tables available and we want the opposite, so that it is machine readable. 

The easiest way to do it is using `pandas.melt` function. Using the same example as above (the GINI Index), you can do that by running:

```python
df = pd.melt(df, id_vars=['Country Name', 'Country Code'], var_name="Year", value_name="Value")     
df = df.sort_values(by=['Country Name', 'Year'], ascending=[True, True])

df.dropna().to_csv('data/gini-index.csv', sep=",", index=False)   
```

The first will reorganize the table so that the first two columns match the structure we reviewed a moment ago. The second is there to organize the data frame accordingly. Ordering it alphabetically and in ascending order seems the most adequate. At the end of this, it makes sense to store the data in the `.CSV` format we have been discussing and that is the code you will be usually looking for.  

By now you can understand what and where programming skills are needed. The workflow at this stage is: 1) Download the source `CSV` file which you can do directly in your programming environment (like in Python, R, ...); 2) Prepare a small and quick Python script to search for these small issues and remove/change them so that there are no problems in the end, and, 3) Run the `Makefile` in the terminal (in Linux, you can do that by simply changing to the directory of the package - `sudo cd ~/path/to/package` - and then by running `make`. You should see no error messages.) to ensure the script is working flawlessly.

1. [Validate](http://data.okfn.org/tools/validate) the Data Package and [review](http://data.okfn.org/tools/view) the data in the Data Package 
2. Post a validation link and a view link in the comments for the issue in the Registry related to your Data Package. 

#### 4. Publishing

We have a few extra specific requirements:

* All Data Packages must (ultimately) be stored in a public GitHub repo
  * First publish to your own repository - Here is a quick reference list of guides on [how to work with Git and GitHub.]({{site.baseurl}}/core-datasets/working-with-git.md)
  * Then arrange a move the repository to [github.com/datasets/ organization](httpss://github.com/datasets/) - as the owner of a repository you can initiate a transfer request to github.com/datasets/ which can then be approved 
* Add to the [catalog list](https://github.com/datasets/registry/blob/master/catalog-list.txt) **and** the [core list](https://github.com/datasets/registry/blob/master/core-list.txt) **and** the associated csv files: [catalog-list.csv](https://github.com/datasets/registry/blob/master/data/catalog-list.csv) and [core-list.csv](https://github.com/datasets/registry/blob/master/data/core-list.csv). 
* Reload [http://data.okfn.org/data/](http://data.okfn.org/data/) by visiting <http://data.okfn.org/admin/reload/>
* If you have access, tweet from the @OKFNLabs account a link to the http://data.okfn.org/data/ page for the dataset. 

### Maintaining Data Packages

Many data packages package data that changes over time - for example, many time series get updated monthly or daily.

We need people to become the "maintainer" for a given dataset and keep it up to date by regularly adding in the new data.

**[List of datasets needing a maintainer][maintainer]**

[maintainer]: https://github.com/datasets/registry/labels/Status%3A%20Maintainer%20Wanted

### Core Data Asseessment Criteria

For a dataset to be designated as "core" it should meet the following criteria:

* Quality - the dataset must be well structured
* Relevance and importance - the focus at present is on indicators and reference data
* Ongoing support - it should have a maintainer
* Openness - data should be <a href="http://opendefinition.org/">open data</a> and openly licensed in accordance with the <a href="http://opendefinition.org/">Open Definition</a>

