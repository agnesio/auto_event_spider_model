#input xpath
evtname = '//p[@class="show-primary-info-title"]'
evtdesc = '//div[@id="main"]/div[@class="container"]'
starttime = '' #only contain starttime
startdate = '' #only fill it with enddate
endtime = '' #only contain endtime
enddate = '' #only fill it with startdate
date = '//p[@class="show-primary-info-showdate"]' #only contain date without time
time = '//p[@class="show-primary-info-showtime"]' #contain the starttime and/or entime without date
tags = ''
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
picurl = '//p[@class="show-artist-img"]/img'
#input the list of community
community = ["gwu", "american", "georgetown", "howard", "agnes"]

#input url #format: "http(s)://xx.xxx.edu(com/net)/xxx/xxx/xxx" The domain name should be the same
mainUrlList = [
				"http://thehowardtheatre.com/",
				]
				
#input a list of regular expression #format: "http(s)://xx.xxx.edu(com/net)/xxx""
#http://thehowardtheatre.com/show/2017/02/22/rawdc-presents-motif/
urlREList = [
				'http://thehowardtheatre.com/show/\d{4}/\d{2}/\d{2}/[\w|-]*?/',
			]

#remove url partial pattern
subUrlList = []

#element modify list
evtnameModifiedList = []
evtdescModifiedList = []
locationModifiedList = []

#input specific location, can ignore
specificLocation = "620 T Street NW, Washington DC, 20001"

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