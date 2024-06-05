# Project Plan

## Title
Diverging Trends: Waste Generation vs. Emissions in the Waste Sector of Ireland

## Main Question

1. Is waste treatment becoming more efficient?  An analysis of disparate trends in waste generation and emissions in the waste sector of Ireland from 2004 to 2018.

## Description
 The results can give insight into trends within the waste sector and compare the amount of waste generated and treated to NMVOC emissions which are known to be harmful as they  directly impact human health, especially when in higher concentrations in urban areas.

## Datasources
<!-- Describe each datasources you plan to use in a section. Use the prefic "DatasourceX" where X is the id of the datasource. -->
### Datasource1: Generation and treatment of waste
* Metadata URL: https://data.gov.ie/
* Data URL1 Generation of waste: https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/GWA01/CSV/1.0/en
* Data URL 2 Treatment of waste: https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/GWA02/CSV/1.0/en
* Data Type: CSV


### Datasource2: NMVOC emissions
* Metadata URL: https://edgar.jrc.ec.europa.eu/
* Data URL: https://jeodpp.jrc.ec.europa.eu/ftp/jrc-opendata/EDGAR/datasets/v61_AP/NMVOC/v61_AP_NMVOC_1970_2018b.zip
* Data Type: xlsx

For NMVOC, emission time series (1970-2018) by sector and country are provided in an overview table (.xls).


## Work Packages

<!-- List of work packages ordered sequentially, each pointing to an issue with more details. -->

1. Find datasets related to waste disposal [#1][i1]
2. Find datasets related to emissions due to waste management [#2][i1]
3. Preprocess the datasets [#3][i1]
4. Plot the data [#4][i1]

[i1]: https://github.com/jvalue/made-template/issues/1
[i2]: https://github.com/jvalue/made-template/issues/2
[i3]: https://github.com/jvalue/made-template/issues/3
[i4]: https://github.com/jvalue/made-template/issues/4
