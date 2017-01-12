#input xpath
evtname = '//h1[@class="headliners summary"]'
evtdesc = '//div[@class="bio"]/text()'
starttime = '' #only contain starttime
startdate = '' #only fill it with enddate
endtime = '' #only contain endtime
enddate = '' #only fill it with startdate
date = '//h2[@class="dates"]' #only contain date without time
time = '//h2[@class="times"]/span[@class="doors"]' #contain the starttime and/or entime without date
tags = ''
dateAndTime = '' #contain the starttime and endtime with date
location = '//div[@class="venue-info"]/text()'


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
picurl = '//div[@class="entry-content event"]/div/img'
#input the list of community
community = ["gwu", "american", "georgetown", "howard", "agnes", "groupten"]

#input url #format: "http(s)://xx.xxx.edu(com/net)/xxx/xxx/xxx" The domain name should be the same
mainUrlList = [
				'http://www.930.com/concerts/',
				]
				
#input a list of regular expression #format: "http(s)://xx.xxx.edu(com/net)/xxx""
#http://www.930.com/event/1364691-cracker-camper-van-beethoven-washington/
urlREList = [
				'http://www.930.com/event/[\w|\-]+?/',
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