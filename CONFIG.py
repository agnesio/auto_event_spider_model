#input xpath
evtname = '//h1[@class="entry-title"]'
evtdesc = '//div[@class="entry-content"]'
starttime = '' #only contain starttime
endtime = '' #only contain endtime
date = '' #only contain date without time
time = '' #contain the starttime and entime without date
tags = 'a[@rel="category"]'
dateAndTime = '//p[@class="entry-date"]/time' #contain the starttime and endtime with date
location = '//*[@id="content"]/div[2]/div/div/div/div/div[1]/div/div[1]/address'

#all the picurl should be included in the src tag
picurl = ''
#input the list of community
community = ["gwu", "american", "georgetown", "agnes"]

#input url #format: "http(s)://xx.xxx.edu(com/net)/xxx/xxx/xxx" The domain name should be the same
mainUrlList = [
				"http://www.aei.org/events/",
				]
				
#input a list of regular expression #format: "http(s)://xx.xxx.edu(com/net)/xxx""
urlREList = [
				'http://www.aei.org/events/[\w|-]*/',
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