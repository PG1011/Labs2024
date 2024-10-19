'''
Pramodh Guduru
KUID: 3114377
Date: 9/18/24
Lab: lab 1
Last modified: 9/18/24
Purpose: Contains the scenarios and methods that execute when a user inputs the correct input
'''
from boardgames import BoardGames

class Executive:
    #this method is used to initialize the object attributes
    def __init__(self, file_name):
        self._init_ = None
        self.name, self.gibbonsrating, self.baverage, self.avgweight, self.yearpublished, self.bggbestplayers = BoardGames.boardgames(file_name)

    #contains all of the scenarios that a user can call
    def user_menu(self):
        self._init_=None
        while True:
            print('')
            print('User Menu Options')
            print('1- Print all games from highest Gibbons rating to lowest')
            print('2- Print all games from a year')
            print('3- Print all games with a weight equal to or lower than a provided weight')
            print('4- The People VS Dr. Gibbons')
            print('5- Print based on player count')
            print('6- Exit the program')
            print('')
            user_choice = input('Please select a number between 1 and 6: ')
            if user_choice in ['1', '2', '3', '4', '5', '6']:

                if user_choice == '1':
                    print("Print all games from highest Gibbons rating to lowest")
                    print('')
                    rating = list(zip(self.name, self.gibbonsrating))
                    sort = sorted(rating, key = lambda x: x[1], reverse = True)
                    for self.name, rating in sort:
                        #print('============')
                        #print(f"{self.name}")
                        #print(f"{self.gibbonsrating}")
                        #print(f"{self.baverage}")
                        #print(f"{self.avgweight}")
                        #print(f"{self.yearpublished}")
                        #print(f"{self.bggbestplayers}")
                        #print('============')
                        print(f"{self.name} with a Gibbons rating of {rating}")
                else:
                    pass

                if user_choice == '2':
                    print("Printing all games from a year")
                    input2 = int(input('Please type in a year: '))
                    print('')
                    found = False

                    for ele in range(len(self.yearpublished)):
                        if self.yearpublished[ele] == input2:
                            print('============')
                            print(f"{self.name[ele]}")
                            print(f"{self.gibbonsrating[ele]}")
                            print(f"{self.baverage[ele]}")
                            print(f"{self.avgweight[ele]}")
                            print(f"{self.yearpublished[ele]}")
                            print(f"{self.bggbestplayers[ele]}")
                            print('============')
                            #print(f"{self.name[ele]} was found for year {self.yearpublished[ele]}" )
                            found = True
                            
                    if not found:
                        print('')
                        print('No games found')
                        print('')

                if user_choice == '3':
                    print("Printing all games with a weight equal to or lower than a provided weight")
                    input3 = float(input('Please type in a weight between 0-5: '))
                    print('')
                    found = False
                    if (input3 <= 5) or (input3 == 0):
                        for ele in range(len(self.avgweight)):
                            if (self.avgweight[ele] == input3) or (self.avgweight[ele] < input3):
                                print('============')
                                print(f"{self.name[ele]}")
                                print(f"{self.gibbonsrating[ele]}")
                                print(f"{self.baverage[ele]}")
                                print(f"{self.avgweight[ele]}")
                                print(f"{self.yearpublished[ele]}")
                                print(f"{self.bggbestplayers[ele]}")
                                print('============')
                                #print(f"{self.name[ele]} was found for weight {self.avgweight[ele]}")
                                found = True
                        if not found:
                            print('')
                            print('No games found')
                            print('')
                    else:
                        print('')
                        print('Not a valid weight')
                        print('')
                else:
                    pass

                if user_choice == '4':
                    print("The People VS Dr. Gibbons")
                    input4 = float(input('Please type in a number that you would like to compare against Dr. Gibbons: '))
                    print("Now Printing: The People VS Dr. Gibbons: The Origin")
                    found = False
                    for ele in range(len(self.name)):
                        diff = abs(self.gibbonsrating[ele] - self.baverage[ele])
                        if diff >= input4:
                            print('============')
                            print(f"{self.name[ele]}")
                            print(f"{self.gibbonsrating[ele]}")
                            print(f"{self.baverage[ele]}")
                            print(f"{self.avgweight[ele]}")
                            print(f"{self.yearpublished	[ele]}")
                            print(f"{self.bggbestplayers[ele]}")
                            print('============')
                            #print(f"{self.name[ele]}  Gibbons Rating: {self.gibbonsrating[ele]}, People's Rating: {self.baverage[ele]} (Difference: {diff})")
                            found = True
                    if not found:
                        print('')
                        print('No games found')
                        print('')
                else:
                    pass

                if user_choice == '5':
                    input5 = int(input('Please type in a player count between 1-10: '))
                    print('')
                    print("Printing based on player count")
                    print('')
                    found = False
                    for ele in range(len(self.bggbestplayers)):
                        if input5 in self.bggbestplayers[ele]:
                            print('============')
                            print(f"{self.name[ele]}")
                            print(f"{self.gibbonsrating[ele]}")
                            print(f"{self.baverage[ele]}")
                            print(f"{self.avgweight[ele]}")
                            print(f"{self.yearpublished[ele]}")
                            print(f"{self.bggbestplayers[ele]}")
                            print('============')
                            #print(f"{self.name[ele]} was found for player count {self.bggbestplayers[ele]}")
                            found = True
                    if not found:
                        print('')
                        print('No games found')
                        print('')
                else:
                    pass

                if user_choice == '6':
                    print('')
                    print("Exiting the program")
                    print("Thanks for playing! Come back soon...")
                    break
                else:
                    pass

            else:
                print('')
                print("Invalid input. Please enter a number between 1 and 6.")
                print("Type 6 if you'd like to exit instead.")
                print('')
