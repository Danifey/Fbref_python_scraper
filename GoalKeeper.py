# takes in data from page scrape and saves it as object in class player 
class GoalKeeper: 
    def __init__(self, name, league, year, club, matchesPlayed, starts, minutes, goalsAgainst, shotsOnTargetAgainst, saves, cleanSheets): # Constructor. Standard Stats
        # player name
        self.name = name
        # league is a competition
        self.league = league
        self.year = year
        self.club = club
        # total games played 
        self.matchesPlayed = matchesPlayed
        # games played as starting player
        self.starts = starts
        # minutes played
        self.minutes = minutes
        # goals scored against
        self.goalsAgainst = goalsAgainst 
        self.shotsOnTargetAgainst = shotsOnTargetAgainst
        self.saves = saves
        self.cleanSheets = cleanSheets
    # writes player to csv 
    def write(self): #print this Player full details
        print(self.name, ',', self.league, ',', self.year, ',', self.club, ',', self.matchesPlayed, ',', self.starts, ',', self.minutes, ',', self.goalsAgainst, ',', self.shotsOnTargetAgainst, ',', self.saves, ',', self.cleanSheets, ',')
        
