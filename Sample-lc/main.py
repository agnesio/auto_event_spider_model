# -*- coding: utf-8 -*-
#######################
###  Picurl Add On  ###
#######################
import CONFIG as Config
import urllib2
import re
import gzip
import zlib
import StringIO
import requests

from lxml import etree
import lxml
import dateutil.parser as dparser
import datetime
import sys
import time
import HTMLParser
import unidecode
from titlecase import titlecase

from bs4 import BeautifulSoup
import linecache

import parsedatetime as pdf
import pytz
from pytz import timezone

import os
sys.path.append(os.path.abspath('../Scripts'))
import dbConnection
from feedData import insertEventData, insertFilter
from getGeoInfo import getGeoInfo

reload(sys)
sys.setdefaultencoding('utf-8') 

#####################
#database setting
conn = dbConnection.conn
LC = conn.Law_Conferences
itemFilter = conn.itemFilter
eventslowercase = LC.eventslowercase
#events = Agnes.events_auto
#urlFilter = itemFilter.urlFilter_auto
#events = Agnes.events
#urlFilter = itemFilter.urlFilter
events = LC.events
urlFilter = itemFilter.urlFilter
communities = LC.communities
evtSource_Community = LC.evtSource_Community
######################

visitList = []
visitedList = []
crawledItem = 0

stopSign = False

#preset parameter
evtnamePattern = ""
evtdescPattern = ""
starttimePattern = ""
startdatePattern = ""
endtimePattern = ""
enddatePattern = ""
timePattern = ""
datePattern = ""
dateAndTimePattern = ""
locationPattern = ""
tagsPattern = []
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
additionalTags = []
specificLocation = ""
unqualifiedStarttimeCount = 0
unqualifiedEndtimeCount = 0
unqualifiedFlag = 3

cityCoordinateDict = {}
localityDict = {}
evtsourceCommunityDict = {}
evtsourceYearDict = {}

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
	global startdatePattern
	global endtimePattern
	global enddatePattern
	global timePattern
	global dateAndTimePattern
	global locationPattern
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
	global specificLocation
	global timezoneName

	global cityCoordinateDict
	global localityDict
	global evtsourceCommunityDict
	global evtsourceYearDict

	evtnamePattern = Config.evtname
	evtdescPattern = Config.evtdesc
	starttimePattern = Config.starttime
	startdatePattern = Config.startdate
	endtimePattern = Config.endtime
	enddatePattern = Config.enddate
	timePattern = Config.time
	dateAndTimePattern = Config.dateAndTime
	locationPattern = Config.location
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
	specificLocation = Config.specificLocation
	timezoneName = Config.timezoneName

	if evtsource == "":
		evtsource = re.sub(r'https?:(//)?(www\.)?', '', mainUrlList[0])
		evtsource = re.sub(r'(?<=com|net|edu|org)/[\w\W]*', '', evtsource)

	if domain == "":
		domain = re.sub(r'(?<=com|net|edu|org)/[\w\W]*', '', mainUrlList[0])

	for eventCommunity in communities.find():
		coordinate = eventCommunity["coordinate"]
		locality = eventCommunity["locality"]
		cityCoordinateDict[eventCommunity["community"]] = coordinate
		if locality not in cityCoordinateDict.keys():
			cityCoordinateDict[locality] = coordinate
		localityDict[eventCommunity["community"]] = locality

	for evtsourceCommunity in evtSource_Community.find():
		evtsourceCommunityDict[evtsourceCommunity["evtsource"]] = evtsourceCommunity["community"]
		evtsourceYearDict[evtsourceCommunity["evtsource"]] = evtsourceCommunity["year"]

