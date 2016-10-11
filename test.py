import dateparser
import dateutil.parser as dparser

print dateparser.parse("10/12 Thursday, October 6, 2016, 3:00 pm")
print dparser.parse("Thursday, October 6, 2016, 3:00 pm")