'''
Pramodh Guduru
KUID: 3114377
Date: 9/18/24
Lab: lab 1
Last modified: 9/11/24
Purpose: main() file, runs the program
'''
# file_name = gibbons-boardgames.tsv
from executive import Executive

#main
def main():
  file_name = input("Enter the name of the input file: ")
  my_exec = Executive(file_name)
  my_exec.user_menu()

if __name__ == "__main__":
  main()

