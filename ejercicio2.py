import csv
from abc import ABC, abstractmethod
import os.path
from typing import Dict
from typing import List


class PizzaAbstractFactory(ABC):
    @abstractmethod
    def create_tipo(self) -> str:
        pass

    @abstractmethod
    def create_estilo(self) -> str:
        pass

class PizzaFactory(PizzaAbstractFactory):
    def create_tipo(self) -> str:
        while True:
            print("Elige el tipo del edificio:")
            print("1 - Residenciales")
            print("2 - Comerciales")
            print("3 - Industriales")
            opcion = input("Opcion: ")
            if opcion == '1':
                return "Residenciales"
            elif opcion == '2':
                return "Comerciales"
            elif opcion == '3':
                return "Industriales"
            else:
                print("Por favor, elige una opcion valida (1, 2, o 3)")

    def create_estilo(self) -> str:
        while True:
            print("Elige el estilo del edificio:")
            print("1 - Moderno")
            print("2 - Clasico")
            print("3 - Futurista")
            opcion = input("Opcion: ")
            if opcion == '1':
                return "Moderno"
            elif opcion == '2':
                return "Clasico"
            elif opcion == '3':
                return "Futurista"
            else:
                print("Por favor, elige una opcion valida (1, 2, o 3)")

    def get_pizza_info(self) -> List[str]:
        tipo = self.create_tipo()
        estilo = self.create_estilo()
        return [tipo, estilo]



# Función para verificar si un usuario ya está registrado
def usuario_existente(correo):
    with open('usuarios.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[1] == correo:
                return True
    return False

# Función para registrar un nuevo usuario si no existe previamente
def registrar_usuario():
    while True:
        print("¡Vamos a crear una cuenta!")
        nombre = input("Ingresa tu nombre: ")
        correo = input("Ingresa tu correo electrónico: ")
        contraseña = input("Ingresa una contraseña: ")

        if nombre.strip() != "" and correo.strip() != "" and contraseña.strip() != "":
            if not usuario_existente(correo):
                with open('usuarios.csv', mode='a', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow([nombre, correo, contraseña])
                    print("Usuario registrado exitosamente. Ahora inicia sesión.")
                    break
            else:
                print("Ya existe un usuario con este correo. Por favor, inicia sesión.")
                break
        else:
            print("Debes completar todos los campos.")

# Función para verificar si el usuario existe en el archivo CSV
def verificar_usuario(correo, contraseña):
    with open('usuarios.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[1] == correo and row[2] == contraseña:
                return True
    return False

# Interacción con el usuario
def iniciar_sesion_o_registrar():
    print("Vamos a crear un edificio")
    opcion = input("¿Estás registrado? (sí/no): ")

    if opcion.lower() == 'no':
        registrar_usuario()
        iniciar_sesion_o_registrar()
    elif opcion.lower() == 'sí':
        correo = input("Ingresa tu correo electrónico: ")
        contraseña = input("Ingresa tu contraseña: ")
        if verificar_usuario(correo, contraseña):
            print("Inicio de sesión exitoso.")
            # Aquí podrías redirigir al usuario a la página principal de la pizzería
        else:
            print("Algun camp es incorrecto. Inténtalo de nuevo.")
            iniciar_sesion_o_registrar()
    else:
        print("Opción no válida. Por favor, responde 'sí' o 'no'.")
        iniciar_sesion_o_registrar()








class PizzaBuilder(ABC):
    @abstractmethod
    def crear_tipo(self):
        pass
    
    @abstractmethod
    def crear_estilo(self):
        pass

    

class Pizza(PizzaBuilder):
    def crear_tipo(self):
        self.tipo = self._factory.create_tipo()

    def crear_estilo(self):
        self.estilo = self._factory.create_estilo()


class PedidoPizzaCSVBuilder:
    def crear_csv(self):
        with open('pedidos_pizza.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Cliente", "Tamano", "Masa", "Ingredientes", "Salsa", "Tecnica de coccion", "Presentacion"])
        file.close()

    def añadir_pedido(self, cliente, pizza):
        with open('pedidos_pizza.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([cliente] + pizza)
        file.close()

class PizzaDirector:
    def __init__(self, builder: PizzaBuilder):
        self._builder = builder
    
    def crear_pizza(self):
        if isinstance(self._builder, PizzaFactory):
            self._builder.create_tipo()
            self._builder.create_estilo()
        else:
            self._builder.crear_tipo()
            self._builder.crear_estilo()

    @property
    def builder(self):
        return self._builder
    
    @builder.setter
    def builder(self, builder):
        self._builder = builder

    def duplica(self):
        # Crea una nueva instancia de PizzaDirector con el mismo builder
        nuevo_director = PizzaDirector(self._builder)
        # Clona el estado actual (puede necesitar ajustes según tu lógica)
        nuevo_director._builder = self._builder
        return nuevo_director



class Producto(ABC):
    @abstractmethod
    def __init__(self, nombre):
        self.nombre = nombre

    @abstractmethod
    def descripcion(self):
        pass


def mostrar_opciones(opciones: Dict[str, str]) -> None:
    for i, opcion in enumerate(opciones, start=1):
        print(f"{i}. {opcion}")

def mostrar_opciones(opciones: Dict[str, str]) -> None:
    for i, opcion in enumerate(opciones, start=1):
        print(f"{i}. {opcion}")

def seleccion_valida(opcion: int, opciones: Dict[str, str]) -> bool:
    return 1 <= opcion <= len(opciones)

def obtener_seleccion(opciones: Dict[str, str]) -> str:
    while True:
        mostrar_opciones(opciones)
        opcion = input("Opcion: ")
        if opcion.isdigit():
            opcion = int(opcion)
            if seleccion_valida(opcion, opciones):
                return list(opciones.values())[opcion - 1]
        print("Error: Ingresa un número válido.")


