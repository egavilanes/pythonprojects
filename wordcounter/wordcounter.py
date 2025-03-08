# create an automatic system that can count the word from a text file automatically

# read text file using Python
# store the whole document in a list variable
# split the document using split() function
# count the number of words in the variable without space

f = open("/wordcounter/story.txt","r")

c = []

for x in f:
    print(x)
    c.append(x.split(' '))


