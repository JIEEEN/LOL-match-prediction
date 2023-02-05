import re
from urllib.request import urlopen
from bs4 import BeautifulSoup


class ProGamer:
    progamer_list = []
    winrate_list = []

    def __init__(self):
        ProGamer.proList(self)
        ProGamer.winRate(self, "T1 Faker", "LCK2023")
    
    def proList(self):
        # url = 'https://lol.inven.co.kr/dataninfo/match/playerList.php'
        url = 'https://lol.inven.co.kr/dataninfo/match/playerList.php?iskin=lol&category=&category2=&shipcode=&shipgroup=&playerName=&champ=0&targetName=&startDate=2023-01-18&endDate=2023-01-30'
        html = urlopen(url)
        bsObject = BeautifulSoup(html, 'html.parser')
        ProGamer.progamer_list = bsObject.find_all(href=re.compile('https://lol.inven.co.kr/dataninfo/proteam/progamer'))

    def winRate(self, proName, season):
        url = 'https://lol.inven.co.kr/dataninfo/match/playerList.php?iskin=lol&category='+season+'&category2=&shipcode=&shipgroup=&playerName='+proName.split()[0]+'+'+proName.split()[1]+'&champ=0&targetName=&startDate=&endDate='
        html = urlopen(url)
        bsObject = BeautifulSoup(html, 'html.parser')
        ProGamer.winrate_list.append(bsObject.find_all('td')[9]) #승률