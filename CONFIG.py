#input xpath
evtname = '//*[@id="body"]/div/table[1]/tr/td[1]/p/span | //*[@id="lo-EventTitle"]'
evtdesc = '//*[@id="body"]/div/table[2]/tr/td[1]/span/p[2] | //*[@id="lo-UserDetailEventDescription"]/p[2]'
starttime = '' #only contain starttime
endtime = '' #only contain endtime
date = '//*[@id="body"]/div/table[2]/tr/td[1]/p/label | //*[@id="calendar-userdetail-date-a15"]' #only contain date without time
time = '//*[@id="body"]/div/table[2]/tr/td[1]/p/text()[2] | //*[@id="lo-start_time"]' #contain the starttime and entime without date
tags = ''
dateAndTime = '' #contain the starttime and endtime with date
location = '//*[@id="footer-top"]/div[1]/p[1]/text()[1] | //*[@id="footer-top"]/div[1]/p[1]/text()[2] | //*[@id="lo-CalendarAddressValue"]'
#all the picurl should be included in the src tag
picurl = '//*[@id="lo-UserDetailEventDescription"]/p[2]/span/img'
#input the list of community
community = ["gwu", "american", "georgetown", "agnes"]

#input url #format: "http(s)://xx.xxx.edu(com/net)/xxx/xxx/xxx" The domain name should be the same
mainUrlList = [
				"http://go.nbm.org/site/Calendar/",
				]
				
#input a list of regular expression #format: "http(s)://xx.xxx.edu(com/net)/xxx""
urlREList = [
				'http://go.nbm.org/site/Calendar/\d+?\?view=Detail&amp;id=\d+',
			]

#remove url partial pattern
subUrlList = []

#element modify list
evtnameModifiedList = []
evtdescModifiedList = []
locationModifiedList = []

#input a list of half regualr experssion
urlPrefixList = []

#input addtional tags for the crawlers
additionalTags = []

#input domain, can ignore
domain = ""

#input evtsource, can ignore
source = ""

#Preset parameter
filterElementList = [".jpg", ".css", ".png", ".js", ".ico", ".pdf", ".docx", ".jpeg"]