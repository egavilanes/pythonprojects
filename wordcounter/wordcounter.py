# create an automatic system that can count the word from a text file automatically

# read text file using Python
# store the whole document in a list variable
# split the document using split() function
# count the number of words in the variable without space

f = open("/Users/emilygavilanes/Coding Projects/pythonprojects/wordcounter/story.txt","r")

count = 0

# read content of file and store into variable
data = f.read()

#split data into seperate lines
lines = data.split()

# add length of lines to count variable
count += len(lines)


print(count)



