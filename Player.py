# takes in data from page scrape and saves it as object in class player 
#Needs player position
class Player: # Constructor. Standard Stats
    def __init__(self, name, league, year, club, matchesPlayed, starts, minutes , goals, assists, pKGoals, pKAttempts, xG , npxG, xAG ): 
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
        # goals scored 
        self.goals = goals 
        self.assists = assists
        # penalty kick goals
        self.pKGoals = pKGoals
        # penalty kick attempts
        self.pKAttempts = pKAttempts 
        # expected goals
        self.xG = xG
        # non penalty expected goals
        self.npxG = npxG
        # expected assisted goals
        self.xAG = xAG
    # writes player to csv 
    def write(self): #print this Player full details
        print(self.name, ',', self.league, ',', self.year, ',', self.club, ',', self.matchesPlayed, ',', self.starts, ',', self.minutes, ',', self.goals, ',', self.assists, ',', self.pKGoals, ',', self.pKAttempts, ',', self.xG, ',', self.npxG, ',', self.xAG, ',')
        
