# -*- coding: utf-8 -*-
import CONFIG as Config
import urllib2
import re
import gzip
import zlib
import StringIO

from lxml import etree
import lxml
import dateutil.parser as dparser
import datetime
import connection
import sys
import time
import HTMLParser
import unidecode
from titlecase import titlecase

from bs4 import BeautifulSoup

reload(sys)
sys.setdefaultencoding('utf-8') 

#####################
#database setting
conn = connection.conn
Agnes = conn.Agnes
itemFilter = conn.itemFilter
events = Agnes.events_auto
urlFilter = itemFilter.urlFilter_auto
######################

visitList = []
visitedList = []
crawledItem = 0

stopSign = False

#preset parameter
evtnamePattern = ""
evtdescPattern = ""
starttimePattern = ""
endtimePattern = ""
timePattern = ""
datePattern = ""
dateAndTimePattern = ""
locationPattern = ""
tagsPattern = []
community = ""
mainUrlList = ""
urlREList = []
subUrlList = []
domain = ""
evtsource = ""
picurl = ""
evtnameModifiedList = []
evtdescModifiedList = []
locationModifiedList = []
urlPrefixList = []
filterElementList = []
tagPattern = []
additionalTags = []
unqualifiedStarttimeCount = 0
unqualifiedEndtimeCount = 0
unqualifiedFlag = 3

def main():
	load_element()
	visit()

def visit():
	global mainUrlList

	visitList.extend(mainUrlList)
	visit_page()

def load_element():
	global evtnamePattern
	global evtdescPattern
	global starttimePattern
	global endtimePattern
	global timePattern
	global dateAndTimePattern
	global locationPattern
	global community
	global evtsource
	global mainUrlList
	global urlREList
	global domain
	global urlPrefix
	global filterElementList
	global datePattern
	global picurlPattern
	global additionalTags
	global subUrlList
	global evtnameModifiedList
	global evtdescModifiedList
	global locationModifiedList
	global tagsPattern

	evtnamePattern = Config.evtname
	evtdescPattern = Config.evtdesc
	starttimePattern = Config.starttime
	endtimePattern = Config.endtime
	timePattern = Config.time
	dateAndTimePattern = Config.dateAndTime
	locationPattern = Config.location
	community = Config.community
	evtsource = Config.source
	mainUrlList = Config.mainUrlList
	urlREList = Config.urlREList
	subUrlList = Config.subUrlList
	domain = Config.domain
	urlPrefixList = Config.urlPrefixList
	filterElementList = Config.filterElementList
	datePattern = Config.date
	picurlPattern = Config.picurl
	additionalTags = Config.additionalTags
	tagsPattern = Config.tags
	evtnameModifiedList = Config.evtnameModifiedList
	evtdescModifiedList = Config.evtdescModifiedList
	locationModifiedList = Config.locationModifiedList

	if evtsource == "":
		evtsource = re.sub(r'https?:(//)?(www\.)?', '', mainUrlList[0])
		evtsource = re.sub(r'(?<=com|net|edu|org)/[\w\W]*', '', evtsource)

	if domain == "":
		domain = re.sub(r'(?<=com|net|edu|org)/[\w\W]*', '', mainUrlList[0])


