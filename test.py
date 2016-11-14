import re
test = "Monday, November 14, 2016 | 9:00 am - 12:30 pm"
print "|" in test
test = re.sub(" \| ","",test)
print test