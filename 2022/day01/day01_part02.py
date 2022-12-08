
def main():
    max = []
    cal = 0
    with open('..\inputs\day01.txt') as f:
        while True:
            line = f.readline()
            if not line:
                break
            if line != "\n":
                cal += int(line.strip())
            else:
                if len(max) < 3:
                    max.append(cal)
                else:
                    if min(max) < cal:
                        max[max.index(min(max))] = cal
                cal = 0
    print(sum(max))

if __name__ == '__main__':
    main()

