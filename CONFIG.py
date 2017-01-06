#input xpath
evtname = '//header/h1'
evtdesc = '//div[@class="info col-md-9 col-sm-8 col-xs-12"]'
starttime = '' #only contain starttime
startdate = '' #only fill it with enddate
endtime = '' #only contain endtime
enddate = '' #only fill it with startdate
date = '' #only contain date without time
time = '' #contain the starttime and entime without date
tags = '//dl[@class="tabular"]/dd[0]'
dateAndTime = '//footer[@class="row"]/time' #contain the starttime and endtime with date
location = '//footer[@class="row"]/p'

#all the picurl should be included in the src tag
picurl = '//div[@class="photo-container col-md-3 col-sm-4 col-xs-12 text-center"]/a/img'
#input the list of community
community = ["american", "agnes"]

#input url #format: "http(s)://xx.xxx.edu(com/net)/xxx/xxx/xxx" The domain name should be the same
mainUrlList = [
				"http://www.american.edu/cas/auarts/index.cfm",
				]
				
#input a list of regular expression #format: "http(s)://xx.xxx.edu(com/net)/xxx""
urlREList = [
				'http://www.american.edu/cas/calendar/\?id=\d{7}',
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