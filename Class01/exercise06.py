#!/usr/bin/env python

import yaml
import json

# List generation
l = range(8)
l.append({})
l[-1]['ip_addr'] = '1.1.1.1'
l[-1]['name'] = 'Default router'
l[-1]['platform'] = {}
l[-1]['platform']['vendor'] = 'cisco'
l[-1]['platform']['system'] = 'IOS'
l.append(range(8, 10))

# Print list as YAML file
with open('exercise06.yaml', 'w') as yaml_file:
    yaml_file.write(yaml.dump(l, default_flow_style=False))

# Print list as JSON file
with open('exercise06.json', 'w') as json_file:
    json.dump(l, json_file)
    #json_file.write(json.dumps(l))

