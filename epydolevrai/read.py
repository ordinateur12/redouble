#!/usr/bin/env python3
##
## EPITECH PROJECT, 2025
## run
## File description:
## run
##

#!/user/bin/env python3

import csv
import sys

if (sys.argv[1] == "get") :
    id = sys.argv[3]
with open('bs.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if (id == row['id']) :
            print(f"id : {row['id']}")
            print(f"name : {row['name']}")
            print(f"email : {row['email']}")