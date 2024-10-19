'''
Pramodh Guduru
KUID: 3114377
Date: 10/07/24
Lab: lab 4
Last modified: 10/07/24
Purpose: displays the number of infected on the specified day 
'''
#outbreak_returns
class Outbreak_Returns:
    def outbreak(self, powerinput):
        if powerinput == 1: #basecase 1
            return 6
        elif powerinput == 2: #basecase 2
            return 20
        elif powerinput == 3: #basecase 3
            return 75
        else: #recursive function
            return self.outbreak(powerinput - 1) + self.outbreak(powerinput -2) + self.outbreak(powerinput -3)

    def execute_command(self):
        while True:  # makes sure that the input is an integer
            try:
                print("OUTBREAK!")
                powerinput = int(input("What day do you want a sick count for?: "))
                break  # exits the try except if the input matches the
            except ValueError:
                print(print(f"Invalid day"))
        if (powerinput >= 1): #only accepts days over 1
            ans = self.outbreak(powerinput)
            print(f"Total people with flu: {ans}")
        else:
            print(f"Invalid day")


def main():
    outbreak = Outbreak_Returns()

    while True:
        command = input("Enter an input to continue or enter exit: ")
        if command.upper() == 'EXIT':
            break
        outbreak.execute_command()


if __name__ == "__main__":
    main()