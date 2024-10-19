'''
Pramodh Guduru
KUID: 3114377
Date: 9/30/24
Lab: lab 3
Last modified: 9/29/24
Purpose: executes from the browser and provides the UI for the user
'''
#executive.py
from background import Node
from background import Stack
from background import LinkedQueue
from background import LinkedList
from webbrowser import Browser

class Executive:
    def __init__(self):
        self.browser = Browser()

    def execute_command(self, command):

        parts = command.split()  # Splits inputs into different tokens
        if len(parts) == 0:
            print("No command provided.")

        input = parts[0].upper()

        if input == "NAVIGATE" or "NAV" and len(parts) == 2:
            url = parts[1]
            self.browser.navigate_to(url)
            print(f"Navigating to: {url}")
            print("")

        elif input == "BACK":
            prev_page = self.browser.back()
            if prev_page is not False and not None:
                print(f"Moved back to: {prev_page}")
            print("")                

        elif input == "FORWARD":
            next_page = self.browser.forward()
            if next_page is not False:
                print(f"Moved forward to: {next_page}")
            print("")

        elif input == "HISTORY":
            self.browser.history()
            print("")

        else:
            print(f"Command Not Found. Try Again")
            print("")

def main():
    web_browser = Executive()

    while True:
        command = input("Enter command 'NAVIGATE' ('NAV'), 'BACK', 'FORWARD', 'HISTORY' or 'EXIT' to quit: ")
        if command.upper() == 'EXIT':
            break
        web_browser.execute_command(command)

if __name__ == "__main__":
    main()
