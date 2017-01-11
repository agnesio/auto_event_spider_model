import dateutil.parser as parser
import sys
import time
reload(sys)
sys.setdefaultencoding('utf-8')

import parsedatetime as pdf

# return code: 1.date 2.time 3.datetime
timeText = "hi I am joe"
cal = pdf.Calendar()
time, code = cal.parseDT(timeText)
print time, code
print parser.parse(timeText)
