# Ladder
import random
from collections import Counter

class Player:

    def __init__(self,name):
        self.name     = name
        self.position = None
        self.match_history = []
        self.position_history = []
        self.stats = {
            "matches won"   :  0,
            "matches lost"  :  0,
            "sets won"      :  0, 
            "sets lost"     :  0,
            "games won"     :  0,
            "games lost"    :  0
        }
        self.ladder_stats = {
            "highest position": None,
            "lowest position" : None,
            "current position": None
        }

    def AlterPosition(self,new_position):
        self.position = new_position
        self.position_history.append(new_position)
        self.ComputeLadderStats()


    def UpdateStats(self,yours,theirs):
        self.stats["matches won"]   +=  yours[0]
        self.stats["matches lost"]  +=  theirs[0]
        self.stats["sets won"]      +=  yours[1]
        self.stats["sets lost"]     +=  theirs[1]
        self.stats["games won"]     +=  yours[2]
        self.stats["games lost"]    +=  theirs[2] 

    def PrintStats(self):
        print(self.stats)

    def UpdateMatchHistory(self,match):
        self.match_history.append(match)

    def ComputeLadderStats(self):
        self.ladder_stats["highest position"] = min(self.position_history)
        self.ladder_stats["lowest position"]  = max(self.position_history)
        self.ladder_stats["current position"] = self.position


class Match:

    def GenerateSetHistory(self):
        set_history = {}
        for index,Set in enumerate(self.score):
            if Set[0] > Set[1]: 
                set_history[index+1] = self.winner
            elif Set[0] < Set[1]:
                set_history[index+1] = self.loser
        
        return set_history

    def __init__(self,winner,loser,date,score):
        self.date   = date
        self.winner = winner
        self.loser  = loser
        self.score  = score 
        self.id     = winner.name + loser.name + str(date)
        self.set_history = self.GenerateSetHistory()
        
        winner_stats = (1, Counter(self.set_history.values())[winner], sum([s[0] for s in score]))
        loser_stats  = (0, Counter(self.set_history.values())[loser],  sum([s[1] for s in score]))
        winner.UpdateStats(winner_stats,loser_stats)
        loser.UpdateStats(loser_stats,winner_stats)


class Ladder:

    def SetPlayerPositions(self):
        for (pos,player) in enumerate(self.ladder): 
            player.AlterPosition(pos)
            # player.position = pos

    def __init__(self,tournament_name,list_of_initial_participants):
        self.tournament_name = tournament_name
        self.list_of_matches = []
        self.list_of_participants = list_of_initial_participants
        self.ladder = random.sample(self.list_of_participants,len(self.list_of_participants))
        self.SetPlayerPositions()

    def ShowLadder(self):
        readable_ladder = [p.name for p in self.ladder]
        print(readable_ladder)

    def AddNewParticipants(self,new_participants):
        self.list_of_participants = [*self.list_of_participants, *new_participants]

    def AddMatch(self,winner,loser,date,score):
        match = Match(winner,loser,date,score)
        self.list_of_matches.append(match)
        self.UpdateLadder(match.winner,match.loser)
        winner.UpdateMatchHistory(match)
        loser.UpdateMatchHistory(match)

    def UpdateLadder(self,winner,loser):
        loser_old_position, winner_old_position = loser.position , winner.position
        if winner_old_position > loser_old_position:
            above  = self.ladder[:loser_old_position]
            remain = [player for player in self.ladder[loser_old_position:] if player not in [winner,loser]]
            self.ladder = [*above,*[winner],*[loser],*remain]
            self.SetPlayerPositions()
        elif winner_old_position < loser_old_position:
            self.SetPlayerPositions()

    def Compute_Ladder_Statistics(self):
        self.ladder_statistics = {}

        most_matches_won = max([player.stats["matches won"] for player in self.list_of_participants])
        self.ladder_statistics["Most Matches Won"] = [player for player in self.list_of_participants if player.stats["matches won"]==most_matches_won]

        least_matches_won = min([player.stats["matches won"] for player in self.list_of_participants])
        self.ladder_statistics["Least Matches Won"] = [player for player in self.list_of_participants if player.stats["matches won"]==least_matches_won]

        most_sets_won = max([player.stats["sets won"] for player in self.list_of_participants])
        self.ladder_statistics["Most Sets Won"] = [player for player in self.list_of_participants if player.stats["sets won"]==most_sets_won]

        least_sets_won = min([player.stats["sets won"] for player in self.list_of_participants])
        self.ladder_statistics["Least Sets Won"] = [player for player in self.list_of_participants if player.stats["sets won"]==least_sets_won]

        most_games_won = max([player.stats["games won"] for player in self.list_of_participants])
        self.ladder_statistics["Most Games Won"] = [player for player in self.list_of_participants if player.stats["games won"]==most_games_won]

        least_games_won = min([player.stats["games won"] for player in self.list_of_participants])
        self.ladder_statistics["Least Games Won"] = [player for player in self.list_of_participants if player.stats["games won"]==least_games_won]

        self.ladder_statistics["Leader"] = [self.ladder[0] ]


        # Print this information
        '''
        Little piece of syntactic magic to print elements on the same line
        '''
        print("LADDER STATISTICS")
        for stat in self.ladder_statistics:
            print("\n")
            print(stat+":")
            size = len(self.ladder_statistics[stat])-1
            for i,p in enumerate(self.ladder_statistics[stat]):
                if i != size: print(p.name,end=", ",flush=True)
                else: print(p.name)