def visit_page():
	global visitList
	global visitedList
	global crawledItem

	while len(visitList) != 0:
		requrl = visitList[0]

		#custom header
		customHeaders = {
					'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
					'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
					'Accept-Encoding': 'none',
					'Accept-Language': 'en-US,en;q=0.8',
					'Connection': 'keep-alive',
					'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
					}

		req = urllib2.Request(requrl, headers = customHeaders)
		res_data = urllib2.urlopen(req, timeout = 10)
		encoding = res_data.info().get('Content-Encoding')
		
		if encoding in ('gzip','x-zip','deflate'):
			res = decode(res_data, encoding)
		else:
			res = res_data.read()

		analyze_page(res, requrl)
		"""
		if "/frontpage?field_event_sub_type_tid[7]=7&field_event_sub_type_tid[8]=8&field_event_sub_type_tid[9]=9&field_event_sub_type_tid[11]=11&field_event_sub_type_tid[12]=12&field_event_sub_type_tid[13]=13&field_event_sub_type_tid[14]=14&field_event_sub_type_tid[15]=15&page=1" in requrl:
			print visitList
			raw_input("23")
		"""
		visitList.remove(requrl)
		visitedList.append(requrl)
		#print visitedList
		#raw_input("visitList")
		
		#sys.stdout.write('visited quantity: '+ str(len(visitedList))+ "\r")
		#sys.stdout.flush()
		print requrl
		#print visitedList
		#print visitList
		#raw_input("123")


	time.sleep(0.5)
	print
	print "visited quantity: " + str(len(visitedList))
	print "crawledItem: " + str(crawledItem)
	#print visitList
	#print visitedList

def decode(res_data, encoding):
	res = res_data.read()
	if encoding == "deflate":
		data = StringIO.StringIO(zlib.decompress(res))
	else:
		data = gzip.GzipFile('', 'rb', 9, StringIO.StringIO(res))
	res = data.read()
	return res

def analyze_page(HTML, requrl):
	global stopSign
	#remove script content
	HTML = re.sub(r'<script[\w\W]*?</script>', '', HTML)
	soup = BeautifulSoup(HTML)
	HTML = str(soup.body)
	#print HTML
	#raw_input("HTML")
	if stopSign == False:
		fetch_url(HTML)
	
	fetch_information(HTML, requrl)

def fetch_url(HTML):
	global urlREList
	global domain
	global visitList
	global visitedList
	global urlPrefixList

	pendingUrlList = []

	urlList = []
	isUrlPrefix = False

	#raw_input(domain)
	#print HTML
	#raw_input(123)

	for urlRE in urlREList:
		urlStr = urlRE
		urlStr = "(?<=href=\")" + urlStr + "(?=\")"
		urlREPattern = re.compile(urlStr)
		tempUrlList = urlREPattern.findall(HTML)
		urlList.extend(tempUrlList)

		urlStr = re.sub(domain, '', urlRE)
		urlStr = "(?<=href=\")" + urlStr + "(?=\")"
		urlREPattern = re.compile(urlStr)
		tempUrlList = urlREPattern.findall(HTML)
		urlList.extend(tempUrlList)

	#print urlList
	#raw_input("urlList")

	if urlPrefixList != []:
		isUrlPrefix = True

	for url in urlList:
		if not checkUselessUrl(url):
			if "http" not in url:
				url = domain + url
			if url not in visitedList and url not in visitList:
				if not isUrlPrefix:
					if domain in url:
						url = modifyUrl(url)
						#visitList.append(url)
						pendingUrlList.append(url)
				else:
					for urlPrefix in urlPrefixList:
						if urlPrefix in url:
							url = modifyUrl(url)
							#visitList.append(url)
							pendingUrlList.append(url)

	for url in pendingUrlList:
		if not check_url(url) and url not in visitList and url not in visitedList:
			visitList.append(url)
		else:
			#print "Visited this page before, won't record this url: ",
			#print url
			pass

	#print visitList
	#raw_input('123')

def modifyUrl(url):
	global subUrlList
	url = HTMLParser.HTMLParser().unescape(url)
	for subUrl in subUrlList:
		url = re.sub(subUrl, "", url)
	return url

def checkUselessUrl(url):
	global filterElementList
	isUseless = False
	uselessList = filterElementList
	for useless in uselessList:
		if useless in url.lower():
			isUseless = True
			break
	return isUseless

