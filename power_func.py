'''
Pramodh Guduru
KUID: 3114377
Date: 10/03/24
Lab: lab 4
Last modified: 10/03/24
Purpose: uses recursion (not python's functions) in order to calculate n^x where n is the base and x is the exponent
'''
#power_func.py
class Power:
    def power_func(self,baseinput,powerinput): #edited function made in class lecture
        if powerinput == 0:
            return 1
        else:
            return baseinput * self.power_func(baseinput, powerinput - 1)

    def execute_command(self):
        while True: #makes sure that the input is an integer
            try:
                baseinput = int(input("Enter a base: "))
                break #exits the try except if the input matches the
            except ValueError:
                print("Sorry, your input must be an integer.")
        while True: #makes sure that the input is an integer
            try:
                powerinput = int(input("Enter a power: "))
                break #exits the try except
            except ValueError:
                print("Sorry, your input must be an integer.")
        if (baseinput >= 0) and (powerinput >= 0):
            ans = self.power_func(baseinput,powerinput)
            print(ans)
        else:
            print(f"Sorry, your base/exponent must be zero or larger.")

def main():
    power = Power()

    while True:
        command = input("Enter an input to continue or enter exit: ")
        if command.upper() == 'EXIT':
            break
        power.execute_command()

if __name__ == "__main__":
    main()