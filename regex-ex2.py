import re

def printEmailAddresses(fileName):
    """ prints email addresses - idenified as after From:
    
        fileName -- the name of the file to read from
    """
    fileName = mbox-short-1.txt
    # open the file
    hand = open(fileName)

    # loop through the lines
    for line in hand:

        # remove white space on the right side of the string
        line = line.rstrip()

        # if starts with From: then print that line
        if line.startswith('From:'):
            print (line)

def printEmailWithRegex(fileName):
    """ prints email addresses using a regex

        fileName - the name of the file to read from
    """

    # open the file for reading
    hand = open(fileName)

    # loop through the lines
    for line in hand:

        # remove white space on the right side
        line = line.rstrip()

        # print lines that start with "From: "
        if re.search('^From:', line) :
            print (line)

def getEmailsWithRegex(fileName):
    """ prints email addresses using a regex

        fileName - the name of the file to read from
    """

    # open the file for reading
    hand = open(fileName)

    # email list
    emailList = []

    # loop through the lines
    for line in hand:

        # remove white space on the right side
        line = line.rstrip()

        # find all that start with a non space then @ then more non space
        currList = re.findall('\S+@\S+', line)

        # print the found emails
        if len(currList) > 0:
            print(currList)

        # add the current list to the list of all
        emailList += currList

    # return the number found
    return emailList

print("Emails found")
print(len(findEmailsWithRegex("mbox-short.txt")))
