####################################################################
####################################################################
####################################################################
#princetonentertain.com CONFIG
#input xpath
evtname = '//h3'
evtdesc = '//*[@id="contentWrapper"]/div[2]/div/div/div[1]/div/div/table/tr[2]/td[2]/p[3]'
starttime = '' #only contain starttime
endtime = '' #only contain endtime
date = '' #only contain date without time
time = '' #contain the starttime and entime without date
dateAndTime = '//*[@id="contentWrapper"]/div[2]/div/div/div[1]/div/div/table/tr[2]/td[2]/p[1]' #contain the starttime and endtime with date
#location = '//table[@cellpadding="5"]/tr[2]/td[2]/p[2]'
location = '//*[@id="contentWrapper"]/div[2]/div/div/div[1]/div/div/table/tr[2]/td[2]/p[2]/text()[position()<3]'
#all the picurl should be included in the src tag
picurl = ""
#input the list of community
community = ["princeton", "agnes"]

#input url #format: "http(s)://xx.xxx.edu(com/net)/xxx/xxx/xxx" The domain name should be the same
mainUrlList = [
				"http://princetonentertain.com/polCalendar.cfm?Calendar_Code=Entert",
				]
#http://events.brown.edu/events/cal/CAL-00147cc4-567dc7a6-0156-7f7dfdcb-00007278events@brown.edu/20160922T160000Z
#input a list of regular expression #format: "http(s)://xx.xxx.edu(com/net)/xxx""
urlREList = [
				'http://princetonentertain.com/events/\d+?-\d+?-\d+?/[\w|-]+',
			]

#remove url partial pattern
subUrlList = []

#element modify list
evtnameModifiedList = []
evtdescModifiedList = []
locationModifiedList = ['^\W*', '[\w\W] \d{3}[-|\s]*\d{3}[-|\s]\d{4}[\w\W]*?$']

#input a list of half regualr experssion
urlPrefixList = []

#input addtional tags for the crawlers
tags = []

#input domain, can ignore
domain = ""

#input evtsource, can ignore
source = ""

#Preset parameter
filterElementList = [".jpg", ".css", ".png", ".js", ".ico", ".pdf", ".docx", ".jpeg"]

####################################################################
####################################################################
####################################################################
#brown.edu CONFIG
#input xpath
evtname = '//*[@id="event-view-details"]/dd[1]/a/strong'
evtdesc = '//*[@id="event-view-details"]/dd[4]'
starttime = '' #only contain starttime
endtime = '' #only contain endtime
date = '' #only contain date without time
time = '' #contain the starttime and entime without date
dateAndTime = '//*[@id="event-view-details"]/dd[2]' #contain the starttime and endtime with date
location = '//*[@id="event-view-details"]/dd[3]/a'

#all the picurl should be included in the src tag
picurl = ""
#input the list of community
community = ["brown", "agnes"]

#input url #format: "http(s)://xx.xxx.edu(com/net)/xxx/xxx/xxx" The domain name should be the same
mainUrlList = [
				"http://events.brown.edu/cal/main/showMain.rdo",
				]
#http://events.brown.edu/events/cal/CAL-00147cc4-567dc7a6-0156-7f7dfdcb-00007278events@brown.edu/20160922T160000Z
#input a list of regular expression #format: "http(s)://xx.xxx.edu(com/net)/xxx""
urlREList = [
				'http://events.brown.edu/events/cal/CAL-[\w|-]+?events@brown\.edu/\d+?T\d+?Z',
			]

#remove url partial pattern
subUrlList = [
				'',
			]

#element modify list
evtnameModifiedList = []
evtdescModifiedList = []
locationModifiedList = []

#input a list of half regualr experssion
urlPrefixList = []

#input addtional tags for the crawlers
tags = []

#input domain, can ignore
domain = ""

#input evtsource, can ignore
source = ""

#Preset parameter
filterElementList = [".jpg", ".css", ".png", ".js", ".ico", ".pdf", ".docx", ".jpeg"]


####################################################################
####################################################################
####################################################################
#princeton.edu CONFIG
#input xpath
evtname = '//*[@id="calendar-entry"]/h2/span[1]'
evtdesc = '//*[@id="calendar-entry"]/p'
starttime = '' #only contain starttime
endtime = '//*[@id="calendar-entry"]/h4[2]/abbr[2]' #only contain endtime
date = '' #only contain date without time
time = '' #contain the starttime and entime without date
dateAndTime = '//*[@id="calendar-entry"]/h4[2]/abbr[1]' #contain the starttime and endtime with date
location = '//*[@id="calendar-entry"]/div[1]/ul/li'

#all the picurl should be included in the src tag
picurl = ""
#input the list of community
community = ["princeton", "agnes"]

#input url #format: "http(s)://xx.xxx.edu(com/net)/xxx/xxx/xxx" The domain name should be the same
mainUrlList = [
				"http://www.princeton.edu/events/?view=upcoming&category=all",
				]

#input a list of regular expression #format: "http(s)://xx.xxx.edu(com/net)/xxx""
urlREList = [
				'http://www.princeton.edu/events/\?view=daily&amp;category=all&amp;from=[\d|-]+&amp;eid=\d+&amp;rid=\d+',
			]

