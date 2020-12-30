# LOOPS - Needs to be completed
# We only care about the edge colours


tiles = {"1": ["", "R", "",
         "G", "", "G",
         "", "R", ""],

         "2": ["", "G", "",
         "R", "", "R",
         "", "G", ""],

         "3": ["", "R", "",
         "R", "", "G",
         "", "G", ""],

         "4": ["", "R", "",
         "G", "", "R",
         "", "G", ""],

         "5": ["", "G", "",
         "G", "", "R",
         "", "R", ""],

         "6": ["", "G", "",
         "R", "", "G",
         "", "R", ""]}




size = int(input())


board = [input().split(" ") for i in range(size)]
temp_board = board

# Board is now a grid with x and y coords


red_pairs = {"1U": ["1", "5", "6"], "1D": ["3", "4"],
                  "2R": ["2", "3", "4"], "2L": ["2", "5", "6"],
                  "3U": ["1", "5","6"], "3L": ["2", "5", "6"],
                  "4U": ["1", "5", "6"], "4R": ["2", "6", "3"],
                  "5R": ["2", "3", "6"], "5D": ["1", "3", "4"],
                  "6D": ["1", "3", "4"], "6L": ["2", "5", "4"]}

blue_pairs = {"2U": ["2", "3", "4"], "2D": ["5", "6"],
                  "1R": ["1", "5", "6"], "1L": ["1", "3", "4"],
                  "5U": ["2", "3","4"], "5L": ["1", "3", "4"],
                  "6U": ["2", "3", "4"], "6R": ["1", "4", "5"],
                  "3R": ["1", "5", "4"], "3D": ["2", "5", "6"],
                  "4D": ["2", "5", "6"], "4L": ["1", "3", "6"]}

def red_compatible(current_tile, next_tile, direction):
  try:

    if next_tile in red_pairs[f"{current_tile}{direction}"]:
      return True

  except KeyError:
    return False

def blue_compatible(current_tile, next_tile, direction):
  try:

    if next_tile in red_pairs[f"{current_tile}{direction}"]:
      return True

  except KeyError:
    return False



def up(x, y, starting_tile):
  try

  except IndexError:
    return Falses



def complete_loop(starting_tile, colour):
  if colour == "Red":
    while True:
      red_compatible(starting_tile, )


def red_score:
  score = 0
  for i in range(size):
    for j in range(size):
      if temp_board[i][j] != True:
