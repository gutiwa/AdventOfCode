def get_play(turn):
    '''
    Función para calcular el puntaje obtenido en el turno
    Recibe una tupla con las opciones del oponente[0] y de uno[1]
    '''
    if ((turn[0] == 'A' and turn[1] == 1) or 
    (turn[0] == 'B' and turn[1] == 2) or
    (turn[0] == 'C' and turn[1] == 3)):
        return 3
    if ((turn[0] == 'A' and turn[1] == 2) or 
    (turn[0] == 'B' and turn[1] == 3) or
    (turn[0] == 'C' and turn[1] == 1)):
        return 6
    return 0

def get_turn_points(result = []):
    '''
    Función para calcular los puntos de todos los turnos
    Recibe una lista de tuplas con lo escogido en cada turno
    '''
    ### Se hace una suma de los resultados obtenidos al enviar cada elemento del result a la función get_play
    turn_points = sum(map(get_play, result))
    return turn_points

def main():
    # Dict con los valores obtenidos por nuestra shape escogida
    my_option = {
        'X': 1, # Rock
        'Y': 2, # Paper 
        'Z': 3  # Scissor
    }
    # list con los resultados totales
    result = []
    total_points = 0

    with open('..\inputs\day02.txt') as f:
        while True:
            line = f.readline()
            if not line:
                break
            result.append((line.split()[0], my_option[line.split()[1]]))
            total_points += result[-1][1]

    total_points += get_turn_points(result)
    print(total_points)

if __name__ == '__main__':
    main()
