'''
10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below. Note that the autograder does not have support for the sorted() function.
'''

name = raw_input("File Name:")
if len(name) < 1 : name = "mbox-short.txt"
text = open(name)

distrib=dict()

for line in text:
    if line.startswith("From "):
        words = line.split()
        time = words[5]
        hms = time.split(':')
        hour = hms[0]
        distrib[hour] = distrib.get(hour, 0 ) + 1

tmp = list()

for hr, count in distrib.items():
    tmp.append( (hr, count ) )
 
tmp.sort()

for k,v in tmp:
    print k,v



