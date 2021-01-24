
theBoard = [1, 'X', 3, 4,\
            'X', 'X', 'X', 'X', 9, \
            'X']
testList = [1, 2, 3, 4, 5, 6]

diceRoll = 6


for i in theBoard[0:(diceRoll-1)]:
    try:
        if i == diceRoll:
            print(i)

        else:
            print(i+1)
    except ValueError:
        continue
    except TypeError:
        continue

def combinations(values):
    if len(values) == 0:
        return [[]]
    combos = []
    for val in combinations(values[1:]):
        combos += [val, val + [values[0]]]
    return combos

print (combinations([1]))  # Expecting: [[1]]
print (combinations([1, 2])) # Expecting: [1], [2], [1 ,2]
print (combinations([1, 2, 3])) #Expecting: [[1], [2], [3], [1, 2], [2, 3], [1, 2, 3]]

                
