from Aventurero import Aventurero

class Arquero(Aventurero):
    def __init__(self, nombre, nivel, flechas):
        super().__init__(nombre, nivel)
        self.flechas = flechas

    def usar_habilidad(self):
        self.flechas -= 1 # Lógica extra para darle realismo
        print(f"¡{self.nombre} dispara una flecha! Le quedan {self.flechas}. ")