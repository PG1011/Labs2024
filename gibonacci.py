'''
Pramodh Guduru
KUID: 3114377
Date: 10/08/24
Lab: lab 4
Last modified: 10/08/24
Purpose: use the fibonacci sequence to display a number from a specific integer in the sequence or check if a number is part of the sequence
'''
#fibonnaci.py
class Fibonacci:
    def fibonnaci_func(self, powerinput): #fibonacci sequence (powerinput is the user input)
        if powerinput == 0:
            return 0
        elif powerinput == 1:
            return 1
        else:
            return self.fibonnaci_func(powerinput -1) + self.fibonnaci_func(powerinput -2)

    def is_in_fibonacci(self, numput, value=0, next_value=1): #method for when the user inputs -v
        if numput == value: #checks if the given number (numput) is equal to a number in the fibonacci sequence (value)
            return True
        elif numput < value:
            return False
        else:
            return self.is_in_fibonacci(numput, value + next_value, value) #value+next_value changes value to the next number in the sequence
    def execute_command(self, command):
        parts = command.split()  # Splits inputs into different tokens
        if len(parts) == 0:
            print("No command provided.")
        else:
            finput = parts[0].upper()

        if (finput == "-I") and len(parts) == 2: #method for when user inputs -i
            try:
                powerinput = int(parts[1])
                print(f"{self.fibonnaci_func(powerinput)}") #simply recurses through the fibonacci sequence
            except ValueError:
                print("Invalid input. Please provide a valid number.")
        elif (finput == "-V") and len(parts) == 2: #method for when user inputs -v
            try:
                numput = int(parts[1]) #userinput
                if self.is_in_fibonacci(numput):
                    print(f"{numput} is in the Fibonacci sequence!")
                else:
                    print(f"{numput} is not in the Fibonacci sequence.")
            except ValueError:
                print("Invalid input. Please provide a valid number.")
        else:
            print("Invalid day or command format.")

def main():
    fibonacci = Fibonacci()
    print("If you'd like to leave at any time type 'exit'")
    while True:
        command = input("Enter mode and value: ")
        if command.upper() == 'EXIT':
            print("Thanks for sequencing the Fibonacci")
            break
        fibonacci.execute_command(command)

if __name__ == "__main__":
    main()
