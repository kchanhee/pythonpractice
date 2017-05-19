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
          print word_position_dict
          print grid[i][j]
          if grid[i][j] in word_position_dict.keys():
              
              word_position_dict[grid[i][j]].add(set([(i,j)]))
          else:
              word_position_dict[grid[i][j]] = set([(i,j)])
  found_words = []
  for word in words:
      if wordFound(grid, word_position_dict, word):
          found_words.append(word)
  return found_words
  
def wordFound(grid, word_position_dict, word, visited=None):
    if visited is None:
        visited = []
    vertex = word_position_dict[word[0]] - set(visited)
    if len(word) == 1:
        if  word in word_position_dict.keys():
            return isAdjacent(word_position_dict[word[0]] - set(visited), visited.pop())
        else:
            return False
    for v in vertex:
        if vertex not in visited:
            last_vertex = visited.pop()
            if isAdjacent(last_vertex, vertex):
                visited.append(last_vertex)
                visited.append(vertex)
                return wordFound(grid, word_position_dict, word[1:], visited)    
            else:
                continue
        else:
            return False
    
def isAdjacent(pos1, pos2):
    if pos1 is None or pos2 is None:
        return False
    r1, c1 = pos1
    r2, c2 = pos2
    if abs(r2-r1) <= 1 and abs(c2-c1) <= 1:
        return True
    return False
    
grid = [['Y','K','D','U'],
        ['A','N','L','P'],
        ['U','T','S','A'],
        ['B','D','A','M']]
words = ['MALT', 'GOOG', 'MAM']

print findWordsInGrid(grid, words)