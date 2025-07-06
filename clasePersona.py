class Persona:
    def __init__(self, nombre: str, apellido: str, edad: int, dni: int,sexo: str):
        self._nombre = nombre
        self.apellido = apellido
        self._edad = edad
        self.dni = dni
        self.sexo = sexo
        
    @property
    def edad(self):
        return self._edad
        
    @edad.setter
    def edad(self, nueva_edad):
        if isinstance(nueva_edad, int) and nueva_edad >= 0:
            self._edad = nueva_edad
        else:
            raise ValueError("La edad debe ser un número entero positivo")
        
    @property
    def nombre(self):
        return self._nombre


    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.edad} años (DNI: {self.dni}, Sexo: {self.sexo})"    
        
    


