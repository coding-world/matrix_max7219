import shelve

regal = shelve.open('score.txt')

def updateScore(neuerScore):
  if('score' in regal):
    score = regal['score']
    if(neuerScore not in score):
      score.insert(0, neuerScore)

    score.sort()
    ranking = score.index(neuerScore)
    ranking = len(score)-ranking
  else:
    score = [neuerScore]
    ranking = 1

  print(score)
  print(ranking)
  regal['score'] = score
  return ranking

neuerScore = int(input("Neuer HighScore: \n"))
updateScore(neuerScore)