#remove url partial pattern
subUrlList = [
				"&from=[\d|-]*"
			]

#element modify list
evtnameModifiedList = []
evtdescModifiedList = []
locationModifiedList = []

#input a list of half regualr experssion
urlPrefixList = []

#input addtional tags for the crawlers
tags = []

#input domain, can ignore
domain = ""

#input evtsource, can ignore
source = ""

#Preset parameter
filterElementList = [".jpg", ".css", ".png", ".js", ".ico", ".pdf", ".docx", ".jpeg"]


####################################################################
####################################################################
####################################################################
#artgallery.yale.edu CONFIG
#input xpath
evtname = "//div[@property='dc:title']/h1"
evtdesc = "//div[@property='content:encoded']/p"
starttime = "" #only contain starttime
endtime = ""#only contain endtime
date = ""#only contain date without time
time = "//div[@class='group-right']/div[@class='field field-name-field-event-time field-type-datetime field-label-hidden']//span[@property='dc:date']"#contain the starttime and entime without date
dateAndTime = ""#contain the starttime and endtime with date
location = "//div[@class='field field-name-field-speaker-performer field-type-text-long field-label-hidden']/div[@class='field-items']/div[@class='field-item even']"

#all the picurl should be included in the src tag
picurl = "//div[@class='photo-wrapper']/a/img"
#input the list of community
community = ["yale", "agnes"]

#input url #format: "http(s)://xx.xxx.edu(com/net)/xxx/xxx/xxx" The domain name should be the same
mainUrlList = [
				"http://artgallery.yale.edu/calendar-upcoming-events",
				]

#input a list of regular expression #format: "http(s)://xx.xxx.edu(com/net)/xxx""
urlREList = [
				'http://artgallery.yale.edu/calendar/events/[\w|-]*', 
				'http://artgallery.yale.edu/calendar-upcoming-events?page=\d+',
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
tags = []

#input domain, can ignore
domain = ""

#input evtsource, can ignore
source = ""

#Preset parameter
filterElementList = [".jpg", ".css", ".png", ".js", ".ico", ".pdf", ".docx", ".jpeg"]


####################################################################
####################################################################
####################################################################
#lisner.gwu.edu CONFIG
evtname = "//div[@class='header clearfix']/h2"
evtdesc = "//div[@class='article']/div/div/div"
starttime = "" #only contain starttime
endtime = ""#only contain endtime
date = "//div[@class='article clearfix']/p[1]"#only contain date without time
time = "//div[@class='article clearfix']/p[2]"#contain the starttime and entime without date
dateAndTime = ""#contain the starttime and endtime with date
location = "//div[@class='article clearfix']/p[3]"

#all the picurl should be included in the src tag
picurl = "//div[@class='header']/div[@class='image-wrapper']/img"
#input the list of community
community = ["gwu", "agnes"]

#input url #format: "http(s)://xx.xxx.edu(com/net)/xxx/xxx/xxx" The domain name should be the same
mainUrlList = [
				"https://lisner.gwu.edu/upcoming-events?page=0", 
				"https://lisner.gwu.edu/upcoming-events?page=1", 
				"https://lisner.gwu.edu/upcoming-events?page=2",
				]

#input a list of regular expression #format: "http(s)://xx.xxx.edu(com/net)/xxx""
urlREList = [
			"https://lisner.gwu.edu/[A-Z|a-z|0-9|\-|\%]+", 
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
tags = []

#input domain, can ignore
domain = ""

#input evtsource, can ignore
source = ""

#Preset parameter
filterElementList = [".jpg", ".css", ".png", ".js", ".ico", ".pdf", ".docx", ".jpeg"]

####################################################################
####################################################################
####################################################################
#news.dartmouth.edu CONFIG
evtname = "//section[@class='intro']/h2"
evtdesc = "//div[@class='row']/div[@class='eleven column push-one']/section[@class='description']"
starttime = ""
endtime = ""
date = "//section[@class='timelocation']/div[@class='date']"
time = "//section[@class='timelocation']/div[@class='time']"
datetime = ""
location = "//section[@class='timelocation']/div[@class='location']"

#all the picurl should be included in the src tag
picurl = "//div[@class='eleven column push-one']/section[@class='image']/img"
#input the list of community
community = ["dartmouth", "agnes"]

#input url #format: "http(s)://xx.xxx.edu(com/net)/xxx/xxx/xxx" The domain name should be the same
mainUrlList = [
				"https://news.dartmouth.edu/events",
				]

#input a list of regular expression #format: "http(s)://xx.xxx.edu(com/net)/xxx""
urlREList = [
				'https://news.dartmouth.edu/events/event\?event=\d+?\&amp\;listing=\d+?', 
				'https://news.dartmouth.edu/events/\?offset=\d+?[\w\W]*?',
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
tags = []

#input domain, can ignore
domain = ""

#input evtsource, can ignore
source = ""

#Preset parameter
filterElementList = [".jpg", ".css", ".png", ".js", ".ico", ".pdf", ".docx", ".jpeg"]