import requests
import pandas as pd
from bs4 import BeautifulSoup

url = 'https://www.basketball-reference.com/boxscores/202102120POR.html'

page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

# locate table containing blazers stats
blazers_table = soup.find(id='box-POR-game-basic')
table_rows = blazers_table.tbody.find_all('tr')
reserves_body = blazers_table.tbody.find('tr', class_='thead')
rows = blazers_table.findAll('tr')[2:]

# starter data extraction
starter_headers = [th.getText() for th in blazers_table.find_all('th', class_='poptip')]

starter_stats = [[td.getText() for td in rows[i].findAll('td')] for i in range(5)]

starter_names = [[td.getText() for td in rows[i].findAll('th')] for i in range(5)]

for i in range(len(starter_names)):
    starter_stats[i].insert(0, starter_names[i][0])

# reserve data extraction
reserve_headers = [th.getText() for th in reserves_body.find_all('th')]

reserve_stats = [[td.getText() for td in rows[i].findAll('td')] for i in range(6, len(rows) - 1)]

reserve_names = [[td.getText() for td in rows[i].findAll('th')] for i in range(6, len(rows) - 1)]

for i in range(len(reserve_names)):
    reserve_stats[i].insert(0, reserve_names[i][0])
    
# overall team stats
team_stats = [[td.getText() for td in rows[-1].findAll('td')]]
team_stats[0].insert(0, "Team Totals")

# pandas dataframe
starter_dataFrame = pd.DataFrame(starter_stats, columns = starter_headers)

reserve_dataFrame = pd.DataFrame(reserve_stats, columns = starter_headers)

print(starter_dataFrame.head(5))
print(reserve_dataFrame.head(9))

# print(starter_headers)
# print(starter_stats)
# print()
# print(reserve_headers)
# print(reserve_stats)
# print(team_stats)
# print()

