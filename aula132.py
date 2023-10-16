class Caneta:
    def __init__(self, cor):
        self.cor = cor 

    def printar(self):
        print(f"A cor da sua caneta é {self.cor}")


caneta_1 = Caneta("azul")
caneta_1.printar()
print(caneta_1.cor)