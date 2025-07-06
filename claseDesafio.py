from clasePersona import Persona

class Familia:
    def __init__(self,padre, madre):
        self.padre = padre
        self.madre = madre
        self.hijos = []

    def agregar_hijo(self,hijo):
        self.hijos.append(hijo)

    def nombres_hijos(self):
        return [hijo.nombre for hijo in self.hijos]
        
    
    

class Desafio:
    def imprimir_mensaje(msg):
        print(msg)

    def crear_persona():
        while input() != "n":
            nombre = input("Ingrese el nombre: ")
            apellido = input("Ingrese Apellido: ")
            edad = int(input("Ingrese edad: "))
            dni = input("Ingrese Numero de DNI: ")
            sexo = input("Ingrese sexo (varon o mujer): ")
            return Persona(nombre,apellido,edad,dni,sexo)
            
        
     

    def execute():
        Desafio.imprimir_mensaje("\n--- Creamos una Familia ---\n")

        """Creamos el padre"""
        print("Desea ingresar los datos del Padre? s/n")
        padre = Desafio.crear_persona()
        

        """Creamos la madre"""
        print("Desea ingresar los datos de la Madre? s/n")
        madre = Desafio.crear_persona()

        familia = Familia(padre,madre)

        """Creamos un hijo y agregamos a la lista de familia"""
        numhijos = int(input("Ingrese la cantidad de hijos: "))
        
        mayores = 0
        menores = 0
        hijovaron = 0
        hijammujer = 0

        if numhijos > 0:
            for i in range(numhijos):
                print("Desea ingresar los datos del hijo? s/n: ")
                hijo = Desafio.crear_persona()
                print(hijo.nombre)
                familia.agregar_hijo(hijo)
                edadhijo = hijo.edad
                if edadhijo >= 18:
                    mayores += 1
                else:
                    menores += 1

                sexohijo = hijo.sexo

                if sexohijo == "mujer".lower():
                    hijammujer += 1
                
                if sexohijo == "varon".lower():
                    hijovaron += 1

        if mayores > 0:
            print("\nLa familia tiene hijos mayores")
        elif menores > 0:
            print("\nLa familia tiene hijos menores")

        if madre:
            print(f"El nombre de la Madre es {madre.nombre}")

        if padre:
            print(f"El nombre de la Padre es {padre.nombre}")
       
        if numhijos > 0:
            print("\nNombres de los hijos:")
            for hijo in familia.hijos:
                print(f"- {hijo.nombre}")

        print(f"La familia tiene {numhijos} hijos/as")
        print(f"La familia tiene {hijammujer} hijas mujeres y {hijovaron} hijos varones")
        
           
    
        
        
        




if __name__ == "__main__":
    Desafio.execute()