def visit_page():
	global visitList
	global visitedList
	global crawledItem

	while len(visitList) != 0:
		requrl = visitList[0]
		print requrl
		# try:
		#custom header
		"""
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
		"""
		
		"""
		encoding = res_data.info().get('Content-Encoding')
		
		#handle compressed file
		if encoding in ('gzip','x-zip','deflate'):
			res = decode(res_data, encoding)
		else:
			res = res_data.read()
		
		"""
		res_data = requests.get(requrl, verify=False)
		res = res_data.text
		

		analyze_page(res, requrl)

		print requrl

		# except Exception as e:
		# 	print "#######################################"
		# 	print "Exception handling: " + str(e)
		# 	print requrl
		# 	printException()
		# 	print "#######################################"

		visitList.remove(requrl)
		visitedList.append(requrl)
		#print visitedList
		#raw_input("visitList")
		
		#sys.stdout.write('visited quantity: '+ str(len(visitedList))+ "\r")
		#sys.stdout.flush()

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
	HTML = re.sub(r'<!--[\w\W]*?-->', '', HTML)
	HTML = HTMLParser.HTMLParser().unescape(HTML)
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

	# print urlList
	# raw_input("urlList")

	if urlPrefixList != []:
		isUrlPrefix = True

	for url in urlList:
		if not checkUselessUrl(url):
			if "http" not in url:
				if url[0] != "/":
					url = domain + "/" + url
				else:
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

	# print visitList
	# raw_input('123')

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
	global startdatePattern
	global endtimePattern
	global enddatePattern
	global timePattern
	global locationPattern
	global dateAndTimePattern
	global evtsource
	global datePattern
	global picurlPattern
	global tagsPattern
	global additionalTags
	global specificLocation
	global evtsourceCommunityDict
	global evtsourceYearDict

	currentTime =  datetime.datetime.now()
	currentDate = currentTime.strftime('%Y-%m-%d')
	currentDate = datetime.datetime.strptime(currentDate, '%Y-%m-%d')
	formerDate = currentDate + datetime.timedelta(days=-1)

	parser = etree.XMLParser(recover = True)
	tree = etree.fromstring(HTML, parser)

	evtname = ""
	evtdesc = ""
	starttime = ""
	startdate = ""
	endtime = ""
	enddate = ""
	time = ""
	dateAndTime = ""
	location = ""
	date = ""
	picurl = ""
	tags = []

	# raw_input(requrl)
	# print HTML
	# raw_input(123)

	evtname = tree.xpath(evtnamePattern)
	evtname = get_text(evtname)

	evtdesc = tree.xpath(evtdescPattern)
	evtdesc = get_text(evtdesc)

	if locationPattern != "":
		location = tree.xpath(locationPattern)
		location = get_text(location)

	if specificLocation != "":
		location = specificLocation

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
		if picurl != "" and picurl[0] == "/" and picurl[1] != "/":
			picurl = evtsource + picurl
		elif picurl != "" and picurl[0] == "/" and picurl[1] == "/":
			picurl = picurl[2:]
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
	if startdatePattern != "":
		startdate = tree.xpath(startdatePattern)
		startdate = get_text(startdate)
	if enddatePattern != "":
		enddate = tree.xpath(enddatePattern)
		enddate = get_text(enddate)

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
	
	starttime, endtime = analyze_time(dateAndTime, date, time, starttime, endtime, startdate, enddate)

	if starttime == "":
		print "Can't crawl time information: ",
		print requrl
		return 0

	community = evtsourceCommunityDict[evtsource]
	year = evtsourceYearDict[evtsource]
	fetch_data(url, evtname, evtdesc, starttime, endtime, location, community, evtsource, formerDate, tags, additionalTags, picurl, year)

def get_picurl(lxmlItems):
	picurl = ""
	for lxmlItem in lxmlItems:
		if lxmlItem.get("src") != None:
			picurl += lxmlItem.get("src")
	picurl = re.sub(r"^\W*?(?=[/|\w])", "", picurl)
	################################################
	#######  ADD ON Part: Need to be tested ########
	if picurl == "":
		picText = ""
		for lxmlItem in lxmlItems:
			picText = picText + " " + etree.tostring(lxmlItem)

		urlPicStr = "url\([\w\W]*?\)"
		urlPicPattern = re.compile(urlPicStr)
		picurlList = urlPicPattern.findall(picText)
		if len(picurlList) > 0:
			picurl = picurlList[0]
		if picurl != "":
			picurl = re.sub(r'url\(', '', picurl)
			picurl = re.sub(r'\)', '', picurl)
			picurl = picurl.strip()

	#################################################
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
	tags = tags.strip()
	tagsSplitCharList = [",", "|", ";", "\\", "/", ".", "\r\n"]
	tagsSplitChar = ""
	for tagsSplitCharItem in tagsSplitCharList:
		if tagsSplitCharItem in tags:
			tagsSplitChar = tagsSplitCharItem
			break
	if tagsSplitChar != "":
		tagsList = tags.split(tagsSplitChar)
	else:
		tagsList = [tags]
	returnedTagsList = []
	for tag in tagsList:
		tag = tag.strip()
		if tag != "":
			returnedTagsList.append(tag)
	return returnedTagsList

