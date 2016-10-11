#input xpath
evtname = '//h3'
evtdesc = '//*[@id="contentWrapper"]/div[2]/div/div/div[1]/div/div/table/tr[2]/td[2]/p[3]'
starttime = '' #only contain starttime
endtime = '' #only contain endtime
date = '' #only contain date without time
time = '' #contain the starttime and entime without date
dateAndTime = '//*[@id="contentWrapper"]/div[2]/div/div/div[1]/div/div/table/tr[2]/td[2]/p[1]' #contain the starttime and endtime with date
#location = '//table[@cellpadding="5"]/tr[2]/td[2]/p[2]'
location = '//*[@id="contentWrapper"]/div[2]/div/div/div[1]/div/div/table/tr[2]/td[2]/p[2]/text()[position()<3]'
#all the picurl should be included in the src tag
picurl = ""
#input the list of community
community = ["princeton", "agnes"]

#input url #format: "http(s)://xx.xxx.edu(com/net)/xxx/xxx/xxx" The domain name should be the same
mainUrlList = [
				"http://princetonentertain.com/polCalendar.cfm?Calendar_Code=Entert",
				]
#http://events.brown.edu/events/cal/CAL-00147cc4-567dc7a6-0156-7f7dfdcb-00007278events@brown.edu/20160922T160000Z
#input a list of regular expression #format: "http(s)://xx.xxx.edu(com/net)/xxx""
urlREList = [
				'http://princetonentertain.com/events/\d+?-\d+?-\d+?/[\w|-]+',
			]

#remove url partial pattern
subUrlList = []

#element modify list
evtnameModifiedList = []
evtdescModifiedList = []
locationModifiedList = ['^\W*', '[\w\W] \d{3}[-|\s]*\d{3}[-|\s]\d{4}[\w\W]*?$']

#input a list of half regualr experssion
urlPrefixList = []

#input addtional tags for the crawlers
tags = []

#input domain, can ignore
domain = ""

#input evtsource, can ignore
source = ""

#Preset parameter
filterElementList = [".jpg", ".css", ".png", ".js", ".ico", ".pdf", ".docx", ".jpeg"]