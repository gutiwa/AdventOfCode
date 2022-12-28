def get_groups(list_items = ""):
    '''
    Función para obtener una lista de listas de grupos de 3
    '''
    groups = []
    for x in range(int(len(list_items)/3)):
        group = []
        group.append(list_items[x*3])
        group.append(list_items[(x*3) + 1])
        group.append(list_items[(x*3) + 2])
        groups.append(group)
    return groups

def get_same_item(compartments = ("", "", "")):
    '''
    Función para obtener el item repetido en los compartimientos
    '''
    same_item = ""
    for item in compartments[0]:
        if item in compartments[1] and item in compartments[2]:
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
    groups = get_groups(list_items)
    # Se crea una lista de los resultados del mismo item obtenido de los compartimientos en cada maleta
    same_items = list(map(get_same_item, groups))
    # Se suma el valor de prioridad del item de cada uno de los items obtenidos
    total_priority = sum(map(get_priority, same_items))
    print(total_priority)
    
if __name__ == '__main__':
    main()