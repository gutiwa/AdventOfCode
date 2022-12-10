def get_compartments(list_items = ""):
    '''
    Función para obtener una tupla con los elementos de cada compartimiento
    '''
    first_half = ""
    second_half = ""
    for i in range(int(len(list_items)/2)):
        first_half += list_items[i]
    for i in range(int(len(list_items)/2), len(list_items)):
        second_half += list_items[i]
    return (first_half, second_half)

def get_same_item(compartments = ("", "")):
    '''
    Función para obtener el item repetido en los compartimientos
    '''
    same_item = ""
    for item in compartments[0]:
        if item in compartments[1]:
            same_item = item
            return same_item
    return same_item

def get_priority(item = ""):
    '''
    Función para obtener la prioridad del item
    Se trasnforma el char del item en código ASCII, así restarle para que inicie la a en 1 y A en 27 
    '''
    priority = 0
    priority = ord(item)
    if priority <= 90:
        priority -= 38
    if priority >= 97:
        priority -= 96
    return priority

def main():
    list_items = []
    with open('..\inputs\day03.txt') as f:
        while True:
            line = f.readline()
            if not line:
                break
            list_items.append(line.rstrip("\n"))
    # Se crea una lista de los resultados en tuplas de cada compartimiento
    halfs = list(map(get_compartments, list_items))
    # Se crea una lista de los resultados del mismo item obtenido de los compartimientos en cada maleta
    same_items = list(map(get_same_item, halfs))
    # Se suma el valor de prioridad del item de cada uno de los items obtenidos
    total_priority = sum(map(get_priority, same_items))
    print(total_priority)
    
if __name__ == '__main__':
    main()