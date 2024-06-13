# Project Plan

## Title
Diverging Trends: Waste Generation vs. Emissions in the Waste Sector of Ireland

## Main Question

1. Is waste treatment becoming more efficient? Investigating Trends in NMVOC Emissions in Ireland: Establishing a Baseline for Climate Action

## Description
 The results can give insight into trends within the waste sector and compare the amount of waste generated and treated to NMVOC emissions which are known to be harmful as they  directly impact human health, especially when in higher concentrations in urban areas.

## Datasources
### Datasource1: Generation of waste (GWA01)
* Metadata URL: https://data.gov.ie/
* Data URL: https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/GWA01/CSV/1.0/en
* Data Type: CSV

### Datasource2: Treatment of waste (GWA02)
* Metadata URL: https://data.gov.ie/
* Data URL: https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/GWA02/CSV/1.0/en
* Data Type: CSV

These datasets are sourced from the Irish government's website. The first dataset provides information on the generation of waste categorized by different types of waste from 2004 to 2020. The second dataset details the treatment of waste, including various waste management operations over the same period.


### Datasource3: NMVOC emissions (NMVOC from EDGARv6.1)
* Metadata URL: https://edgar.jrc.ec.europa.eu/index.php/dataset_ap61
* Data URL: https://jeodpp.jrc.ec.europa.eu/ftp/jrc-opendata/EDGAR/datasets/v61_AP/NMVOC/v61_AP_NMVOC_1970_2018b.zip
* Data Type: xlsx

This dataset is part of a larget dataset, EDGARv6.1. The study focuses on NMVOC emission time series (1970-2018) by sector and country and the data provided in an overview table (.xls).

## Work Packages

1. Find datasets related to waste disposal [#1][i1]
2. Find datasets related to emissions due to waste management [#2][i1]
3. Preprocess the datasets [#3][i1]
4. Plot the data [#4][i1]
5. Automated test for data pipeline [#5][i5]

[i1]: https://github.com/Taim974-H/MADE-project-at12uryb/issues/1
[i2]: https://github.com/Taim974-H/MADE-project-at12uryb/issues/2
[i3]: https://github.com/Taim974-H/MADE-project-at12uryb/issues/3
[i4]: https://github.com/Taim974-H/MADE-project-at12uryb/issues/4
[i5]: https://github.com/Taim974-H/MADE-project-at12uryb/issues/7