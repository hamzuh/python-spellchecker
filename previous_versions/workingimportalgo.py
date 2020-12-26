import string
import tkinter
from tkinter import filedialog
from tkinter import Tk
from difflib import SequenceMatcher

punctable = str.maketrans("", "", string.punctuation)
numbertable = str.maketrans("", "", string.digits)
poundtable = str.maketrans("", "", "£")

dictionaryfile = open("EnglishWords.txt", "r")
dictionary = (dictionaryfile.read()).split()

def stats():
      print(stats)

def spellChecker(splitlist):
      for word in splitlist:
            if word in dictionary:
                  continue
            bestword = ""
            highscore = 0
            currentscore = 0
            for item in dictionary:
                  currentscore = SequenceMatcher(None, word, item).ratio()
                  if currentscore >= highscore:
                        highscore = currentscore
                        bestword = item
            print("Instead of " + word + ", did you mean " + bestword + "?")

def sentenceCleaner(dirtysentence):
      dirtysentence = dirtysentence.translate(numbertable)
      dirtysentence = dirtysentence.translate(punctable)
      dirtysentence = dirtysentence.translate(poundtable)
      dirtysentence = dirtysentence.lower()
      elements = dirtysentence.split()
      print("The raw words you've inputted are as follows \u2023 ", end = "")
      for x in range(0, len(elements)):
            print(elements[x], end = " ")
      print("\n")
      spellChecker(elements)

def checkSentence():
      sentence = str(input("\nEnter the sentence you want to spell check \u2023 "))
      sentenceCleaner(sentence)

def checkFile():
      print("\nSelect the file you want to spell check \u2023 ")
      Tk().withdraw()
      filepath = filedialog.askopenfilename()
      sentence = open(filepath, "r")
      sentenceCleaner(sentence.read())

for x in range(0, 11):
      print("\u2550", end = "")
print("\n\u24EA \u2023 Quit the program.")
print("\u2460 \u2023 Spell check a sentence.")
print("\u2461 \u2023 Spell check a file.")
for x in range(0, 11):
      print("\u2550", end = "")
      
def firstQuestion():
      firstanswer = input("\nType in the corresponding number to choose an option from the list above \u2023 ")
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
