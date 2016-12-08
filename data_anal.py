import numpy
import os
import os.path

class Game(object):
    def __init__(self, game_list):
        self.week = int(game_list[0])
        if game_list[1].upper() == "W": # Win 
            self.result = 1.0
        elif game_list[1].upper() == "L": # Loss
            self.result = 0.0
        elif game_list[1].upper() == "T":  # Tie 
            self.result = 0.5 
        else: # Empty string or other implies game has not yet been played                      
            self.result = -1.0
        if game_list[2] == "@": # Away game
            self.athome = False
        else: # Either a home game, bye week, or game has not yet been played
            self.athome = True
        if game_list[3] == "" or game_list[3] == "Bye Week":
            self.opponent = None
        else: # Game has been played
            self.opponent = all_teams[game_list[3]]
        if game_list[4] == "" or game_list[5] == "":
            self.pts_scored = 0
            self.pts_allowed = 0
        else: # Game has already been played and scores exist
            self.pts_scored = int(game_list[4])
            self.pts_allowed = int(game_list[5]) 

class Team(object):
    def __init__(self, team_name):
        self.team_name = team_name
        self.games = []
        self.elo = 1500
        self.running_elo = []
        self.record = numpy.zeros((3,17), dtype='i')
        self. global_rank = None # Overall NFL Rank
        self.div_rank = None # Division rank
        
        # Check what conference the team is in
        if team_name == "New England Patriots" or team_name =="Miami Dolphins" \
                or team_name == "Buffalo Bills" or team_name == "New York Jets":
            self.conference = "AFC East"
        elif team_name == "Houston Texans" or team_name =="Tennessee Titans" \
                or team_name == "Indianapolis Colts" or \
                team_name == "Jacksonville Jaguars":
            self.conference = "AFC South"
        elif team_name == "Baltimore Ravens" or team_name =="Pittsburgh Steelers" \
                or team_name == "Cincinnati Bengals" or team_name == "Cleveland Browns":
            self.conference = "AFC North"
        elif team_name == "Oakland Raiders" or team_name =="Kansas City Chiefs" \
                or team_name == "Denver Broncos" or team_name == "San Diego Chargers":
            self.conference = "AFC West"
        elif team_name == "Dallas Cowboys" or team_name =="New York Giants" \
                or team_name == "Washington Redskins" or \
                team_name == "Philadelphia Eagles":
            self.conference = "NFC East"
        elif team_name == "Tampa Bay Buccaneers" or team_name =="Atlanta Falcons" \
                or team_name == "New Orleans Saints" or \
                team_name == "Carolina Panthers":
            self.conference = "NFC South"
        elif team_name == "Detroit Lions" or team_name =="Minnesota Vikings" \
                or team_name == "Green Bay Packers" or team_name == "Chicago Bears":
            self.conference = "NFC North"
        else: # Seahawks, Cardinals, Rams, 49ers
            self.conference = "NFC West"
                     
    def add_game(self, game):
        self.games.append(game)
        
    def set_elo(self, elo):
        self.elo = elo

    def calculate_elo(self, week):
        """Calculates the ELO Rating of a specific NFL team for a given Week.
        
        This function calculates the ELO Rating of a Team object up to a given 
    week in the season. 
    
    Positional Input Parameters:
        week | int:
            The week in the current NFL you would like to calculate.
            
    Returns:
        none:
        """
        if week == 1: # Base case
            if self.games[week - 1].opponent == None: # Bye week (elo unchanged)
                pass
            else: # Not a bye week
                k = 20 # regular season game k-factor (week <= 17)
                if week == 18: # playoffs: wild-card
                    k = 25
                elif week == 19: # playoffs: divisional
                    k = 30
                elif week == 20: # playoffs: conference
                    k = 35
                elif week == 21: # playoffs: superbowl
                    k = 40
                
                # Margin of victory multiplier
                mov = numpy.log(abs(self.games[week - 1].pts_scored - \
                    self.games[week - 1].pts_allowed) + 1) * \
                    (2.2/((0.001*(self.elo - self.games[week - 1].opponent.elo)) + \
                    2.2))
                
                s = self.games[week - 1].result
                
                # Expected result of game
                mu = 1/(1 + 10**((self.elo - self.games[week - 1].opponent.elo)/400))
                
                # Calculate and set new ELO Rating
                self.elo = self.elo + (k * mov * (s - mu))
        else:
            return self.calculate_elo(week - 1)
     
