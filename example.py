
from ladder import Player,Match,Ladder


ethan =Player("Ethan")
caz   = Player("Caz")
mads  = Player("Mads")
chris = Player("Chris")
flora = Player("Flora")


Lad = Ladder("Competition",[ethan,caz,flora,chris,mads])


Lad.ShowLadder()

print(chris.position)

Lad.AddMatch(flora,chris,"today",((6,4),(7,6)))

Lad.AddMatch(ethan,caz,"today2",((6,4),(7,6)))


Lad.ShowLadder()

Lad.Compute_Ladder_Statistics()

# print(chris.position_history)