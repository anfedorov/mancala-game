import json


class InvalidMove(RuntimeError):
  pass


class MancalaGame(object):
  def __init__(self, game_state=None):
    if game_state == None:
      self.board = [4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0]
      self.player_turn = 0
    else:
      self.board = game_state['board']
      self.player_turn = game_state['player_turn']

  def __str__(self):
    return """-----------------------------------------
|    | {12:2d} | {11:2d} | {10:2d} | {9:2d} | {8:2d} | {7:2d} |    |
| {13:2d} |-----------------------------| {6:2d} |
|    | {0:2d} | {1:2d} | {2:2d} | {3:2d} | {4:2d} | {5:2d} |    |
-----------------------------------------""".format(*self.board)

  def to_dict(self):
    return {
      'board': self.board,
      'player_turn': self.player_turn,
    }

  def make_move(self, move_bin):
    """Makes a move, modifying `board`.

    move (int): [0, 5] or [7, 12], the bin to be moved

    Raises InvalidMove if bin has no stones

    """
    limits = [0, 5] if self.player_turn == 0 else [7, 12]
    if not limits[0] <= move_bin <= limits[1]:
      raise InvalidMove('move_bin must be in %s during turn of player %s' % (limits, self.player_turn))

    num_stones = self.board[move_bin]

    if not num_stones > 0:
      raise InvalidMove('not enough stones (%s) in bin %s' % (num_stones, move_bin))

    self.board[move_bin] = 0
    n = move_bin  # n will be the bin the stones go in

    op = lambda x: [12, 11, 10, 9, 8, 7, 13, 5, 4, 3, 2, 1, 0, 6][x]
    bin_of = lambda player: 6 if player == 0 else 13

    while num_stones > 0:
      n = (n + 1) % 14
      # if (self.player_turn == 0 and n == 13) or (self.player_turn == 1 and n == 6):
      if n == op(bin_of(self.player_turn)):
        continue
      self.board[n] += 1
      num_stones -= 1

    if self.board[n] == 1 and self.board[op(n)] != 0:
      if (self.player_turn == 0 and 0 <= n < 6) or (self.player_turn == 1 and 7 <= n < 13):
        self.board[bin_of(self.player_turn)] += self.board[n] + self.board[op(n)]
        self.board[n] = 0
        self.board[op(n)] = 0

    if bin_of(self.player_turn) != n:
      # ended in small bin, swap player turn
      self.player_turn = [1, 0][self.player_turn]

    return self.player_turn

  @property
  def is_over(self):
    return not (any(self.board[0:6]) or any(self.board[7:13]))

  @property
  def score(self):
    return [self.board[0], self.board[6]]
