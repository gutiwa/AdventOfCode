bag = {
    'red': 12,
    'green': 13,
    'blue': 14
}

def main():
    result = []
    with open('..\inputs\day02.txt') as f:
        while True:
            line = f.readline()
            if not line:
                break
            valid = True
            game, sets = line.split(":")
            game = game.split(' ')[1]
            sets = sets.split(';')
            for set in sets:
                set = set.split(',')
                for s in set:
                    number, color = s.lstrip().split(' ')
                    color = color.rstrip('\n')
                    if int(number) > bag[color]:
                        valid = False
                        break
            if valid:
                result.append(int(game))
    print(f'result: {sum(result)}')
            
if __name__ == '__main__':
    main()