def analyze_text(text):
	text = re.sub(r'<br>', ' ', text)
	text = re.sub(r'<[\w\W]*?>', '', text)
	text = re.sub(r'\s{2,}', ' ', text)
	text = text.strip()
	return text

#precoss some time format
def format_time(timeString):
	timeString = timeString.lower()
	uselessCharList = [
		"|", "@", ",", "from", 
		" est", " cst", " mst", " pst", " akst", " hast", " edt", " cdt", " mdt", " pdt", " akdt", " hadt", " et", " ct", " mt", " pt",
		"monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday",
		"mon ", "tue ", "tues ", "wed ", "thu ", "thur ", "thurs ", "fri ", "sat ", "sun ", "·"
		]

	if "time:" or "time" in timeString:
		timeString = re.sub(r'time:?', '', timeString)
	if "date:" or "date" in timeString:
		timeString = re.sub(r'date:?', '', timeString)

	for uselessChar in uselessCharList:
		#build regex format
		if len(uselessChar) == 1:
			uselessChar = "\\" + uselessChar
		timeString = re.sub(uselessChar, '', timeString, flags = re.I)

	timeString = re.sub(r'\([\w\W]*?\)', '', timeString)
	timeString = re.sub(r'noon', '12:00 pm', timeString)
	timeString = re.sub(r'midnight', '12:00 am', timeString)

	timeString = re.sub(r'\s{2,}', ' ', timeString)
	timeString = timeString.strip()
	return timeString

