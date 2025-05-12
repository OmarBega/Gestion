
En Python, los diccionarios, que también se conocen como "maps" o "hashtables", tienen varios métodos útiles para manipular y acceder a los datos. Algunos de los más comunes incluyen: keys(), values(), items(), get(), pop(), popitem(), update(), clear(), y setdefault().
Métodos para acceder a los datos:

    keys():
    Devuelve una vista de las claves del diccionario como un objeto dict_keys.
    values():
    Devuelve una vista de los valores del diccionario como un objeto dict_values.
    items():
    Devuelve una vista de los pares clave-valor del diccionario como un objeto dict_items.
    get(key, default=None):
    Devuelve el valor asociado a la clave key, o default si la clave no existe.
    __getitem__(key) (también conocido como d[key]):
    Accede al valor asociado a la clave key. Si la clave no existe, lanza una excepción KeyError.

Métodos para modificar los datos:

    pop(key, default=None): Elimina el par clave-valor asociado a la clave key y devuelve el valor. Si la clave no existe, devuelve default o lanza una excepción si no se proporciona default.
    popitem(): Elimina un par clave-valor arbitrario (el último agregado, en versiones de Python antes de 3.7) y lo devuelve como una tupla.
    update(other_dict): Actualiza el diccionario con los pares clave-valor de otro diccionario. Si una clave ya existe, su valor se sobrescribe.
    clear(): Elimina todos los elementos del diccionario.
    setdefault(key, default=None): Si la clave key ya existe, devuelve su valor. De lo contrario, agrega la clave con el valor default y devuelve default.
    __setitem__(key, value) (también conocido como d[key] = value): Asocia un valor a una clave. Si la clave no existe, la crea.

Otros métodos y consideraciones:

    __delitem__(key) (también conocido como del d[key]): Elimina la clave key del diccionario.
    len(d): Devuelve el número de elementos (pares clave-valor) en el diccionario.
    in: Comprueba si una clave existe en el diccionario (ej: if 'clave' in d: ...).
    ==, !=: Compara diccionarios para igualdad o desigualdad (se basan en los pares clave-valor).




En Python, las listas son estructuras de datos versátiles que se pueden modificar utilizando varios métodos. Algunos de los métodos más comunes incluyen append(), extend(), insert(), remove(), pop(), index(), count(), sort(), reverse() y clear(). Estos métodos permiten agregar, eliminar, modificar y reorganizar elementos dentro de una lista. 
Métodos de lista en Python:

    append(): Agrega un elemento al final de la lista. 

Python

    mi_lista = [1, 2, 3]
    mi_lista.append(4)
    print(mi_lista)  # Output: [1, 2, 3, 4]

    extend(): Agrega los elementos de una lista iterable al final de la lista. 

Python

    mi_lista = [1, 2, 3]
    otra_lista = [4, 5]
    mi_lista.extend(otra_lista)
    print(mi_lista)  # Output: [1, 2, 3, 4, 5]

    insert(): Agrega un elemento en una posición específica de la lista. 

Python

    mi_lista = [1, 2, 3]
    mi_lista.insert(1, 0)  # Inserta 0 en la posición 1
    print(mi_lista)  # Output: [1, 0, 2, 3]

    remove(): Elimina la primera ocurrencia de un elemento de la lista. 

Python

    mi_lista = [1, 2, 2, 3]
    mi_lista.remove(2)
    print(mi_lista)  # Output: [1, 2, 3]

    pop(): Elimina y devuelve el elemento en una posición específica de la lista (o el último elemento si no se proporciona una posición). 

Python

    mi_lista = [1, 2, 3]
    elemento_eliminado = mi_lista.pop(1)
    print(mi_lista)  # Output: [1, 3]
    print(elemento_eliminado)  # Output: 2

    index(): Devuelve el índice de la primera ocurrencia de un elemento en la lista. 

Python

    mi_lista = [1, 2, 3, 2]
    indice = mi_lista.index(2)
    print(indice)  # Output: 1

    count(): Devuelve el número de veces que aparece un elemento en la lista. 

Python

    mi_lista = [1, 2, 2, 3]
    cantidad = mi_lista.count(2)
    print(cantidad)  # Output: 2

    sort(): Ordena los elementos de la lista en el lugar (modificando la lista original). 

Python

    mi_lista = [3, 1, 4, 1, 5, 9]
    mi_lista.sort()
    print(mi_lista)  # Output: [1, 1, 3, 4, 5, 9]

    reverse(): Invierte el orden de los elementos en la lista. 

Python

    mi_lista = [1, 2, 3]
    mi_lista.reverse()
    print(mi_lista)  # Output: [3, 2, 1]

    clear(): Elimina todos los elementos de la lista. 

Python

    mi_lista = [1, 2, 3]
    mi_lista.clear()
    print(mi_lista)  # Output: []

    len(): Devuelve la longitud de la lista (número de elementos). 

