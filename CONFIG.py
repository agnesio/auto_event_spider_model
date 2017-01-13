#input xpath
evtname = '//h1[@itemprop="headline"]/text()'
evtdesc = '//div[@class="ng-article-lead"]'
starttime = '' #only contain starttime
startdate = '' #only fill it with enddate
endtime = '' #only contain endtime
enddate = '' #only fill it with startdate
date = '//div[@style="display:inline-block;"]/h4/text()' #only contain date without time
time = '//li/div[@class="ng-article-subhead ng-margin-remove"]/text()' #contain the starttime and/or entime without date
tags = '//p[@class="ng-article-kicker"]'
dateAndTime = '' #contain the starttime and endtime with date
location = ''


#timezone information: 'US/Alaska', 'US/Aleutian', 'US/Arizona', 'US/Central', 'US/East-Indiana', 'US/Eastern', 'US/Hawaii', 'US/Indiana-Starke', 'US/Michigan', 'US/Mountain', 'US/Pacific', 'US/Pacific-New', 'US/Samoa'
## "US/Eastern" #EST EDT
## "US/Central" #CST CDT
## "US/Mountain" #MST MDT
## "US/Pacific" #PST PDT
## "US/Alaska" #AKST AKMT
## "US/Hawaii" #HST HST
## "US/Arizona" #No dayling saving time there exception for Navajo Nation
timezoneName = 'US/Eastern'

#all the picurl should be included in the src tag
picurl = ''
#input the list of community
community = ["gwu", "american", "georgetown", "howard", "agnes", "groupten"]

#input url #format: "http(s)://xx.xxx.edu(com/net)/xxx/xxx/xxx" The domain name should be the same
mainUrlList = [
				'http://nationalgeographic.org/dc/events/?q=&occurrences=&per_page=90&category=Talk&category=Film',
				'http://nationalgeographic.org/dc/events/?q=&occurrences=&per_page=90&category=Student+Matinees+',
				'http://nationalgeographic.org/dc/events/?q=&occurrences=&per_page=90&category=Happy+Hour',
				'http://nationalgeographic.org/dc/events/?q=&occurrences=&per_page=90&category=Film',
				]
				
#input a list of regular expression #format: "http(s)://xx.xxx.edu(com/net)/xxx""
#http://nationalgeographic.org/dc/events/beauty-and-bizarre/
urlREList = [
				'http://nationalgeographic.org/dc/events/[\w|\-]*/',
			]

#remove url partial pattern
subUrlList = []

#element modify list
evtnameModifiedList = []
evtdescModifiedList = []
locationModifiedList = []

#input specific location, can ignore
specificLocation = "The National Geographic Museum, 1145 17th Street, NW, Washington, DC 20036"

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