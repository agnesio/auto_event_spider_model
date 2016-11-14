####################################################################
####################################################################
####################################################################
#csis.org CONFIG
#input xpath
evtname = '//article[@role="article"]/h1'
evtdesc = '//article[@role="article"]/p'
starttime = '' #only contain starttime
endtime = '' #only contain endtime
date = '' #only contain date without time
time = '' #contain the starttime and entime without date
tags = ''
dateAndTime = '//div[@class="byline"]/text()' #contain the starttime and endtime with date
location = '//div[@class="byline"]/a/text()'
#all the picurl should be included in the src tag
picurl = ''
#input the list of community
community = ["gwu", "american", "georgetown", "agnes"]

#input url #format: "http(s)://xx.xxx.edu(com/net)/xxx/xxx/xxx" The domain name should be the same
mainUrlList = [
				"https://www.csis.org/events-upcoming?title=&page=0",
				]
				
#input a list of regular expression #format: "http(s)://xx.xxx.edu(com/net)/xxx""
urlREList = [
				'https://www.csis.org/events-upcoming?title=&page=\d+',
				'https://www.csis.org/events/[\w|-]*',
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


####################################################################
####################################################################
####################################################################
#capitolgrapevine.com CONFIG
#input xpath
evtname = '//div[@class="sqs-events-collection-item"]/article/div[1]/h1'
evtdesc = '//div[@class="sqs-block-content"]'
starttime = '//time[@class="event-time-12hr-start"]' #only contain starttime
endtime = '//time[@class="event-time-12hr-end"]' #only contain endtime
date = '//time[@class="event-date"]/text()' #only contain date without time
time = '//*[@id="body"]/div/table[2]/tr/td[1]/p/text()[2] | //*[@id="lo-start_time"]' #contain the starttime and entime without date
tags = ''
dateAndTime = '' #contain the starttime and endtime with date
location = '//span[@class="eventitem-meta-address-line eventitem-meta-address-line--title"]/text()'
#all the picurl should be included in the src tag
picurl = ''
#input the list of community
community = ["gwu", "american", "georgetown", "agnes"]

#input url #format: "http(s)://xx.xxx.edu(com/net)/xxx/xxx/xxx" The domain name should be the same
mainUrlList = [
				"http://www.capitolgrapevine.com/",
				]
				
#input a list of regular expression #format: "http(s)://xx.xxx.edu(com/net)/xxx""
urlREList = [
				'http://www.capitolgrapevine.com/calendar/\d*/\d*/\d*/[\w|-]*',
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


####################################################################
####################################################################
####################################################################
#go.nbm.org CONFIG
#input xpath
evtname = '//*[@id="body"]/div/table[1]/tr/td[1]/p/span | //*[@id="lo-EventTitle"]'
evtdesc = '//*[@id="body"]/div/table[2]/tr/td[1]/span/p[2] | //*[@id="lo-UserDetailEventDescription"]/p[2]'
starttime = '' #only contain starttime
endtime = '' #only contain endtime
date = '//*[@id="body"]/div/table[2]/tr/td[1]/p/label | //*[@id="calendar-userdetail-date-a15"]' #only contain date without time
time = '//*[@id="body"]/div/table[2]/tr/td[1]/p/text()[2] | //*[@id="lo-start_time"]' #contain the starttime and entime without date
tags = ''
dateAndTime = '' #contain the starttime and endtime with date
location = '//*[@id="footer-top"]/div[1]/p[1]/text()[1] | //*[@id="footer-top"]/div[1]/p[1]/text()[2] | //*[@id="lo-CalendarAddressValue"]'
#all the picurl should be included in the src tag
picurl = '//*[@id="lo-UserDetailEventDescription"]/p[2]/span/img'
#input the list of community
community = ["gwu", "american", "georgetown", "agnes"]

#input url #format: "http(s)://xx.xxx.edu(com/net)/xxx/xxx/xxx" The domain name should be the same
mainUrlList = [
				"http://go.nbm.org/site/Calendar/",
				]
				
#input a list of regular expression #format: "http(s)://xx.xxx.edu(com/net)/xxx""
urlREList = [
				'http://go.nbm.org/site/Calendar/\d+?\?view=Detail&amp;id=\d+',
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

####################################################################
####################################################################
####################################################################
#ustreetmusichall.com CONFIG
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
				"http://www.ustreetmusichall.com/calendar/",
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

####################################################################
####################################################################
####################################################################
#visitnewhaven.com CONFIG
#input xpath
evtname = '//*[@id="jcl_component"]/div[2]/div[1]/div/div[1]/div[1]/h2'
evtdesc = '//*[@id="jcl_component"]/div[2]/div[1]/div/div[4]/div/div[1]/p'
starttime = '' #only contain starttime
endtime = '' #only contain endtime
date = '' #only contain date without time
time = '//*[@id="page-content"]/div[3]/div[1]/h2[2]/span/text()' #contain the starttime and/or entime without date
tags = '//*[@id="jcl_component"]/div[2]/div[1]/div/div[3]/div[1]/ul/li/span/a/text()'
dateAndTime = '//*[@id="jcl_component"]/div[2]/div[1]/div/div[3]/div[2]/div[1]/text()' #contain the starttime and endtime with date
location = '//*[@id="page-content"]/div[3]/div[1]/h2[3]'
#all the picurl should be included in the src tag
picurl = ""
#input the list of community
community = ["yale", "agnes"]

#input url #format: "http(s)://xx.xxx.edu(com/net)/xxx/xxx/xxx" The domain name should be the same
mainUrlList = [
				"http://www.visitnewhaven.com/index.php/things-to-do/events-calendar",
				]
#http://events.brown.edu/events/cal/CAL-00147cc4-567dc7a6-0156-7f7dfdcb-00007278events@brown.edu/20160922T160000Z
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
tags = ''
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
additionalTags = []

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
tags = ''
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
additionalTags = []

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
tags = ''
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
additionalTags = []

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
tags = ""
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
additionalTags = []

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
tags = ""
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
additionalTags = []

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
tags = ""
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
additionalTags = []

#input domain, can ignore
domain = ""

#input evtsource, can ignore
source = ""

#Preset parameter
filterElementList = [".jpg", ".css", ".png", ".js", ".ico", ".pdf", ".docx", ".jpeg"]