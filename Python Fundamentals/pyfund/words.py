#Shebang
#!usr/bin/env python3
import sys
from urllib.request import urlopen
#'http://sixty-north.com/c/t.txt'
def fetch(url):
	"""Some docs: Fetch stuff"""
	with urlopen(url) as story:
	 story_words=[]
	 for line in story:
		 line_words=line.decode('utf-8').split(' ')
		 for word in line_words:
			 story_words.append(word)
	return story_words

def print_items(items):			 
	for item in items:
	  print(item)

def main(ulr):
	url=sys.argv[1]
	print(fetch(url))

if __name__=='__main__':
	main(sys.argv[1])
