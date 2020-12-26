import string
import tkinter
from tkinter import filedialog
from tkinter import Tk

punctable = str.maketrans("", "", string.punctuation)
numbertable = str.maketrans("", "", string.digits)
poundtable = str.maketrans("", "", "£")

dictionaryfile = open("EnglishWords.txt", "r")
dictionary = (dictionaryfile.read()).split()

def spellChecker(splitlist):
      print(splitlist)
      for word in splitlist:
            correctcount = 0
            anchorword = ("")
            for item in dictionary:
                  if len(word) > len(item):
                        anchorword = item
                  else:
                        anchorword = word
                  for x in range(0, len(anchorword)):
                        if word[x] == item[x]:
                              correctcount += 1
            if correctcount >= (0.5 * len(word)):
                  print(item)

def sentenceCleaner(dirtysentence):
      dirtysentence = dirtysentence.translate(numbertable)
      dirtysentence = dirtysentence.translate(punctable)
      dirtysentence = dirtysentence.translate(poundtable)
      dirtysentence = dirtysentence.lower()
      elements = dirtysentence.split()
      spellChecker(elements)

def checkSentence():
      sentence = str(input("\nEnter the sentence you want to spell check: "))
      sentenceCleaner(sentence)

def checkFile():
      print("\nSelect the file you want to spell check: ")
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
