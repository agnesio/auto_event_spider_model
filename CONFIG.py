#input xpath
evtname = '//article[@role="article"]/h1'
evtdesc = '//article[@role="article"]/p'
starttime = '' #only contain starttime
endtime = '' #only contain endtime
date = '' #only contain date without time
time = '' #contain the starttime and entime without date
tags = ''
dateAndTime = '//div[@class="byline"]/text()' #contain the starttime and endtime with date
location = '//div[@class="byline"]/a/text()'
#all the picurl should be included in the src tag
picurl = ''
#input the list of community
community = ["gwu", "american", "georgetown", "agnes"]

#input url #format: "http(s)://xx.xxx.edu(com/net)/xxx/xxx/xxx" The domain name should be the same
mainUrlList = [
				"https://www.csis.org/events-upcoming?title=&page=0",
				]
				
#input a list of regular expression #format: "http(s)://xx.xxx.edu(com/net)/xxx""
urlREList = [
				'https://www.csis.org/events-upcoming?title=&page=\d+',
				'https://www.csis.org/events/[\w|-]*',
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