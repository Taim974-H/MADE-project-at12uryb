# Diverging Trends: Waste Generation vs. Emissions in the Waste Sector of Ireland

## Main Question

Is waste treatment becoming more efficient? Investigating Trends in NMVOC Emissions in Ireland: Establishing a Baseline for Climate Action

## Description
The results can give insight into trends within the waste sector and compare the amount of waste generated and treated to NMVOC emissions which are known to be harmful as they directly impact human health, especially when in higher concentrations in urban areas.

## Datasources
### Generation of waste (GWA01)
* Metadata URL: https://data.gov.ie/
* Data URL: https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/GWA01/CSV/1.0/en
* Data Type: CSV

### Treatment of waste (GWA02)
* Metadata URL: https://data.gov.ie/
* Data URL: https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/GWA02/CSV/1.0/en
* Data Type: CSV

These datasets are sourced from the Irish government's website. The first dataset provides information on the generation of waste categorized by different types of waste from 2004 to 2020. The second dataset details the treatment of waste, including various waste management operations over the same period.

### NMVOC emissions (NMVOC from EDGARv6.1)
* Metadata URL: https://edgar.jrc.ec.europa.eu/index.php/dataset_ap61
* Data URL: https://jeodpp.jrc.ec.europa.eu/ftp/jrc-opendata/EDGAR/datasets/v61_AP/NMVOC/v61_AP_NMVOC_1970_2018b.zip
* Data Type: xlsx

This dataset is part of a larger dataset, EDGARv6.1. The study focuses on NMVOC emission time series (1970-2018) by sector and country and the data provided in an overview table (.xls). Emission country totals are expressed in kt substance/year and the IPCC 1996 and 2006 codes are used for specification of the sectors.

## License
MIT

# Exercise Badges

![](https://byob.yarr.is/Taim974-H/MADE-project-at12uryb/score_ex1) ![](https://byob.yarr.is/Taim974-H/MADE-project-at12uryb/score_ex2) ![](https://byob.yarr.is/Taim974-H/MADE-project-at12uryb/score_ex3) ![](https://byob.yarr.is/Taim974-H/MADE-project-at12uryb/score_ex4) ![](https://byob.yarr.is/Taim974-H/MADE-project-at12uryb/score_ex5)

Taim974-H/MADE-project-at12uryb

# Methods of Advanced Data Engineering Template Project

This template project provides some structure for your open data project in the MADE module at FAU.
This repository contains (a) a data science project that is developed by the student over the course of the semester, and (b) the exercises that are submitted over the course of the semester.
Before you begin, make sure you have [Python](https://www.python.org/) and [Jayvee](https://github.com/jvalue/jayvee) installed. We will work with [Jupyter notebooks](https://jupyter.org/). The easiest way to do so is to set up [VSCode](https://code.visualstudio.com/) with the [Jupyter extension](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter).

To get started, please follow these steps:
1. Create your own fork of this repository. Feel free to rename the repository right after creation, before you let the teaching instructors know your repository URL. **Do not rename the repository during the semester**.
2. Setup the exercise feedback by changing the exercise badge sources in the `README.md` file following the patter `![](https://byob.yarr.is/<github-user-name>/<github-repo>/score_ex<exercise-number>)`. 
For example, if your user is _myuser_ and your repo is _myrepo_, then update the badge for _exercise 1_ to `![](https://byob.yarr.is/myrepo/myuser/score_ex1)`. Proceed with the remaining badges accordingly.


## Project Work
Your data engineering project will run alongside lectures during the semester. We will ask you to regularly submit project work as milestones so you can reasonably pace your work. All project work submissions **must** be placed in the `project` folder.

### Exporting a Jupyter Notebook
Jupyter Notebooks can be exported using `nbconvert` (`pip install nbconvert`). For example, to export the example notebook to html: `jupyter nbconvert --to html examples/final-report-example.ipynb --embed-images --output final-report.html`


## Exercises
During the semester you will need to complete exercises using [Jayvee](https://github.com/jvalue/jayvee). You **must** place your submission in the `exercises` folder in your repository and name them according to their number from one to five: `exercise<number from 1-5>.jv`.

In regular intervalls, exercises will be given as homework to complete during the semester. Details and deadlines will be discussed in the lecture, also see the [course schedule](https://made.uni1.de/). At the end of the semester, you will therefore have the following files in your repository:

1. `./exercises/exercise1.jv`
2. `./exercises/exercise2.jv`
3. `./exercises/exercise3.jv`
4. `./exercises/exercise4.jv`
5. `./exercises/exercise5.jv`

### Exercise Feedback
We provide automated exercise feedback using a GitHub action (that is defined in `.github/workflows/exercise-feedback.yml`). 

To view your exercise feedback, navigate to Actions -> Exercise Feedback in your repository.

The exercise feedback is executed whenever you make a change in files in the `exercise` folder and push your local changes to the repository on GitHub. To see the feedback, open the latest GitHub Action run, open the `exercise-feedback` job and `Exercise Feedback` step. You should see command line output that contains output like this:

```sh
Found exercises/exercise1.jv, executing model...
Found output file airports.sqlite, grading...
Grading Exercise 1
	Overall points 17 of 17
	---
	By category:
		Shape: 4 of 4
		Types: 13 of 13
```
