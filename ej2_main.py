from ejercicio2 import *
import csv
import os.path

def main():
    iniciar_sesion_o_registrar()

    # Asegúrate de que pedido_builder está definido antes de usarlo
    pedido_builder = PedidoPizzaCSVBuilder()

    for i in range(3):  # Iteramos tres veces para crear tres pizzas
        # Crea la pizza utilizando la fábrica abstracta
        factory = PizzaFactory()
        director = PizzaDirector(factory)
        director.crear_pizza()
        pizza_info = director.builder.get_pizza_info()

        # Añade la pizza al pedido (ajusta según tus necesidades)
        pedido_builder.añadir_pedido("cliente1", pizza_info)

    try:
        tipo_seleccion = obtener_seleccion({"Residenciales": "Residenciales", "Comerciales": "Comerciales", "Industriales": "Industriales"})
        estilo_seleccion = obtener_seleccion({"Moderno": "Moderno", "Clasico": "Clasico", "Futurista": "Futurista"})

        # Utiliza las selecciones del usuario para escribir en el archivo CSV
        nueva_fila = ['elemento1', 'elemento2', 'elemento3', 'elemento4']

        nombre_archivo = 'complementos.csv'
        with open(nombre_archivo, mode='a', newline='') as archivo_csv:
            escritor_csv = csv.writer(archivo_csv)
            escritor_csv.writerow(nueva_fila)

    except ValueError as e:
        print("Error: Ingresa un número válido.")

    # Muestra la información de las pizzas almacenadas en el CSV
    with open('pedidos_pizza.csv', 'r') as file:
        reader = csv.reader(file)
        print("\nInformacion de los edificios:")
        for row in reader:
            print(row)

   

    

if __name__ == "__main__":
    main()
