#input xpath
evtname = '//h1[@class="headliners summary"]'
evtdesc = '//h2[@class="age-restriction over-18"] | //h2[@class="age-restriction all-ages"]'
starttime = '' #only contain starttime
endtime = '' #only contain endtime
date = '//h2[@class="dates"]' #only contain date without time
time = '//h2[@class="times"]/span' #contain the starttime and entime without date
tags = ''
dateAndTime = '' #contain the starttime and endtime with date
location = '//h2[@class="venue location"]'
#all the picurl should be included in the src tag
picurl = '//*[@id="page-content"]/div[2]/img'
#input the list of community
community = ["gwu", "american", "georgetown", "agnes"]

#input url #format: "http(s)://xx.xxx.edu(com/net)/xxx/xxx/xxx" The domain name should be the same
mainUrlList = [
				"http://www.blackcatdc.com/schedule.html",
				]
				
#input a list of regular expression #format: "http(s)://xx.xxx.edu(com/net)/xxx""
urlREList = [
				'/event/\d*-[\w|-]*/',
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