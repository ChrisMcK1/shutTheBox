import itertools


theBoard = [1, 2, 3, 4,\
            'X', 'X', 'X', 8, 9, \
            'X']
testList = [1, 2, 3, 4, 5, 6]

diceRoll = 8

availablePlay = []   #empty list that will then populate with current integers on the board
for i in theBoard[:10]:
    try:
        
        if i == 'X':
            continue
        else:
            availablePlay.append(i)
            
    except ValueError:
        continue
    except TypeError:
        continue
    
result = [seq for i in range(len(availablePlay), 0 , -1) for seq in itertools.combinations(availablePlay, i) if sum(seq) == diceRoll]  #itertools sequence to create list variable containing all available plays
print(result)
