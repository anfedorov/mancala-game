from collections import defaultdict

from bottle import route, run, template, redirect, response

from macala import MancalaGame, InvalidMove
from util import random_string


GAMES = defaultdict(MancalaGame)


def game_to_html(game):
  return """
<style>
  a {{
    text-decoration: none;
  }}
  p {{
    font-family: monospace;
    white-space: pre;
  }}
</style>
<p>&#x2554;&#x2550;&#x2550;&#x2550;&#x2550;&#x2564;&#x2550;&#x2550;&#x2550;&#x2550;&#x2564;&#x2550;&#x2550;&#x2550;&#x2550;&#x2564;&#x2550;&#x2550;&#x2550;&#x2550;&#x2564;&#x2550;&#x2550;&#x2550;&#x2550;&#x2564;&#x2550;&#x2550;&#x2550;&#x2550;&#x2564;&#x2550;&#x2550;&#x2550;&#x2550;&#x2564;&#x2550;&#x2550;&#x2550;&#x2550;&#x2557;
&#x2551;    &#x2502; <a href='move/12'>{12:2d}</a> &#x2502; <a href='move/11'>{11:2d}</a> &#x2502; <a href='move/10'>{10:2d}</a> &#x2502; <a href='move/9'>{9:2d}</a> &#x2502; <a href='move/8'>{8:2d}</a> &#x2502; <a href='move/7'>{7:2d}</a> &#x2502;    &#x2551;
&#x2551; <a href='move/13'>{13:2d}</a> &#x251C;&#x2500;&#x2500;&#x2500;&#x2500;&#x253C;&#x2500;&#x2500;&#x2500;&#x2500;&#x253C;&#x2500;&#x2500;&#x2500;&#x2500;&#x253C;&#x2500;&#x2500;&#x2500;&#x2500;&#x253C;&#x2500;&#x2500;&#x2500;&#x2500;&#x253C;&#x2500;&#x2500;&#x2500;&#x2500;&#x2524; <a href='move/6'>{6:2d}</a> &#x2551;
&#x2551;    &#x2502; <a href='move/0'>{0:2d}</a> &#x2502; <a href='move/1'>{1:2d}</a> &#x2502; <a href='move/2'>{2:2d}</a> &#x2502; <a href='move/3'>{3:2d}</a> &#x2502; <a href='move/4'>{4:2d}</a> &#x2502; <a href='move/5'>{5:2d}</a> &#x2502;    &#x2551;
&#x255A;&#x2550;&#x2550;&#x2550;&#x2550;&#x2567;&#x2550;&#x2550;&#x2550;&#x2550;&#x2567;&#x2550;&#x2550;&#x2550;&#x2550;&#x2567;&#x2550;&#x2550;&#x2550;&#x2550;&#x2567;&#x2550;&#x2550;&#x2550;&#x2550;&#x2567;&#x2550;&#x2550;&#x2550;&#x2550;&#x2567;&#x2550;&#x2550;&#x2550;&#x2550;&#x2567;&#x2550;&#x2550;&#x2550;&#x2550;&#x255D;</p>
<p>it is {player} player's turn</p>
    """.format(*game.board, player=game.player_turn)


@route('/')
def main():
  redirect('/game/' + random_string() + '/')


@route('/game/<game_id>/')
def game(game_id):
  return game_to_html(GAMES[game_id])


@route('/game/<game_id>.json')
def game_json(game_id):
  return GAMES[game_id].to_dict()


@route('/game/<game_id>/move/<move>')
def move_game(game_id, move):
    move = int(move)
    try:
      GAMES[game_id].make_move(move)
    except InvalidMove as e:
      print 'invalid move: %s' % e
    redirect('/game/%s/' % game_id)



run(host='localhost', port=8080, debug=True, reloader=True)
