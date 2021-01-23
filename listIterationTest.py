theBoard = ['1', 'X', '3','4',\
            'X', 'X', 'X', 'X', '9', \
            'X']

diceRoll = 6


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

for pieces in theBoard[0:(diceRoll)]:
    try:
        if int(pieces) == diceRoll:
            print(pieces)
        if int(theBoard[0]) + int(theBoard[2]) == 4:
            print('winner!')

        else:
            print('no hit')
    except ValueError:
        continue


                
