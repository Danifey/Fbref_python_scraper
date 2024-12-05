# imports
from bs4 import BeautifulSoup
import pandas as pd
from fetchWithTimer import Fetcher
import Player
from PlayerList import PlayerList
from ScrapeTest import scrape
import time


def GetLeague(startYear, endYear, leagueName,
              leagueID):  # Each team has a unique ID specific to FBref. This is the number in the html.
    # List declarations. One each for URLs and names
    # instantiations
    playerListInstance = PlayerList()
    teamURLs = []
    teamNames = []

    playerNames = []
    playerSoups = []

    seasons = StringFormat(startYear, endYear)
    formattedName = leagueName.replace(" ", "-")  # Need a function call for information to access arrays
    formattedName += '-Stats'
    fetcherInstance = Fetcher()  # this might be c

    for seasonIndex in seasons:
        compURLBase = f'https://fbref.com/en/comps/{leagueID}/{seasonIndex}/{seasonIndex}-{formattedName}'

        # is saying that (ua) is never defined for below method call
        # Fetcher.getRandomUserAgent()

        # string obect of year relative to leagueName
        compContent = fetcherInstance.fetchUrlContent(compURLBase)
        if isinstance(compContent, str):
            soup = BeautifulSoup(compContent, 'html.parser')
        else:
            # raise ValueError("html_text is not valid")
            print("ERROR with competition fetch")
            continue
        # soup = BeautifulSoup(compContent, 'html.parser')

        # The first "table" header is the one we want to parse to grab team URL additions
        # Table name may change on other leagues, more research required.
        table = soup.find('table', class_='stats_table sortable min_width force_mobilize')

        # Parse within "table" for the <tbody> header
        tableBody = table.find('tbody')

        # tr is indexed in data-row, we need to create and iterate a loop for each team in this table
        tableRows = tableBody.find_all('tr')

        # Loop fills the 2 teams lists. Can then iterate through each team.
        for row in tableRows:
            teamURLs.append('https://fbref.com' + row.td.a['href'])
            teamNames.append(row.td.a.text)

        # Can now iterate through all the teams in current season, of current league.

        for url in teamURLs:

            html_text = fetcherInstance.fetchUrlContent(url)
            if html_text == False:
                print("ERROR with team fetch")
                continue
            else:
                soup = BeautifulSoup(html_text, "html.parser")
                table = soup.find(
                    'table')  # Takes first table on page. If not always first table than will be an issue.
                if table == 'None':
                    print(f'ERROR: table from URL: {url} does not exist.')
                    continue
                else:
                    tableBody = table.find('tbody')
                    tableRows = tableBody.find_all('tr')

                    # This loop iterates through all players from the current; league->year->team tree
                    # it creates two lists, one for player names and another for player URLs

                    for playerRow in tableRows:
                        if playerRow.th is None or playerRow.th.a['href'] is None:
                            print("ERROR no player URL")
                            continue
                        else:
                            newURL = 'https://fbref.com' + playerRow.th.a['href']
                            html_text = fetcherInstance.fetchUrlContent(newURL)
                            if html_text == False:
                                print("ERROR with player fetch")
                                continue
                            else:
                                soup = BeautifulSoup(html_text, 'html.parser')
                            if soup in playerSoups:
                                continue
                            else:
                                # playerSoups.append(soup)
                                playerNames.append(playerRow.th.a.text)
                                scrape(soup, playerListInstance)
                                # playerListInstance.addPlayer(scrape(soup, playerListInstance))
                                # print(soup.prettify())
                                playerListInstance.exportCSV(f'{formattedName}.csv')
                                print("one cycle done")


# Take in start and end year, then format to URL acceptable input
def StringFormat(startYear, endYear):
    formattedName = []
    tempYear = startYear + 1
    # Start year cannot be > than or = to end
    if (startYear >= endYear):
        raise Exception('End year must be greater than start')

    # Create array of formatted years for all years in range
    else:
        while (startYear != endYear):
            startString = (str)(startYear)
            tempString = (str)(tempYear)
            formattedName.append(startString + '-' + tempString)
            startYear += 1
            tempYear += 1
        return formattedName


# example call; must know FBref's league id for that league. Can find in url of league. Also below...
# Premier League = 9
# La Liga = 12
# Ligue 1 = 13
# Fußball-Bundesliga = 20
# Serie A = 11

leagueName = 'FuBball-Bundesliga'
lowYear = 2017
# scrapping partial seasons might be an issue
highYear = 2024
leagueID = 20
GetLeague(lowYear, highYear, leagueName, leagueID)
