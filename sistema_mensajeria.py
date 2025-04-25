#   Ejercicio de entrega POO.

class Contactos:
    def __init__(self, nombre, telefono):
        self.nombre = nombre
        self.telefono = telefono

    def verificar_contactos(self):
        while True:
            if self.nombre.isalpha() == False or len(self.nombre) < 1 and len(self.nombre) > 10:
                print("Los nombres deben componerse solo de letras con un mínimo de 2 y un máximo de 10 carácteres")
                break
            elif self.telefono.isdigit() == False or len(self.telefono) != 9:
                print("Los teléfonos deben componerse de una secuencia de 9 dígitos")
                break
            else:
                return True
                

class Agenda:
    def __init__(self):
        self.propietario = "Asier de Blas"
        self.lista_contactos = []

    def añadir_contacto(self, contacto):
        self.lista_contactos.append(contacto)
        print(f"{contacto.nombre} se ha añadido correctamente.")

    def mostrar_lista(self):
        cantidad = 0
        for indice, elemento in enumerate(self.lista_contactos):
            print(f"{indice + 1}. Nombre: {elemento.nombre}; Teléfono: {elemento.telefono}")
            cantidad += 1
        return cantidad

    def buscar_contacto(self, persona):
        for contacto in self.lista_contactos:
            if contacto.nombre == persona:
                print(f"¡{persona} está en la lista de contactos!")
                return True
            elif contacto.telefono == persona:
                print(f"¡El número {persona} está en la lista de contactos!")
                return True
            else:
                return False
            
    def editar_contacto(self, contacto):
        while True:
            edicion = input("Editar nombre, teléfono o ambos: ")
            if edicion == "nombre":
                self.lista_contactos[contacto].nombre = input("Escribe el nuevo nombre: ")
                break
            elif edicion == "teléfono":
                self.lista_contactos[contacto].telefono = input("Escribe el nuevo teléfono: ")
                break
            elif edicion == "ambos":
                self.lista_contactos[contacto] = Contactos(input("Nombre: "), input("Teléfono: "))
                break
            else:
                print("Comando invalido, por favor escriba una de las opciones.")
            
    def eliminar_contacto(self, eleccion):
        self.lista_contactos.pop(eleccion)
        print("Contacto correctamente eliminado.")
            

def main():
    menu = ""
    agendar = Agenda()

    while menu != "salir":

        menu = input("¿Quieres añadir/mostrar/buscar/editar/eliminar/salir?: ")   

        match menu.lower():
            case "añadir":
                validacion = False
                contacto = Contactos(input("Nombre: "), input("Teléfono: "))
                validacion = contacto.verificar_contactos()
                if validacion == True:
                    agendar.añadir_contacto(contacto)

            case "mostrar":
                agendar.mostrar_lista()

            case "buscar":
                comprobacion = False
                persona = input("¿Qué contacto quieres buscar?, escribe su nombre o número: ")
                comprobacion = agendar.buscar_contacto(persona)
                if comprobacion == False:
                    print(f"¡{persona} no está agregado a la lista de contactos!")

            case "editar":
                cantidad = agendar.mostrar_lista()
                eleccion = int(input("¿Que contacto quieres editar? Pon su posición en la lista: "))
                if eleccion < cantidad:
                    agendar.editar_contacto(eleccion - 1)

            case "eliminar":
                agendar.mostrar_lista()
                eleccion = int(input("¿Que contacto quieres eliminar? Pon su posición en la lista: "))
                agendar.eliminar_contacto(eleccion - 1)
            
            case _:
                print("Comando invalido, por favor escriba una de las opciones.")

main()