def fetch_information(HTML, requrl):
	global evtnamePattern
	global evtdescPattern
	global starttimePattern
	global endtimePattern
	global timePattern
	global locationPattern
	global dateAndTimePattern
	global community
	global evtsource
	global datePattern
	global picurlPattern
	global tagsPattern
	global additionalTags

	currentTime =  datetime.datetime.now()
	currentDate = currentTime.strftime('%Y-%m-%d')
	currentDate = datetime.datetime.strptime(currentDate, '%Y-%m-%d')
	formerDate = currentDate + datetime.timedelta(days=-1)

	parser = etree.XMLParser(recover = True)
	tree = etree.fromstring(HTML, parser)

	evtname = ""
	evtdesc = ""
	starttime = ""
	endtime = ""
	time = ""
	dateAndTime = ""
	location = ""
	date = ""
	picurl = ""
	tags = []

	#raw_input(requrl)
	#print HTML
	#raw_input(123)

	evtname = tree.xpath(evtnamePattern)
	evtname = get_text(evtname)

	evtdesc = tree.xpath(evtdescPattern)
	evtdesc = get_text(evtdesc)

	location = tree.xpath(locationPattern)
	location = get_text(location)

	if evtname == "":
		print "evtname unqualified: ",
		print requrl
		return 0
	elif location == "":
		print "location unqualified: ",
		print requrl
		return 0


	if picurlPattern != "":
		picurl = tree.xpath(picurlPattern)
		picurl = get_picurl(picurl)
	else:
		picurl = ""

	if tagsPattern != "":
		tags = tree.xpath(tagsPattern)
		tags = get_text(tags)
		tags = analyze_tags(tags)
	'''
	if datePattern != "":
		date = tree.xpath(datePattern)
		date = get_text(date)

	if timePattern != "":
		time = tree.xpath(timePattern)
		time = get_text(time)
	else:
		starttime = tree.xpath(starttimePattern)
		endtime = tree.xpath(endtimePattern)
		starttime = get_text(starttime)
		endtime = get_text(endtime)
	'''
	if dateAndTimePattern != "":
		dateAndTime = tree.xpath(dateAndTimePattern)
		dateAndTime = get_text(dateAndTime)
	if datePattern != "":
		date = tree.xpath(datePattern)
		date = get_text(date)
	if timePattern != "":
		time = tree.xpath(timePattern)
		time = get_text(time)
	if starttimePattern != "":
		starttime = tree.xpath(starttimePattern)
		starttime = get_text(starttime)
	if endtimePattern != "":
		endtime = tree.xpath(endtimePattern)
		endtime = get_text(endtime)


	url = requrl

	#decode as unicode and analyze text
	evtname = analyze_text(unidecode.unidecode(evtname))
	evtdesc = analyze_text(unidecode.unidecode(evtdesc))

	location = analyze_text(location)
	dateAndTime = analyze_text(dateAndTime)
	date = analyze_text(date)
	time = analyze_text(time)
	starttime = analyze_text(starttime)
	endtime = analyze_text(endtime)

	starttime, endtime = analyze_time(dateAndTime, date, time, starttime, endtime)

	if starttime == "":
		print "Can't crawl time information: ",
		print requrl
		return 0
	fetch_data(url, evtname, evtdesc, starttime, endtime, location, community, evtsource, formerDate, tags, additionalTags, picurl)

def get_picurl(lxmlItems):
	picurl = ""
	for lxmlItem in lxmlItems:
		picurl += lxmlItem.get("src")
	picurl = re.sub(r"^\W*?(?=\w)", "", picurl)

	return picurl

def get_text(lxmlItems):
	text = ""
	for lxmlItem in lxmlItems:
		if isinstance(lxmlItem, unicode) or isinstance(lxmlItem, str):
			text = text + "\n" + lxmlItem
		else:
			for item in lxmlItem.itertext():
				text = text + "\r\n" + item
	return text

def analyze_tags(tags):
	tagsSplitCharList = [",", "|", ";", "\\", "/", "."]
	tagsSplitChar = ""
	for tagsSplitCharItem in tagsSplitCharList:
		if tagsSplitCharItem in tags:
			tagsSplitChar = tagsSplitCharItem
			break
	if tagsSplitChar != "":
		tagsList = tags.split(tagsSplitChar)
	else:
		tagsList = [tags]		
	return tagsList

