def main():
    result = []
    with open('..\inputs\day02.txt') as f:
        while True:
            line = f.readline()
            if not line:
                break
            valid = True
            red, blue, green = 0, 0, 0
            game, sets = line.split(":")
            game = game.split(' ')[1]
            sets = sets.split(';')
            for set in sets:
                set = set.split(',')
                for s in set:
                    number, color = s.lstrip().split(' ')
                    color = color.rstrip('\n')
                    number = int(number)
                    if color == 'red':
                        if number > red:
                            red = number
                    elif color == 'blue':
                        if number > blue:
                            blue = number
                    elif color == 'green':
                        if number > green:
                            green = number
            result.append(red*blue*green)
    print(f'result: {sum(result)}')
            
if __name__ == '__main__':
    main()