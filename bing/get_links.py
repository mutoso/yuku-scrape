import requests
import lxml.html
from sys import argv

try:
	start = int(argv[1])
except IndexError:
	start = 1

output_file = open('bingscrape-raw.txt', 'a')
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
for i in xrange(start, 99999999999, 14):
	r = requests.get('https://www.bing.com/search?q=site%3ayuku.com&go=Submit&qs=n&pq=site%3ayuku.com&sc=0-13&sp=-1&sk=&cvid=6E6C24CE5D6E460A8E81C62D21341D42&first=' + str(i) + '&FORM=PERE', headers=headers)
        page = lxml.html.fromstring(r.content)
	links = [link.get('href') for link in page.xpath('//a')]
	print i, '\t', 'page', (i / 14) +1, '\t', len(links), 'extracted',
        for link in links:
		if link:
			output_file.write(link + '\n')
	print 'SAVED'
