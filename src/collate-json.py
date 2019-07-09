import csv
import json
from pathlib import Path
import re

SRC_PATH = Path('data/stashed/acs5-2017-detailed-variables.json')
DEST_PATH = Path('data/collated/acs5-2017-detailed-variables.csv')
DEST_PATH.parent.mkdir(exist_ok=True, parents=True)
OUT_HEADERS = ['year', 'survey', 'official_name', 'label', 'concept',
                'predicateType', 'group', 'limit', 'attributes',
             ]



#     # "B24123_133E": {
#     #   "label": "Estimate!!Total!!Preschool and kindergarten teachers",
#     #   "concept": "DETAILED OCCUPATION BY MEDIAN EARNINGS IN THE PAST 12 MONTHS (IN 2017 INFLATION-ADJUSTED DOLLARS) FOR THE FULL-TIME, YEAR-ROUND CIVILIAN EMPLOYED FEMALE POPULATION 16 YEARS AND OVER",
#     #   "predicateType": "int",
#     #   "group": "B24123",
#     #   "limit": 0,
#     #   "attributes": "B24123_133M,B24123_133MA,B24123_133EA"
#     # },


with open(SRC_PATH) as src:
    datavars = json.load(src)['variables']


destfile = DEST_PATH.open('w')
outs =csv.DictWriter(destfile, fieldnames=OUT_HEADERS)
outs.writeheader()

survey, year = re.match(r'^(\w+)-(\d{4})', SRC_PATH.name).groups()


for name, datum in datavars.items():
    if not datum.get('predicateOnly') and not datum.get('required'): # skip predicateOnly variables for now
        row = {k: v for k, v in datum.items()}
        row['survey'] = survey
        row['year'] = year
        row['official_name'] = name

        outs.writerow(row)

destfile.close()

