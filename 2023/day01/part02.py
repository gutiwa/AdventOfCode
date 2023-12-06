numbers = [
    'one',
    'two', 
    'three', 
    'four', 
    'five', 
    'six', 
    'seven', 
    'eight', 
    'nine']

def main():
    calibration_value = []
    with open('..\inputs\day01.txt') as f:
        while True:
            line = f.readline()
            if not line:
                break
            aux = 0
            for i, letter in enumerate(line):
                if aux == 1:
                    break
                if letter.isdigit():
                    first_num = letter
                    break
                for j, num in enumerate(numbers):
                    if line[i:].startswith(num):
                        first_num = str(j + 1)
                        aux = 1
                        break
            aux = 0
            for n in range(len(line)-1, -1, -1):
                if aux == 1:
                    break
                if line[n].isdigit():
                    second_num = line[n]
                    break
                for j, num in enumerate(numbers):
                    if line[n:].startswith(num):
                        second_num = str(j + 1)
                        aux = 1
                        break
            calibration_value.append(int(first_num + second_num))   
    print(sum(calibration_value))
            
if __name__ == '__main__':
    main()