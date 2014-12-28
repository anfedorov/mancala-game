
from macala import MancalaGame

mg = MancalaGame()

while not mg.is_over:
  print mg
  print "it is player %s's turn" % mg.player_turn
  mg.make_move(int(raw_input('> ')))

print mg
p0, p1 = mg.score

if p0 < p1:
  print "player 1 wins!"
elif p1 < p0:
  print "player 0 wins!"
else:
  print "it's a tie!"
