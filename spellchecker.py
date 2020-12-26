# Here I've imported "string" to clean user inputs
# "Tkinter" allows the user to select their file through a file dialog window
# "Difflib" lets me compare strings to check their similarity
# "Datetime" lets me check the current time and find the difference between two times
import string
import tkinter
from tkinter import filedialog
from tkinter import Tk
from difflib import SequenceMatcher
import datetime

# The translate tables are set up so I can remove punctuation, digits and the "£" sign from the user's sentences
punctable = str.maketrans("", "", string.punctuation)
numbertable = str.maketrans("", "", string.digits)
poundtable = str.maketrans("", "", "£")

# I've divided this whole program into functions that can be used to execute these code blocks
# This is so that I can mix and match the order of their execution, incase I want the whole program to repeat
# This is also useful for re-asking users a question or branching off into different paths based on their answer

# This function is used late into the program to create the resulting output file
# This includes stats, raw input, cleaned sentence and spellchecked sentence
# You may notice that multiple variables have been passed to this function, this is done so that it can use information from earlier functions
def createFile(rawinput, uncorrectedsentence, correctedsentence, starttime, wordlength, correctwords, incorrectwords, dictwords, changedwords):
      endtime = datetime.datetime.now()
      timetaken = str(endtime - starttime)
      raw = rawinput
      cleaned = uncorrectedsentence
      spellchecked = correctedsentence
      # Asking user for filename
      newname = input("Enter the filename under which you want your sentence saved \u2023 ")
      if newname == "":
            createFile(raw, cleaned, spellchecked)
      # File is opened and all stats written to it
      newfile = open((str(newname) + ".txt") , "w+")
      newfile.write("TIME OF SPELLCHECKING: " + (endtime.strftime("%c")) + "\n")
      newfile.write("TIME TAKEN " + timetaken + "\n")
      newfile.write("WORDS INPUTTED: " + str(wordlength) + "\n")
      newfile.write("CORRECT SPELLINGS: " + str(correctwords) + "\n")
      newfile.write("INCORRECT SPELLINGS: " + str(incorrectwords) + "\n")
      newfile.write("WORDS ADDED TO DICTIONARY: " + str(dictwords) + "\n")
      newfile.write("CHANGED WORDS: " + str(changedwords) + "\n")
      newfile.write("THE SENTENCE YOU ENTERED WAS: " + str(raw) + "\n")
      newfile.write("THE CLEANED INPUT WAS: " + str(cleaned) + "\n")
      newfile.write("THE SPELLCHECKED SENTENCE IS: " + str(spellchecked))
      newfile.close()
      # Stats function is called and several variables are passed onto it
      stats(endtime, timetaken, wordlength, correctwords, incorrectwords, dictwords, changedwords)

# This function uses variables generated earlier to print out various statistics about the spellchecking process
# I've included a few unicode characters to create a border when printed
def stats(endtime, timetaken, wordlength, correctwords, incorrectwords, dictwords, changedwords):
      print("")
      for x in range(0, 17):
                  print("\u2550", end = "")
      print("\nTIME OF SPELLCHECKING: " + (endtime.strftime("%c")))
      print("TIME TAKEN: " + timetaken)
      print("During that time, we've checked " + str(wordlength) + " words.")
      print("OF THOSE WORDS...")
      print(str(correctwords) + " was/were correctly spelled.")
      print(str(incorrectwords) + " was/were incorrectly spelled.")
      print(str(dictwords) + " was/were added to the dictionary.")
      print(str(changedwords) + " was/ were changed.")
      for x in range(0, 17):
                  print("\u2550", end = "")
      # Here we ask the user if they want to return to the start of the program or quit entirely
      lastanswer = input("\n\nType 'return' to return to the main menu, or type anything else to quit \u2023 ")
      print("")
      if lastanswer == ("return"):
            printOptions()
      else:
            quit()

# This function asks for an answer when an incorrectly spelt word is encountered
# I've put it in its own function so if the answer is invalid it can loop back on itself
# It may be inefficient to use a function for this but it's useful incase I expand the project later
def secondQuestion():
      selection = input("Type in the corresponding number to choose an option from the list above \u2023 ")
      selection = selection.replace(" ","")
      if selection in ["1", "2", "3", "4"]:
            return(selection)
      else:
            secondQuestion()

