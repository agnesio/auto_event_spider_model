import datetime
############################################################
#fetch server date info to construct the start url
currentTime = datetime.datetime.now()
#startTime = currentTime + datetime.timedelta(days=-3)
startTime = currentTime
startTimeStr = startTime.strftime('%Y-%m-%d')

endTime = currentTime + datetime.timedelta(weeks=8)
endTimeStr = endTime.strftime('%Y-%m-%d')

startTimeList = startTimeStr.split("-")
endTimeList = endTimeStr.split("-")

startYear = startTimeList[0]
startMonth = startTimeList[1]
startDate = startTimeList[2]

endYear = endTimeList[0]
endMonth = endTimeList[1]
endDate = endTimeList[2]
###############################################################
#input xpath
evtname = '//li[@class="social-title"]/h2'
evtdesc = '//div[@class="event-info-description __sectionmargintophalf"]/p'
starttime = '' #only contain starttime
startdate = '' #only fill it with enddate
endtime = '' #only contain endtime
enddate = '' #only fill it with startdate
date = '' #only contain date without time
time = '' #contain the starttime and/or entime without date
tags = '//p[@style="margin-bottom:0;"]/text()'
#dateAndTime = '//div[@id="mainContent"]/section[@class="section container-eventdetails"][1]//div[@class="event-info"]/div[@class="event-info-h3indent"]' #contain the starttime and endtime with date
dateAndTime = '//*[@id="mainContent"]/section[1]/div/div[1]/div[1]/div[1]/text()[1]'
location = '//div[@class="event-info hidden-xs"]/div[@class="event-info-h3indent"]/text()'

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
community = ["cua", "groupten"]

#input url #format: "http(s)://xx.xxx.edu(com/net)/xxx/xxx/xxx" The domain name should be the same
mainUrlList = [
				'https://nest.cua.edu/events',
				]
				
#input a list of regular expression #format: "http(s)://xx.xxx.edu(com/net)/xxx""
#/events/details/1175638
urlREList = [
				'/events/details/\d*',
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