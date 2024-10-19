'''
Pramodh Guduru
KUID: 3114377
Date: 9/18/24
Lab: lab 1
Last modified: 9/17/24
Purpose: Creates lists that then store the data from the boardgames file
'''
import csv

class BoardGames:
    #contains the initialization of lists
    def boardgames (file_name):
        name = []
        gibbonsrating = []
        baverage = []
        avgweight = []
        yearpublished = []
        bggbestplayers = []
        with open (file_name, 'r') as games: #opens the specified file and allows the program to read and place data in lists
            next(games) #skips the string headers that
            for line in games:
                columns = line.strip().split('\t') #makes sure that the data is taken from the columns instead of from the rows
                name.append(str(columns[0]))
                gibbonsrating.append(float(columns[1]))
                baverage.append(float(columns[2]))
                avgweight.append(float(columns[3]))
                yearpublished.append(int(columns[4]))
                bggbestplayers.append([int(player) for player in columns[5].split(',')]) #.split allows multiple integers to be be read

        return name, gibbonsrating, baverage, avgweight, yearpublished, bggbestplayers
