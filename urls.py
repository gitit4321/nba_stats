import requests
import datetime
from bs4 import BeautifulSoup

year = datetime.date.today().year

def get_yesterdays_date():
    """Gathers the year. month, and day prior to the moment of execution. Formats data into string that can be inserted into the basketball-reference url"""
    month = datetime.date.today().month
    day = datetime.date.today().day - 2

    output_string  = str(year)
    if month < 10:
        output_string += '0' + str(month)
    else:
        output_string += str(month)
    if day < 10:
        output_string += '0' + str(day)
    else:
        output_string += str(day)
    return output_string

def get_game_schedule():
    """Scrapes a Beautiful Soup obeject for a list of all scheduled games in the given season for a given NBA team. The returned list contains strings that can be inserted into the basketball-reference url."""
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
    """Strips a schedule argument list further to return a list that cotains only the date information. 

    Args:
        schedule (list): list of semi-stripped date string present in a basketball-reference url. (Ex: '202101140POR')

    Returns:
        list: fully stripped date strings in a basketball-reference url. (Ex: '20210114')
    """
    game_dates = []
    for game in schedule:
        game_dates.append(game[:8])
    return game_dates

def get_box_score_url():
    """Returns the complete basketball-reference url referencing the box score of a game taking place the day before execution. If no game took place, returns None."""
    date = get_yesterdays_date()
    schedule = get_game_schedule()
    game_dates = get_game_dates(schedule)
    
    if date in game_dates:
        index = game_dates.index(date)
        game = schedule[index]
        return f'https://www.basketball-reference.com/boxscores/{game}.html'
