'''
Pramodh Guduru
KUID: 3114377
Date: 9/25/24
Lab: lab 2
Last modified: 9/25/24
Purpose: main() file, runs the program, and provides cases for possible inputs from user
'''
from process import Process
from function import Function
from process import LinkedQueue

class CPU_Scheduler:
    def __init__(self): #initializes queue
        self.queuey = LinkedQueue()

    def add_process(self, process): #adds process to queue
        self.queuey.enqueue(process)
        print(f"Process {process.name} added to the scheduler.")

    def execute_command(self, command): #executes based on input received
        parts = command.split() #splits inputs into different tokens
        if len(parts) == 0:
            print("No command provided.")
            return

        input = parts[0].upper()

        if input == "START" and len(parts) == 2:
            process_name = parts[1]
            new_process = Process(process_name)
            self.add_process(new_process)

        elif input == "CALL" and len(parts) == 3:
            if self.queuey.is_empty():
                print("No processes in the queue.")
                return
            function_name = parts[1]
            third = parts[2]
            lowercase_third = third.lower()
            can_handle_exceptions = lowercase_third == "true"
            process = self.queuey.dequeue()
            process.add_call(Function(function_name, handle_exceptions = can_handle_exceptions))
            self.queuey.enqueue(process)

        elif input == "RETURN":
            if self.queuey.is_empty():
                print("No processes in the queue.")
                return
            process = self.queuey.dequeue()
            if process.return_from_call():
                print(f"Process {process.name} removed from the queue.")
            else:
                self.queuey.enqueue(process)

        elif input == "RAISE":
            if self.queuey.is_empty():
                print("No processes in the queue.")
                return
            process = self.queuey.dequeue()
            if process.handle_exception():
                print(f"Process {process.name} removed from the queue due to unhandled exception.")
            else:
                self.queuey.enqueue(process)

        else:
            print("Unknown Command")

def main(): #main method
    scheduler = CPU_Scheduler()

    while True:
        command = input("Enter command 'START', 'CALL', 'RETURN', 'RAISE' or 'EXIT' to quit: ")
        if command.lower() == 'exit':
            break
        scheduler.execute_command(command)

if __name__ == "__main__":
    main()