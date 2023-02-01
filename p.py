from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://lol.inven.co.kr/dataninfo/match/playerList.php')
bsObject = BeautifulSoup(html, 'html.parser')

print(bsObject.head.find('meta', {'name':'description'}).get('content'))
