from threading import Timer
import random
import string
import HTMLParser

def hello():
	with open("openword.txt","w") as f:
		f.write("hello, world")

if __name__ == '__main__':
  print HTMLParser.HTMLParser().unescape("a&amp;b")
