import re
from urllib.request import urlopen
from bs4 import BeautifulSoup


class ProGamer:
    progamer_list = [1]
    def __init__(self, url, html, bsObject):
        url = 'https://lol.inven.co.kr/dataninfo/match/playerList.php'
        html = urlopen(url)
        bsObject = BeautifulSoup(html, 'html.parser')
        self.progamer_list = bsObject.find_all(href=re.compile('https://lol.inven.co.kr/dataninfo/proteam/progamer'))


