#input xpath
evtname = '//*[@id="jcl_component"]/div[2]/div[1]/div/div[1]/div[1]/h2'
evtdesc = '//*[@id="jcl_component"]/div[2]/div[1]/div/div[4]/div/div[1]/p'
starttime = '' #only contain starttime
endtime = '' #only contain endtime
date = '' #only contain date without time
time = '' #contain the starttime and entime without date
tags = '//*[@id="jcl_component"]/div[2]/div[1]/div/div[3]/div[1]/ul/li/span/a/text()'
dateAndTime = '//*[@id="jcl_component"]/div[2]/div[1]/div/div[3]/div[2]/div[1]/text()' #contain the starttime and endtime with date
location = ''
#all the picurl should be included in the src tag
picurl = ""
#input the list of community
community = ["yale", "agnes"]

#input url #format: "http(s)://xx.xxx.edu(com/net)/xxx/xxx/xxx" The domain name should be the same
mainUrlList = [
				"http://www.visitnewhaven.com/index.php/things-to-do/events-calendar",
				]
				
#input a list of regular expression #format: "http(s)://xx.xxx.edu(com/net)/xxx""

urlREList = [
				'/things-to-do/events-calendar/[\w|-]*/[\w|-]*',
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