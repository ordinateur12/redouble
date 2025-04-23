#!/usr/bin/env python3
##
## EPITECH PROJECT, 2025
## run
## File description:
## run
##

#!/user/bin/env python3

import csv

# Ouverture du fichier CSV
with open('bs.csv', 'r') as csvfile:
    # Création de l'objet reader
    reader = csv.reader(file, delimiter=',', quotechar='|')
    for row in reader: print(row)
        if row(id) == id
        # Affichage id dans le terminal
        print(f"ID: {ligne[0]}, Nom: {ligne[1]}, Email: {ligne[2]}")