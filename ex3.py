class Calculadora:
    def __init__(self, operacao):
        self.operacao = operacao
    
    def calcular(self, x, y):
        if self.operacao == '+':
            return x + y
        elif self.operacao == '-':
            return x - y
