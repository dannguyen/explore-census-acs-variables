# import json
# from pathlib import Path

# SRC_PATH = Path('data/stashed/acs5-2017-detailed-variables.json')
# DEST_PATH = Path('data/collated/acs5-2017-detailed-variables.csv')

# OUT_HEADERS = ['official_name', 'official_label',
#                 'concept', 'required', 'limit', 'predicate',
#                 ]

# with open(SRC_PATH) as o:
#     variables = json.load(o)['variables']


#     # "B24123_133E": {
#     #   "label": "Estimate!!Total!!Preschool and kindergarten teachers",
#     #   "concept": "DETAILED OCCUPATION BY MEDIAN EARNINGS IN THE PAST 12 MONTHS (IN 2017 INFLATION-ADJUSTED DOLLARS) FOR THE FULL-TIME, YEAR-ROUND CIVILIAN EMPLOYED FEMALE POPULATION 16 YEARS AND OVER",
#     #   "predicateType": "int",
#     #   "group": "B24123",
#     #   "limit": 0,
#     #   "attributes": "B24123_133M,B24123_133MA,B24123_133EA"
#     # },
