def main():
    calibration_value = []
    with open('..\inputs\day01.txt') as f:
        while True:
            line = f.readline()
            if not line:
                break
            for letter in line:
                if letter.isdigit():
                    first_num = letter
                    break
            for n in range(len(line)-1, -1, -1):
                if line[n].isdigit():
                    second_num = line[n]
                    break
            calibration_value.append(int(first_num + second_num))   
    print(sum(calibration_value))
            
if __name__ == '__main__':
    main()