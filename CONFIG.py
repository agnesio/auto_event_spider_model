#input xpath
evtname = '//h2[@class="calendar-interior-title"]/text()'
evtdesc = '//div[@class="calendar-content -prosaic"]/p'
starttime = '' #only contain starttime
startdate = '' #only fill it with enddate
endtime = '' #only contain endtime
enddate = '' #only fill it with startdate
date = '' #only contain date without time
time = '' #contain the starttime and entime without date
tags = ''
dateAndTime = '//span[@class="showtime-cta-date"]' #contain the starttime and endtime with date
location = '//span[@class="showtime-cta-venue"]'

#all the picurl should be included in the src tag
picurl = '//div[@class="calendar-content -prosaic"]/p[2]/img'
#input the list of community
community = ["gwu", "american", "georgetown", "howard", "agnes"]

#input url #format: "http(s)://xx.xxx.edu(com/net)/xxx/xxx/xxx" The domain name should be the same
mainUrlList = [
				"https://www.capitalfringe.org/calendar",
				]
				
#input a list of regular expression #format: "http(s)://xx.xxx.edu(com/net)/xxx""
#https://www.capitalfringe.org/events/1003-amadou-kouyate-solo-kora-performance
urlREList = [
				'https://www.capitalfringe.org/events/[\w|-]*?',
			]

#remove url partial pattern
subUrlList = []

#element modify list
evtnameModifiedList = []
evtdescModifiedList = []
locationModifiedList = []

#input specific location, can ignore
specificLocation = ""

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