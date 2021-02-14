from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd


year = 2021

url = "https://www.basketball-reference.com/leagues/NBA_{}_per_game.html".format(year)

html = urlopen(url)

soup = BeautifulSoup(html, 'lxml')

headers = [th.getText() for th in soup.findAll('tr', limit=2)[0].findAll('th')]

headers = headers[1:]

rows = soup.findAll('tr')[1:]
player_stats = [[td.getText() for td in rows[i].findAll('td')] for i in range(len(rows))]

stats = pd.DataFrame(player_stats, columns = headers)
print(stats.head(515))