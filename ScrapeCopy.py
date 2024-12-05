
from bs4 import BeautifulSoup
import requests
from Player import Player


html_text1 = requests.get('https://fbref.com/en/players/cb3a3ff4/Katie-McCabe').text
html_text2 =  requests.get('https://fbref.com/en/players/9c36ed83/Nicolas-Jackson').text
html_text3 =  requests.get('https://fbref.com/en/players/6a713852/Robert-Sanchez').text
html_text4 =  requests.get('https://fbref.com/en/players/e342ad68/Mohamed-Salah').text

playerStats = []

text = [html_text1, html_text2, html_text3, html_text4]

for pages in text:
    soup = BeautifulSoup(text, 'html.parser')
    playerStats = []
    # Navigate to header to grab name and position
    playerName = soup.find('h1')
    playerName = str(playerName)
    start = 'span>'
    end = '<'
    start = playerName.index(start) + len(start)
    end = playerName.index(end, start)
    name = playerName[start:end]

    # Navigate to P tags, pull all and parse for position
    playerPosition = soup.find_all('p')
    playerPosition = str(playerPosition)
    start = '/strong> '
    end = ' '
    start = playerPosition.index(start) + len(start)
    end = playerPosition.index(end, start)
    position = playerPosition[start:end]

    # Find the table containing the stats
    soup2 = soup.find('table', class_='stats_table sortable min_width')
    #soup2 = soup.find('table', id='stats_standard_dom_lg')
    soup3 = soup2.find('tbody')

    # Find rows in the table
    rows = soup3.find_all('tr')

    # Ensure there is more than one row in the table before accessing it
    if len(rows) > 1:
        for row in rows:
            cols = row.find_all('td')
            if len(cols) > 0:  # Ensure we have columns in the row
                cols_text = [col.text.strip() for col in cols]

                # Make sure there are enough columns to extract player stats
                if len(cols_text) > 19:
                    # Extracting league information
                    league = cols_text[3]  
                    club = cols_text[1]
                    matchesPlayed = cols_text[5]
                    starts = cols_text[6]
                    minutes = cols_text[7]
                    goals = cols_text[9]
                    assists = cols_text[10]
                    pKGoals = cols_text[13]
                    pKAttempts = cols_text[13] 
                    xG = cols_text[17]
                    npxG = cols_text[18]
                    xAG = cols_text[19]

                    # Extract season year information
                    yearsLocation = row.find('th')  
                    year = yearsLocation.text.strip()

                    # Create a Player object and add it to the playerStats list
                    #currPlayerList.addPlayer(Player(name, year, league, club, matchesPlayed, starts, minutes, goals, assists, pKGoals, pKAttempts, xG, npxG, xAG))

    else:
        print("Not enough rows in the table.")


    # After looping through all pages, print player stats
    print(f"{'Name (year)':<30} {'League':<20} {'Club':<20} {'Matches Played':<15} {'starts':<5} {'minutes':<5} {'Goals':<5} {'Assists':<5} {'pKGoals':<5} {'pKAttempts':<5} {'xG':<5} {'npxG':<5} {'xAG':<5}")

#for player in playerStats:
    #print(f"{player.name} ({player.year})" + f" {player.league:<20} {player.club:<20} {player.matchesPlayed:<15} {player.starts:<5} {player.minutes:<5} {player.goals:<5} {player.assists:<5} {player.pKGoals:<5} {player.pKAttempts:<5} {player.xG:<5} {player.npxG:<5} {player.xAG:<5}")

