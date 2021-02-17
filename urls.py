import requests
import datetime
from bs4 import BeautifulSoup

year = datetime.date.today().year

def get_yesterdays_date():
    month = datetime.date.today().month
    day = datetime.date.today().day - 1

    output_string  = str(year)
    if month < 10:
        output_string += '0' + str(month)
    else:
        output_string += str(month)
    if day < 10:
        output_string += '0' + str(day) + '0'
    else:
        output_string += str(day) + '0'
    return output_string

def get_game_schedule():
    url = f'https://www.basketball-reference.com/teams/POR/{year}_games.html'
    html = requests.get(url)
    soup = BeautifulSoup(html.content, 'html.parser')
    schedule_table = soup.find(id='games')
    rows = schedule_table.find_all('td', class_='center')
    stripped_links = []
    for row in rows:
        try:
            link = row.find('a')['href']
            stripped_link = link.strip('/boxscores/').strip('.html')
            stripped_links.append(stripped_link)
        except Exception as e:
            pass
    return stripped_links

def get_game_dates(schedule):
    game_dates = []
    for game in schedule:
        game_dates.append(game[:9])
    return game_dates

def get_box_score_url():
    date = get_yesterdays_date()
    schedule = get_game_schedule()
    game_dates = get_game_dates(schedule)
    
    if date in game_dates:
        index = game_dates.index(date)
        game = schedule[index]
        return f'https://www.basketball-reference.com/boxscores/{game}.html'
        
print(get_box_score_url())
