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
import pprint
from new import get_csv_path

def get(id, reader):
    for row in reader:
        if (id == row['id']) :
            print(f"id : {row['id']}")
            print(f"name : {row['name']}")
            print(f"email : {row['email']}")

def delete(id, data):
    fieldnames = ['id', 'name', 'email']
    tab = []
    for row in data:
        if (id == row['id']):
            print(f"delete  user {id}")
            continue
        tab.append(row)
    with open('bs.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(tab)

def opn():
    with open('bs.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        return list(reader)

if __name__ == '__main__':
    data = opn()
    if (sys.argv[1] == "get") :
        id = sys.argv[3]
        get(id, data)
    if (sys.argv[1] == "del") :
        id = sys.argv[3]
        delete(id, data)