def analyze_time(dateAndTime, date, time, starttime, endtime, startdate, enddate):
	returnedStarttime = ""
	returnedEndtime = ""

	splitCharList = [" to ", "until", "-", u"–", "—"]
	splitCharacter = ""

	dateAndTime = format_time(dateAndTime)
	date = format_time(date)
	time = format_time(time)
	starttime = format_time(starttime)
	endtime = format_time(endtime)
	startdate = format_time(startdate)
	enddate = format_time(enddate)

	try:
		if startdate != "" and enddate != "" and starttime != "" and endtime != "":
			starttime = starttime.encode("ascii","ignore")
			endtime = endtime.encode("ascii","ignore")
			
			returnedStarttime = parsetime(startdate + " " + starttime)
			returnedEndtime = parsetime(enddate + " " + endtime)
		else:
			if dateAndTime != "":
				for splitChar in splitCharList:
					if splitChar in dateAndTime:
						splitCharacter = splitChar
						break

				if splitCharacter != "":
					rawStarttime = dateAndTime.split(splitCharacter)[0]
					rawEndtime = dateAndTime.split(splitCharacter)[1]

					rawStarttime = rawStarttime.encode("ascii","ignore")
					rawEndtime = rawEndtime.encode("ascii","ignore")

					isStarttimeDateExist = isDateExist(rawStarttime)
					isEndtimeDateExist = isDateExist(rawEndtime)

					if isEndtimeDateExist == False:
						returnedStarttime = parsetime(rawStarttime)
						if isDateExistInEndDay(rawEndtime):
							returnedEndtime = parsetime(rawEndtime)
						else:
							returnedEndtime = parsetime(returnedStarttime.strftime('%Y-%m-%d') + " " + rawEndtime)
					elif isStarttimeDateExist == True:
						returnedStarttime = parsetime(rawStarttime)
						returnedEndtime = parsetime(rawEndtime)
					elif isStarttimeDateExist == False:
						returnedEndtime = parsetime(rawEndtime)
						returnedStarttime = parsetime(returnedEndtime.strftime('%Y-%m-%d') + " " + rawStarttime)
					else:
						print "ERROR"
						raise NameError("returnTimeError")

					"""
					returnedStarttime = parsetime(dateAndTime.split(splitCharacter)[0])
					if isDateExist(dateAndTime.split(splitCharacter)[1]):
						returnedEndtime = parsetime(dateAndTime.split(splitCharacter)[1])
					else:
						returnedEndtime = parsetime(returnedStarttime.strftime('%Y-%m-%d') + " " + dateAndTime.split(splitCharacter)[1])
					"""
				elif endtime != "":
					dateAndTime = dateAndTime.encode("ascii","ignore")
					endtime = endtime.encode("ascii","ignore")
					returnedStarttime = parsetime(dateAndTime)
					returnedEndtime = parsetime(returnedStarttime.strftime('%Y-%m-%d') + " " + endtime)
				else:
					dateAndTime = dateAndTime.encode("ascii","ignore")
					returnedStarttime = parsetime(dateAndTime)
					returnedEndtime = returnedStarttime + datetime.timedelta(hours=1)

			else:
				if date != "":
					if time != "":
						for splitChar in splitCharList:
							if splitChar in time:
								splitCharacter = splitChar
								break
						if splitCharacter != "":

							rawStarttime = time.split(splitCharacter)[0]
							rawEndtime = time.split(splitCharacter)[1]

							rawStarttime = rawStarttime.encode("ascii","ignore")
							rawEndtime = rawEndtime.encode("ascii","ignore")

							returnedStarttime = parsetime(date + " " + rawStarttime)
							returnedEndtime = parsetime(date + " " + rawEndtime)

						else:
							date = date.encode("ascii","ignore")
							time = time.encode("ascii","ignore")

							returnedStarttime = parsetime(date + " " + time)
							returnedEndtime = returnedStarttime + datetime.timedelta(hours=1)
					else:
						date = date.encode("ascii","ignore")
						starttime = starttime.encode("ascii","ignore")
						endtime = endtime.encode("ascii","ignore")

						if starttime != "" and endtime != "":
							returnedStarttime = parsetime(date + " " + starttime)
							returnedEndtime = parsetime(date + " " + endtime)
						else:
							returnedStarttime = parsetime(date + " " + "00:01:00")
							returnedEndtime = returnedStarttime
				else:
					starttime = starttime.encode("ascii","ignore")
					endtime = endtime.encode("ascii","ignore")

					if starttime != "" and endtime != "":
						returnedStarttime = parsetime(starttime)
						returnedEndtime = parsetime(endtime)
					else:
						returnedStarttime = ""
						returnedEndtime = ""
	except Exception as e:
		print e
		print "Something wrong in parsing time"
		printException()

	return returnedStarttime, returnedEndtime

# use two ways to parse time string: dparser and parsedatetime
def parsetime(timeString):
	try:
		returnTime = dparser.parse(timeString)
	except Exception as e:
		print e
		print "parser doesn't work, using parsedatetime instead"
		cal = pdf.Calendar()
		returnTime, code = cal.parseDT(timeString)
		if code == 0:
			raise AttributeError("time parameter error")
	return returnTime

def isDateExist(time):
	cal = pdf.Calendar()
	time, code = cal.parseDT(time)
	if code == 2:
		return False
	elif code == 0:
		return False
	return True

def isDateExistInEndDay(time):
	try:
		currentTime = datetime.datetime.now()
		time = dparser.parse(time)
		timeDate = time.strftime('%Y-%m-%d')
		currentTimeDate = currentTime.strftime('%Y-%m-%d')
		return timeDate != currentTimeDate
	except Exception as e:
		print e
		return False

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

	location = re.sub(r'\s+', ' ', location)
	location = location.encode("ascii","ignore")
	return location


def fetch_data(url, evtname, evtdesc, starttime, endtime, location, community, evtsource, formerDate, tags, additionalTags, picurl, year):

	if not check_url(url):
		evtname = modify_evtname(evtname)
		evtdesc = modify_evtdesc(evtdesc)
		location = modify_location(location)
		evtname = titlecase(evtname)

		feed_item(url, evtname, evtdesc, starttime, endtime, location, community, evtsource, formerDate, tags, additionalTags, picurl, year)
	else:
		print "Exist: ",
		print url

def check_url(url):
	isExist = False
	ele = {"url":url}
	for flag in urlFilter.find(ele):
		isExist = True
	return isExist

