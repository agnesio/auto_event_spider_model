#input xpath
evtname = '//h1[@itemprop="name"]/span'
evtdesc = '//div[@class="section-block description"]/p[@itemprop="description"]'
starttime = '' #only contain starttime
startdate = '' #only fill it with enddate
endtime = '' #only contain endtime
enddate = '' #only fill it with startdate
date = '//div[@itemprop="startDate"]/text()' #only contain date without time
time = '//div[@itemprop="startDate"]/p' #contain the starttime and entime without date
tags = '//div[@class="section-block description"]/p[2]/a'
dateAndTime = '' #contain the starttime and endtime with date
location = '//p[@itemprop="address"]'

#all the picurl should be included in the src tag
picurl = '//div[@class="image-viewer"]/ul/li/a/img'
#input the list of community
community = ["gwu", "american", "georgetown", "howard", "agnes"]

#input url #format: "http(s)://xx.xxx.edu(com/net)/xxx/xxx/xxx" The domain name should be the same
mainUrlList = [
				"http://washingtondc.eventful.com/events/categories?page_number=1",
				]
				
#input a list of regular expression #format: "http(s)://xx.xxx.edu(com/net)/xxx""
urlREList = [
				'http://washingtondc.eventful.com/events/[\w|\-]*?/E\d-\d{3}-\d{9}-\d',
				'http://washingtondc.eventful.com/events/categories?page_number=\d*',
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