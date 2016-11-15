import re
test = "Monday, NovembMaNer 14, 2016 | 9:00 am - 12:30 pm"
print "|" in test
test = re.sub("M[\w\W]*?N","",test)
print test