team_names = ["New England Patriots","Miami Dolphins","Buffalo Bills",
    "New York Jets","Houston Texans","Tennessee Titans","Indianapolis Colts",
    "Jacksonville Jaguars","Baltimore Ravens","Pittsburgh Steelers",
    "Cincinnati Bengals","Cleveland Browns","Oakland Raiders",
    "Kansas City Chiefs","Denver Broncos","San Diego Chargers","Dallas Cowboys",
    "New York Giants","Washington Redskins","Philadelphia Eagles",
    "Tampa Bay Buccaneers","Atlanta Falcons","New Orleans Saints",
    "Carolina Panthers","Detroit Lions","Minnesota Vikings","Green Bay Packers",
    "Chicago Bears","Seattle Seahawks","Arizona Cardinals","Los Angeles Rams",
    "San Francisco 49ers"] 

all_teams = {} # Dictionary of all Team objects
for iteam in team_names:
    all_teams[iteam] = Team(iteam)
            
        
team_files = [] # csv files
for filenames in os.walk("Team_Files"):               
    for ifile in filenames:
        fileobj = open(ifile, 'r')
        for igame in fileobj:
            all_teams[os.path.splitext(ifile)[0]].add_game(Game(igame.split(",")))
        fileobj.close()

# ~~~~~~~~~~~~~~~~~~~~~ Non-Graphical Analysis ~~~~~~~~~~~~~~~~~~~~~~~~~~
#               
# Calculate each team's ELO Rating
for key in all_teams.keys():
    all_teams[key].calculate_elo(17)
    print(all_teams[key].elo)

# ~~~~~~~~~~~~~~~~~~~~~ Non-Graphical Analysis ~~~~~~~~~~~~~~~~~~~~~~~~~~
# 
# Calculate the mean of the data set (Adj. Close)
total = 0.0
for i in range(numpy.shape(data2)[0]):
    total += data2[i,6]
mean = total / float(numpy.shape(data2)[0])    
print("The mean (adj. close) of the data set is: " + str(mean))

# Calculate number of days S&P 500 has been over $2,000 (Adj. Close) since
# Dec. 7, 2000.
tot_days = 0
for i in range(numpy.shape(data2)[0]):
    if data2[i,6] >= 2000.0:
        tot_days += 1    
print("\nThe number of days S&P 500 has been over \n$2,000 (Adj. Close)" \
    + "since Dec. 7, 2000 is: " + str(tot_days))

# Calculate the highest and lowest values the S&P500 has had since Dec. 7, 2000
high = data2[0,2]
low = data2[0,3]
for i in range(numpy.shape(data2)[0]):
    if data2[i,2] > high:
        high = data2[i,2]
    if data2[i,3] < low:
        low = data2[i,3]
print("\nThe highest price the S&P500 has been \nsince Dec. 7, 2000 is: " + \
    str(high))
print("\nThe lowest price the S&P500 has been \nsince Dec. 7, 2000 is: " + \
    str(low))
    
# ~~~~~~~~~~~~~~~~~~~~~ Further Analysis ~~~~~~~~~~~~~~~~~~~~~~~~~~
#
# For my dataset analysis project, I used the the last seventeen years of S&P500 
# stock index, from December 7, 2000 to December 6, 2016. My graphical analysis
# has shown (Plot 1) that despite some major world changing events (e.g. 9/11
# which is shown about 300 trading days into the graph) that the economy is 
# resilient and has bounced back to an adjusted close price of over $2,200 (as
# of today). After the 2008 financial crisis, the S&P500 saw a significant
# decrease in value, and reached a low of just $666.79 on March 6, 2009. Given
# a lag of 7 days, the S&P500 stock index (toward the end of the time series)
# is still somewhat correlated (about 0.7) and then drops significantly as the
# lag increases past 7 days. Overall the S&P500 data set is quite diverse, and
# that is why I believe it was a good choice.
