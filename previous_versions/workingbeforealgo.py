import string
import tkinter
from tkinter import filedialog
from tkinter import Tk

punctable = str.maketrans("", "", string.punctuation)
numbertable = str.maketrans("", "", string.digits)
poundtable = str.maketrans("", "", "£")

def sentenceCleaner(dirtysentence):
      dirtysentence = dirtysentence.translate(numbertable)
      dirtysentence = dirtysentence.translate(punctable)
      dirtysentence = dirtysentence.translate(poundtable)
      dirtysentence = dirtysentence.lower()
      elements = dirtysentence.split()
      print(elements)

def checkSentence():
      sentence = str(input("Enter the sentence you want to spell check: "))
      sentenceCleaner(sentence)

def checkFile():
      Tk().withdraw()
      filepath = filedialog.askopenfilename()
      sentence = open(filepath, "r")
      sentenceCleaner(sentence.read())

print("0 - Quit the program.")
print("1 - Spell check a sentence.")
print("2 - Spell check a file.")

def firstQuestion():
      firstanswer = input("\nType in the corresponding number to choose an option from the list above: ")
      firstanswer = firstanswer.replace(" ","")
      if firstanswer == ("0"):
            quit()
      elif firstanswer == ("1"):
            checkSentence()
      elif firstanswer == ("2"):
            checkFile()
      else:
            firstQuestion()

firstQuestion()
