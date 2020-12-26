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
dictionaryfile.close()

def stats():
      print(stats)

def secondQuestion():
      selection = input("Type in the corresponding number to choose an option from the list above \u2023 ")
      selection = selection.replace(" ","")
      if selection in ["1", "2", "3", "4"]:
            return(selection)
      else:
            secondQuestion()

def spellChecker(splitlist):
      for word in splitlist:
            if word in dictionary:
                  continue
            bestwords = []
            highscore = 0
            currentscore = 0
            for item in dictionary:
                  currentscore = SequenceMatcher(None, word, item).ratio()
                  if currentscore >= highscore:
                        highscore = currentscore
            for item in dictionary:
                  currentscore = SequenceMatcher(None, word, item).ratio()
                  if currentscore == highscore:
                        bestwords.append(item)
            for x in range(0, 17):
                  print("\u2550", end = "")
            print("\n'" + word + "'" + " is incorrectly spelt.\n")
            print("\u2460 \u2023 Ignore the word.")
            print("\u2461 \u2023 Mark as incorrectly spelt.")
            print("\u2462 \u2023 Add the word to the dictionary.")
            print("\u2463 \u2023 Replace the word with a suggestion.")
            for x in range(0, 17):
                  print("\u2550", end = "")
            print("\n")
            selection = secondQuestion()
            if selection == ("1"):
                  pass
            if selection == ("2"):
                  splitlist[(splitlist.index(word))] = str("\u2754" + word + "\u2754")
            if selection == ("3"):
                  addword = open("EnglishWords.txt", "a")
                  addword.write("\n" + word)
                  addword.close()
            if selection == ("4"):
                  if len(item) == 1:
                        print("\nInstead of " + word + ", did you mean " + bestwords[0] + "?")
                  if len(item) > 1:
                        print("\nInstead of " + word + ", did you mean ", end = "")
                        for x in range(0, (len(bestwords)-1)):
                              print(bestwords[x], end = " or ")
                        print(bestwords[-1] + "?")
                        option = str(input("Enter the word you meant as it appears in the suggestion, or type anything else to mark the original word as incorrect \u2023 "))
                        if option in bestwords:
                              splitlist[(splitlist.index(word))] = option
                        else:
                              splitlist[(splitlist.index(word))] = str("\u2754" + word + "\u2754")
      for x in range(0, len(splitlist)):
            print(splitlist[x], end = " ")
                              
def sentenceCleaner(dirtysentence):
      dirtysentence = dirtysentence.translate(numbertable)
      dirtysentence = dirtysentence.translate(punctable)
      dirtysentence = dirtysentence.translate(poundtable)
      dirtysentence = dirtysentence.lower()
      elements = dirtysentence.split()
      print("\nThe raw words you've inputted are as follows \u2023 ", end = "")
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
print("\n")
      
def firstQuestion():
      firstanswer = input("Type in the corresponding number to choose an option from the list above \u2023 ")
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
