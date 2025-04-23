#!/usr/bin/env python3
##
## EPITECH PROJECT, 2025
## run
## File description:
## run
##

#!/user/bin/env python3

import csv

with open('bs.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in reader:
        print(row)