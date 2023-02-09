# Agregar nodo al último de una lista circular.
# Eliminar último nodo de una lista circular
# Verificar si una lista circular esta vacía.
# Agregar nodo al inicio de una lista circular.
# Eliminar primer nodo de una lista circular.
# Mostrar lista.

class Node(object):
    '''Crear una clase nodo'''
    def __init__(self, data):
        self.data = data
        self.next = None

class lista_circular(object):
    '''Crear una clase que cree una lista circular vinculada'''
    def __init__(self):
        self.head = None
        self.tail = self.head
    
    def lista_vacia(self):
        '''Determine si la lista circular esta vacía'''
        return self.head is None
    
    def recorrer_lista(self):
        '''Recorreindo lista circular'''
        if self.lista_vacia():
            return
        aux = self.head
        print(aux.data)
        while aux.next != self.head:
            aux = aux.next
            print(aux.data)
    
    def agregar_inicio(self,data):
        '''Agregar un nodo a la cabeza'''
        nodo = Node(data)
        if self.lista_vacia():
            self.head = nodo
        else:
            aux=self.head
            while aux.next != self.head:
                aux = aux.next
            aux.next = nodo
            nodo.next = self.head
            self.head = nodo

    def agregar_ultimo(self,data):
        '''Agregar un nodo al final'''
        nodo = Node(data)
        if self.lista_vacia():
            self.head = nodo
            nodo.next = self.head
        else:
            aux = self.head
            while aux.next != self.head:
                aux = aux.next
            aux.next = nodo
            nodo.next = self.head

    def eliminar_ultimo(self):
        '''Eliminar ultimo nodo'''
        if self.lista_vacia():
            return
        else:
            aux = self.head
            pre = None
            while aux.next != self.head:
                pre = aux
                aux = aux.next
        pre.next = aux.next

try:
    if __name__ == '__main__':
        lista = lista_circular()
        opcion = 0
        while opcion != 6:
            print('Lista enlazada circular: \n 1. Agregar ultimo\n 2. Eliminar ultimo\n 3. Lista vacia?\n 4. Agregar inicio\n 5. Mostrar\n 6.Salir')
            opcion = int(input('Ingrese opcion '))
            if opcion == 1:
                dato = input('Ingrese un dato ')
                lista.agregar_ultimo(dato)
            elif opcion == 2:
                lista.eliminar_ultimo()
            elif opcion == 3:
                print('Si' if lista.lista_vacia() else 'No')
            elif opcion == 4:
                dato = input('Ingrese un dato ')
                lista.agregar_inicio(dato)
            elif opcion == 5:
                lista.recorrer_lista()
            elif opcion == 6:
                print('FIN')
            else:
                print('Ingrese un dato correcto')

except Exception as e:
    print(e)