def analyze_text(text):
	text = re.sub(r'<br>', ' ', text)
	text = re.sub(r'<[\w\W]*?>', '', text)
	text = re.sub(r'\s{2,}', ' ', text)
	text = text.strip()
	return text

#precoss some time format
def format_time(timeString):
	if "time:" or "time" in timeString:
		timeString = re.sub(r'time:?', '', timeString)
	if "date:" or "date" in timeString:
		timeString = re.sub(r'date:?', '', timeString)
	timeString = timeString.strip()
	return timeString

def analyze_time(dateAndTime, date, time, starttime, endtime):
	returnedStarttime = ""
	returnedEndtime = ""
	uselessCharList = ["|"]
	splitCharList = ["-"]
	splitCharacter = ""

	dateAndTime = format_time(dateAndTime)
	date = format_time(date)
	time = format_time(time)
	starttime = format_time(starttime)
	endtime = format_time(endtime)

	try:
		if dateAndTime != "":
			for uselessChar in uselessCharList:
				#build regex format
				uselessChar = "\\" + uselessChar
				dateAndTime = re.sub(uselessChar, '', dateAndTime)

			for splitChar in splitCharList:
				if splitChar in dateAndTime:
					splitCharacter = splitChar
					break

			if splitCharacter != "":
				returnedStarttime = dparser.parse(dateAndTime.split(splitCharacter)[0])
				if isDateExist(dateAndTime.split(splitCharacter)[1]):
					returnedEndtime = dparser.parse(dateAndTime.split(splitCharacter)[1])
				else:
					returnedEndtime = dparser.parse(returnedStarttime.strftime('%Y-%m-%d') + " " + dateAndTime.split(splitCharacter)[1])
			elif endtime != "":
				returnedStarttime = dparser.parse(dateAndTime)
				returnedEndtime = dparser.parse(returnedStarttime.strftime('%Y-%m-%d') + " " + endtime)
			else:
				returnedStarttime = dparser.parse(dateAndTime)
				returnedEndtime = returnedStarttime + datetime.timedelta(hours=1)

		else:
			if date != "":
				if time != "":
					for splitChar in splitCharList:
						if splitChar in time:
							splitCharacter = splitChar
							break

					if splitCharacter != "":
						returnedStarttime = dparser.parse(date + " " + time.split(splitCharacter)[0])
						returnedEndtime = dparser.parse(date + " " + time.split(splitCharacter)[1])
					else:
						returnedStarttime = dparser.parse(date + " " + time)
						returnedEndtime = returnedStarttime + datetime.timedelta(hours=1)
				else:
					if starttime != "" and endtime != "":
						returnedStarttime = dparser.parse(date + " " + starttime)
						returnedEndtime = dparser.parse(date + " " + endtime)
					else:
						returnedStarttime = dparser.parse(date + " " + "00:01:00")
						returnedEndtime = returnedStarttime
			else:
				if starttime != "" and endtime != "":
					returnedStarttime = dparser.parse(starttime)
					returnedEndtime = dparse.parse(endtime)
				else:
					returnedStarttime = ""
					returnedEndtime = ""
	except Exception as e:
		print e
		print "Something wrong in parsing time"

	return returnedStarttime, returnedEndtime

def isDateExist(time):
	currentTime = datetime.datetime.now()
	time = dparser.parse(time)
	timeDate = time.strftime('%Y-%m-%d')
	currentTimeDate = currentTime.strftime('%Y-%m-%d')
	return timeDate != currentTimeDate

def modify_evtname(evtname):
	global evtnameModifiedList

	for evtnameModifiedItem in evtnameModifiedList:
		evtname = re.sub(evtnameModifiedItem, '', evtname)
	return evtname

