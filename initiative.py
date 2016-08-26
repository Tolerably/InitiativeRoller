# Better Initative
# Eric Williams, August of 2016

"""This program, provided the correctly formatted input file(S), will roll initative
for all combatants given.

This program takes two combinations of input files: a file called "combatants.csv",
which will contain all combatants, players and npcs alike."""


import os.path
    
def prepFile(name):
    """Preps a file in the the given folder for access to other functions.
     - Takes one argument: name, a string containing the name of the file being 
     accessed
     - Returns a list of strings from the file provided"""
    
    # Find absolute path
    directory = os.path.dirname(os.path.abspath(__file__))
    # Build an absolute filename from directory + filename 
    filename = os.path.join(directory, name) 
    # Open the file and store it in a file object variable. 
    file = open(filename,'r')
    
    # Move contents of the file into a list of strings
    filecontents = []
    for line in file:
        filecontents.append(line)
        
    # Close the file because it's not needed
    file.close()
    
    # Return the list of strings
    return filecontents
    
def d20():
    """Returns the outcome of a 20 sided die.
     - Takes no arguments
     - Returns one integer between 1 and 20"""
    from random import randint # for rolling
    return randint(1,20)
    
def init(mod):
    """Returns an initative roll.
     - Takes one argument: mod, an int containing the combatant's intiative modifier
     - Returns one int representing a roll made using the combatant's initative 
     modifier"""
    
    return d20()+mod

def parseFile(fileContents):
    """Parses the fileContents
     - Takes one argument: fileContents, a list of strings, such as one provided
     by the function prepFile()
     - Returns a list of lists of strings that has been properly formatted for
     further processing by this program"""
    
    commentLines = [] # Stores lines that need to be removed entirely
    for i in range(len(fileContents)):
        # removing escape characters
        fileContents[i-1] = fileContents[i-1].replace('\n','')
        # Put all the strings that need to be removed in a seperate list
        if '#' in fileContents[i-1]:
            commentLines.append(fileContents[i-1])
        else:
            # splitting the strings that don't need to be removed
            fileContents[i-1] = fileContents[i-1].split(',')
    
    for line in commentLines:
        fileContents.remove(line)
    return fileContents

# Prep and parse file
contents = parseFile(prepFile("combatants.csv"))

# Do the actual rolling
rolls = {} # Dictionary
for entry in contents:
    rolls[entry[0]] = init(int(entry[1])) # Dict syntax- Name:mod

# Sort the rolls from greatest to least
sortedRolls = sorted(rolls,key=rolls.get)
sortedRolls.reverse()

# Print and format the sorted rolls
for i in range(len(sortedRolls)):
    print(str(i+1)+". "+sortedRolls[i]+": "+str(rolls[sortedRolls[i]]))
