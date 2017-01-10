#input xpath
evtname = '//h1[@class="entry-title"]'
evtdesc = '//div[@class="entry-content"]'
starttime = '' #only contain starttime
startdate = '' #only fill it with enddate
endtime = '' #only contain endtime
enddate = '' #only fill it with startdate
date = '' #only contain date without time
time = '' #contain the starttime and entime without date
tags = '//p[@class="entry-categories"]/a |  ul[@class="entry-tags"]'
dateAndTime = '//time' #contain the starttime and endtime with date
location = '//address'

#all the picurl should be included in the src tag
picurl = '//div[@class="entry-featured-image"]/img'
#input the list of community
community = ["gwu", "american", "georgetown", "howard", "agnes"]

#input url #format: "http(s)://xx.xxx.edu(com/net)/xxx/xxx/xxx" The domain name should be the same
mainUrlList = [
				"http://www.aei.org/events/",
				]
				
#input a list of regular expression #format: "http(s)://xx.xxx.edu(com/net)/xxx""
#http://www.aei.org/events/regulatory-relief-for-small-businesses-a-conversation-with-house-small-business-committee-chairman-steve-chabot-r-oh/
urlREList = [
				'http://www.aei.org/events/[\w|-]*?/',
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