#!/usr/bin/env python

import yaml
import json
from pprint import pprint

# Read YAML file
with open('exercise06.yaml') as yaml_file:
    yaml_list = yaml.load(yaml_file)
    print 'YAML list:'
    pprint(yaml_list)

print ''

# Read JSON file
with open('exercise06.json',) as json_file:
    json_list = json.load(json_file)
    print 'JSON list:'
    pprint(json_list)

