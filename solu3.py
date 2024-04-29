class Operacao:
    def calcular(self, x, y):
        pass

class Soma(Operacao):
    def calcular(self, x, y):
        return x + y

class Subtracao(Operacao):
    def calcular(self, x, y):
        return x - y

class Calculadora:
    def __init__(self, operacao):
        self.operacao = operacao
    
    def executar_calculo(self, x, y):
        return self.operacao.calcular(x, y)
