''' /**
  * Problem Given a 4x4 grid of letter tiles
  *
  * Find words by:
  * 
  * Visiting immediately adjacent tiles.
  *
  * Diagonals are valid moves.
  *
  * A letter tile can only be used once per word.
  *
  * Y K D U
  * A N L P
  * U T S A
  * B D A M
  *
  * list of words 
  * MALT
  * GOOG
  * MAM
  *
  * 200K other words
  */'''
  
def findWordsInGrid(grid, words):
  word_position_dict = {}
  for i in range(4):
    for j in range(4):
    # print word_position_dict
    # print grid[i][j]
      if grid[i][j] in word_position_dict.keys():
          word_position_dict[grid[i][j]].add((i,j))
      else:
          word_position_dict[grid[i][j]] = set([(i,j)])
  found_words = []
  for word in words:
    # save word (if there is a valid path)
    if wordFound(word_position_dict, word):
      found_words.append(word)
  return found_words
  
# need to see if there's a valid path from front to end of string
# This method prints the path if there is one and None if not.
# Uses DFS and backtracing via recursion to generate paths.

def wordFound(word_position_dict, word, visited=None):
  if visited is None:
    visited = []
  # print word[0]
  # At end of word return empty
  if word == "":
    return []
  # Check if next letter is even in the grid
  if word[0] not in word_position_dict.keys():
    return []
  visited_len = len(visited)
  for v in word_position_dict[word[0]]:
    if v in visited:
      continue
    if visited_len > 0:
      if not isAdjacent(v, visited[-1]):
        continue
    else:
      if not isAdjacent(v, []):
        continue
    word_path = wordFound(word_position_dict, word[1:], visited + [v])
    if word_path is not None:
      return [v] + word_path
  return None

# Helper Method to check if two points are adjacent
# pos2 will be empty in the beginning so we return True. (beginning of DFS)

def isAdjacent(pos1, pos2):
  if len(pos2) == 0:
      return True
  return abs(pos2[1] - pos1[1]) <= 1 and abs(pos2[0] - pos1[0]) <= 1
  
  
    
grid = [['Y','K','D','U'],
        ['A','N','L','P'],
        ['U','T','S','A'],
        ['B','D','A','M']]
words = ['MALT', 'GOOG', 'MAM', 'ANLP', 'UTSA', 'YKDUPLNAUTSAMADBU', 'YKDUPLNAUTSAMADB', 'YAUB', 'YKNA', 'PSDU', 'NAUT', '']

print set(findWordsInGrid(grid, words)) == set(['MALT', 'ANLP', 'UTSA', 'YKDUPLNAUTSAMADB', 'YAUB', 'YKNA', 'PSDU', 'NAUT'])
