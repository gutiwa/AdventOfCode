
def main():
    max = 0
    cal = 0
    with open('..\inputs\day01.txt') as f:
        while True:
            line = f.readline()
            if not line:
                break
            if line != "\n":
                cal += int(line.strip())
            else:
                if cal > max:
                    max = cal
                cal = 0
    print(max)

if __name__ == '__main__':
    main()

