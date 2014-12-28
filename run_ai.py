import requests
import time

from macala import MancalaGame, InvalidMove
from ai import AI

game_id = raw_input('Game id [test]: ') or 'test'
player = raw_input('Player [0]: ') or '0'
ai = AI(int(player))

while True:
  game = MancalaGame(requests.get('http://localhost:8080/game/%s.json' % game_id).json())

  if game.player_turn != ai.player:
    print 'waiting for my turn'
    time.sleep(3)
    continue

  move = ai.find_move(game)
  print 'moving %s' % move
  requests.get('http://localhost:8080/game/%s/move/%s' % (game_id, move))
