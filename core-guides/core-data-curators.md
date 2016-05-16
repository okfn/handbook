---
title: Data Curators & Data Curator Managers
---

As mentioned in the introductory page, one key issue is that the problem with open data is not a matter of *creation*, rather *curation*. This means the role of a Data Curator is to take data from known (quality-proven and reliable) sources and transform that into data packages.

This guide will introduce you to key routines we usually do, before publishing any data package.

## Quick Links

- [Discussion forum](http://discuss.okfn.org/category/open-knowledge-labs/core-datasets) - discussion takes place here by default 
   - This is the place to ask questions, get help etc - just open a new topic 
- [Introduction to Core Datasets Project](http://data.okfn.org/roadmap/core-datasets) 
   - [Join the Team Post](http://okfnlabs.org/blog/2015/01/03/data-curators-wanted-for-core-datasets.html) 
- [Packaging Queue (Github Issues Tracker)](https://github.com/datasets/registry/issues) 
- [Publish Data Packages Documentation on Frictionless Data Site](http://data.okfn.org/doc/publish) 

## Getting Started

The first thing you should if you are interested in contributing to the OKFN Labs project as a data curator is to take two minutes to introduce yourself in the [discussion forum](http://discuss.okfn.org/t/core-data-curators-introductions/145) so that other team members can get to know you
The second step is to read the contributing guide below so you can understand:
* The details of the curator workflow
* Can work out where you'd like to contribute

1. *Stop: Have you read the contributing guide? The next items only make sense if you have!*
2. Now you can dive in with one or both of:

- Researching: start reviewing the [current queue](https://github.com/datasets/registry/issues) - add new items, comment on existing ones etc 
- Packaging:  check out the [“Ready to Package”](https://github.com/datasets/registry/labels/Status%3A%20Ready%20to%20Package) section of the queue and assign yourself (drop a comment in the issue claiming it)

# Contributors Guide

<img src="https://docs.google.com/drawings/d/1Emi_N9GTv95Z_STW7XO2PVo0ykZgbgKvT30b1tpuXqI/pub?w=1136&h=318" alt="" style="min-width: 950px; margin-left: -200px;" />
*Fig 1: Overview of the Curation Workflow [[Source Drawing - Full Size](https://docs.google.com/a/okfn.org/drawings/d/1Emi_N9GTv95Z_STW7XO2PVo0ykZgbgKvT30b1tpuXqI/edit)]*

There are 2 areas of activity:

1. Preparing datasets as Core Data Packages - finding them, cleaning them, data-packaging them 
2. Maintaining Core Data Packages - keeping them up to date with the source dataset, handling changes, responding to user queries 

There are different areas where people can contribute:

1. Research
2. Packaging up data
3. Quality assurance
4. Publishing 

Often you will contribute in all 4 by taking a dataset all the way from a suggestion to a fully packaged data package published online.

#### 1. Research 

This involves researching and selecting datasets as core datasets and add them to the queue for packaging - no coding or data wrangling skills needed.

The first step is, naturally, finding data to work with. There are two common ways you can do this:

1. Follow the [GitHub's issue tracker](https://github.com/datasets/registry/issue) and look for a package with 3-star priority, or

2. Get your own data and start preparing it.

Which one you should go to first is really up to you. The difference, however, is that some are more needed than others and you could use that knowledge and skill to tackle on some of the project's priorities.

Other than that, the workflow and requirements is pretty much the same.

#### 2. Packaging up data

Once we have a suggested dataset marked as "ready to package" we can move to packaging it up.

How to package up data is covered in the [general publishing guide](http://data.okfn.org/doc/publish).


##### Directory structure

In order to keep everything organized and as "universal" as possible, we have found a structure that pleases the most of us that any contributor should also go by:

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

##### Unpivoting Tables

This is usually the most difficult part - initially! If you read the [Data Guides](data-guides/), you know by now what pivot tables are. Even though those are more human-friendly, if you check one carefully, you can see they are exactly the opposite of clean and machine readable formats. 

They usually have it in a tabular format, lots of columns - and most of the cells need some work.

You can work these manually, in Excel or using Python, R or whatever suite you prefer. 

In Python, we recommend using the [pandas](http://pandas.pydata.org/) package, as it eases off the work significantly.

To "unpivot" a table, you can simply run the following snippet:

```python
import pandas as pd
df = pd.read_csv('source/source.csv')
df = pd.melt(df, id_vars=['Country], var_name="Year", value_name="Value")
df = df.sort_value(['Country', 'Year'], ascending  = [True, True])
df.to_csv('data/package-name.csv', sep=",", index=False)
```

This is the code we usually run to unpivot and reoder the entire frame. This is just an example and this is scalable. Under `id_vars`, you can add as many variables as you want - as long they have matching data in the dataframe you have loaded.


##### The JSON format

When you have your `CSV` file ready, you sure want to create the `datapackage.json` file. Now, there are two ways to do this:

* Manually, implying you know `[JSON](http://www.json.org/)` and its structure (you should look at their website).
* Using the [Data Package Manager](https://github.com/okfn-oe/datapackage-validator), which creates the file and the main fields automatically.

In either case, we advise you to go through the document and make sure everything is correct. Some things to go by:

* Value fields should have `number` type.
* Year fields should have `date` type.
* Always add a description if you had to change anything in that field.
* Go to the bottom of the file (if you used the [Data Package Manager](https://github.com/okfn-oe/datapackage-validator) and make sure you have the data package name, title and description correct.
* You can use the GitHub's repository link as the homepage.
* You can add a field called `maintainers` if you want to. `"homepage": [{"name": "", "email":""}]` is just an example.
* For the first version, you can let it be `0.1.0.`. Future and updated versions should see this changed.
* As for the license, we truly advise you to use [ODC-PDDL-1.0](http://opendatacommons.org/licenses/pddl/1-0/)


#### 3. Quality Assurance

This involves validating and checking packaged datasets to ensure they are of high quality and ready to publish.

At this stage, you are ready to load the source `csv` file and check for any inconsistencies, blank spaces and other things that are important to ensure the data package is machine readible. Here follows a list of a few things you can look up to:

* The common structure of these packages is `COUNTRY,YEAR,VALUE`. This is not static though. The World Bank of Data usually provides such structure that we generally use `COUNTRY,COUNTRY CODE, YEAR, VALUE`. 
* We prefer using `.` rather than `,` to separate decimal values. We also want to avoid using certain symbols such as `%, &, #, ;, :, ` and a few others that can interfere with the data package.
* If data is not available, you either make that cell as `0` or `NaN`.
* The data package name should be `your-package.csv`. We rather use `-` (underscores) to refer to spaces.

By now you can understand why we use programming skills here. The workflow at this stage is: 1) Download the source `CSV` file which you can do directly in your programming environment (like in Python, R, ...); 2) Prepare a small and quick Python script to search for these small inconsistencies and remove/change them so that there are no problems in the and, 3) Run the `Makefile` in the terminal (in Linux, you can do that by simply changing to the directory of the package - `sudo cd ~/path/to/package` - and then by running `make`. You should see no error messages.) to ensure the script is working flawlessly.


Finally, we use two tools to validate the quality of our packages, namely the [Data Package Validator](http://data.okfn.org/tools/validate) and [Daa PAckage Viewer](http://data.okfn.org/tools/view) the data in the Data Package. You should keep these links because you will need them in the next task.



#### 4. Publishing

After making sure everything is in place, then you are ready to announce your package. You should go the [datasets/registry issues page](https://github.com/datasets/registry/issues) and, in the issue related to your package:

* Package Name (eg. GINI Index)
* [Data Package Validator link](http://data.okfn.org/tools/validate) - just paste your GitHub repository here and copy the link afterwards
* [Data Package Viewer link](http://data.okfn.org/tools/view) - same as with the validator
* The link to your repository

If you do not have experience working with GitHub, [this](/core-guides/working-with-git) should help you understand and perform the basic tasks with Git, within the terminal and in the browser. 

# Guide for Managing Curators

### Intro Email for New Joiners

You are being added to the Core Data Curators mailing list as you indicated your interest in the project through the online form.

This list is announce-only and will be used rarely. General discussion takes place in the public forum:

http://discuss.okfn.org/category/open-knowledge-labs/core-datasets

**Getting Started**

To kick-off your core data curatorship we encourage you to:

1. Introduce yourself in forum here: http://discuss.okfn.org/t/core-data-curators-introductions/145/24

2. Take a look at the Core Data Curators guide: http://data.okfn.org/doc/core-data-curators

