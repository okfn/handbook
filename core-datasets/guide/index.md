---
title: Contributing to the Core Datasets 
---

## Quick Links

- [Discussion forum](http://discuss.okfn.org/category/open-knowledge-labs/core-datasets) - discussion takes place here by default 
  - This is the place to ask questions, get help etc - just open a new topic 
- [Introduction to Core Datasets Project](http://data.okfn.org/roadmap/core-datasets) 
  - [Join the Team Post](http://okfnlabs.org/blog/2015/01/03/data-curators-wanted-for-core-datasets.html) 
- [Packaging Queue (Github Issues Tracker)](https://github.com/datasets/registry/issues) 
- [Publish Data Packages Documentation on Frictionless Data Site](http://data.okfn.org/doc/publish) 

## Quick Start

1. Please take 2m to introduce yourself in the [discussion forum](http://discuss.okfn.org/t/core-data-curators-introductions/145) so that other team members can get to know you
2. Read the contributing guide below so you:
  * understand the details of the curator workflow
  * can work out where you'd like to contribute
3.  **Stop: have you read the contributing guide? The next items only make sense if you have!**
4.  Now you can dive in with one or both of:

  - Researching: start reviewing the [current queue](https://github.com/datasets/registry/issues) - add new items, comment on existing ones etc 
  - Packaging:  check out the [“Ready to Package”](https://github.com/datasets/registry/labels/Status%3A%20Ready%20to%20Package) section of the queue and assign yourself (drop a comment in the issue claiming it) 

## Contributor Guide

<img src="https://docs.google.com/drawings/d/1Emi_N9GTv95Z_STW7XO2PVo0ykZgbgKvT30b1tpuXqI/pub?w=1136&h=318" alt="" style="min-width: 950px; margin-left: -200px;" />

*Fig 1: Overview of the Curation Workflow [[Source Drawing - Full Size](https://docs.google.com/a/okfn.org/drawings/d/1Emi_N9GTv95Z_STW7XO2PVo0ykZgbgKvT30b1tpuXqI/edit)]*

There are 2 areas of activity:

1. Preparing datasets as Core Data Packages - finding them, cleaning them, data-packaging them 
2. Maintaining Core Data Packages - keeping them up to date with the source dataset, handling changes, responding to user queries 

Each of these have sub-steps which we detail below and you can contribute in any and all of these. [In fact given how many of us there are you will almost end up doing several of these at once!]

### Preparing Datasets as Core Data Packages

There are different areas where people can contribute:

1. Research
2. Packaging up data
3. Quality assurance
4. Final Publication into the official core datasets list

Often you will contribute in all 4 by taking a dataset all the way from a suggestion to a fully packaged data package published online.

#### 1. Research

This involves researching and selecting datasets as core datasets and adding them to the queue for packaging - no coding or data wrangling skill is needed for this 

* To propose a dataset for addition you [open an issue in the Registry](https://github.com/datasets/registry/issues/new) with the details of the proposed dataset. 
* Identify relevant source or sources for the dataset 
  * To propose a dataset you do not have to know where to get the data from (e.g. you could suggest “US GDP” as a core dataset without yet knowing where to get the data from) 
* Discuss with Queue Manager(s) (they will spot your submission and start commenting in the github issue)
* If good =&gt; Shortlist for Packaging - add [Label “Status: Ready to Package”](https://github.com/datasets/registry/labels/Status%3A%20Ready%20to%20Package) 

#### 2. Packaging up data

Once we have a suggested dataset marked as "ready to package" we can move to packaging it up.

Assuming you already have a `.CSV` file with the data you fetched from the source and that it is ready to be packaged, the goal now is to have it under a structure such that allows for a standardization of the datapackages.

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

As for the Makefile, which is the easiest part, the common Makefile structure is as follows:

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

Assuming you have a Python script that fetches data from an API, it is easy for a managing curator to update your data package by just running the make file from the terminal, using `make` as you are telling Python where everything is stored.

#### 3. Quality Assurance

This involves validating and checking packaged datasets to ensure they are of high quality and ready to publish.

Here is a list of things you must pay attention to in your `.CSV` file, before submitting your package for final appreciation:

* The common structure of these packages is `COUNTRY,YEAR,VALUE`. This is not static though. The World Bank of Data usually provides such structure that we generally use `COUNTRY,COUNTRY CODE, YEAR, VALUE`. For country codes, we use the ones promoted by [SMDG](https://github.com/datasets/country-codes)
* We prefer using `.` rather than `,` to separate decimal values. We also want to avoid using certain symbols such as `%, &, #, ;, :, ` and a few others that can interfere with the data package.
* If data is not available, you either make that cell as `0` or `NaN`.
* The data package name should be `your-package.csv`. We rather use `-` (underscores) to refer to spaces.

By now you can understand why we use programming skills here. The workflow at this stage is: 1) Download the source `CSV` file which you can do directly in your programming environment (like in Python, R, ...); 2) Prepare a small and quick Python script to search for these small inconsistencies and remove/change them so that there are no problems in the and, 3) Run the `Makefile` in the terminal (in Linux, you can do that by simply changing to the directory of the package - `sudo cd ~/path/to/package` - and then by running `make`. You should see no error messages.) to ensure the script is working flawlessly.

1. [Validate](http://data.okfn.org/tools/validate) the Data Package and [review](http://data.okfn.org/tools/view) the data in the Data Package 
2. Post a validation link and a view link in the comments for the issue in the Registry related to your Data Package. 

#### 4. Publishing 

We have a few extra specific requirements:

* All Data Packages must (ultimately) be stored in a public github repo
  * First publish to your own repository
  * Then arrange a move the repository to [github.com/datasets/ organization](https://github.com/datasets/) - as the owner of a repository you can initiate a transfer request to github.com/datasets/ which can then be approved 
* Add to the [catalog list](https://github.com/datasets/registry/blob/master/catalog-list.txt) **and** the [core list](https://github.com/datasets/registry/blob/master/core-list.txt) **and** the associated csv files: [catalog-list.csv](https://github.com/datasets/registry/blob/master/data/catalog-list.csv) and [core-list.csv](https://github.com/datasets/registry/blob/master/data/core-list.csv). 
* Reload [http://data.okfn.org/data/](http://data.okfn.org/data/) by visiting <http://data.okfn.org/admin/reload/>
* If you have access, tweet from the @OKFNLabs account a link to the http://data.okfn.org/data/ page for the dataset. 


### Maintaining Data Packages

Many data packages package data that changes over time - for example, many time series get updated monthly or daily.

We need people to become the "maintainer" for a given dataset and keep it up to date by regularly adding in the new data.

**[List of datasets needing a maintainer][maintainer]**

[maintainer]: https://github.com/datasets/registry/labels/Status%3A%20Maintainer%20Wanted


### Core Data Assessment Criteria

For a dataset to be designated as "core" it should meet the following criteria:

* Quality - the dataset must be well structured
* Relevance and importance - the focus at present is on indicators and reference data
* Ongoing support - it should have a maintainer
* Openness - data should be <a href="http://opendefinition.org/">open data</a> and openly licensed in accordance with the <a href="http://opendefinition.org/">Open Definition</a>

