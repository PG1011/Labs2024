'''
Pramodh Guduru
KUID: 3114377
Date: 10/2/24
Lab: lab 3
Last modified: 10/2/24
Purpose: defines each of the functions 
'''
#webbrowser.py
from background import Node
from background import Stack
from background import LinkedQueue
from background import LinkedList

class Browser:
    def __init__(self):
        self.browser = LinkedList()
        self.current = -1

    def navigate_to(self,url): #adds a new "webpage" to the linked list
        if self.browser.length > 0:
            for _ in range(self.browser.length - self.current - 1):
                self.browser.remove(self.current + 1)
        self.browser.insert(self.browser.length, url)
        self.current = self.browser.length -1

    def forward(self): #goes forward from the previous node
        if self.current + 1 < self.browser.length:
            self.current += 1
            return self.browser.get_entry(self.current)
        else:
            print("No pages available")
            return None

    def back(self): #goes back from the previous node
        if self.current > 0:
            self.current -= 1
            return self.browser.get_entry(self.current)
        else:
            print("No pages available")
            return None

    def history(self): #shows a histroy of all the webpages that have been added to the list
        print("Oldest")
        print("===========")
        history_pages = []
        for i in range(self.browser.length):
            try:
                url = self.browser.get_entry(i)
                if i == self.current:
                    url2 = f"{url}  <==current"
                else:
                    url2 = url
                history_entries.append(formatted_url)
            except:
                raise RunTimeError("No more pages")

        if len(history_entries) == 0:     # Check if the history is empty
            print("No history available.")
        else:
            for entry in history_entries:
                print(entry)
        print("===========")
        print("Newest")

    def jumper(self, start, end):
        jumper = self.front
        for i in range(start, end + 1):
            jumper = jumper.next
        return jumper