def getLowercase(field):
	if isinstance(field, str):
		newField = field.lower()
	elif isinstance(field, unicode):
		newField = field.encode('ascii', 'ignore').lower()
	elif isinstance(field, list):
		newField = []
		for item in field:
			item = getLowercase(item)
			newField.append(item)
	elif isinstance(field, dict):
		newField = {}
		for key, value in field.iteritems():
			newField[key.lower()] = getLowercase(value)
	else:
		newField = field
	return newField

def feed_item(url, evtname, evtdesc, starttime, endtime, location, community, evtsource, formerDate, tags, additionalTags, picurl, year):

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

	item["attended"] = []
	item["attendedCount"] = 0

	item["admin"] = []
	item["keywords"] = []
	item["community"] = community
	item["other"] = {"tags":tags, "year":year}
	item["just_crawled"] = True
	item["evtsource"] = evtsource
	item["isAvailable"] = True
	# item["other"]["tags"].extend(additionalTags)
	# item["other"]["currentDistance"] = ""
	

	# item["freqmatchedcr"] = 0
	# item["freqmatchedcb"] = 0
	# item["freqmatched"] = 0

	# item["evtnamelowercase"] = getLowercase(item["evtname"])
	# item["evtdesclowercase"] = getLowercase(item["evtdesc"])
	# item["keywordslowercase"] = getLowercase(item["keywords"])
	# item["otherlowercase"] = getLowercase(item["other"])
	
	# #using geo instead of latitude and longitude
	# #item["latitude"] = latitude
	# #item["longitude"] = longitude

	# #geo="70,-30"
	# if latitude != "" and longitude != "":
	# 	item["geo"] = str(latitude) + "," + str(longitude)
	# else:
	# 	item["geo"] = ""

	# item["maxdistance"] = maxdistance
	# print item
	# print item["location"]
	# raw_input("item")
	timeFilter(item)


def timeFilter(item):
	global crawledItem
	global stopSign
	global unqualifiedStarttimeCount
	global unqualifiedEndtimeCount
	global unqualifiedFlag
	global timezoneName

	global cityCoordinateDict
	global localityDict

	currentTime = datetime.datetime.now()

	# add timezone information to current time
	endTime = currentTime + datetime.timedelta(weeks=8)

	if item["starttime"] > endTime:
		#if there are 10 continuous events that starttime is later than our period, we will stop running our spider
		if unqualifiedFlag != 1:
			unqualifiedStarttimeCount = 0
			unqualifiedFlag = 1
		else:
			unqualifiedStarttimeCount += 1
		if unqualifiedStarttimeCount == 10:
			print "Ten continuous events that starttime is later than our period endtime, stop running spider"
			stopSign = True

		print "Drop Item: starttime is not qualified"
		return 0
	elif item["endtime"] < currentTime:
		#if there are 40 continuous events that endtime is earlier than current time, we will stop running our spider
		if unqualifiedFlag != 2:
			unqualifiedEndtimeCount = 0
			unqualifiedFlag = 2
		else:
			unqualifiedEndtimeCount += 1
		if unqualifiedEndtimeCount == 40:
			print "Forty continuous events that endtime is earlier than our period endtime, stop running spider"
			stopSign = True

		print "Drop Item: endtime is not qualified"
		feed_url(item["url"])
		return 0
	else:
		unqualifiedFlag = 3

		if selfDefFilter(item):
			print "Insert!"
			crawledItem += 1
			if insertEventData(events, item, cityCoordinateDict, localityDict, timezoneName):
				feed_url(item["url"])
		else:
			print "Filtered by selfDefFilter!! Event doesn't insert into MongoDB"
			feed_url(item["url"])
		#raw_input(item["url"])

def feed_url(url):
	insert_url(url)
	pass

def insert_url(url):
	ele = {"url":url}
	insertFilter(urlFilter, ele)

def printException():
	exc_type, exc_obj, tb = sys.exc_info()
	f = tb.tb_frame
	lineno = tb.tb_lineno
	filename = f.f_code.co_filename
	linecache.checkcache(filename)
	line = linecache.getline(filename, lineno, f.f_globals)
	print 'EXCEPTION IN ({}, LINE {} "{}"): {}'.format(filename, lineno, line.strip(), exc_obj)

def selfDefFilter(item):
	return True

if __name__ == '__main__':
	main()


	