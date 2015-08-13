'''
9.4 Write a program to read through the mbox-short.txt and figure out who has the sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
'''


name = raw_input("File Name:")
text = open(name)

committed=dict()

for line in text:
    if line.startswith("From "):
        words = line.split()
        sender = words[1]
        committed[sender]=committed.get(sender,0) + 1


bigsender=None
commits=None

for key,value in committed.items() :
    if bigsender is None or value > commits:
        bigsender=key
        commits=value

print bigsender, commits

print committed

