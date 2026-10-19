class Estudiante:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self._notas = []  

    @property
    def notas(self):
        """Getter de notas que retorna una copia para evitar mutabilidad externa no deseada."""
        return self._notas.copy()

    def agregar_nota(self, nota: float):
        """Método para agregar una nota con validación de rango (0.0 a 5.0)."""
        if 0.0 <= nota <= 5.0:
            self._notas.append(nota)
            print(f"Nota {nota} agregada exitosamente para {self.nombre}.")
        else:
            print(f"Error: La nota {nota} es inválida. Debe estar entre 0.0 y 5.0.")

    def calcular_promedio(self) -> float:
        """Calcula y retorna el promedio de las notas del estudiante."""
        if not self._notas:
            return 0.0
        return sum(self._notas) / len(self._notas)


if __name__ == "__main__":
    estudiante1 = Estudiante("Jesus Meriño")
    
    
    estudiante1.agregar_nota(4.5)
    estudiante1.agregar_nota(3.8)
    estudiante1.agregar_nota(3.0)
    estudiante1.agregar_nota(1.0) 
    estudiante1.agregar_nota(4.2)


    print(f"El promedio de {estudiante1.nombre} es: {estudiante1.calcular_promedio():.2f}")
    

    print(f"Notas registradas: {estudiante1.notas}")
