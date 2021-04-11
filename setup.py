#!/bin/python

import pprint
from utils import read_json_file

# import argparse
# parser = argparse.ArgumentParser(description='Add some integers.')
# parser.add_argument('integers', metavar='N', type=int, nargs='+', help='interger list')
# parser.add_argument('--sum', action='store_const', const=sum, default=max,
#                   help='sum the integers (default: find the max)')
# args = parser.parse_args()
# print(args.sum(args.integers))


steps = read_json_file('configs/setup.json')
options = {}
skippable = []

for step in steps:
    hasDefault = 'default' in step
    isParameter = 'name' in step
    isSkippable = 'skippable' in step and step['skippable'] is True

    if isParameter and 'skippable' in step and step['skippable'] in skippable:
        print(step['name'] + ' Skipped')
        continue

    if 'section' in step and step['section'] is True:
        print()
        print(step['description'])
    else:
        print('  ' + step['description'])

    if isSkippable:
        print('  or press enter and skip this server')

    if hasDefault:
        print('  or press enter to set default (' + step['default'] + ')')

    if isParameter:
        options[step['name']] = input('  :>')
        if hasDefault and options[step['name']] == '':
            options[step['name']] = step['default']
        if isSkippable and options[step['name']] == '':
            skippable.append(step['name'])
        pprint.pprint(options)

if len(skippable) > 0:
    print('Simple scheme')

config_json = ''
with open('configs/env.template.json', "r") as read_file:
    config_json = read_file.read()
    for key in options:
        config_json = config_json.replace('%' + key + '%', options[key])

text_file = open('projects/' + options['site-name'] + '.json', 'w')
text_file.write(config_json)
text_file.close()
