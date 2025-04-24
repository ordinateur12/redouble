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

def get(id, reader):
    for row in reader:
        if (id == row['id']) :
            print(f"id : {row['id']}")
            print(f"name : {row['name']}")
            print(f"email : {row['email']}")

def delete():
    

if __name__ == '__main__':
    with open('bs.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        if (sys.argv[1] == "get") :
            id = sys.argv[3]
            get(id, reader)
        if (sys.argv[1] == "del") :
            id = sys.argv[3]
            delete(id)