# Exploring the Census American Community Survey's many variables

The Census API/Developer site contains handy (if massive) files that list every variable and that variable's metadata for a given survey. For example, here's the developer's landing page for the 5-year American Community Survey:

https://www.census.gov/data/developers/data-sets/acs-5year.html 

Under the year header (e.g. **2017**) and **Detailed Tables** subhead, there are links to that year's list of variables for the ACS5, in HTML, JSON, and XML format. For example, here are 2017's links on the Census website:

- [html](https://api.census.gov/data/2017/acs/acs5/variables.html)
- [xml](https://api.census.gov/data/2017/acs/acs5/variables.xml)
- [json](https://api.census.gov/data/2017/acs/acs5/variables.json)




## Repo details

### Stashed data

The [data/stashed](data/stashed) directory contains the original files as saved from the Census website.

The script [src/stash-files.sh](src/stash-files.sh) downloads the data into [data/stashed](data/stashed).

### Collated data

The [data/collated](data/collated) directory contains structural transformations of the original data, e.g. converting JSON to CSV.


[src/collate-json-as-csv.py](src/collate-json-as-csv.py) converts the regular variables to CSV format and saves to [data/collated/acs5-2017-detailed-variables.csv](data/collated/acs5-2017-detailed-variables.csv).