def modify_evtdesc(evtdesc):
	global evtdescModifiedList

	for evtdescModifiedItem in evtdescModifiedList:
		evtdesc = re.sub(evtdescModifiedItem, '', evtdesc)
	return evtdesc

def modify_location(location):
	global locationModifiedList

	for locationModifiedItem in locationModifiedList:
		location = re.sub(locationModifiedItem, '', location)
	return location


def fetch_data(url, evtname, evtdesc, starttime, endtime, location, community, evtsource, formerDate, tags, additionalTags, picurl):
	if not check_url(url):
		evtname = modify_evtname(evtname)
		evtdesc = modify_evtdesc(evtdesc)
		location = modify_location(location)
		evtname = titlecase(evtname)
		feed_item(url, evtname, evtdesc, starttime, endtime, location, community, evtsource, formerDate, tags, additionalTags, picurl)
	else:
		print "Exist: ",
		print url

def check_url(url):
	isExist = False
	ele = {"url":url}
	for flag in urlFilter.find(ele):
		isExist = True
	return isExist

def feed_item(url, evtname, evtdesc, starttime, endtime, location, community, evtsource, formerDate, tags, additionalTags, picurl):

	item = {}
	item["url"] = HTMLParser.HTMLParser().unescape(url)

	item["grps"] = []
	item["evtname"] = evtname
	item["evtdesc"] = evtdesc
	item["createdate"] = formerDate

	item["starttime"] = starttime
	item["endtime"] = endtime
	item["location"] = location

	item["picurl"] = picurl
	item["weburl"] = []
	item["weburl"].append(url)

	item["status"] = False
	item["evttype"] = "public"
	item["featured"] = False

	item["attendees"] = []
	item["attendcount"] = 0

	item["admin"] = []
	item["keywords"] = []
	item["community"] = community
	if tags == []:
		item["other"] = {"tags":[]}
	else:
		item["other"] = {"tags":tags}
	item["other"]["tags"].extend(additionalTags)
	item["evtsource"] = evtsource
	item["just_crawled"] = True
	item["isAvailable"] = True

	#print item
	#print item["location"]
	#raw_input("item")
	
	
	insert_item(item)

def feed_url(url):
	insert_url(url)
	pass

def insert_url(url):
	ele = {"url":url}
	urlFilter.insert(ele)

def insert_item(item):
	global crawledItem
	global stopSign
	global unqualifiedStarttimeCount
	global unqualifiedEndtimeCount
	global unqualifiedFlag

	currentTime = datetime.datetime.now()
	endTime = currentTime + datetime.timedelta(weeks=8)
	if item["starttime"] > endTime:
		#if there are 5 continuous events that starttime is later than our period, we will stop running our spider
		if unqualifiedFlag != 1:
			unqualifiedStarttimeCount = 0
			unqualifiedFlag = 1
		else:
			unqualifiedStarttimeCount += 1
		if unqualifiedStarttimeCount == 5:
			print "Five continuous events that starttime is later than our period endtime, stop running spider"
			stopSign = True

		print "Drop Item: starttime is not qualified"
		return 0
	elif item["endtime"] < currentTime:
		#if there are 10 continuous events that endtime is earlier than current time, we will stop running our spider
		if unqualifiedFlag != 2:
			unqualifiedEndtimeCount = 0
			unqualifiedFlag = 2
		else:
			unqualifiedEndtimeCount += 1
		if unqualifiedEndtimeCount == 10:
			print "Ten continuous events that endtime is earlier than our period endtime, stop running spider"
			stopSign = True

		print "Drop Item: endtime is not qualified"
		feed_url(item["url"])
		return 0
	else:
		unqualifiedFlag = 3
		print "Insert!"
		crawledItem += 1
		#print item["evtname"]
		#print item
		events.insert(item)
		feed_url(item["url"])
		#raw_input(item["url"])

if __name__ == '__main__':
	main()


	