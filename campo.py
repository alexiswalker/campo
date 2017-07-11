import urllib2
from bs4 import BeautifulSoup


url = 'http://www.pkfsrl.com.ar/modules.php?name=News&new_topic=2'

page = urllib2.urlopen(url)
soup = BeautifulSoup(page, 'html.parser')


x = soup.find_all('div', attrs={'class': 'promedio'})
for i in x:
    print (i)