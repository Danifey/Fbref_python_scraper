import Player
import csv
#Needs player position
class PlayerList:
    def __init__(self): #constructor takes play obj as arg
        self.list = []
    
    def addPlayer(self, Player):
        self.list.append(Player)
    def getPlayer(self, index):
        return self.list[index]
    # TODO add method to sort list, or to add new players in in alph then year order
    def sortPlayerList(self):
        return sorted(self.list, key=lambda player: player.name)
        
    def exportCSV(self, filename): #filename must end in '.csv' this funcion will create a csv with all player obj in this playerList obj
        self.list = self.sortPlayerList()
        with open(filename, "wt") as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            writer.writerow(['Name'] + ['League'] + ['Year'] + ['Club'] + ['Matches Played'] + ['Starts'] + ['Minutes'] + ['Goals'] + ['Assists'] + ['Penalty Goals'] + ['Penalty Attempts'] + ['xGoals'] + ['non-penalty xGoals'] + ['xAssists'])
            for index in range(len(self.list)):
                player = self.list[index]
                writer.writerow([player.name] + [player.league] + [player.year] + [player.club] + [player.matchesPlayed] + [player.starts] + [player.minutes] + [player.goals] + [player.assists] + [player.pKGoals] + [player.pKAttempts] + [player.xG] + [player.npxG] + [player.xAG])
    