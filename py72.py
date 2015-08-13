'''
7.2 Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
X-DSPAM-Confidence:    0.8475
Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below.
You can download the sample data at http://www.pythonlearn.com/code/mbox-short.txt when you are testing below enter mbox-short.txt as the file name.
'''
# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
try:
    fh = open(fname)
except:
    print "That is not a valid filename"
    quit()
sum = 0
total = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    sum += float(line[19:].rstrip())
    total += 1

average = str(sum/total)
print "Average spam confidence: " + average
