#!/bin/sh

curl -o data/stashed/acs5-2017-detailed-variables.json \
    https://api.census.gov/data/2017/acs/acs5/variables.json

curl -o data/stashed/acs5-2017-detailed-variables.html \
    https://api.census.gov/data/2017/acs/acs5/variables.html