# This function is the main meat of the program
# It is used to check every inputted word against every word in the dictionary to check for a match
# If there is a match, most of the rest of the function is skipped
# If a match is not encountered, the most similar words are added to a list for later
def spellChecker(splitlist, dirtysentence):
      uncorrectedsentence = " ".join(splitlist)
      rawinput = dirtysentence
      # Take the time now so we can minus it from the program's end time
      starttime = datetime.datetime.now()
      wordlength = len(splitlist)
      correctwords = 0
      incorrectwords = 0
      dictwords = 0
      changedwords = 0
      # For every word...
      for word in splitlist:
            # If the word is correctly spelt...
            if word in dictionary:
                  # Skip the rest
                  correctwords += 1
                  continue
            # Otherwise...
            incorrectwords += 1
            bestwords = []
            highscore = 0
            currentscore = 0
            # For every word in our dictionary set ("EnglishWords.txt")...
            for item in dictionary:
                  # Find the highest scoring match...
                  currentscore = SequenceMatcher(None, word, item).ratio()
                  if currentscore >= highscore:
                        highscore = currentscore
            for item in dictionary:
                  # And any word that matches that score is added to our "bestwords" list
                  currentscore = SequenceMatcher(None, word, item).ratio()
                  if currentscore == highscore:
                        bestwords.append(item)
            # Present options to the user
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
            # Skip if the user chooses to ignore the misspelt word
            if selection == ("1"):
                  pass
            # Mark the word as incorrect by adding a question mark to the start and end of the word
            if selection == ("2"):
                  splitlist[(splitlist.index(word))] = str("?" + word + "?")
            # Add the word to the "EnglishWords" text file, effectively adding it to our dictionary
            if selection == ("3"):
                  addword = open("EnglishWords.txt", "a")
                  addword.write("\n" + word)
                  addword.close()
                  dictwords += 1
            # If the user wants a suggestion to change the word...
            if selection == ("4"):
                  if len(item) == 1:
                        print("\nInstead of " + word + ", did you mean '" + bestwords[0] + "'?")
                  if len(item) > 1:
                        print("\nInstead of " + word + ", did you mean '", end = "")
                        for x in range(0, (len(bestwords)-1)):
                              print(bestwords[x], end = "' or '")
                        print(bestwords[-1] + "'?")
                        option = str(input("\nEnter the word you meant as it appears in the suggestion, or if the word doesn't appear type what you meant followed by an exclamation mark. Alternatively, type anything else to mark the original word as incorrect \u2023 "))
                        print("")
                        # If the user wants to change it to our suggestion...
                        if option in bestwords:
                              # Change the list of words accordingly
                              splitlist[(splitlist.index(word))] = option
                              changedwords += 1
                        # If the user wants to replace it using their own new spelling...
                        elif "!" in option:
                              # Clean the user input
                              option = option.strip()
                              option = option.translate(punctable)
                              # Change the list of words using the user's spelling
                              splitlist[(splitlist.index(word))] = option
                              changedwords += 1
                        # Otherwise...
                        else:
                              # Mark the word as incorrect as we've demonstrated earlier
                              splitlist[(splitlist.index(word))] = str("?" + word + "?")
      # Reconnect all the words in the list into a string and print it
      correctedsentence = " ".join(splitlist)
      print("Your corrected sentence is \u2023 '" + correctedsentence + "'")
      # Execute the file creating function and pass on several stat counters
      createFile(rawinput, uncorrectedsentence, correctedsentence, starttime, wordlength, correctwords, incorrectwords, dictwords, changedwords)

# This function cleans the user input by removing all punctuation, numbers and £s using the translation tables defined earlier
def sentenceCleaner(dirtysentence):
      remaindirty = dirtysentence
      dirtysentence = dirtysentence.translate(numbertable)
      dirtysentence = dirtysentence.translate(punctable)
      dirtysentence = dirtysentence.translate(poundtable)
      dirtysentence = dirtysentence.lower()
      elements = dirtysentence.split()
      # Print out the cleaned result
      print("\nThe raw words you've inputted are as follows \u2023 '", end = "")
      for x in range(0, len(elements)):
            print(elements[x], end = " ")
      print("'\n")
      # Execute the spellchecking function and pass on the "dirty" and cleaned sentences
      spellChecker(elements, remaindirty)

#This function allows the user to type in their own sentence when prompted by the program
def checkSentence():
      sentence = str(input("\nEnter the sentence you want to spell check \u2023 "))
      # Send the result to the next function to be "cleaned"
      # This is so that only words remain in the sentence, no unnecessary symbols
      sentenceCleaner(sentence)

# This function allows the user to select a file containing their sentence via Tkinter
def checkFile():
      print("\nSelect the file you want to spell check \u2023 ")
      Tk().withdraw()
      filepath = filedialog.askopenfilename()
      if filepath == "":
            checkFile()
      # Read the opened file straight to the sentence cleaning function
      sentence = open(filepath, "r")
      sentenceCleaner(sentence.read())

# This function prompts the user for an answer to whether they want to quit or spellcheck a typed or file-based sentence
def firstQuestion():
      # Ask the user the question
      firstanswer = input("Type in the corresponding number to choose an option from the list above \u2023 ")
      # Remove all spaces from their input
      firstanswer = firstanswer.replace(" ","")
      # If the user types 0...
      if firstanswer == ("0"):
            # Quit the program
            quit()
      # If the user types 1...
      elif firstanswer == ("1"):
            # Ask the user to type in a sentence
            checkSentence()
      # If the user types 2...
      elif firstanswer == ("2"):
            # Open a file dialog for the user to select their file
            checkFile()
      # If the user doesn't provide a valid input...
      else:
            # Re-ask the question
            firstQuestion()
            
# This function is the first in the program to be executed
# It resets the dictionary set using a text file
# It also prints out the user's inital options
def printOptions():
      # The "EnglishWords" text files is read and converted to a set "dictionary"
      # (We use a set because the contents need not be ordered like a list and using a set is faster than a list)
      # The file is then closed
      # This is so that we can check if an inputted word is correctly spelt by seeing if it appears in this set
      dictionaryfile = open("EnglishWords.txt", "r")
      global dictionary
      dictionary = set(dictionaryfile.read().split())
      dictionaryfile.close()
      # Print out the user's options
      for x in range(0, 11):
            print("\u2550", end = "")
      print("\n\u24EA \u2023 Quit the program.")
      print("\u2460 \u2023 Spell check a sentence.")
      print("\u2461 \u2023 Spell check a file.")
      for x in range(0, 11):
            print("\u2550", end = "")
      print("\n")
      # Execute the function that asks for and deals with an input
      firstQuestion()

# Get the program started off by executing the inital function
printOptions()
