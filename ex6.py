x = "There are %d types of people." % 10

binary = "binary"

do_not = "don't"

y = "Those who know %s and those who %s." %(binary,do_not)

print x

print y

print "I said: %r" % x

print "I also said: '%s'." % y

hilarious = False

joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

formatter ="%r %r %r %r"

print formatter % (1,2,3,4)

print formatter % ("one","two","three","four")

print formatter % (True,False,True,False)

print formatter % (formatter, formatter,formatter,formatter)

print formatter % (
"I had this thing.",
"That you could type up right.",
"But it didn't sing.",
"So I said good night.")

tabby_cat = "\tI'm tabbed in."

persian_cat = "I'm split\non a line."

backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass"""

print tabby_cat

print persian_cat

print backslash_cat

print fat_cat

print "How old are you?",

# age = raw_input()

print "How tall are you?",

# height = raw_input()

print "How much do you weigh?",

# weight = raw_input()

# print "So,you're %r old, %r tall and %r heavy." %(age,height,weight)

# age = raw_input("How old are you?")

# height = raw_input("How tall are you?")

# weight = raw_input("How much do you weigh?")

# print "So, you're %r old, %r tall and %r heavy." %(age,height,weight)

from sys import argv 

script,first,second,third = argv

print "\nThe script is called:",script

print "Your first variable is:",first

print "Your second variable is:",second

print "Your third variable is:",third

