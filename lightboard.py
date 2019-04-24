#!/usr/bin/env python3
import column, multihelp, sys, json
import multiprocessing

# Values for the Characters for the 14 Seg
character_source = './data/characters.json'
# configuration_source
config = './data/hardware.json'

with open(character_source) as file:
    character_source = json.load(file)
with open(config) as file:
    config = json.load(file)

#List Comprehension that stores Column object and display name
columns = [(column.Column(
 config[col]['segments']['bus_number'],
 config[col]['segments']['address'],
 character_source,
 config[col]['button'],
 config[col]['lightline']
 ), col) for col in sys.argv[2:]]

if sys.argv[1] == 'off':
    for c in columns:
        print(c)
        c[0].off()

else:
    for col in columns:
        extra = multiprocessing.Pool(process = len(columns))
        col[0].activate(col[1])
        extra.apply_async(multihelp.run_activate(col[0], col[1]))

    


